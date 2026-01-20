# Project: E-Commerce Operational Efficiency Analysis
# Author: Giorgos Pantsios
# Date: January 2026

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- STEP 1: LOAD DATA ---
# In a real environment, you would use: df = pd.read_csv('Amazon Sale Report.csv')
# For this portfolio file, we are defining the path clearly.
file_path = 'Amazon Sale Report.csv'

try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully.")
except FileNotFoundError:
    print("File not found. Please ensure the CSV is in the same directory.")

# --- STEP 2: DATA CLEANING (Phase 3: Process) ---

# 2.1 Drop irrelevant columns / technical artifacts
# 'index' and 'Unnamed: 22' were identified as redundant in the initial review.
df.drop(['index', 'Unnamed: 22'], axis=1, inplace=True, errors='ignore')

# 2.2 Handle Missing Values
# We identified that missing 'Amount' values correlate with Cancelled/Returned orders.
# We impute 0.0 to keep the record for volume analysis without skewing revenue sums.
df['Amount'].fillna(0.0, inplace=True)

# 2.3 Drop rows where critical categorical data is missing (if any)
df.dropna(subset=['Status', 'Fulfilment'], inplace=True)

# 2.4 Convert Data Types
# Convert 'Date' to datetime objects for potential time-series analysis
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# --- STEP 3: ANALYSIS (Phase 4: Analyze) ---

# 3.1 Calculate Total Orders per Fulfillment Method
fulfillment_counts = df['Fulfilment'].value_counts().reset_index()
fulfillment_counts.columns = ['Fulfillment_Method', 'Total_Orders']

# 3.2 Filter for Cancelled Orders
# We filter for statuses that explicitly indicate a cancellation
cancelled_df = df[df['Status'].isin(['Cancelled', 'Cancelled by Seller'])]
cancel_counts = cancelled_df['Fulfilment'].value_counts().reset_index()
cancel_counts.columns = ['Fulfillment_Method', 'Cancelled_Orders']

# 3.3 Merge and Calculate Rates
analysis_df = pd.merge(fulfillment_counts, cancel_counts, on='Fulfillment_Method')

# Calculate the percentage
analysis_df['Cancel_Rate_%'] = (analysis_df['Cancelled_Orders'] / analysis_df['Total_Orders']) * 100
analysis_df['Cancel_Rate_%'] = analysis_df['Cancel_Rate_%'].round(2)

print("--- FINAL ANALYSIS RESULTS ---")
print(analysis_df)

# --- STEP 4: VISUALIZATION (Phase 5: Share) ---

# Setting the style for professional reports
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Chart 1: Total Volume
sns.barplot(x='Fulfillment_Method', y='Total_Orders', data=analysis_df, ax=axes[0], palette='viridis')
axes[0].set_title('Total Orders by Fulfillment Method')
axes[0].set_ylabel('Order Volume')

# Chart 2: Cancellation Rate
sns.barplot(x='Fulfillment_Method', y='Cancel_Rate_%', data=analysis_df, ax=axes[1], palette='magma')
axes[1].set_title('Cancellation Risk (%) by Fulfillment Method')
axes[1].set_ylabel('Cancellation Rate (%)')
axes[1].set_ylim(0, 20) # Setting limit to make comparison clear

# Add value labels to the Cancellation Chart
for index, row in analysis_df.iterrows():
    axes[1].text(index, row['Cancel_Rate_%'] + 0.2, f"{row['Cancel_Rate_%']}%", 
                 color='black', ha="center")

plt.tight_layout()
plt.savefig('fulfillment_analysis_results.png')
print("Charts saved as 'fulfillment_analysis_results.png'")