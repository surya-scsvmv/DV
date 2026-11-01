"""Smoke tests for the Python dataset and visualization exercises."""
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON_01 = ROOT / "python" / "Experiment-01"
PYTHON_02 = ROOT / "python" / "Experiment-02"

class LabTests(unittest.TestCase):
    def test_dataset(self):
        import pandas as pd
        data = pd.read_csv(ROOT / "data" / "student_scores.csv")
        self.assertEqual(data.shape, (10, 6))
        self.assertEqual(data.Student.nunique(), 10)
        self.assertTrue(data[["Math", "Science", "English"]].apply(
            lambda column: column.between(0, 100).all()
        ).all())

    def test_scripts_compile(self):
        for folder in (PYTHON_01, PYTHON_02):
            for script in folder.glob("*.py"):
                result = subprocess.run(
                    [sys.executable, "-m", "py_compile", str(script)],
                    capture_output=True, text=True
                )
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_charts_run(self):
        env = os.environ.copy()
        env["MPLBACKEND"] = "Agg"
        names = [
            "2B - Line Chart.py",
            "2C - Bar Chart.py",
            "2D - Histogram.py",
            "2E - Scatter Plot.py",
            "2F - Correlation Heatmap.py",
            "2G - Box Plot.py",
        ]
        for name in names:
            result = subprocess.run(
                [sys.executable, str(PYTHON_02 / name)],
                cwd=ROOT, env=env, capture_output=True, text=True
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Saved:", result.stdout)

if __name__ == "__main__":
    unittest.main()
