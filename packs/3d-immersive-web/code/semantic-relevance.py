from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MAP = json.loads((ROOT / "3d/subject-domain-map.json").read_text(encoding="utf-8"))

def _norm(value: str) -> str:
    return " ".join(value.lower().replace("-", " ").split())

def detect_domain(brief: str) -> dict | None:
    hay = _norm(brief)
    ranked = []
    for domain in MAP["domains"]:
        score = sum(1 for signal in domain["signals"] if _norm(signal) in hay)
        ranked.append((score, domain))
    ranked.sort(key=lambda pair: -pair[0])
    return ranked[0][1] if ranked and ranked[0][0] > 0 else None

def subject_relevance(brief: str, subject: str) -> dict:
    domain = detect_domain(brief)
    item = _norm(subject)
    if domain is None:
        return {"decision":"manual-review","score":0,"reason":"No domain detected; derive approved subjects from verified business research."}
    stop = {"a","an","and","as","at","by","for","from","in","into","of","on","or","the","to","with","actual","random","unrelated","verified","generic"}
    item_words = set(item.split())
    def meaningful_terms(value: str) -> set[str]:
        return {word for word in _norm(value).split() if word not in stop and len(word) >= 3}
    def matches(values: list[str]) -> bool:
        return any(bool(meaningful_terms(value) & item_words) for value in values)
    # Explicit exclusions win over broad approved vocabulary.
    rejected = matches(domain["rejectExamples"])
    if rejected:
        return {"decision":"reject","score":0,"domain":domain["id"],"reason":"Subject matches an explicit unrelated example for this domain."}
    approved = matches(domain["approvedSubjects"]) or any(_norm(signal) in item_words for signal in domain["signals"])
    if approved:
        return {"decision":"candidate","score":4,"domain":domain["id"],"reason":"Subject matches the domain visual vocabulary; verify exact business/page evidence before approval."}
    return {"decision":"manual-review","score":2,"domain":domain["id"],"reason":"No direct domain match; do not use as a primary visual without specific verified justification."}


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
