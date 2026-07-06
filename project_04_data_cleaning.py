import pandas as pd

def separate():
    print("--" * 60)

df = pd.read_json("datasets/data_cleaning.json")

# displaying the first 5 rows
print(df.head(5))
separate()

# displaying the last 5 rows
print(df.tail(5))
separate()

# displaying the data frame info
df.info()
separate()

# displaying the data frame statistics
print(df.describe())
separate()

# checking if theres a null value
print(df.isna().sum())
separate()

# replacing null age values with -1
df["age"] = df["age"].fillna(-1)
print(df[["name", "age"]])
separate()

# replace missing salary with average salary
df["salary"] = df["salary"].fillna(df["salary"].mean())
print(df[["name", "salary"]])
separate()

# replace missing department with Unknown
df["department"] = df["department"].fillna("Unknown")
print(df)
separate()

# counting duplicated rows
print(df.duplicated(subset = ["name", "age", "department", "salary"]).sum())
separate()

# dropping duplicated rows
df = df.drop_duplicates(subset = ["name", "age", "department", "salary"])
print(df)
separate()

# counting duplicated rows again to make sure every duplicated row has been deleted
print(df.duplicated(subset = ["name", "age", "department", "salary"]).sum())
separate()

# replacing department names
df["department"] = df["department"].replace({
                  "IT": "AI Engineering",
                  "HR": "Human Resources" })

print(df[["name", "department"]])
separate()

# renaming salary column
df = df.rename(columns = {
    "salary": "monthly_salary" })

print(df)
separate()

# displaying the average salary and number of employees for each department
grouped = df.groupby(["department"])

print(grouped["monthly_salary"].mean())
separate()
print(grouped["id"].count())
separate()