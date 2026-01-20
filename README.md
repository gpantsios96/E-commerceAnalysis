# E-Commerce Operational Efficiency Analysis 📦

**Author:** Giorgos Pantsios  
**Date:** January 2026  
**Certification:** Google Data Analytics Professional Certificate

## 📑 Executive Summary
This analysis evaluates the operational efficiency of two primary order fulfillment methods: **Amazon Fulfillment** and **Merchant Fulfillment**. By analyzing over 128,000 sales records, the study identified a critical performance gap. Amazon Fulfillment demonstrates superior reliability with a cancellation rate of **12.79%**, whereas Merchant Fulfillment lags at **17.47%**.

The project concludes that shifting high-velocity inventory to Amazon’s network could recover significant lost revenue.

## 🛠 Tools Used
- **Python:** Data cleaning, manipulation, and analysis (`Pandas`)
- **Visualization:** Bar charts and trend analysis (`Matplotlib`, `Seaborn`)
- **Data Source:** "Unlock Profits with E-commerce Sales Data" (Kaggle - CC0)

## 📊 Key Insights
| Metric | Amazon Fulfillment | Merchant Fulfillment |
| :--- | :--- | :--- |
| **Total Orders** | 89,698 | 39,277 |
| **Cancelled Orders** | 11,471 | 6,861 |
| **Cancellation Rate** | **12.79%** (Stable) | **17.47%** (High Risk) |

**Visualization of the Gap:**
![Analysis Charts](assets/fulfillment_analysis_results.png)

## 🚀 Recommendations (The "Act" Phase)
Based on the **4.68% variance** in cancellation rates, I recommended the following strategy:
1.  **Immediate Shift:** Move top-selling SKUs to Amazon Fulfillment to reduce cancellation risk by ~27%.
2.  **Process Improvement:** Implement daily inventory synchronization for Merchant fulfillment to reduce "Out of Stock" cancellations.
3.  **Target KPI:** Reduce Merchant cancellation rate to <14% in Q2.

## 📂 Project Files
- **`main.py`**: The complete Python script for cleaning, analyzing, and plotting the data.
- **`Project_Report.pdf`**: The formal business report delivered to stakeholders.

## 💻 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python main.py`
