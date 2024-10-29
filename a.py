import pandas as pd

# Sample data dictionary
data = {
    "Date": [
        "2024-01-05", "2024-01-15", "2024-02-01", "2024-02-10",
        "2024-03-03", "2024-03-18", "2024-04-05", "2024-04-12",
        "2024-05-05", "2024-05-20", "2024-06-10", "2024-06-20",
        "2024-07-10", "2024-07-15", "2024-08-01", "2024-08-10",
        "2024-09-05", "2024-09-12", "2024-10-01", "2024-10-15"
    ],
    "Product": [
        "Product A", "Product B", "Product C", "Product A",
        "Product D", "Product B", "Product C", "Product E",
        "Product A", "Product C", "Product D", "Product B",
        "Product E", "Product A", "Product C", "Product D",
        "Product B", "Product A", "Product C", "Product E"
    ],
    "Quantity": [10, 5, 20, 15, 8, 12, 25, 7, 18, 20, 10, 5, 10, 20, 30, 15, 10, 5, 18, 8],
    "Price": [15, 25, 10, 15, 30, 25, 10, 35, 15, 10, 30, 25, 35, 15, 10, 30, 25, 15, 10, 35],
}

# Calculate total sales
data["Total_Sales"] = [q * p for q, p in zip(data["Quantity"], data["Price"])]

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sales_data.csv", index=False)
