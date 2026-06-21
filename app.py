import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("models/customer_churn_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

st.title("📊 Customer Churn Prediction")

# User Inputs
# Numerical Inputs
tenure = st.slider("Tenure (Months)", 0, 72, 12)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

# Predict Button
if st.button("Predict Churn"):

    # Create dataframe with ALL model columns
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    # Fill numerical features
    if 'tenure' in input_data.columns:
        input_data['tenure'] = tenure

    if 'MonthlyCharges' in input_data.columns:
        input_data['MonthlyCharges'] = monthly_charges

    if 'TotalCharges' in input_data.columns:
        input_data['TotalCharges'] = total_charges

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(
            f"⚠️ Customer likely to churn\n\nProbability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Customer likely to stay\n\nProbability of churn: {probability:.2%}"
        )