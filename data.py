import pandas as pd

# Load your actual files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all data
df = pd.concat([df1, df2, df3])

# Keep only pink morsel
df = df[df["product"] == "pink morsel"]

# Clean price (remove $ and convert to float)
df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

# Create Sales column
df["Sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["Sales", "date", "region"]]

# Rename columns
df.columns = ["Sales", "Date", "Region"]

# Save output
df.to_csv("formatted_data.csv", index=False)

print("Done!")