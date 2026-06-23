import pandas as pd
import os

folder_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\dataanalytics_Internship_Project"
file_path = os.path.join(folder_path, "cleaned_apexplanet_sales_2026.csv")
df = pd.read_csv(file_path)

# -----------------------------
# KPI 1: Total Revenue
# -----------------------------
total_revenue = df["Total_Sales"].sum()

# -----------------------------
# KPI 2: Total Orders
# -----------------------------
total_orders = df["Order_ID"].nunique()

# -----------------------------
# KPI 3: Total Units Sold
# -----------------------------
total_units_sold = df["Quantity"].sum()

# -----------------------------
# KPI 4: Average Order Value
# -----------------------------
average_order_value = total_revenue / total_orders

# -----------------------------
# KPI 5: Unique Customers
# -----------------------------
unique_customers = df["Customer_ID"].nunique()

# -----------------------------
# KPI 6: Revenue per Customer
# -----------------------------
revenue_per_customer = total_revenue / unique_customers

#Print Results
print("===== CORE KPIs =====")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Unique Customers: {unique_customers}")
print(f"Revenue per Customer: ₹{revenue_per_customer:,.2f}")