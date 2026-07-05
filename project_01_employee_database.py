import pandas as pd
def separator():
    print("-" * 100)
df = pd.read_json("datasets/new_employees.json")

print("Data frame info: \n")
df.info()
separator()

# # Showing the whole data frame
# print("Whole data frame:\n\n", df)
# print("--" * 50)

# changing the full_time column into boolean instead of 0's and 1's
df["full_time"] = df["full_time"].astype(bool)
print(df)
separator()

# displaying first 10 employees
print("First 10 employees:\n\n", df.head(10))
separator()

# displaying last 5 employees
print("Last 5 employees:\n\n", df.tail(5))
separator()

# displaying data frame rows and columns
print("Data frame shape:\n\n", df.shape)
separator()

# displaying data frame columns alone
print("Data frame columns:\n", df.columns)
separator()

# displaying data frame data types
print(df.dtypes)
separator()

print(df.describe())
separator()

# displaying name and salary
print(df[["name", "salary"]])
separator()

# displaying employees older than 36
print(df[df["age"] >= 36])
separator()

# displaying employees with salary higher than 12k
print(df[df["salary"] >= 12000])
separator()

# displaying employees older than 35 and working full time
print("Employees that are older than 35 and works full job:\n",
      df[(df["age"] >= 35) & (df["full_time"] == True)])
separator()

# displaying employees that works in engineering or have salary higher than 10000
print(df[(df["department"] == "Engineering") | (df["salary"] >= 10000)])
separator()