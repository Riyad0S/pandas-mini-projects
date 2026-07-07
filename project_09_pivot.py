import pandas as pd

def separator():
    print("--" * 60)

df = pd.read_json("datasets/pivot.json")
print(df.head(5))
separator()

df.info()
separator()

print(df.describe())
separator()

df["total_sales"] = df["quantity"] * df["price"]
print(df.head(5))
separator()

print(pd.pivot_table(df, index = "department", values = "total_sales", aggfunc = "sum"))
separator()

print(pd.pivot_table(df, index = "department", values = "price", aggfunc = "mean"))
separator()

print(pd.pivot_table(df, index = "department", values = "quantity", aggfunc = "max"))
separator()

print(df["price"].agg(["mean", "min", "max"]))

print(pd.pivot_table(df, index = "department", columns = "product", values = "quantity", aggfunc = "sum"))