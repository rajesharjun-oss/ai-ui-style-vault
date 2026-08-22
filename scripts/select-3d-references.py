#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(path): return json.loads(path.read_text(encoding="utf-8"))
def score(item, words, filters):
    hay = json.dumps(item, ensure_ascii=False).lower()
    return sum(3 for word in words if word in hay) + sum(5 for value in filters if value and value.lower() in hay)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("brief")
    parser.add_argument("--style-family", default="")
    parser.add_argument("--stack", default="")
    parser.add_argument("--best-for", default="")
    parser.add_argument("--performance-risk", default="")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--json", dest="json_path", default="")
    args = parser.parse_args()
    records = []
    for item in load(ROOT / "packs/3d-immersive-web/style-families.json")["families"]: records.append({"recordType": "style-family", **item})
    for item in load(ROOT / "3d/techniques/technique-catalog.json")["techniques"]: records.append({"recordType": "technique", **item})
    for item in load(ROOT / "3d/source-catalog.json")["sources"]: records.append({"recordType": "source", **item})
    for item in load(ROOT / "3d/references/refs-gallery-3d.json").get("references", []): records.append({"recordType": "reference", **item})
    words = set(re.findall(r"[a-z0-9]+", args.brief.lower()))
    filters = [args.style_family, args.stack, args.best_for, args.performance_risk]
    ranked = sorted(((score(item, words, filters), item) for item in records), key=lambda pair: (-pair[0], pair[1].get("id", "")))
    selected = [item for value, item in ranked if value > 0][:max(1, args.limit)]
    result = {"brief": args.brief, "count": len(selected), "selections": selected, "reminder": "A reference is not a reuse licence."}
    if args.json_path: Path(args.json_path).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0
if __name__ == "__main__": raise SystemExit(main())
