#!/usr/bin/env python3
"""Local read-only stdio MCP adapter for the AI UI Style Vault."""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EFFECTS = ROOT / "interactive-effects" / "effects.json"
IMMERSIVE = ROOT / "immersive-templates" / "template-catalog.json"
PRODUCTION = ROOT / "3d-production-resources" / "resource-catalog.json"
DELIVERY = ROOT / "3d-delivery-runtimes" / "runtime-catalog.json"
EFFECT_ENGINE = ROOT / "scripts" / "interactive-effects.py"
IMMERSIVE_ENGINE = ROOT / "scripts" / "immersive-templates.py"
PRODUCTION_ENGINE = ROOT / "scripts" / "3d-production-resources.py"
DELIVERY_ENGINE = ROOT / "scripts" / "3d-delivery-runtimes.py"


def effect_catalog():
    return json.loads(EFFECTS.read_text(encoding="utf-8"))["effects"]


def immersive_catalog():
    return json.loads(IMMERSIVE.read_text(encoding="utf-8"))["templates"]


def production_catalog():
    return json.loads(PRODUCTION.read_text(encoding="utf-8"))["categories"]


def delivery_catalog():
    return json.loads(DELIVERY.read_text(encoding="utf-8"))["profiles"]


def search(query):
    terms = [x for x in query.lower().split() if x]
    out = []
    for e in effect_catalog():
        hay = " ".join([e["id"], e["label"], e["summary"], e["family"], *e["sections"], *e["domains"], *e["signals"]]).lower()
        score = sum(term in hay for term in terms)
        if score:
            out.append({"kind": "interactive-effect", "id": e["id"], "label": e["label"], "score": score, "runtime": e["runtime"], "performanceTier": e["tier"], "sections": e["sections"]})
    for t in immersive_catalog():
        hay = " ".join([t["id"], t["label"], t["summary"], *t["domains"], *t["goals"], *t["signals"], *t["runtimes"]]).lower()
        score = sum(term in hay for term in terms)
        if score:
            out.append({"kind": "immersive-template", "id": t["id"], "label": t["label"], "score": score, "level": t["level"], "blueprint": t["blueprint"], "performanceTier": t["performanceTier"]})
    for r in production_catalog():
        resource_words = []
        for candidate in r["resourceCandidates"]:
            resource_words.extend([candidate["name"], candidate["role"]])
        hay = " ".join([r["id"], r["label"], r["summary"], *r["domains"], *r["needs"], *r["outputs"], *resource_words]).lower()
        score = sum(term in hay for term in terms)
        if score:
            out.append({"kind": "3d-production-resource", "id": r["id"], "label": r["label"], "score": score, "outputs": r["outputs"], "candidateCount": len(r["resourceCandidates"])})
    for d in delivery_catalog():
        hay = " ".join([d["id"], d["label"], d["summary"], *d["goals"], *d["signals"], *d["features"]]).lower()
        score = sum(term in hay for term in terms)
        if score:
            out.append({"kind": "3d-delivery-runtime", "id": d["id"], "label": d["label"], "score": score, "performanceTier": d["performanceTier"], "features": d["features"][:6]})
    return sorted(out, key=lambda x: (-x["score"], x["kind"], x["id"]))[:18]


def get_effect(effect_id):
    for e in effect_catalog():
        if e["id"] == effect_id:
            return e
    raise KeyError(effect_id)


def get_immersive(template_id):
    for t in immersive_catalog():
        if t["id"] == template_id:
            return t
    raise KeyError(template_id)


def get_production(category_id):
    for r in production_catalog():
        if r["id"] == category_id:
            return r
    raise KeyError(category_id)


def get_delivery(profile_id):
    for d in delivery_catalog():
        if d["id"] == profile_id:
            return d
    raise KeyError(profile_id)


def run_engine(engine, args, input_profile=None):
    if input_profile is None:
        r = subprocess.run([sys.executable, str(engine), *args], cwd=ROOT, capture_output=True, text=True)
    else:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "profile.json"
            p.write_text(json.dumps(input_profile), encoding="utf-8")
            r = subprocess.run([sys.executable, str(engine), args[0], str(p), *args[1:]], cwd=ROOT, capture_output=True, text=True)
    if r.returncode not in (0, 1, 2):
        raise RuntimeError(r.stderr or r.stdout)
    return r


