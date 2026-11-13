import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv(r"add titanic csv file path here")

print("Original Dataset")
print(df.head())

print("\nMISSING VALUES BEFORE PROCESSING")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)

df["Sex"] = LabelEncoder().fit_transform(df["Sex"])
df = pd.get_dummies(df, columns=["Embarked"], dtype=int)

print("\nDataset After Encoding: ")
print(df.head())

cols = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
df[cols] = StandardScaler().fit_transform(df[cols])

print("\nDataset After Scaling: ")
print(df.head())

print("\nFinal Dataset: ")
print(df.head())

df.to_csv("cleaned_dataset.csv")