import pandas as pd 

data = {
    "Name": ["Abhinav", "Amod", "Karan", "David"],
    "Age":  [20, 19, 20, 21],
    "Salary": [200000, 30000, 40000, 50000],
}
df = pd.DataFrame(data)

# Filter Rows 
print(df[df["Age"] > 19])       # only age above 19
print(df[df["Salary"] > 40000]) # only salary above 40000

# Combine Codition

# AND condition
print(df[(df["Age"] > 19) & (df["Salary"] > 40000)])

# OR Condition 
print(df[(df["Age"] > 20) | (df["Salary"] > 100000 )])

# Add New Column 
df["Bonus"] = df["Salary"] * 0.23
print(df)

# Drop a Column 
df =  df.drop("Bonus", axis=1)
print(df)

# Update A value 
df.loc[0,"Salary"] = 250000 # change Abhinav's salary
df.loc[0,"Age"] = 22 # Chnge Abhinav's age
print(df)
