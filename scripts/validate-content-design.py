#!/usr/bin/env python3
"""Heuristic content-density and generic-AI UI validator (stdlib only)."""
from __future__ import annotations
import argparse,json,re,sys
from collections import Counter,defaultdict
from dataclasses import asdict,dataclass
from html import unescape
from pathlib import Path
from typing import Iterable,Sequence

SRC={'.html','.htm','.jsx','.tsx','.vue','.svelte','.md','.mdx'}
CODE=SRC|{'.js','.ts','.css','.scss'}
IGNORE_FILES={'README.md','CHANGELOG.md','LICENSE.md','AGENTS.md','PRD.md','VAULT_SELECTION.md','BUILD_CONTRACT.md','CONTENT_PLAN.md','AI_IMPLEMENTATION_INSTRUCTIONS.md'}
IGNORE_DIRS={'.git','node_modules','dist','build','.next','.nuxt','.svelte-kit','coverage','vendor','.cache','.turbo','storybook-static','out'}
TAG=re.compile(r'<(?P<k>h[1-6]|p|button|a|li)\b[^>]*>(?P<t>.*?)</(?P=k)\s*>',re.I|re.S)
PROP=re.compile(r'\b(?P<k>title|heading|headline|description|label|aria-label|placeholder)\s*=\s*(?P<q>[\'\"])(?P<t>.*?)(?P=q)',re.I|re.S)
WORD=re.compile(r"[A-Za-z0-9][A-Za-z0-9'’&+./-]*")

@dataclass(order=True)
class Issue:
    severity:str; code:str; message:str; file:str=''; line:int|None=None; evidence:str=''
@dataclass
class Record:
    kind:str; text:str; file:str; line:int

def clean(s:str)->str:
    s=unescape(s); s=re.sub(r'<(?:script|style|noscript|template|svg)\b.*?</(?:script|style|noscript|template|svg)>',' ',s,flags=re.I|re.S)
    s=re.sub(r'\{[^{}]*\}|<[^>]+>|[`*_>#~]',' ',s); return re.sub(r'\s+',' ',s).strip()
def wc(s:str)->int:return len(WORD.findall(s))
def norm(s:str)->str:return ' '.join(re.findall(r'[a-z0-9]+',s.lower()))
def lineno(s:str,p:int)->int:return s.count('\n',0,p)+1
def read(p:Path)->str:return p.read_text(encoding='utf-8',errors='ignore')
def files(root:Path,ext:set[str])->Iterable[Path]:
    for p in root.rglob('*'):
        if p.is_file() and p.suffix.lower() in ext and p.name not in IGNORE_FILES and not any(x.lower() in IGNORE_DIRS for x in p.parts):yield p

def extract(p:Path,root:Path)->tuple[list[Record],int,int]:
    rel=p.relative_to(root).as_posix(); s=read(p); out=[]
    if p.suffix.lower() in {'.md','.mdx'}:
        buf=[]; start=1
        def flush():
            nonlocal buf
            t=clean(' '.join(buf));
            if t:out.append(Record('p',t,rel,start))
            buf=[]
        for n,raw in enumerate(s.splitlines(),1):
            x=raw.strip(); m=re.match(r'^(#{1,6})\s+(.+?)\s*$',x)
            if m:flush(); out.append(Record('h'+str(len(m.group(1))),clean(m.group(2)),rel,n)); continue
            if not x or x.startswith('```') or x.startswith('|'):flush(); continue
            if re.match(r'^(?:[-*+]|\d+[.)])\s+',x):
                flush(); t=clean(re.sub(r'^(?:[-*+]|\d+[.)])\s+','',x));
                if t:out.append(Record('li',t,rel,n))
                continue
            if not buf:start=n
            buf.append(x)
        flush(); return out,sum(r.kind in {'h2','h3'} for r in out),0
    for m in TAG.finditer(s):
        t=clean(m.group('t'))
        if t and not t.startswith('{'):out.append(Record(m.group('k').lower(),t,rel,lineno(s,m.start())))
    for m in PROP.finditer(s):
        t=clean(m.group('t'))
        if wc(t)>=2:out.append(Record(m.group('k').lower(),t,rel,lineno(s,m.start())))
    sec=len(re.findall(r'<(?:section|article)\b',s,re.I))
    card=len(re.findall(r'(?:className|class)\s*=\s*[\'\"][^\'\"]*\b(?:card|feature-card|metric-card|pricing-card)\b',s,re.I))
    return out,sec,card

