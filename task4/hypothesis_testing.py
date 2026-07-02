import pandas as pd
from scipy.stats import f_oneway

# Load dataset
df = pd.read_csv("cleaned_apexplanet_sales_2026.csv")

# Group sales by age group
genz = df[df["Age_Group"] == "Gen Z"]["Total_Sales"]
millennials = df[df["Age_Group"] == "Millennials"]["Total_Sales"]
genx = df[df["Age_Group"] == "Gen X"]["Total_Sales"]

# Perform One-Way ANOVA
f_stat, p_value = f_oneway(genz, millennials, genx)

print("========== HYPOTHESIS TEST ==========")
print(f"F-Statistic : {f_stat:.4f}")
print(f"P-Value     : {p_value:.4f}")

alpha = 0.05

if p_value < alpha:
    print("\nResult:")
    print("Reject the Null Hypothesis")
    print("Average spending differs significantly across age groups.")
else:
    print("\nResult:")
    print("Fail to Reject the Null Hypothesis")
    print("No significant difference in average spending across age groups.")