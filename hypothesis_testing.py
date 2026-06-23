import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
df = pd.read_excel('ApexPlanet_DataAnalytics_Dataset.xlsx')

# Hypothesis 1: Male vs Female Total Sales difference
male_sales = df[df['Gender'] == 'Male']['Total_Sales']
female_sales = df[df['Gender'] == 'Female']['Total_Sales']

t_stat, p_value = stats.ttest_ind(male_sales, female_sales)

print("=== HYPOTHESIS TEST 1 ===")
print("H0: No significant difference between Male & Female sales")
print("H1: Significant difference exists")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Result: REJECT H0 - Significant difference exists!")
else:
    print("Result: FAIL TO REJECT H0 - No significant difference!")

# Hypothesis 2: Electronics vs Other categories
electronics = df[df['Category'] == 'Electronics']['Total_Sales']
others = df[df['Category'] != 'Electronics']['Total_Sales']

t_stat2, p_value2 = stats.ttest_ind(electronics, others)

print("\n=== HYPOTHESIS TEST 2 ===")
print("H0: Electronics sales = Other categories sales")
print("H1: Electronics sales significantly different")
print(f"T-statistic: {t_stat2:.4f}")
print(f"P-value: {p_value2:.4f}")
if p_value2 < 0.05:
    print("Result: REJECT H0 - Electronics significantly different!")
else:
    print("Result: FAIL TO REJECT H0 - No significant difference!")

# Correlation Analysis
print("\n=== CORRELATION ANALYSIS ===")
correlation = df['Unit_Price'].corr(df['Total_Sales'])
print(f"Correlation between Unit_Price & Total_Sales: {correlation:.4f}")

print("\n=== STATISTICAL SUMMARY ===")
print(df[['Age', 'Quantity', 'Unit_Price', 'Total_Sales']].describe())