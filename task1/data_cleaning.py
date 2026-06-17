import pandas as pd
import numpy as np
import os

# 1. Path Configuration
folder_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\dataanalytics_Internship_Project"
input_file = os.path.join(folder_path, "ApexPlanet_DataAnalytics_Dataset.xlsx")
output_file = os.path.join(folder_path, "cleaned_apexplanet_sales_2026.csv")

print("Initializing ApexPlanet Data Analytics Cleaning Pipeline...\n")

# Load raw excel data
df = pd.read_excel(input_file)

# --- STEP 1: REMEDIATION & IMPUTATION ---

# Check and remove exact duplicates if present
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
print(f"Removed {initial_rows - df.shape[0]} duplicate entries.")

# Fill missing numerical customer ages with the median age 
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing categorical cities with 'Unknown'
df['City'] = df['City'].fillna('Unknown')


# --- STEP 2: TYPE STANDARDIZATION ---

# Convert Date strings into active Pandas Datetime types
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Cast Age from a float decimal layout into clear integers
df['Age'] = df['Age'].astype(int)


# --- STEP 3: FEATURE ENGINEERING ---

# Feature 1: Demographic Grouping (Age Cohorts)
age_bins = [0, 25, 45, 65, np.inf]
age_labels = ['Gen Z', 'Millennials', 'Gen X', 'Seniors']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Feature 2: Time Intelligence Key (Year-Month extraction)
df['Year_Month'] = df['Order_Date'].dt.to_period('M').astype(str)


# --- STEP 4: VALIDATION & OUTPUT ---
print("\n--- CLEANED PIPELINE METRICS ---")
df.info()

# Export clean version as a CSV for easy upload & database ingestion
df.to_csv(output_file, index=False)
print(f"\nPipeline successfully saved your new dataset to:\n{output_file}")
