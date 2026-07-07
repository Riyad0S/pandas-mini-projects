import pandas as pd

def separate():
    print("--" * 60)

df = pd.read_json("datasets/dates.json")

print(df.head())
separate()
print(df.tail())
separate()

df.info()
separate()

print(df.dtypes)
separate()

# converting hire_date into a date instead of string
df["hire_date"] = pd.to_datetime(df["hire_date"])
print(df.dtypes)
separate()

# creating a new column named hire_year and adding the number of the year to it
df["hire_year"] = df["hire_date"].dt.year
print(df)
separate()

# creating a new column named hire_month and adding the number of the month to it
df["hire_month"] = df["hire_date"].dt.month
print(df)
separate()

# creating a new column named month_name and adding the name of the month to it
df["month_name"] = df["hire_date"].dt.month_name()
print(df)
separate()

# creating a new column named day_of_week and adding the name of the day to it
df["day_of_week"] = df["hire_date"].dt.day_name()
print(df)
separate()

print(df[["name", "hire_date", "hire_year", "month_name"]])
separate()

print(df[df["hire_year"] >= 2022])
separate()

sorted_df = df.sort_values("hire_year", ascending = False)
print(sorted_df)
separate()

grouped = df.groupby("hire_year")
print(grouped["hire_year"].count())
separate()