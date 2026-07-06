import pandas as pd

def separate():
    print("--" * 70)

# reading the file and creating a data frame
df = pd.read_json("datasets/sales.json")

# display first 5 employees
print("First 5 employees:\n\n", df.head(5))
separate()

# display last 5 employees
print("Last 5 employees:\n\n", df.tail(5))
separate()

# displaying data frame infos
df.info()
separate()

# display data types
print(df.dtypes)
separate()

# displaying statistical infos
print(df.describe())
separate()

# creating a new column named Total_sales and printing some stuff
df["total_sales"] = df["quantity"] * df["price"]
print(df[["employee", "department", "total_sales"]])
separate()

# displaying only employee, product, total sale
print(df[["employee", "product", "total_sales"]])
separate()

# displaying the product with highest price
sorted_df = df.sort_values("total_sales", ascending = False)
print(sorted_df.head(1))
separate()

# displaying the product with lowest price
print(sorted_df.tail(1))
separate()

# displaying mean, max, min for each department
group = df.groupby("department")
print("Average price:\n", group["price"].mean())
separate()
print("Maximum price:\n", group["price"].max())
separate()
print("Minimum price:\n", group["price"].min())
separate()

# displaying how many products in each department
print(group["product"].count())
separate()

# displaying total products sold
print(group["quantity"].sum())
separate()

# # displaying the highest 3 items
# highest = df.sort_values("price", ascending = False)
# print(highest.head(3))
# separate()
#
# # displaying the cheapest 3 items -- or we can use highest variable with tail(3) method
# cheapest = df.sort_values("price")
# print(cheapest.head(3))
# separate()

# another way for largest and smallest
print(df.nlargest(3, "price"))
separate()

print(df.nsmallest(3, "price"))
separate()


# a really important method  df[" "].agg(["  ", "  " ... ])
print(group["price"].agg(["min", "max", "mean", "count", "sum"]))
separate()