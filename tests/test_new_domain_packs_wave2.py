import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class NewDomainPackWave2Tests(unittest.TestCase):
 def test_pack_files_and_validators(self):
  for pack,validator in [('beauty-wellness','validate-beauty-wellness-pack.py'),('hospitality','validate-hospitality-pack.py'),('saas-technology','validate-saas-technology-pack.py')]:
   p=json.loads((ROOT/'packs'/pack/'pack.json').read_text())
   self.assertEqual(p['id'],pack); self.assertIn('business-profile.json',p['requiredPlanningArtifacts'])
   r=subprocess.run([sys.executable,str(ROOT/'scripts'/validator)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stdout+r.stderr)
 def test_planner_has_new_domains(self):
  text=(ROOT/'scripts/plan-vault-build.py').read_text()
  for name in ['beauty-wellness','hospitality','saas-technology']:
   self.assertIn(name,text)
 def test_pack_index_has_new_domains(self):
  ids={p['id'] for p in json.loads((ROOT/'packs/pack-index.json').read_text())['packs']}
  self.assertTrue({'beauty-wellness','hospitality','saas-technology'}.issubset(ids))
if __name__=='__main__': unittest.main()