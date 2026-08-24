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
EFFECT_ENGINE = ROOT / "scripts" / "interactive-effects.py"
IMMERSIVE_ENGINE = ROOT / "scripts" / "immersive-templates.py"


def effect_catalog():
    return json.loads(EFFECTS.read_text(encoding="utf-8"))["effects"]


def immersive_catalog():
    return json.loads(IMMERSIVE.read_text(encoding="utf-8"))["templates"]


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
    return sorted(out, key=lambda x: (-x["score"], x["kind"], x["id"]))[:12]


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
    {"name": "search_vault", "description": "Search interactive effects and immersive templates by business purpose, runtime or signal.", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
    {"name": "get_effect_contract", "description": "Return one machine-readable interactive-effect contract.", "inputSchema": {"type": "object", "properties": {"effect_id": {"type": "string"}}, "required": ["effect_id"]}},
    {"name": "select_interactive_effect", "description": "Select an effect or deliberately return none from a validated business profile.", "inputSchema": {"type": "object", "properties": {"profile": {"type": "object"}, "section": {"type": "string", "default": "hero"}, "performance_priority": {"enum": ["normal", "high"], "default": "normal"}, "asset_readiness": {"enum": ["strong", "adequate", "limited", "none"], "default": "limited"}}, "required": ["profile"]}},
    {"name": "get_effect_skill", "description": "Generate implementation Skill.md for a selected effect.", "inputSchema": {"type": "object", "properties": {"effect_id": {"type": "string"}}, "required": ["effect_id"]}},
    {"name": "get_immersive_template", "description": "Return one machine-readable immersive website template contract.", "inputSchema": {"type": "object", "properties": {"template_id": {"type": "string"}}, "required": ["template_id"]}},
    {"name": "select_immersive_template", "description": "Select an immersive architecture or deliberately return none from a validated business profile and user goal.", "inputSchema": {"type": "object", "properties": {"profile": {"type": "object"}, "goal": {"type": "string"}, "level": {"type": "integer", "minimum": 1, "maximum": 4}, "performance_priority": {"enum": ["normal", "high"], "default": "normal"}, "asset_readiness": {"enum": ["strong", "adequate", "limited", "none"], "default": "limited"}}, "required": ["profile", "goal"]}},
    {"name": "get_immersive_skill", "description": "Generate implementation Skill.md for a selected immersive template.", "inputSchema": {"type": "object", "properties": {"template_id": {"type": "string"}}, "required": ["template_id"]}}
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
        return response(i, {"protocolVersion": pv, "capabilities": {"tools": {"listChanged": False}}, "serverInfo": {"name": "ai-ui-style-vault", "version": "1.1.0"}})
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
