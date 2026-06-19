import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("rainfallprediction4.joblib")  # change filename if different

st.title("Rainfall Prediction System")

# Input fields
day = st.number_input("Day", min_value=1, max_value=31, value=15)

pressure = st.number_input("Pressure (hPa)", value=1000.0)

max_temp = st.number_input("Max Temperature (°C)", value=28.0)

avg_temp = st.number_input("Average Temperature (°C)", value=25.0)

min_temp = st.number_input("Min Temperature (°C)", value=22.0)

dewpoint = st.number_input("Dew Point (°C)", value=21.0)

humidity = st.number_input("Humidity (%)", value=90.0)

cloud_cover = st.number_input("Cloud Cover (%)", value=85.0)

sunshine = st.number_input("Sunshine Hours", value=2.0)

windspeed = st.number_input("Wind Speed (km/h)", value=15.0)

if st.button("Predict"):

    # IMPORTANT:
    # Same order used during training
    input_data = pd.DataFrame([[
        cloud_cover,
        humidity,
        windspeed,
        dewpoint,
        day,
        pressure,
        max_temp,
        min_temp,
        avg_temp,
        sunshine
    ]])

    prediction = model.predict(input_data)

    st.write("Raw Prediction:", prediction)

    if prediction[0] > 0.5:
        st.success("🌧 Rain Expected")
    else:
        st.error("☀ No Rain Expected")