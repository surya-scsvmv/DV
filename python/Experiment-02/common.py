"""Shared utilities for the Python visualization exercises."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "student_scores.csv"
OUTPUT_DIR = ROOT / "output"
SUBJECTS = ["Math", "Science", "English"]

def load_students():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}. Run the dataset experiment first.")
    df = pd.read_csv(DATA_FILE)
    required = {"Student", *SUBJECTS, "Age", "Hours_Studied"}
    missing = required.difference(df.columns)
    if missing or df.empty:
        raise ValueError(f"Invalid dataset; missing columns: {sorted(missing)}")
    return df

def save_figure(fig, filename):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    fig.savefig(path, dpi=180, bbox_inches="tight")
    return path