def add(a:list[Issue],sev:str,code:str,msg:str,r:Record|None=None,evidence:str='')->None:
    a.append(Issue(sev,code,msg,r.file if r else '',r.line if r else None,evidence or (r.text[:180] if r else '')))
def config(path:Path)->dict:
    try:return json.loads(path.read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as e:raise SystemExit(f'Invalid content rules: {path}: {e}')
def recipe(root:Path,a:list[Issue])->dict|None:
    p=root/'design-recipe.json'
    if not p.exists():return None
    try:d=json.loads(read(p))
    except json.JSONDecodeError as e:add(a,'error','RECIPE_INVALID_JSON',f'design-recipe.json is invalid: {e}'); return None
    req={'schemaVersion','product','experience','content','visualDirection','layout','components','motion','accessibility','performance','assetPolicy','quality'}
    miss=sorted(req-set(d))
    if miss:add(a,'error','RECIPE_MISSING_KEYS','design-recipe.json is missing: '+', '.join(miss))
    if any(x in json.dumps(d).lower() for x in ('to complete','to select','placeholder')):add(a,'error','RECIPE_INCOMPLETE','design-recipe.json still contains placeholder values.')
    return d

def artifacts(root:Path,c:dict,allow:bool,a:list[Issue])->None:
    if allow:return
    for name in c.get('requiredArtifacts',[]):
        p=root/name
        if not p.exists():add(a,'error','MISSING_ARTIFACT',f'Missing required planning artifact: {name}.');continue
        if p.suffix.lower()=='.md':
            s=read(p)
            if len(clean(s))<160:add(a,'error','ARTIFACT_INCOMPLETE',f'Planning artifact appears incomplete: {name}.')
            if re.search(r'\b(?:TO COMPLETE|TO SELECT|TBD|PLACEHOLDER)\b',s):add(a,'error','ARTIFACT_PLACEHOLDER',f'Planning artifact contains placeholder text: {name}.')

def text_checks(rs:Sequence[Record],c:dict,a:list[Issue])->None:
    t=c['thresholds']; h1=[r for r in rs if r.kind=='h1']
    if not h1:add(a,'warning','MISSING_H1','No visible page-level h1 was detected.')
    if len(h1)>1:add(a,'warning','MULTIPLE_H1',f'Detected {len(h1)} h1 elements. Verify one logical page heading per route/view.',h1[1])
    groups=defaultdict(list)
    for r in rs:
        n=wc(r.text); lim=None; codes=None
        if r.kind=='h1':lim=t['heroHeadline']; codes=('HERO_HEADLINE_WORDY','HERO_HEADLINE_TOO_LONG'); warn=lim['recommendedMaxWords']; err=lim['errorMaxWords']
        elif r.kind in {'h2','h3','h4','h5','h6','heading','headline','title'}:lim=t['sectionHeading']; codes=('HEADING_WORDY','HEADING_TOO_LONG'); warn=lim['warningMaxWords']; err=lim['errorMaxWords']
        elif r.kind in {'p','description'}:lim=t['paragraph']; codes=('PARAGRAPH_WORDY','PARAGRAPH_TOO_LONG'); warn=lim['warningMaxWords']; err=lim['errorMaxWords']
        elif r.kind in {'button','label','aria-label'}:lim=t['cta']; codes=('ACTION_LABEL_WORDY','ACTION_LABEL_TOO_LONG'); warn=lim['warningMaxWords']; err=lim['errorMaxWords']
        if lim and n>err:add(a,'error',codes[1],f'{r.kind} has {n} words; review threshold is {err}.',r)
        elif lim and n>warn:add(a,'warning',codes[0],f'{r.kind} has {n} words; recommended maximum is {warn}.',r)
        if r.kind in {'h1','h2','h3','p','description'} and n>=t.get('duplicateTextMinWords',8):groups[norm(r.text)].append(r)
    for k,v in groups.items():
        if k and len(v)>1:add(a,'warning','DUPLICATE_MESSAGE',f'The same {wc(v[0].text)}-word message appears {len(v)} times.',v[0])

def language(rs:Sequence[Record],c:dict,a:list[Issue])->None:
    hits=[]; vague={norm(x) for x in c.get('vagueCtas',[])}
    for r in rs:
        low=r.text.lower()
        hits += [(p,r) for p in c.get('genericPhrases',[]) if p.lower() in low]
        if r.kind in {'button','a','label','aria-label'} and norm(r.text) in vague:add(a,'warning','VAGUE_CTA',f'Action label “{r.text}” is vague; use a concrete verb and object.',r)
    sev='error' if len(hits)>=c['thresholds'].get('genericPhraseErrorCount',4) else 'warning'
    for p,r in hits[:12]:add(a,sev,'GENERIC_AI_PHRASE',f'Generic marketing phrase detected: “{p}”. Replace it with a concrete action, outcome, or evidence.',r)

def density(by:dict[str,list[Record]],counts:dict[str,tuple[int,int]],c:dict,d:dict|None,a:list[Issue])->None:
    lim=c['thresholds']['marketingPage']; typ=(((d or {}).get('product') or {}).get('type') or '').lower(); apply=not typ or typ in {'marketing-website','professional-services-website','ecommerce'}
    for f,rs in by.items():
        if not rs:continue
        words=sum(wc(r.text) for r in rs); sec,cards=counts.get(f,(0,0))
        if apply:
            if words>lim['errorTotalWords']:a.append(Issue('error','PAGE_TOO_WORDY',f'Detected approximately {words} visible words; review threshold is {lim["errorTotalWords"]}.',f))
            elif words>lim['warningTotalWords']:a.append(Issue('warning','PAGE_WORD_DENSITY',f'Detected approximately {words} visible words; consider compression or dedicated pages.',f))
            if sec>lim['errorSectionCount']:a.append(Issue('error','TOO_MANY_SECTIONS',f'Detected {sec} section/article blocks.',f))
            elif sec>lim['warningSectionCount']:a.append(Issue('warning','SECTION_COUNT_HIGH',f'Detected {sec} section/article blocks; verify distinct purpose.',f))
        if cards>lim['errorCardCount']:a.append(Issue('error','CARD_SOUP',f'Detected at least {cards} card-like elements.',f))
        elif cards>lim['warningCardCount']:a.append(Issue('warning','CARD_COUNT_HIGH',f'Detected at least {cards} card-like elements.',f))

def code_checks(root:Path,c:dict,d:dict|None,a:list[Issue])->dict:
    parts=[]; counts=Counter(); motion=reduced=False
    for p in files(root,CODE):
        s=read(p); low=s.lower(); rel=p.relative_to(root).as_posix(); parts.append(low)
        for pat,code in [(r'\blorem ipsum\b','LOREM'),(r'\bTODO\b','TODO'),(r'console\.log\s*\(','CONSOLE_LOG'),(r'\bPLACEHOLDER\b','PLACEHOLDER')]:
            m=re.search(pat,s,re.I)
            if m:a.append(Issue('error','DEBUG_'+code,f'Placeholder or debug marker detected: {code}.',rel,lineno(s,m.start()),s[m.start():m.start()+120]))
        motion|=any(x.lower() in low for x in c.get('motionSignals',[])); reduced|=any(x.lower() in low for x in c.get('reducedMotionSignals',[]))
        for name,r in c.get('visualRiskSignals',{}).items():
            counts[name]+=sum(low.count(x.lower()) for x in r.get('patterns',[]))
    score=0;e=[]
    for name,n in counts.items():
        r=c['visualRiskSignals'][name]
        if n>=r.get('pointsAfter',1):score+=int(r.get('points',1));e.append(f'{name}={n}')
    t=c['thresholds']
    if score>=t.get('genericVisualRiskErrorScore',9):a.append(Issue('error','GENERIC_VISUAL_RISK',f'Generic visual-pattern risk score is {score}.',evidence=', '.join(e)))
    elif score>=t.get('genericVisualRiskWarningScore',5):a.append(Issue('warning','GENERIC_VISUAL_RISK',f'Generic visual-pattern risk score is {score}.',evidence=', '.join(e)))
    if motion and not reduced:add(a,'error','REDUCED_MOTION_MISSING','Motion signals were found without an obvious reduced-motion implementation.')
    combined='\n'.join(parts).replace('-',' '); req=(((d or {}).get('components') or {}).get('requiredStates') or [])
    miss=[x for x in req if x.lower().replace('-',' ') not in combined]
    if miss:add(a,'warning','STATE_SIGNALS_MISSING','Required state signals were not detected: '+', '.join(miss)+'.')
    return {'genericVisualRiskScore':score,'motionFound':motion,'reducedMotionFound':reduced}

def summary(a:Sequence[Issue])->dict:
    c=Counter(x.severity for x in a);return {'errors':c['error'],'warnings':c['warning'],'info':c['info']}
def parser()->argparse.ArgumentParser:
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--config',type=Path);p.add_argument('--allow-missing-artifacts',action='store_true');p.add_argument('--strict',action='store_true');p.add_argument('--json-output',type=Path);p.add_argument('--quiet',action='store_true');return p

def main(argv:Sequence[str]|None=None)->int:
    x=parser().parse_args(argv);root=x.root.resolve()
    if not root.is_dir():print(f'Target root not found: {root}',file=sys.stderr);return 2
    c=config((x.config or Path(__file__).resolve().parents[1]/'quality/content-rules.json').resolve());a=[];artifacts(root,c,x.allow_missing_artifacts,a);d=recipe(root,a)
    by={};counts={}
    for p in files(root,SRC):
        rs,s,k=extract(p,root); rel=p.relative_to(root).as_posix();by[rel]=rs;counts[rel]=(s,k)
    allr=[r for rs in by.values() for r in rs];text_checks(allr,c,a);language(allr,c,a);density(by,counts,c,d,a);metrics=code_checks(root,c,d,a)
    a.sort(key=lambda i:({'error':0,'warning':1,'info':2}.get(i.severity,3),i.file,i.line or 0,i.code));rep={'root':str(root),'sourceFilesScanned':len(by),'textRecords':len(allr),'summary':summary(a),'metrics':metrics,'issues':[asdict(i) for i in a]}
    if x.json_output:x.json_output.parent.mkdir(parents=True,exist_ok=True);x.json_output.write_text(json.dumps(rep,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if not x.quiet:
        print(f'ROOT={root}\nSOURCE_FILES_SCANNED={len(by)}\nTEXT_RECORDS={len(allr)}\nERRORS={rep["summary"]["errors"]}\nWARNINGS={rep["summary"]["warnings"]}\nGENERIC_VISUAL_RISK_SCORE={metrics["genericVisualRiskScore"]}')
        for i in a:
            loc=f' [{i.file}{":"+str(i.line) if i.line else ""}]' if i.file else '';ev=f' — {i.evidence}' if i.evidence else '';print(f'- {i.severity.upper()} {i.code}{loc}: {i.message}{ev}')
        print('VALIDATION=PASS' if not rep['summary']['errors'] else 'VALIDATION=FAIL')
    return 1 if rep['summary']['errors'] or (x.strict and rep['summary']['warnings']) else 0
if __name__=='__main__':raise SystemExit(main())
