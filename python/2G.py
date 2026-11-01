"""Experiment 2G: compare subject-score distributions using box plots."""
import matplotlib.pyplot as plt
import seaborn as sns
from common import load_students,save_figure,SUBJECTS
df=load_students(); long=df.melt(id_vars="Student",value_vars=SUBJECTS,var_name="Subject",value_name="Score"); fig,ax=plt.subplots(figsize=(8,5.5)); sns.boxplot(data=long,x="Subject",y="Score",hue="Subject",legend=False,showmeans=True,ax=ax); sns.stripplot(data=long,x="Subject",y="Score",color="black",alpha=.45,size=4,jitter=.12,ax=ax); ax.set(title="Score Distribution by Subject",xlabel="Subject",ylabel="Score",ylim=(50,105)); ax.grid(axis="y",alpha=.2); fig.tight_layout(); print("Saved:",save_figure(fig,"2G_subject_boxplots.png")); plt.close(fig)
