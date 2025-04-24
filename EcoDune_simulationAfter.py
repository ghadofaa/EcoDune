import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("EcoDune_Scenario_After.csv")

st.set_page_config(page_title="EcoDune Simulation", layout="centered")
st.image("logo.png", width=165)
st.markdown("<h1 style='color:#4B8856;'>🏟️ EcoDune Digital Twin simulation </h1>", unsafe_allow_html=True)
st.markdown("<p style = 'color:#7B6EA3;font-size:18px;'>Display of actual event data after implementing EcoDune 🚀🌱</p>", unsafe_allow_html=True)

# Custom button style
st.markdown("""
<style>
div.stButton > button {
    background-color: #4E3524;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    margin: 0.5em 0em;
}
</style>
""", unsafe_allow_html=True)

# Event type buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Regular"):
        event_type = "Regular"
with col2:
    if st.button("Major"):
        event_type = "Major"

if "event_type" not in locals():
    event_type = "Regular"

# Extract values
row = df[df["Event_Type"] == event_type].iloc[0]
audience = row["Audience_Count"]
temperature = row["Temperature_C"]
electricity = row["Electricity_kWh"]
water = row["Water_Liters"]
emissions = row["Carbon_Emissions_kg"]


# Format numbers with commas
audience_display = f"{audience:}"
electricity_display = f"{electricity:}"
water_display = f"{water:}"
emissions_display = f"{emissions:}"
temperature_display = f"{temperature}"

# Display results
st.markdown("<h2 style='color:#4B8856;'>📊 Results </h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<p style='color:#7B6EA3; font-size:16px;'>👥 Audience</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:#4E3524;'>{audience_display}</h3>", unsafe_allow_html=True)

    st.markdown("<p style='color:#7B6EA3; font-size:16px;'>⚡ Electricity (kWh)</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:#4E3524;'>{electricity_display}</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:green; font-size:14px;'>↓ 70% reduction</p>", unsafe_allow_html=True)

    st.markdown("<p style='color:#7B6EA3; font-size:16px;'>💧 Water (L)</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:#4E3524;'>{water_display}</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:green; font-size:14px;'>↓ 40% reduction</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<p style='color:#7B6EA3; font-size:16px;'>🌡️ Temperature (°C)</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:#4E3524;'>{temperature_display}</h3>", unsafe_allow_html=True)

    st.markdown("<p style='color:#7B6EA3; font-size:16px;'>🫧 Emissions (kg CO₂)</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:#4E3524;'>{emissions_display}</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:green; font-size:14px;'>↓ 60% reduction</p>", unsafe_allow_html=True)

    
