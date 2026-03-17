import pandas as pd

df = pd.read_csv("Week3_NumPy_Pandas/data.csv")

print("Original Data:")
print(df)

df = df.dropna()

print("\nAfter removing missing values:")
print(df)

print("\nAverage Age:", df["Age"].mean())
print("Average Salary:", df["Salary"].mean())