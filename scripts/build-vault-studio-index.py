#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

def main():
    p=argparse.ArgumentParser(description="Build the compact data index consumed by the future Vault Studio browser.")
    p.add_argument("--output",default="studio/catalog-index.json")
    args=p.parse_args()
    effects=load(Path("interactive-effects/effects.json"))
    packs=load(Path("packs/pack-index.json"))
    sections=load(Path("system/section-recipes.json"))
    refs=load(Path("references/threeui-community.json"))
    product=[x for x in packs["packs"] if x.get("packKind")=="product-domain"]
    capability=[x for x in packs["packs"] if x.get("packKind")=="capability"]
    recipes=sections["recipes"]
    data={
      "name":"AI UI Style Vault Studio Index","version":"1.0.0",
      "browseKinds":["domain-pack","section-recipe","interactive-effect","capability-pack","reference-pattern"],
      "counts":{"domainPacks":len(product),"capabilityPacks":len(capability),"sectionRecipes":len(recipes),"interactiveEffects":len(effects["effects"]),"referencePatterns":len(refs["referencePatterns"])},
      "domainPacks":[{"id":x["id"],"name":x["name"],"triggers":x.get("triggers",[])[:8]} for x in product],
      "capabilityPacks":[{"id":x["id"],"name":x["name"]} for x in capability],
      "sectionRecipes":[{"id":x["id"],"section":x["section"],"composition":x["composition"]} for x in recipes],
      "interactiveEffects":[{"id":x["id"],"label":x["label"],"family":x["family"],"sections":x["sections"],"domains":x["domains"],"runtime":x["runtime"],"performanceTier":x["tier"],"signals":x["signals"]} for x in effects["effects"]],
      "referencePatterns":[{"id":x["id"],"family":x["family"],"runtime":x["runtime"],"reuse":x["reuse"]} for x in refs["referencePatterns"]],
      "rule":"Studio browsing never bypasses business research, semantic effect selection or source/licence boundaries."
    }
    target=ROOT/args.output; target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"ready","output":str(target.relative_to(ROOT)),"counts":data["counts"]},indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
