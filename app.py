import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Load Model and Feature Columns
# --------------------------------------------------

model = joblib.load("flight_delay_model.pkl")
model_columns = joblib.load("flight_delay_columns.pkl")


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("✈️ Flight Delay Prediction")

st.write(
    "Enter the flight details below to predict whether "
    "the flight is likely to be delayed."
)


# --------------------------------------------------
# Flight Information
# --------------------------------------------------

st.header("🛫 Flight Information")

col1, col2, col3 = st.columns(3)


with col1:

    airline = st.selectbox(
        "Airline",
        [
            "Air India Express",
            "Akasa Air",
            "Alliance Air",
            "Fly91",
            "IndiGo",
            "SpiceJet",
            "Star Air",
            "Vistara"
        ]
    )


with col2:

    origin = st.selectbox(
        "Origin Airport",
        [
            "AJL", "AKD", "AMD", "ATQ", "BBI", "BDQ",
            "BHJ", "BHO", "BHU", "BKB", "BLR", "BOM",
            "CCU", "CJB", "CNN", "COK", "DBR", "DED",
            "DEL", "DHM", "DIB", "DIU", "DMU", "GAU",
            "GAY", "GOI", "GOP", "GWL", "HBX", "HYD",
            "IDR", "IMF", "ISK", "IXA", "IXB", "IXC",
            "IXD", "IXE", "IXG", "IXJ", "IXM", "IXR",
            "IXU", "IXW", "IXY", "IXZ", "JAI", "JDH",
            "JGA", "JLR", "JRH", "JSA", "KNU", "KUU",
            "LEH", "LKO", "MAA", "MYQ", "NAG", "NDC",
            "PAT", "PBD", "PNQ", "RAJ", "RDP", "REW",
            "RPR", "SHL", "SLV", "STV", "SXR", "SXV",
            "TCR", "TIR", "TRV", "TRZ", "UDR", "VDY",
            "VGA", "VNS", "VOBL", "VOPC", "VOPN", "VTU",
            "VTZ"
        ]
    )


with col3:

    destination = st.selectbox(
        "Destination Airport",
        [
            "AJL", "AKD", "AMD", "ATQ", "BBI", "BDQ",
            "BHJ", "BHO", "BHU", "BKB", "BLR", "BOM",
            "CCU", "CJB", "CNN", "COK", "DBR", "DED",
            "DEL", "DHM", "DIB", "DIU", "DMU", "GAU",
            "GAY", "GOI", "GOP", "GWL", "HBX", "HYD",
            "IDR", "IMF", "ISK", "IXA", "IXB", "IXC",
            "IXD", "IXE", "IXG", "IXJ", "IXM", "IXR",
            "IXU", "IXW", "IXY", "IXZ", "JAI", "JDH",
            "JGA", "JLR", "JRH", "JSA", "KNU", "KUU",
            "LEH", "LKO", "MAA", "MYQ", "NAG", "NDC",
            "PAT", "PBD", "PNQ", "RAJ", "RDP", "REW",
            "RPR", "SHL", "SLV", "STV", "SXR", "SXV",
            "TCR", "TIR", "TRV", "TRZ", "UDR", "VDY",
            "VGA", "VNS", "VOBL", "VOPC", "VOPN", "VTU",
            "VTZ"
        ]
    )


# --------------------------------------------------
# Schedule Information
# --------------------------------------------------

st.header("📅 Schedule Information")

col1, col2, col3 = st.columns(3)


with col1:

    scheduled_hour = st.slider(
        "Scheduled Departure Hour",
        0,
        23,
        12
    )


with col2:

    scheduled_minute = st.slider(
        "Scheduled Departure Minute",
        0,
        59,
        0
    )


with col3:

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


col1, col2, col3 = st.columns(3)


with col1:

    month = st.slider(
        "Month",
        1,
        12,
        6
    )


with col2:

    year = st.selectbox(
        "Year",
        [2024, 2025, 2026]
    )


with col3:

    day = st.slider(
        "Day",
        1,
        31,
        15
    )


col1, col2 = st.columns(2)


with col1:

    is_weekend = st.selectbox(
        "Is Weekend?",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


with col2:

    peak_hour = st.selectbox(
        "Peak Hour?",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


# --------------------------------------------------
# Weather Information
# --------------------------------------------------

st.header("🌦️ Weather Information")

col1, col2, col3 = st.columns(3)


with col1:

    weather = st.selectbox(
        "Weather",
        [
            "Clear/Partly Cloudy",
            "Cloudy",
            "Heavy Rain",
            "Rain"
        ]
    )


with col2:

    temperature = st.number_input(
        "Temperature (°C)",
        value=25.0
    )


with col3:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )


col1, col2, col3 = st.columns(3)


with col1:

    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        min_value=0.0,
        value=10.0
    )


with col2:

    visibility = st.number_input(
        "Visibility (km)",
        min_value=0.0,
        value=10.0
    )


with col3:

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=0.0
    )


cloud_cover = st.number_input(
    "Cloud Cover (%)",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)


# --------------------------------------------------
# Operational Information
# --------------------------------------------------

st.header("⚙️ Operational Information")

col1, col2, col3 = st.columns(3)


with col1:

    congestion = st.number_input(
        "Origin Congestion Index",
        min_value=0.0,
        value=50.0
    )


with col2:

    previous_delay = st.number_input(
        "Previous Flight Delay (minutes)",
        min_value=0.0,
        value=0.0
    )


with col3:

    turnaround_risk = st.number_input(
        "Turnaround Risk Index",
        min_value=0.0,
        value=50.0
    )


# --------------------------------------------------
# Create Input Data
# --------------------------------------------------

if st.button("🔮 Predict Flight Delay", type="primary"):

    # Start with all model columns set to zero
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )


    # Numerical features
    input_data["Scheduled_Departure_Hour"] = scheduled_hour
    input_data["Scheduled_Departure_Minute"] = scheduled_minute
    input_data["Day_of_Week"] = day_of_week
    input_data["Month"] = month
    input_data["Is_Weekend"] = is_weekend
    input_data["Peak_Hour"] = peak_hour
    input_data["Temperature_C"] = temperature
    input_data["Humidity_pct"] = humidity
    input_data["Wind_Speed_kmh"] = wind_speed
    input_data["Visibility_km"] = visibility
    input_data["Rainfall_mm"] = rainfall
    input_data["Cloud_Cover_pct"] = cloud_cover
    input_data["Origin_Congestion_Index"] = congestion
    input_data["Previous_Flight_Delay_Minutes"] = previous_delay
    input_data["Turnaround_Risk_Index"] = turnaround_risk
    input_data["Year"] = year
    input_data["Day"] = day


    # Airline
    airline_column = f"Airline_{airline}"

    if airline_column in input_data.columns:
        input_data[airline_column] = 1


    # Origin Airport
    origin_column = f"Origin_Airport_{origin}"

    if origin_column in input_data.columns:
        input_data[origin_column] = 1


    # Destination Airport
    destination_column = f"Destination_Airport_{destination}"

    if destination_column in input_data.columns:
        input_data[destination_column] = 1


    # Weather
    weather_column = f"Weather_{weather}"

    if weather_column in input_data.columns:
        input_data[weather_column] = 1


    # Make sure column order is exactly the same
    input_data = input_data[model_columns]


    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]


    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------

    st.header("📊 Prediction Result")

    if prediction == 1:

        st.error("⚠️ Flight is likely to be DELAYED")

    else:

        st.success("✅ Flight is likely to be ON TIME")


    st.metric(
        "Delay Probability",
        f"{probability:.2%}"
    )
