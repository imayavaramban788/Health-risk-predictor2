def predict_risk(age, heart_rate, temperature, spo2):
    if spo2 < 90:
        return "Critical"
    elif heart_rate > 100 or temperature > 37.5:
        return "At Risk"
    else:
        return "Normal"
