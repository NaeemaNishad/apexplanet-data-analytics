import pandas as pd
import pandasql as ps
import os

folder_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\dataanalytics_Internship_Project"
file_path = os.path.join(folder_path, "cleaned_apexplanet_sales_2026.csv")
df = pd.read_csv(file_path)

print("Executing SQL Business Queries on Cleaned Dataset...\n")

# Q1: What is the total gross revenue and total quantity sold across all transactions?
q1 = "SELECT SUM(Total_Sales) as Gross_Revenue, SUM(Quantity) as Total_Units_Sold FROM df;"

# Q2: Which are the top 5 generating product categories by revenue?
q2 = """
SELECT Category, SUM(Total_Sales) as Category_Revenue
FROM df
GROUP BY Category
ORDER BY Category_Revenue DESC
LIMIT 5;
"""

# Q3: Which individual cities bring in the highest transaction volumes?
q3 = """
SELECT City, COUNT(Order_ID) as Order_Count, SUM(Total_Sales) as City_Revenue
FROM df
GROUP BY City
ORDER BY Order_Count DESC
LIMIT 5;
"""

# Q4: How does performance split across different age demographics?
q4 = """
SELECT Age_Group, COUNT(Order_ID) as Sales_Volume, ROUND(AVG(Total_Sales), 2) as Avg_Order_Value
FROM df
GROUP BY Age_Group
ORDER BY Sales_Volume DESC;
"""

# Q5: What is the monthly sales trend to identify peak performance periods?
q5 = """
SELECT Year_Month, COUNT(Order_ID) as Monthly_Orders, SUM(Total_Sales) as Monthly_Revenue
FROM df
GROUP BY Year_Month
ORDER BY Year_Month ASC;
"""

# Q6: Identify high-value customers who spent over $500,000 in total historical sales.
q6 = """
SELECT Customer_ID, Customer_Name, SUM(Total_Sales) as Lifetime_Value
FROM df
GROUP BY Customer_ID, Customer_Name
HAVING Lifetime_Value > 500000
ORDER BY Lifetime_Value DESC;
"""

queries = [q1, q2, q3, q4, q5, q6]
titles = ["Q1: Key Revenue Totals", "Q2: Revenue by Product Category", "Q3: Geographic Split", "Q4: Demographic Output", "Q5: Monthly Performance Trends", "Q6: High-Value Customers VIP List"]

for title, q in zip(titles, queries):
    print(f"=== {title} ===")
    print(ps.sqldf(q, locals()))
    print("\n" + "="*40 + "\n")
