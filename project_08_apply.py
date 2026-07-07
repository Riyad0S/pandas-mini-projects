import pandas as pd

def separator():
    print("--" * 60)

def salary_bonus(salary):
    if salary <= 10000:
        return salary + 2000
    else:
        return salary + 1000

def salary_level(salary):
    if salary < 10000:
        return "low"
    else:
        return "high"

df = pd.read_json("datasets/apply.json")
print(df)
separator()

print(df.head(3))
separator()
print(df.tail(3))
separator()

df["salary_level"] = df["salary"].apply(salary_level)

print(df)

df["new_salary"] = df["salary"].apply(salary_bonus)



group = df.groupby("salary_level")
print(group["salary_level"].count())