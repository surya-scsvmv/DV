"""Experiment 2E: study time versus marks with a fitted linear trend."""
import matplotlib.pyplot as plt
import numpy as np
from common import load_students,save_figure
df=load_students(); x=df.Hours_Studied; y=df.Math; slope,intercept=np.polyfit(x,y,1); line=np.linspace(x.min(),x.max(),100); fig,ax=plt.subplots(figsize=(8,5.5)); points=ax.scatter(x,y,c=y,cmap="viridis",s=85,edgecolors="white"); ax.plot(line,slope*line+intercept,ls="--",lw=2,label="Linear trend")
for _,r in df.iterrows(): ax.annotate(r.Student,(r.Hours_Studied,r.Math),xytext=(4,5),textcoords="offset points",fontsize=8)
fig.colorbar(points,ax=ax,label="Math score"); ax.set(title="Study Hours vs Mathematics Score",xlabel="Hours studied",ylabel="Math score"); ax.legend(frameon=False); ax.grid(alpha=.2); fig.tight_layout(); print(f"Pearson correlation: {x.corr(y):.3f}"); print("Saved:",save_figure(fig,"2E_study_hours_scatter.png")); plt.close(fig)
