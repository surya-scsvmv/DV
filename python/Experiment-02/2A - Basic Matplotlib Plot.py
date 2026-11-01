"""Experiment 2A: create a basic Matplotlib scatter plot of student math scores."""
import matplotlib.pyplot as plt

from common import load_students, save_figure

df = load_students()

fig, ax = plt.subplots(figsize=(10, 5.5))
points = ax.scatter(
    df["Student"],
    df["Math"],
    s=90,
    c=df["Math"],
    cmap="viridis",
    edgecolors="white",
    linewidths=0.8,
    zorder=3,
)

ax.set(
    title="Basic Matplotlib Plot — Student Math Scores",
    xlabel="Student",
    ylabel="Math Score (0–100)",
    ylim=(0, 105),
)
ax.grid(axis="y", linestyle="--", alpha=0.3, zorder=0)
ax.tick_params(axis="x", rotation=35)
fig.colorbar(points, ax=ax, label="Math Score")
fig.tight_layout()

print("Saved:", save_figure(fig, "2A_basic_matplotlib_plot.png"))
plt.close(fig)
