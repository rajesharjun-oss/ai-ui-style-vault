#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; PACK=ROOT/'packs/hospitality'
REQ=['pack.json','production-themes.json','page-blueprints.json','component-manifest.json','state-vocabulary.json','content-and-booking-standard.md','property-media-standard.md','motion-guidance.md','accessibility-and-responsive.md','implementation-prompt.md','templates/HOSPITALITY_BUILD_CONTRACT.md']
JSONS=REQ[:5]
def main():
 e=[]
 for r in REQ:
  if not (PACK/r).exists(): e.append('missing: '+r)
 for r in JSONS:
  try: json.loads((PACK/r).read_text())
  except Exception as x: e.append(f'invalid JSON {r}: {x}')
 if not e:
  p=json.loads((PACK/'pack.json').read_text())
  if p.get('id')!='hospitality': e.append('wrong pack id')
  if 'business-profile.json' not in p.get('requiredPlanningArtifacts',[]): e.append('business-profile required')
 if e:
  print('HOSPITALITY PACK: FAIL'); [print('- '+x) for x in e]; return 1
 print('HOSPITALITY PACK: PASS'); return 0
if __name__=='__main__': raise SystemExit(main())