TOOLS = [
    {"name": "search_vault", "description": "Search interactive effects, immersive templates, 3D production resources and 3D delivery-runtime profiles by purpose or need.", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
    {"name": "get_effect_contract", "description": "Return one machine-readable interactive-effect contract.", "inputSchema": {"type": "object", "properties": {"effect_id": {"type": "string"}}, "required": ["effect_id"]}},
    {"name": "select_interactive_effect", "description": "Select an effect or deliberately return none from a validated business profile.", "inputSchema": {"type": "object", "properties": {"profile": {"type": "object"}, "section": {"type": "string", "default": "hero"}, "performance_priority": {"enum": ["normal", "high"], "default": "normal"}, "asset_readiness": {"enum": ["strong", "adequate", "limited", "none"], "default": "limited"}}, "required": ["profile"]}},
    {"name": "get_effect_skill", "description": "Generate implementation Skill.md for a selected effect.", "inputSchema": {"type": "object", "properties": {"effect_id": {"type": "string"}}, "required": ["effect_id"]}},
    {"name": "get_immersive_template", "description": "Return one machine-readable immersive website template contract.", "inputSchema": {"type": "object", "properties": {"template_id": {"type": "string"}}, "required": ["template_id"]}},
    {"name": "select_immersive_template", "description": "Select an immersive architecture or deliberately return none from a validated business profile and user goal.", "inputSchema": {"type": "object", "properties": {"profile": {"type": "object"}, "goal": {"type": "string"}, "level": {"type": "integer", "minimum": 1, "maximum": 4}, "performance_priority": {"enum": ["normal", "high"], "default": "normal"}, "asset_readiness": {"enum": ["strong", "adequate", "limited", "none"], "default": "limited"}}, "required": ["profile", "goal"]}},
    {"name": "get_immersive_skill", "description": "Generate implementation Skill.md for a selected immersive template.", "inputSchema": {"type": "object", "properties": {"template_id": {"type": "string"}}, "required": ["template_id"]}},
    {"name": "get_3d_production_resource", "description": "Return one machine-readable 3D production-resource category and its discovery candidates.", "inputSchema": {"type": "object", "properties": {"category_id": {"type": "string"}}, "required": ["category_id"]}},
    {"name": "select_3d_production_resource", "description": "Select a 3D production-resource category for a concrete asset/production need. This does not justify 3D or approve external resources.", "inputSchema": {"type": "object", "properties": {"need": {"type": "string"}, "domain": {"type": "string"}, "max": {"type": "integer", "minimum": 1, "maximum": 8}}, "required": ["need"]}},
    {"name": "get_3d_production_skill", "description": "Generate a production Skill.md for a selected 3D resource category with rights/provenance and web-delivery gates.", "inputSchema": {"type": "object", "properties": {"category_id": {"type": "string"}}, "required": ["category_id"]}},
    {"name": "get_3d_delivery_runtime", "description": "Return one machine-readable 3D delivery-runtime profile, currently backed by Google <model-viewer> profiles.", "inputSchema": {"type": "object", "properties": {"profile_id": {"type": "string"}}, "required": ["profile_id"]}},
    {"name": "select_3d_delivery_runtime", "description": "Select the smallest sufficient 3D browser-delivery profile or escalate beyond <model-viewer> when the interaction is too complex.", "inputSchema": {"type": "object", "properties": {"need": {"type": "string"}, "format": {"enum": ["glb", "gltf", "other"]}, "ar": {"type": "boolean", "default": False}}, "required": ["need"]}},
    {"name": "get_3d_delivery_skill", "description": "Generate implementation Skill.md for a selected 3D delivery-runtime profile.", "inputSchema": {"type": "object", "properties": {"profile_id": {"type": "string"}}, "required": ["profile_id"]}}
]


def call(name, args):
    if name == "search_vault":
        return search(args.get("query", ""))
    if name == "get_effect_contract":
        return get_effect(args["effect_id"])
    if name == "select_interactive_effect":
        r = run_engine(EFFECT_ENGINE, ["select", "--section", args.get("section", "hero"), "--performance-priority", args.get("performance_priority", "normal"), "--asset-readiness", args.get("asset_readiness", "limited")], args["profile"])
        return json.loads(r.stdout)
    if name == "get_effect_skill":
        r = run_engine(EFFECT_ENGINE, ["skill", args["effect_id"]])
        if r.returncode:
            raise KeyError(args["effect_id"])
        return r.stdout
    if name == "get_immersive_template":
        return get_immersive(args["template_id"])
    if name == "select_immersive_template":
        forwarded = ["select", "--goal", args["goal"], "--performance-priority", args.get("performance_priority", "normal"), "--asset-readiness", args.get("asset_readiness", "limited")]
        if args.get("level"):
            forwarded += ["--level", str(args["level"])]
        r = run_engine(IMMERSIVE_ENGINE, forwarded, args["profile"])
        return json.loads(r.stdout)
    if name == "get_immersive_skill":
        r = run_engine(IMMERSIVE_ENGINE, ["skill", args["template_id"]])
        if r.returncode:
            raise KeyError(args["template_id"])
        return r.stdout
    if name == "get_3d_production_resource":
        return get_production(args["category_id"])
    if name == "select_3d_production_resource":
        forwarded = ["select", args["need"]]
        if args.get("domain"):
            forwarded += ["--domain", args["domain"]]
        if args.get("max"):
            forwarded += ["--max", str(args["max"])]
        r = run_engine(PRODUCTION_ENGINE, forwarded)
        return json.loads(r.stdout)
    if name == "get_3d_production_skill":
        r = run_engine(PRODUCTION_ENGINE, ["skill", args["category_id"]])
        if r.returncode:
            raise KeyError(args["category_id"])
        return r.stdout
    if name == "get_3d_delivery_runtime":
        return get_delivery(args["profile_id"])
    if name == "select_3d_delivery_runtime":
        forwarded = ["select", args["need"]]
        if args.get("format"):
            forwarded += ["--format", args["format"]]
        if args.get("ar"):
            forwarded.append("--ar")
        r = run_engine(DELIVERY_ENGINE, forwarded)
        return json.loads(r.stdout)
    if name == "get_3d_delivery_skill":
        r = run_engine(DELIVERY_ENGINE, ["skill", args["profile_id"]])
        if r.returncode:
            raise KeyError(args["profile_id"])
        return r.stdout
    raise KeyError(name)


def response(i, result=None, error=None):
    x = {"jsonrpc": "2.0", "id": i}
    if error is None:
        x["result"] = result
    else:
        x["error"] = error
    return x


def handle(msg):
    method = msg.get("method")
    i = msg.get("id")
    if method == "initialize":
        pv = msg.get("params", {}).get("protocolVersion") or "2025-06-18"
        return response(i, {"protocolVersion": pv, "capabilities": {"tools": {"listChanged": False}}, "serverInfo": {"name": "ai-ui-style-vault", "version": "1.3.0"}})
    if method == "notifications/initialized":
        return None
    if method == "ping":
        return response(i, {})
    if method == "tools/list":
        return response(i, {"tools": TOOLS})
    if method == "tools/call":
        p = msg.get("params", {})
        try:
            value = call(p.get("name", ""), p.get("arguments") or {})
            text = value if isinstance(value, str) else json.dumps(value, indent=2, ensure_ascii=False)
            return response(i, {"content": [{"type": "text", "text": text}], "isError": False})
        except Exception as exc:
            return response(i, {"content": [{"type": "text", "text": str(exc)}], "isError": True})
    return response(i, error={"code": -32601, "message": f"Method not found: {method}"})


def serve():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            out = handle(json.loads(line))
        except Exception as exc:
            out = response(None, error={"code": -32700, "message": str(exc)})
        if out is not None:
            sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
            sys.stdout.flush()


def main():
    p = argparse.ArgumentParser(description="Local read-only stdio MCP adapter for the Vault.")
    p.add_argument("--list-tools", action="store_true")
    args = p.parse_args()
    if args.list_tools:
        print(json.dumps({"tools": TOOLS}, indent=2))
        return 0
    serve()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
