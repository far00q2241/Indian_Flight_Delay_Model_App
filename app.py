import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("flight_delay_model.pkl")


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------
st.title("✈️ Flight Delay Prediction")
st.write(
    "Enter the flight details below to predict whether the flight "
    "is likely to be delayed."
)


# -----------------------------
# Input Section
# -----------------------------
st.header("Flight Information")

col1, col2, col3 = st.columns(3)

with col1:
    airline = st.selectbox(
        "Airline",
        ["Air India", "IndiGo", "Vistara", "SpiceJet", "Go First"]
    )

    origin = st.selectbox(
        "Origin Airport",
        ["HYD", "DEL", "BOM", "BLR", "MAA"]
    )

    destination = st.selectbox(
        "Destination Airport",
        ["HYD", "DEL", "BOM", "BLR", "MAA"]
    )

with col2:
    scheduled_hour = st.slider(
        "Scheduled Departure Hour",
        min_value=0,
        max_value=23,
        value=12
    )

    scheduled_minute = st.slider(
        "Scheduled Departure Minute",
        min_value=0,
        max_value=59,
        value=0
    )

    day_of_week = st.selectbox(
        "Day of Week",
        [0, 1, 2, 3, 4, 5, 6],
        format_func=lambda x: [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ][x]
    )

with col3:
    month = st.slider(
        "Month",
        min_value=1,
        max_value=12,
        value=6
    )

    is_weekend = st.selectbox(
        "Is Weekend?",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    peak_hour = st.selectbox(
        "Peak Hour?",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


# -----------------------------
# Weather Information
# -----------------------------
st.header("🌦️ Weather Information")

col1, col2, col3 = st.columns(3)

with col1:
    weather = st.selectbox(
        "Weather",
        ["Clear", "Cloudy", "Rainy", "Storm"]
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=25.0
    )

with col2:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        min_value=0.0,
        value=10.0
    )

with col3:
    visibility = st.number_input(
        "Visibility (km)",
        min_value=0.0,
        value=10.0
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=0.0
    )


# -----------------------------
# Operational Information
# -----------------------------
st.header("🛫 Operational Information")

col1, col2, col3 = st.columns(3)

with col1:
    cloud_cover = st.number_input(
        "Cloud Cover (%)",
        min_value=0.0,
        max_value=100.0,
        value=30.0
    )

with col2:
    congestion = st.number_input(
        "Origin Congestion Index",
        min_value=0.0,
        value=50.0
    )

with col3:
    previous_delay = st.number_input(
        "Previous Flight Delay (minutes)",
        min_value=0.0,
        value=0.0
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Flight Delay", type="primary"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "Scheduled_Departure_Hour": [scheduled_hour],
        "Scheduled_Departure_Minute": [scheduled_minute],
        "Day_of_Week": [day_of_week],
        "Month": [month],
        "Is_Weekend": [is_weekend],
        "Peak_Hour": [peak_hour],
        "Temperature_C": [temperature],
        "Humidity_pct": [humidity],
        "Wind_Speed_kmh": [wind_speed],
        "Visibility_km": [visibility],
        "Rainfall_mm": [rainfall],
        "Cloud_Cover_pct": [cloud_cover],
        "Origin_Congestion_Index": [congestion],
        "Previous_Flight_Delay_Minutes": [previous_delay]
    })


    # Prediction
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]


    # Display result
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Flight is likely to be DELAYED")
    else:
        st.success("✅ Flight is likely to be ON TIME")

    st.write(
        f"Delay Probability: **{probability:.2%}**"
    )
