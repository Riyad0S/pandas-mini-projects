import pandas as pd

def separator():
    print("--" * 60)

df = pd.read_json("datasets/company_performance.json")

print(df.head())
separator()

print(df.tail())
separator()

df.info()
separator()

print(df.describe())
separator()

# total sales
df["total_sales"] = df["quantity"] * df["price"]

df["hire_year"] = pd.to_datetime(df["hire_date"]).dt.year

df["hire_month_name"] = pd.to_datetime(df["hire_date"]).dt.month_name()

df["hire_day_of_week"] = pd.to_datetime(df["hire_date"]).dt.day_name()


# filtering
print(df[df["hire_year"] >= 2022])
separator()

print(df[df["total_sales"] > 20000])
separator()

print(df[(df["department"] == "Engineering") & (df["total_sales"] > 10000)])
separator()

# sorting
print(df.nlargest(5, "total_sales"))
separator()

print(df.nsmallest(5, "total_sales"))
separator()

group = df.groupby("department")
print(group["price"].mean())
separator()

print(group["quantity"].sum())
separator()

print(group["total_sales"].max())
separator()

print(group["employee"].count())
separator()

print(pd.pivot_table(df, index = "department", values = "total_sales", aggfunc = "sum"))
separator()

print(pd.pivot_table(df, index = "department", values = "price", aggfunc = "mean"))
separator()

print(pd.pivot_table(df, index = "department", columns = "product", values = "quantity", aggfunc = "sum"))
separator()

def perform(total_sales):

    if total_sales >= 20000:
        return "Excellent"

    elif total_sales < 20000 and total_sales >= 10000:
        return "Good"

    else:
        return "Needs Improvement"

df["performance"] = df["total_sales"].apply(perform)
print(df)
separator()

print("Department:", group["total_sales"].sum().idxmax())
print("With:", group["total_sales"].sum().max())
separator()

group = df.groupby("employee")
print("Employee:", group["total_sales"].sum().idxmax())
print("With:", group["total_sales"].sum().max())
separator()

group = df.groupby("product")
print(group["quantity"].sum().idxmax())
separator()

print("With:", group["quantity"].sum().max())
separator()

group = df.groupby("hire_year")
print(group["hire_year"].count())
separator()

group = df.groupby("performance")
print(group["employee"].count())
separator()