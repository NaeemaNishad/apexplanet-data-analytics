import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
folder_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\dataanalytics_Internship_Project"
file_path = os.path.join(folder_path, "cleaned_apexplanet_sales_2026.csv")
df = pd.read_csv(file_path)

print("--- NUMERICAL FIELDS DESCRIPTIVE STATISTICS ---")
print(df[['Age', 'Quantity', 'Unit_Price', 'Total_Sales']].describe())

print("\n--- CATEGORICAL FIELDS VALUE COUNTS ---")
print("\nTop 5 Cities:\n", df['City'].value_counts().head())
print("\nProduct Categories:\n", df['Category'].value_counts())

# Plot 1: Univariate Distributions
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Total_Sales'], bins=30, kde=True, color='purple')
plt.title('Distribution of Transaction Total Sales')
plt.xlabel('Total Sales ($)')

plt.subplot(1, 2, 2)
sns.countplot(data=df, x='Age_Group', order=['Gen Z', 'Millennials', 'Gen X', 'Seniors'], palette='pastel')
plt.title('Customer Demographics Breakdown')
plt.xlabel('Age Group')
plt.tight_layout()
plt.savefig(os.path.join(folder_path, "univariate_distributions.png"))
plt.show()

# Plot 2: Multivariate Analysis (Correlation Heatmap)
plt.figure(figsize=(8, 6))
numeric_cols = df[['Age', 'Quantity', 'Unit_Price', 'Total_Sales']]
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Matrix (Sales Metrics)')
plt.tight_layout()
plt.savefig(os.path.join(folder_path, "multivariate_correlation.png"))
plt.show()
