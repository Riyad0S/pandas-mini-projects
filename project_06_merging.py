import pandas as pd

def separate():
    print("--" * 60)

df1 = pd.read_json("datasets/employees.json")
df2 = pd.read_json("datasets/salaries.json")

print(df1)
separate()

print(df2)
separate()

# merging 2 data frames
merged_df = pd.merge(df1, df2, on = "id", how = "outer")
print(merged_df)
separate()

# displaying employees with salaries more than 12000
print(merged_df[merged_df["monthly_salary"] >= 12000])
separate()

grouped_df = merged_df.groupby("department")

# displaying average max and min for each department
print(grouped_df["monthly_salary"].agg(["mean", "max", "min"]))
separate()

# creating a new column
merged_df["annual_salary"] = merged_df["monthly_salary"] * 12

print(merged_df.nlargest(3, "monthly_salary"))
separate()

print(merged_df.nsmallest(3, "monthly_salary"))
separate()
