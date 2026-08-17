import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module

validator = load("business_understanding_validator", "scripts/validate-business-understanding.py")
planner = load("vault_build_planner", "scripts/plan-vault-build.py")


def ready_profile():
    return {
        "status": "ready",
        "officialName": "Example Couture",
        "businessCategory": "fashion couture and bespoke tailoring",
        "subcategories": ["corporate wear", "kaftan"],
        "offers": [{"name": "Corporate suits", "evidenceStatus": "owner-confirmed"}],
        "audiences": ["professionals"],
        "primaryConversion": {"action": "Order on WhatsApp", "channel": "WhatsApp", "evidenceStatus": "owner-confirmed"},
        "evidenceSources": [{"type": "owner brief", "reference": "current brief", "accessStatus": "user-supplied"}],
        "brandSignals": {"positioning": ["premium"], "visualSignals": ["black and amber logo"], "tone": ["elegant"]},
        "operationalFacts": {},
        "researchGaps": ["delivery coverage"],
        "confidence": {"score": 90, "rationale": "Core offer, audience and conversion are owner-confirmed."},
        "recommendedDomainPack": None,
        "designSelectionAllowed": True,
    }


def test_ready_profile_passes():
    assert validator.validate(ready_profile()) == []


def test_blocked_profile_cannot_allow_design_selection():
    profile = ready_profile()
    profile["status"] = "blocked"
    profile["designSelectionAllowed"] = True
    assert any("must not allow design selection" in e for e in validator.validate(profile))


def test_fashion_profile_routes_to_fashion_pack():
    assert planner.choose_domain(ready_profile()) == "fashion-couture"


def test_ready_requires_meaningful_confidence():
    profile = ready_profile()
    profile["confidence"]["score"] = 50
    assert any("confidence.score >= 70" in e for e in validator.validate(profile))
