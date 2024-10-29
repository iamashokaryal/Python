import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print("Data Preview:\n", df.head())

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values if any, or drop them if appropriate
df.fillna(0, inplace=True)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Extract month from Date column
df['Month'] = df['Date'].dt.month

# Group data by month and calculate total sales
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

print("Monthly Sales:\n", monthly_sales)
# Group by product and calculate total sales for each product
product_sales = df.groupby('Product')['Total_Sales'].sum()

# Sort products by sales in descending order
top_products = product_sales.sort_values(ascending=False).head(5)

print("Top-Selling Products:\n", top_products)

# Plot monthly sales
monthly_sales.plot(kind='bar', color='skyblue')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Plot top-selling products
top_products.plot(kind='bar', color='orange')
plt.title("Top-Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Save the monthly sales analysis to a new CSV file
monthly_sales.to_csv('monthly_sales_report.csv')

# Save the top products report
top_products.to_csv('top_products_report.csv')

