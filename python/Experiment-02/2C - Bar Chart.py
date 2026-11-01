"""Experiment 2C: calculate and plot average marks by subject."""
import matplotlib.pyplot as plt
from common import load_students,save_figure,SUBJECTS
df=load_students(); avgs=df[SUBJECTS].mean().sort_values(ascending=False); fig,ax=plt.subplots(figsize=(7.5,5)); bars=ax.bar(avgs.index,avgs.values); ax.bar_label(bars,fmt="%.1f",padding=4,fontweight="bold"); ax.set(title="Average Score by Subject",ylabel="Average score",ylim=(0,110)); ax.grid(axis="y",alpha=.25); fig.tight_layout()
print(avgs.round(2).to_string()); print("Saved:",save_figure(fig,"2C_average_bar_chart.png")); plt.close(fig)
