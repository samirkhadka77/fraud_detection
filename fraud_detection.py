import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_pipeline.pkl')

st.title("Fraud Detection Model")

st.markdown("please input the transaction details below to predict if it's fraudulent or not.")

st.divider()

transaction_type = st.selectbox("Transaction Type", options=['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount = st.number_input("Transaction Amount", min_value=0.0, value = 1000.00)
oldbalanceOrg = st.number_input("Old Balance of Origin Account", min_value=0.0, value = 10000.00)
newbalanceOrig = st.number_input("New Balance of Origin Account", min_value=0.0, value = 9000.00)

oldbalanceDest = st.number_input("Old Balance of Destination Account", min_value=0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance of Destination Account", min_value=0.0, value = 0.0)

if st.button("predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"prediction: {int(prediction)}")

    if prediction == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be LEGITIMATE.")