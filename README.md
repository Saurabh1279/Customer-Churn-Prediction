# 📊 Customer Churn Prediction

## 🚀 Project Overview

Customer churn is one of the most critical business challenges faced by telecom companies. Retaining existing customers is often more cost-effective than acquiring new ones. This project aims to predict whether a customer is likely to churn based on their demographic information, account details, and subscribed services.

Using the IBM Telco Customer Churn Dataset, multiple machine learning models were trained and evaluated to identify customers at risk of leaving the company.

---

## 🎯 Objectives

- Analyze customer behavior and service usage patterns.
- Identify factors contributing to customer churn.
- Build and compare multiple machine learning models.
- Select the best-performing model based on evaluation metrics.
- Deploy the final model using Streamlit.

---

## 📂 Dataset Information

**Dataset:** IBM Telco Customer Churn Dataset

### Dataset Summary

| Attribute | Value |
|------------|--------|
| Total Records | 7,043 |
| Features | 21 |
| Target Variable | Churn |
| Problem Type | Binary Classification |

### Target Variable

| Value | Meaning |
|---------|---------|
| Yes | Customer Churned |
| No | Customer Retained |

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- CatBoost
- Joblib
- Streamlit

### Development Environment
- VS Code
- Jupyter Notebook

---

## 📊 Exploratory Data Analysis (EDA)

Several visualizations were created to understand customer behavior and identify churn patterns.

### Key Insights

- Customers with month-to-month contracts have the highest churn rate.
- Customers with shorter tenure are more likely to leave.
- Higher monthly charges are associated with increased churn.
- Fiber optic internet users show a higher churn tendency.
- Long-term contract customers are less likely to churn.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

### Data Cleaning

- Converted `TotalCharges` from object to numeric.
- Removed missing values.
- Removed unnecessary identifier column (`customerID`).

### Feature Engineering

- Converted target variable (`Churn`) into binary format.
- Applied One-Hot Encoding to categorical features.
- Standardized numerical variables using StandardScaler.

### Train-Test Split

- Training Data: 80%
- Testing Data: 20%
- Stratified Sampling used to preserve class distribution.

---

## 🤖 Machine Learning Models

The following machine learning algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. XGBoost Classifier
5. CatBoost Classifier

---

## 📈 Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|---------|---------|---------|---------|
| Logistic Regression | 0.8038 | 0.6485 | 0.5722 | **0.6080** |
| XGBoost | 0.7839 | 0.6101 | 0.5187 | 0.5607 |
| CatBoost | 0.7775 | 0.5962 | 0.5053 | 0.5470 |
| Random Forest | 0.7882 | 0.6357 | 0.4759 | 0.5443 |
| Decision Tree | 0.7164 | 0.4661 | 0.4599 | 0.4630 |

---

## 🏆 Best Model

### Logistic Regression

The Logistic Regression model achieved the highest F1 Score and Recall among all evaluated models.

#### Performance Metrics

- Accuracy: 80.38%
- Precision: 64.85%
- Recall: 57.22%
- F1 Score: 60.80%

Therefore, Logistic Regression was selected as the final model for customer churn prediction.

---

## 📉 ROC Curve Analysis

ROC-AUC analysis was performed to evaluate the model's ability to distinguish between churned and retained customers.

The Logistic Regression model demonstrated strong classification performance and was selected as the final model.

---

## 🔍 Feature Importance

Feature importance analysis revealed that the following variables significantly influence customer churn:

- Contract Type
- Tenure
- Monthly Charges
- Total Charges
- Internet Service Type
- Online Security
- Tech Support

These features provide valuable business insights for customer retention strategies.

---

## 🌐 Streamlit Web Application

A Streamlit web application was developed to allow users to interact with the trained model and predict customer churn.

### Features

- User-friendly interface
- Customer churn prediction
- Churn probability estimation
- Real-time prediction results

Run the application locally:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── images/
│
├── models/
│   ├── customer_churn_model.pkl
│   ├── scaler.pkl
│   └── model_columns.pkl
│
├── notebooks/
│   └── customer_churn_prediction.ipynb
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📸 Project Screenshots

### Customer Churn Distribution

![Customer Churn Distribution](images/customer%20churn%20Distribution.png)

### Contract Type vs Churn

![Contract Type vs Churn](images/contract%20type%20vs%20churn.png)

### Model Comparison

![Model Comparison](images/Model%20Comparison%20Table.png)

### ROC Curve

![ROC Curve](images/ROC%20curve.png)

### Feature Importance

![Feature Importance](images/Feature%20Importance%20Chart.png)

### Streamlit Application

![Streamlit App](images/Streamlit%20App.png)

---

## 💡 Business Impact

This project can help telecom companies:

- Identify customers likely to churn.
- Develop targeted retention campaigns.
- Improve customer satisfaction.
- Reduce revenue loss due to customer attrition.

---

## 🔮 Future Improvements

- Hyperparameter Tuning using GridSearchCV
- Cross Validation
- SMOTE for handling class imbalance
- Advanced Feature Engineering
- Cloud Deployment using Streamlit Cloud
- Real-time Prediction API using Flask/FastAPI

---

## 👨‍💻 Author

**Saurabh Pradip Mahajan**

- MCA Graduate
- Data Analytics Enthusiast
- Machine Learning Practitioner

### Connect With Me

🔗 [LinkedIn](https://www.linkedin.com/in/saurabh-mahajan-/)

💻 [GitHub](https://github.com/Saurabh1279)

⭐ If you found this project useful, please consider giving it a star on GitHub!
