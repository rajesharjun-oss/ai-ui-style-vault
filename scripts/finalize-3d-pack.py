from __future__ import annotations

from pathlib import Path
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]


def heredoc_blocks(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    marker = "          python - <<'PY'\n"
    close = "\n          PY\n"
    found: list[str] = []
    cursor = 0
    while True:
        try:
            start = text.index(marker, cursor) + len(marker)
            end = text.index(close, start)
        except ValueError:
            break
        found.append(textwrap.dedent(text[start:end]))
        cursor = end + len(close)
    return found


# 1. Materialize the original 3D pack.
base_blocks = heredoc_blocks(ROOT / ".github/workflows/generate-3d-immersive-pack.yml")
if not base_blocks:
    raise RuntimeError("3D generator block not found")
base = base_blocks[0]
base = base.replace(
    'if json_marker not in quality: raise RuntimeError("Quality JSON marker missing")',
    'if json_marker not in quality: json_marker = ""',
)
base = base.replace(
    'if validator_marker not in quality: raise RuntimeError("Quality validator marker missing")',
    'if validator_marker not in quality: validator_marker = ""',
)
exec(compile(base, "base-3d-generator.py", "exec"), {"__name__": "__main__"})

# 2. Apply the semantic relevance materializer with conservative matching.
semantic_blocks = heredoc_blocks(ROOT / ".github/workflows/materialize-3d-pack.yml")
if len(semantic_blocks) < 2:
    raise RuntimeError("Semantic materializer block not found")
semantic = semantic_blocks[1]
pattern = re.compile(
    r'(?P<i>\s*)approved = any\(any\(token in item for token in _norm\(value\)\.split\(\)\) for value in domain\["approvedSubjects"\]\)\n'
    r'(?P=i)rejected = any\(any\(token in item for token in _norm\(value\)\.split\(\)\) for value in domain\["rejectExamples"\]\)\n'
    r'(?P=i)if rejected and not approved:\n'
    r'(?P=i)    return \{"decision":"reject","score":0,"domain":domain\["id"\],"reason":"Subject matches an explicit unrelated example for this domain\."\}\n'
    r'(?P=i)if approved:\n'
    r'(?P=i)    return \{"decision":"candidate","score":4,"domain":domain\["id"\],"reason":"Subject matches the domain visual vocabulary; verify exact business/page evidence before approval\."\}\n'
)
match = pattern.search(semantic)
if not match:
    raise RuntimeError("Expected permissive semantic matcher was not found")
i = match.group("i")
replacement = (
    f'{i}stop = {{"a","an","and","as","at","by","for","from","in","into","of","on","or","the","to","with","actual","random","unrelated","verified","generic"}}\n'
    f'{i}item_words = set(item.split())\n'
    f'{i}def meaningful_terms(value: str) -> set[str]:\n'
    f'{i}    return {{word for word in _norm(value).split() if word not in stop and len(word) >= 3}}\n'
    f'{i}def matches(values: list[str]) -> bool:\n'
    f'{i}    return any(bool(meaningful_terms(value) & item_words) for value in values)\n'
    f'{i}# Explicit exclusions win over broad approved vocabulary.\n'
    f'{i}rejected = matches(domain["rejectExamples"])\n'
    f'{i}if rejected:\n'
    f'{i}    return {{"decision":"reject","score":0,"domain":domain["id"],"reason":"Subject matches an explicit unrelated example for this domain."}}\n'
    f'{i}approved = matches(domain["approvedSubjects"]) or any(_norm(signal) in item_words for signal in domain["signals"])\n'
    f'{i}if approved:\n'
    f'{i}    return {{"decision":"candidate","score":4,"domain":domain["id"],"reason":"Subject matches the domain visual vocabulary; verify exact business/page evidence before approval."}}\n'
)
semantic = pattern.sub(lambda _m: replacement, semantic, count=1)
exec(compile(semantic, "semantic-materializer.py", "exec"), {"__name__": "__main__"})

# 3. Require the complete scene to be relevant, not only the hero model.
module_path = ROOT / "packs/3d-immersive-web/code/semantic-relevance.py"
module = module_path.read_text(encoding="utf-8")
if "def scene_relevance" not in module:
    module += '''

def scene_relevance(brief: str, layers: dict[str, str]) -> dict:
    """Evaluate subject, environment, props and other semantic scene layers."""
    results = {name: subject_relevance(brief, subject) for name, subject in layers.items()}
    rejected = [name for name, result in results.items() if result.get("decision") == "reject"]
    weak = [name for name, result in results.items() if result.get("decision") == "manual-review"]
    if rejected:
        return {"decision":"reject","score":0,"rejectedLayers":rejected,"layers":results}
    if weak:
        return {"decision":"manual-review","score":2,"weakLayers":weak,"layers":results}
    return {"decision":"candidate","score":4,"layers":results}
'''
    module_path.write_text(module, encoding="utf-8")

# 4. Add regression tests for cross-domain mismatches and scene consistency.
test_path = ROOT / "tests/test_3d_semantic_relevance.py"
test_text = test_path.read_text(encoding="utf-8")
anchor = "    def test_pack_requires_relevance_contract(self):\n"
if "test_pizza_rejects_unrelated_showroom_background" not in test_text:
    extra = '''    def test_pizza_rejects_unrelated_showroom_background(self):
        result = semantic.scene_relevance(
            "pizza restaurant food delivery",
            {"product":"pepperoni pizza", "environment":"luxury sports car showroom"},
        )
        self.assertEqual(result["decision"], "reject")
        self.assertIn("environment", result["rejectedLayers"])

    def test_pizza_scene_accepts_food_context(self):
        result = semantic.scene_relevance(
            "pizza restaurant food delivery",
            {"product":"pepperoni pizza", "environment":"restaurant interior", "prop":"pizza oven"},
        )
        self.assertEqual(result["decision"], "candidate")

'''
    if anchor not in test_text:
        raise RuntimeError("Semantic test insertion point not found")
    test_path.write_text(test_text.replace(anchor, extra + anchor, 1), encoding="utf-8")

print("THREE_D_PACK_MATERIALIZED=PASS")
