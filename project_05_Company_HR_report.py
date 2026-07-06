import pandas as pd

def separator():
    print("--" * 50)

df = pd.read_json("datasets/company_hr.json")

# display first and last 5 employees
print("First 5 employees:\n", df.head(5))
separator()
print("Last 5 employees:\n", df.tail(5))
separator()

# checking if there's not assigned values
print("Checking if theres values not assigned:\n", df.isna())
separator()
# filling not assigned values for - age, department, monthly salary, full time -
df["age"] = df["age"].fillna(-1)
df["department"] = df["department"].fillna("Unknown")
df["monthly_salary"] = df["monthly_salary"].fillna(df["monthly_salary"].mean())
df["full_time"] = df["full_time"].fillna(0)

# checking  for duplicated values
print("How many duplicated employees:\n", df.duplicated(["name", "age", "department", "monthly_salary", "full_time"]).sum())
separator()
df = df.drop_duplicates(["name", "age", "department", "monthly_salary", "full_time"])

# converting full time into True or False values - Boolean -
df["full_time"] = df["full_time"].astype(bool)

# displaying employees with salary higher than 10000
print(df[df["monthly_salary"] >= 10000])
separator()

# display employee works in Engineering and older than 30
print(df[(df["department"] == "Engineering") & (df["age"] >= 30)])
separator()

# adding a new column to show yearly salary
df["annual_salary"] = df["monthly_salary"] * 12
print(df)
separator()

# displaying highest and lowest 5 employees)
print("Highest paid employees:\n", df.nlargest(5, "monthly_salary"))
separator()
print("Lowest paid employees:\n", df.nsmallest(5, "monthly_salary"))
separator()

# displaying unique departments
print(df["department"].unique())
separator()

# displaying how many workers in each department
group = df.groupby("department")
print(group["name"].count())
separator()

# displaying monthly salary's average, max, and minimum for each department
print(group["monthly_salary"].agg(["mean", "max", "min"]))
separator()

# displaying which department has the highest average salary
print("Highest department in salary:", group["monthly_salary"].mean().idxmax())
print("With average:",group["monthly_salary"].mean().max())
separator()

# renaming column monthly_salary to salary
df = df.rename(columns = {
    "monthly_salary": "salary"
})

# final data frame structure
print(df)
separator()