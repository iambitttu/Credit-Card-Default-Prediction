import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model using pickle
with open('LogR_Model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a Streamlit web app
st.title("Credit Card Default Prediction Dashboard")

# Add input fields for user input
st.sidebar.header("User Input Features")

# Input fields for each feature
limit_bal = st.sidebar.slider("LIMIT_BAL (Amount of Credit in NT dollars)", 0, 1000000, 50000)
sex = st.sidebar.radio("SEX (Gender)", ["Male", "Female"])
education = st.sidebar.radio("EDUCATION (Education Level)", ["Graduate School", "University", "High School", "Others"])
marriage = st.sidebar.radio("MARRIAGE (Marital Status)", ["Married", "Single", "Others"])
age = st.sidebar.slider("AGE (Age in years)", 20, 80, 30)
pay_status_sept = st.sidebar.slider("PAY_0 (Repayment status in September, 2005)", -2, 8, 0)
pay_status_aug = st.sidebar.slider("PAY_2 (Repayment status in August, 2005)", -2, 8, 0)
pay_status_jul = st.sidebar.slider("PAY_3 (Repayment status in July, 2005)", -2, 8, 0)
pay_status_jun = st.sidebar.slider("PAY_4 (Repayment status in June, 2005)", -2, 8, 0)
pay_status_may = st.sidebar.slider("PAY_5 (Repayment status in May, 2005)", -2, 8, 0)
pay_status_apr = st.sidebar.slider("PAY_6 (Repayment status in April, 2005)", -2, 8, 0)
bill_amt_sept = st.sidebar.slider("BILL_AMT1 (Bill statement in September, 2005 - NT dollar)", 0, 1000000, 5000)
bill_amt_aug = st.sidebar.slider("BILL_AMT2 (Bill statement in August, 2005 - NT dollar)", 0, 1000000, 5000)
bill_amt_jul = st.sidebar.slider("BILL_AMT3 (Bill statement in July, 2005 - NT dollar)", 0, 1000000, 5000)
bill_amt_jun = st.sidebar.slider("BILL_AMT4 (Bill statement in June, 2005 - NT dollar)", 0, 1000000, 5000)
bill_amt_may = st.sidebar.slider("BILL_AMT5 (Bill statement in May, 2005 - NT dollar)", 0, 1000000, 5000)
bill_amt_apr = st.sidebar.slider("BILL_AMT6 (Bill statement in April, 2005 - NT dollar)", 0, 1000000, 5000)
pay_amt_sept = st.sidebar.slider("PAY_AMT1 (Previous payment in September, 2005 - NT dollar)", 0, 100000, 500)
pay_amt_aug = st.sidebar.slider("PAY_AMT2 (Previous payment in August, 2005 - NT dollar)", 0, 100000, 500)
pay_amt_jul = st.sidebar.slider("PAY_AMT3 (Previous payment in July, 2005 - NT dollar)", 0, 100000, 500)
pay_amt_jun = st.sidebar.slider("PAY_AMT4 (Previous payment in June, 2005 - NT dollar)", 0, 100000, 500)
pay_amt_may = st.sidebar.slider("PAY_AMT5 (Previous payment in May, 2005 - NT dollar)", 0, 100000, 500)
pay_amt_apr = st.sidebar.slider("PAY_AMT6 (Previous payment in April, 2005 - NT dollar)", 0, 100000, 500)

# Define mappings for education and marriage
education_mapping = {
    "Graduate School": 1,
    "University": 2,
    "High School": 3,
    "Others": 4
}

marriage_mapping = {
    "Married": 1,
    "Single": 2,
    "Others": 3
}

# Create a DataFrame with user input data
user_input_data = pd.DataFrame({
    "LIMIT_BAL": [limit_bal],
    "SEX": [1 if sex == "Male" else 2],  # Map 'Male' to 1 and 'Female' to 2
    "EDUCATION": [education_mapping[education]],
    "MARRIAGE": [marriage_mapping[marriage]],
    "AGE": [age],
    "PAY_0": [pay_status_sept],
    "PAY_2": [pay_status_aug],
    "PAY_3": [pay_status_jul],
    "PAY_4": [pay_status_jun],
    "PAY_5": [pay_status_may],
    "PAY_6": [pay_status_apr],
    "BILL_AMT1": [bill_amt_sept],
    "BILL_AMT2": [bill_amt_aug],
    "BILL_AMT3": [bill_amt_jul],
    "BILL_AMT4": [bill_amt_jun],
    "BILL_AMT5": [bill_amt_may],
    "BILL_AMT6": [bill_amt_apr],
    "PAY_AMT1": [pay_amt_sept],
    "PAY_AMT2": [pay_amt_aug],
    "PAY_AMT3": [pay_amt_jul],
    "PAY_AMT4": [pay_amt_jun],
    "PAY_AMT5": [pay_amt_may],
    "PAY_AMT6": [pay_amt_apr]
})

# Predict button
if st.sidebar.button("Predict"):
    # Make predictions using the loaded model
    predicted_default = model.predict(user_input_data)

    # Display the prediction result
    st.subheader("Prediction Result")
    if predicted_default[0] == 1:
        st.write("The model predicts that the client may default on their credit card payment.")
    else:
        st.write("The model predicts that the client is unlikely to default on their credit card payment.")
