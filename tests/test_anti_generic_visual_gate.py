import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("visual_gate", ROOT / "scripts/validate-anti-generic-visual.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class AntiGenericVisualGateTests(unittest.TestCase):
    def observations(self, **overrides):
        data = {
            "desktopReviewed":True,"mobileReviewed":True,"primaryActionVisible":True,
            "productOrServiceVisibleEarly":True,"sectionRhythmVaries":True,
            "mobileCompositionTransformed":True,"reducedMotionVerified":True,
            "noHorizontalOverflow":True,"mediaProvenanceVerified":True,
            "operationalStatesVerified":True,"sameImageRepeated":False,
            "productHiddenBelowMarketing":False,"desktopOnlyComposition":False,
            "motionEverywhere":False,"genericFeatureCardCopy":False,"notes":[]
        }
        data.update(overrides)
        return data

    def test_specific_site_passes(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            root.joinpath("index.html").write_text('<main><h1>Tax advisory for Nigerian businesses</h1><a href="/contact">Book a consultation</a><section>VAT health check</section></main>')
            root.joinpath("styles.css").write_text('@media (prefers-reduced-motion: reduce){*{animation:none!important}} h1{font-size:64px}')
            result=mod.score(root,self.observations())
            self.assertEqual(result["status"],"pass")
            self.assertGreaterEqual(result["score"],75)

    def test_generic_site_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            root.joinpath("index.html").write_text('<main><h1>Unlock your potential</h1><p>Transform your business with a seamless experience.</p><img src="hero.jpg"><img src="hero.jpg"><img src="hero.jpg"></main>')
            css=' '.join(['.x{backdrop-filter:blur(20px);background:linear-gradient(90deg,#7c3aed,#4f46e5);border-radius:9999px}']*14)+ ' h1{font-size:160px}'
            root.joinpath("styles.css").write_text(css)
            result=mod.score(root,self.observations(sectionRhythmVaries=False,mobileCompositionTransformed=False,reducedMotionVerified=False,sameImageRepeated=True,productHiddenBelowMarketing=True,motionEverywhere=True,genericFeatureCardCopy=True))
            self.assertEqual(result["status"],"fail")
            self.assertLess(result["score"],75)

    def test_missing_mobile_overflow_clearance_is_hard_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            root.joinpath("index.html").write_text('<main><h1>Specific product</h1></main>')
            root.joinpath("styles.css").write_text('@media (prefers-reduced-motion: reduce){*{animation:none!important}}')
            result=mod.score(root,self.observations(noHorizontalOverflow=False))
            self.assertEqual(result["status"],"fail")
            self.assertTrue(result["hardFails"])

if __name__ == "__main__":
    unittest.main()
