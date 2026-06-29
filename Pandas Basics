# Pandas practice
# Created By Abhinav 
#Topic: DataFrame basics

import pandas as pd

data = {
    "Name": ["Abhinav", "Amod", "Karan", "David"],
    "Age":  [20, 19, 20, 21],
    "Salary": [200000, 30000, 40000, 50000],
}

df = pd.DataFrame(data)
print(df)            
print(df.head())     # Shows first 5 rows
print(df.shape)     # (rows,columns)
print(df.info())    # Information about data 
print(df.describe()) # Gives statistics automatically - mean,min,max etc.
print(df["Age"])     # Slicing using index name 
print(df["Name"])
print(df["Salary"]>40000)
print(df.sort_values("Age"))
print(df.sort_values("Age",ascending=False))
