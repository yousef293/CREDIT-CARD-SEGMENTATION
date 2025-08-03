# 💳 K-Means Clustering & AI-Powered Customer Segmentation System

This project combines **machine learning** and **web technologies** to segment credit card customers using **K-Means clustering** and serve predictive insights through a full-stack API-driven architecture. The system identifies customer behavior patterns to help financial institutions improve **marketing strategies**, **credit offerings**, and **customer management**.

---

## 📊 Dataset Description

Each row in the dataset represents a credit card holder and their historical financial behavior. The features include balance information, purchase habits, payment history, and credit usage.

| Feature                          | Description                                      |
|----------------------------------|--------------------------------------------------|
| `CUST_ID`                        | Unique credit card holder ID                     |
| `BALANCE`                        | Monthly average balance                          |
| `BALANCE_FREQUENCY`             | Ratio of months with non-zero balance            |
| `PURCHASES`                      | Total purchase amount in the last 12 months      |
| `ONEOFF_PURCHASES`              | One-time purchase amount                         |
| `INSTALLMENTS_PURCHASES`        | Installment purchase amount                      |
| `CASH_ADVANCE`                   | Total amount of cash advances                    |
| `PURCHASES_FREQUENCY`           | Frequency of purchases across months             |
| `ONEOFF_PURCHASES_FREQUENCY`    | Frequency of one-off purchases                   |
| `PURCHASES_INSTALLMENTS_FREQUENCY` | Frequency of installment purchases          |
| `CASH_ADVANCE_FREQUENCY`        | Frequency of cash advances                       |
| `AVERAGE_PURCHASE_TRX`          | Average amount per purchase transaction          |
| `CASH_ADVANCE_TRX`              | Average amount per cash advance transaction      |
| `PURCHASES_TRX`                 | Number of purchase transactions                  |
| `CREDIT_LIMIT`                   | Credit limit assigned                            |
| `PAYMENTS`                       | Total amount of payments made                    |
| `MINIMUM_PAYMENTS`              | Total minimum payments made                      |
| `PRC_FULL_PAYMENT`              | % of months with full balance payments           |
| `TENURE`                         | Number of months as a customer                   |

---

## 🎯 Objectives

- Clean and preprocess the credit card dataset
- Apply **K-Means clustering** to group customers
- Visualize and interpret customer clusters
- Expose a **FastAPI prediction endpoint** for real-time predictions
- Build a **Node.js/Express backend** to manage data and communicate with the AI model
- Store and retrieve customer data using **MongoDB**
- Serve predictions via **HTTP APIs**

---

## 🛠️ Technologies Used

### 🧠 Machine Learning & Backend (Python)
- Python
- Scikit-learn
- Pandas, NumPy
- FastAPI
- K-Means Clustering
- Matplotlib, Seaborn

### 🌐 Web Backend (JavaScript)
- Node.js
- Express.js
- MongoDB (via Mongoose)
- RESTful APIs
- Modular architecture: `controllers/`, `routes/`, `services/`

---


