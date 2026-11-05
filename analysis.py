import pandas as pd
from pathlib import Path 
import matplotlib.pyplot as plt
folder=Path(__file__).resolve().parent
data=pd.read_csv(
    folder / "period_data.csv",
  header=0,
    names=["cycle","duration","pain","mood symptoms","acne"]
)
print("periodcare data analysis")
print("total participants:",len(data))
print("\nCorrect column names:")
print(data.columns.tolist())
print("\nfirst five records:")
print(data.head())

symptom_counts=data[["pain","mood symptoms","acne"]].astype(str).apply(lambda x:x.str.strip().eq("yes")).sum()
print("\nsymptom counts:")
print(symptom_counts)
symptom_counts.plot(kind="bar",
title="periodcare symptom analysis")
plt.xlabel("symptoms")
plt.ylabel("number of participants")
plt.tight_layout()
plt.savefig(folder/"periodcare_symptom_graph.png")
plt.show()












