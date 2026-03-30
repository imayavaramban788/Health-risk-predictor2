import streamlit as st
from model import predict_risk

st.title("Health Risk Predictor")

age = st.number_input("Age", 1, 100)
heart_rate = st.number_input("Heart Rate")
temperature = st.number_input("Temperature")
spo2 = st.number_input("SpO2")

if st.button("Predict"):
    result = predict_risk(age, heart_rate, temperature, spo2)

    if result == "Critical":
        st.error("Critical Condition!")
    elif result == "At Risk":
        st.warning("At Risk!")
    else:
        st.success("Normal")
