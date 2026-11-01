"""Experiment 2D: inspect the distribution of mathematics scores."""
import matplotlib.pyplot as plt
from common import load_students,save_figure
df=load_students(); mean=df.Math.mean(); fig,ax=plt.subplots(figsize=(7.5,5)); ax.hist(df.Math,bins=5,edgecolor="white",alpha=.9); ax.axvline(mean,ls="--",lw=2,label=f"Mean: {mean:.1f}"); ax.set(title="Distribution of Mathematics Scores",xlabel="Math score",ylabel="Number of students"); ax.legend(frameon=False); ax.grid(axis="y",alpha=.2); fig.tight_layout()
print("Saved:",save_figure(fig,"2D_math_histogram.png")); plt.close(fig)
