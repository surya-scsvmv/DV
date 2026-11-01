"""Experiment 1: create, validate, inspect, and export the student dataset."""
from pathlib import Path
import pandas as pd
students=pd.DataFrame({"Student":["Srinivas","Siva","Naveen","Srinath","Ganesh","Anil","Deep","Radhakrishna","Kiran","Harsha"],"Math":[82,72,91,65,78,85,60,95,70,83],"Science":[90,82,76,88,72,80,91,85,94,80],"English":[91,78,89,88,86,87,83,92,97,90],"Age":[17,18,16,19,17,18,16,19,17,18],"Hours_Studied":[3,4,5,7,8,10,2,4,5,6]})
assert students.Student.is_unique
assert students[["Math","Science","English"]].apply(lambda s:s.between(0,100).all()).all()
out=Path(__file__).resolve().parents[1]/"data"/"student_scores.csv"; out.parent.mkdir(parents=True,exist_ok=True); students.to_csv(out,index=False)
print(students.to_string(index=False)); print("\nSummary statistics:\n",students.describe(numeric_only=True).round(2)); print(f"\nSaved to {out}")
