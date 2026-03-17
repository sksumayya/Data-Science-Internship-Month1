import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Week4_Visualization/data.csv")

plt.figure()
plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.savefig("Week4_Visualization/plots/scatter.png")

plt.figure()
plt.hist(df["Salary"])
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.savefig("Week4_Visualization/plots/histogram.png")

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("Week4_Visualization/plots/heatmap.png")

print("Plots saved successfully")