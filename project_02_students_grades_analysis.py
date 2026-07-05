import pandas as pd

def separator():
    print("--" * 100)

df = pd.read_json("datasets/students.json")

# displaying first 5 students
print("First 5 students\n\n", df.head())
separator()

# displaying last 5 students
print("Last 5 students\n\n", df.tail())
separator()

# displaying how many rows and columns are there
print("Data frame rows and columns:\n", df.shape)
separator()

# displaying only columns number
print("Data frame column names:\n\n", df.columns)
separator()

# displaying data types
print(df.dtypes)
separator()

df.info()
separator()

# displaying statistic infos
print(df.describe())
separator()

# displaying student name, subjects enrolled in, score
print("Student name:\n", df[["name", "subject", "score"]])
separator()

# displaying highest grade
sorted_df = df.sort_values("score", ascending = False)
print("Highest grade:\n\n", sorted_df.head(1))
separator()

# displaying lowest grade
print("Lowest grade:\n\n", sorted_df.tail(1))
separator()

# displaying each subject
print(df["subject"].unique())
separator()

# counting how many students enrolled in each subject
print(df["subject"].value_counts())
separator()

# displaying students with grade higher than or equals 90
print(df[(df["score"] >= 90)])
separator()

# displaying students with grade lower than 70
print(df[(df["score"] < 70)])
separator()

# creating a new column named passed
df["passed"] = df["score"] >= 70
print(df.head())
separator()

# showing only students that passed
print(df[(df["passed"])])
separator()

# showing only students that failed
print(df[(df["passed"] == False)])
separator()

# Sorting students from higher score to lower
sorted_df = df.sort_values("score", ascending = False)
print("Sorted students\n\n", sorted_df)
separator()

# sorting subjects alphabetically and scores from descendingly
sorted_df = df.sort_values(["subject", "score"], ascending = [ True, False])
print("Sorted students\n\n", sorted_df)
separator()