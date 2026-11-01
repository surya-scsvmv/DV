"""Smoke tests for the dataset and Python plotting scripts."""
import os,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class LabTests(unittest.TestCase):
 def test_dataset(self):
  import pandas as pd
  d=pd.read_csv(ROOT/"data"/"student_scores.csv"); self.assertEqual(d.shape,(10,6)); self.assertEqual(d.Student.nunique(),10); self.assertTrue(d[["Math","Science","English"]].apply(lambda s:s.between(0,100).all()).all())
 def test_scripts_compile(self):
  for f in (ROOT/"python").glob("*.py"):
   if f.name!="common.py": self.assertEqual(subprocess.run([sys.executable,"-m","py_compile",str(f)],capture_output=True).returncode,0)
 def test_charts_run(self):
  env=os.environ.copy(); env["MPLBACKEND"]="Agg"
  for name in ["2B.py","2C.py","2D.py","2E.py","2F.py","2G.py"]:
   p=subprocess.run([sys.executable,str(ROOT/"python"/name)],cwd=ROOT,env=env,capture_output=True,text=True); self.assertEqual(p.returncode,0,p.stderr); self.assertIn("Saved:",p.stdout)
if __name__=="__main__": unittest.main()
