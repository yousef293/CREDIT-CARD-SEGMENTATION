# K-Means Clustering on Credit Card Data

This project applies the K-Means clustering algorithm to segment credit card customers based on their spending patterns and payment behaviors. The goal is to uncover meaningful customer groups to help financial institutions improve targeted marketing and customer service.

---

## 📊 Dataset Description

Each row in the dataset represents a credit card holder, and each column describes various aspects of their credit and purchasing behavior:

| Feature | Description |
|--------|-------------|
| **CUST_ID** | Unique credit card holder ID |
| **BALANCE** | Monthly average balance (based on daily balances) |
| **BALANCE_FREQUENCY** | Ratio of months with non-zero balance |
| **PURCHASES** | Total purchase amount in the last 12 months |
| **ONEOFF_PURCHASES** | Total of one-time purchases |
| **INSTALLMENTS_PURCHASES** | Total of purchases paid via installments |
| **CASH_ADVANCE** | Total amount of cash advances |
| **PURCHASES_FREQUENCY** | % of months with at least one purchase |
| **ONEOFF_PURCHASES_FREQUENCY** | Frequency of one-off purchases |
| **PURCHASES_INSTALLMENTS_FREQUENCY** | Frequency of installment purchases |
| **CASH_ADVANCE_FREQUENCY** | Frequency of cash advances |
| **AVERAGE_PURCHASE_TRX** | Average amount per purchase transaction |
| **CASH_ADVANCE_TRX** | Average amount per cash advance transaction |
| **PURCHASES_TRX** | Number of purchase transactions |
| **CREDIT_LIMIT** | Credit limit of the customer |
| **PAYMENTS** | Total payments made by the customer |
| **MINIMUM_PAYMENTS** | Total minimum payments due |
| **PRC_FULL_PAYMENT** | % of months with full balance payments |
| **TENURE** | Number of months as a customer |

---

## 🎯 Objective

- **Preprocess** the dataset (handle missing values, scale features)
- **Apply K-Means Clustering** to segment customers
- **Visualize clusters** and interpret the behavior of each group
- **Generate insights** for business decisions such as targeted campaigns or credit offerings

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

---
