"""Experiment 2F: visualise correlations among numeric student metrics."""
import matplotlib.pyplot as plt
import seaborn as sns
from common import load_students,save_figure,SUBJECTS
df=load_students(); corr=df[SUBJECTS+["Hours_Studied","Age"]].corr(numeric_only=True); fig,ax=plt.subplots(figsize=(8,6)); sns.heatmap(corr,annot=True,fmt=".2f",cmap="vlag",center=0,vmin=-1,vmax=1,square=True,linewidths=.5,ax=ax); ax.set_title("Correlation Matrix of Student Metrics",pad=14); fig.tight_layout(); print("Saved:",save_figure(fig,"2F_correlation_heatmap.png")); plt.close(fig)
