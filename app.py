import streamlit as st

st.title("Neonatal Health Risk Detector")

# --- Input Section ---
age = st.number_input("Age", min_value=0)
heart_rate = st.number_input("Heart Rate")
temperature = st.number_input("Temperature")
spo2 = st.number_input("SpO2")

def predict_risk(hr, temp, spo2):
    if hr > 160 or spo2 < 90 or temp > 38:
        return "High Risk ⚠️"
    else:
        return "Normal ✅"

if st.button("Predict"):
    result = predict_risk(heart_rate, temperature, spo2)
    st.success(f"Result: {result}")

# --- QUIZ SECTION ---
st.header("🧠 Quiz")

q1 = st.radio("What is normal SpO2?", ["70%", "85%", "95-100%"])
q2 = st.radio("High heart rate means?", ["Normal", "Risk", "Low oxygen"])
q3 = st.radio("Normal body temperature?", ["35°C", "37°C", "40°C"])

if st.button("Submit Quiz"):
    score = 0

    if q1 == "95-100%":
        score += 1
    if q2 == "Risk":
        score += 1
    if q3 == "37°C":
        score += 1

    st.success(f"Your Score: {score}/3")
