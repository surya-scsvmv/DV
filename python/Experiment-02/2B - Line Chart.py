"""Experiment 2B: compare subject marks with a line chart."""
import matplotlib.pyplot as plt
from common import load_students,save_figure,SUBJECTS
df=load_students(); fig,ax=plt.subplots(figsize=(10,5.5))
for subject,marker in zip(SUBJECTS,["o","s","^"]): ax.plot(df.Student,df[subject],marker=marker,lw=2,label=subject)
ax.set(title="Student Performance Across Subjects",xlabel="Student",ylabel="Score (0–100)",ylim=(0,105)); ax.grid(axis="y",alpha=.25); ax.tick_params(axis="x",rotation=35); ax.legend(ncol=3,frameon=False); fig.tight_layout()
print("Saved:",save_figure(fig,"2B_line_chart.png")); plt.close(fig)
