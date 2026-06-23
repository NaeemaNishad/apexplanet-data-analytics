import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
folder_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\dataanalytics_Internship_Project\task3"
file_path = os.path.join(folder_path, "cleaned_apexplanet_sales_2026.csv")
df = pd.read_csv(file_path)

# Preview dataset
print("===== DATASET INFO =====")
print(df.info())

print("\n===== FIRST 5 RECORDS =====")
print(df.head())

# Convert date column to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Check data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# =====================================================
# STEP 2: KPI CALCULATIONS
# =====================================================

total_revenue = df["Total_Sales"].sum()

total_orders = df["Order_ID"].nunique()

total_units_sold = df["Quantity"].sum()

unique_customers = df["Customer_ID"].nunique()

average_order_value = total_revenue / total_orders

revenue_per_customer = total_revenue / unique_customers

print("\n===== CORE KPIs =====")

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Unique Customers: {unique_customers}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Revenue per Customer: ₹{revenue_per_customer:,.2f}")

# =====================================================
# STEP 3: CUSTOMER SEGMENTATION
# =====================================================
customer_sales = df.groupby(
    ["Customer_ID", "Customer_Name"]
)["Total_Sales"].sum().reset_index()

customer_sales["Segment"] = pd.qcut(
    customer_sales["Total_Sales"],
    q=3,
    labels=["Low Value", "Medium Value", "High Value"]
)

print("\n===== CUSTOMER SEGMENTS =====")
print(customer_sales.head())

# =====================================================
# STEP 4: SEGMENT SUMMARY
# =====================================================
segment_summary = customer_sales.groupby(
    "Segment",
    observed=False
).agg(
    Customers=("Customer_ID", "count"),
    Revenue=("Total_Sales", "sum"),
    Avg_Revenue=("Total_Sales", "mean")
)

print("\n===== SEGMENT SUMMARY =====")
print(segment_summary)

# =====================================================
# STEP 5: Visualizations
# =====================================================
#Chart 1: Revenue by Customer Segment
plt.figure(figsize=(8,5))

segment_summary["Revenue"].plot(kind="bar")

plt.title("Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

#Chart 2: Customer Distribution
plt.figure(figsize=(7,7))

segment_summary["Customers"].plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Customer Distribution by Segment")

plt.show()

# =====================================================
#Age Group Performance
# =====================================================
age_analysis = df.groupby("Age_Group").agg(
    Revenue=("Total_Sales", "sum"),
    Orders=("Order_ID", "count")
)

print("\n===== AGE GROUP ANALYSIS =====")
print(age_analysis)

#Chart 3: Revenue by Age Group Chart
plt.figure(figsize=(8,5))

age_analysis["Revenue"].plot(kind="bar")

plt.title("Revenue by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
# =====================================================
# CATEGORY ANALYSIS
# =====================================================

category_analysis = df.groupby("Category").agg(
    Revenue=("Total_Sales", "sum"),
    Orders=("Order_ID", "count"),
    Units_Sold=("Quantity", "sum")
)

print("\n===== CATEGORY ANALYSIS =====")
print(category_analysis.sort_values(
    by="Revenue",
    ascending=False
))

#Chart 4: Category Revenue Chart
plt.figure(figsize=(8,5))

category_analysis["Revenue"].sort_values().plot(
    kind="barh"
)

plt.title("Revenue by Product Category")
plt.xlabel("Revenue")
plt.ylabel("Category")

plt.tight_layout()
plt.show()

# =====================================================
# MONTHLY SALES TREND
# =====================================================

monthly_sales = df.groupby("Year_Month").agg(
    Revenue=("Total_Sales", "sum")
)

print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales)

#Chart 5: Monthly Revenue Trend
plt.figure(figsize=(10,5))

monthly_sales["Revenue"].plot(
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)
plt.tight_layout()

plt.show()

# JSON exports
segment_summary.to_json("segment_summary.json")
category_analysis.to_json("category_analysis.json")
monthly_sales.to_json("monthly_sales.json")
customer_sales.to_json("customer_segments.json", orient="records")

# CSV exports
segment_summary.to_csv("segment_summary.csv")
category_analysis.to_csv("category_analysis.csv")
monthly_sales.to_csv("monthly_sales.csv")
customer_sales.to_csv("customer_segments.csv", index=False)

print("\nFiles exported successfully!")