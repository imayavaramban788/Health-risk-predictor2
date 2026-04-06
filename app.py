import streamlit as st

# --- TITLE ---
st.title("🩺 AI-Based Neonatal Health Risk Detection System")

# --- AIM ---
st.header("🎯 Aim")
st.write("""
To develop a biomedical application that monitors neonatal vital parameters 
and predicts early health risks using a rule-based AI approach.
""")

# --- PROCEDURE ---
st.header("⚙️ Procedure")
st.write("""
1. Collect neonatal vital parameters:
   - Heart Rate
   - Body Temperature
   - Oxygen Saturation (SpO2)

2. Input the data into the system.

3. The system analyzes the values using predefined medical rules.

4. The system predicts whether the condition is:
   - Normal
   - High Risk

5. Display the result to the user.
""")

# --- INPUT SECTION ---
st.header("🧪 Enter Patient Details")

age = st.number_input("Age (in days)", min_value=0)
heart_rate = st.number_input("Heart Rate (bpm)")
temperature = st.number_input("Temperature (°C)")
spo2 = st.number_input("SpO2 (%)")

# --- AI LOGIC ---
def predict_risk(hr, temp, spo2):
    if hr > 160 or spo2 < 90 or temp > 38:
        return "High Risk ⚠️"
    else:
        return "Normal ✅"

# --- PREDICT BUTTON ---
if st.button("Predict"):
    result = predict_risk(heart_rate, temperature, spo2)
    st.success(f"Result: {result}")

# --- QUIZ SECTION ---
st.header("🧠 Quiz")

q1 = st.radio("1. What is the normal SpO2 level in neonates?", 
              ["70%", "85%", "95-100%"])

q2 = st.radio("2. High heart rate in neonates indicates?", 
              ["Normal Condition",
