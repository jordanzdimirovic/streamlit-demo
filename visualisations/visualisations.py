"""
    Module 3: Visualisations
    > Line plots
    > Bar charts
    > Controlling visualisations with input
"""

# Import streamlit
import streamlit as st
import pandas as pd

# Write a title
st.title("User Interaction")

st.markdown("Streamlit provides ways to create beautiful data visualisations")

# Read in data from CSV
# >>>
traffic_data = pd.read_csv("visualisations/foot_traffic.csv")

# Optionally look at data in tabular form
if st.checkbox("Show table?"):
    st.write(traffic_data)

# Create a bar-chart
# >>>
st.bar_chart(traffic_data, x = "hour")

# Get last (max) hour value
max_hour = max(traffic_data['hour'])

# Create a range to filter what window we see
window_start, window_end = st.slider("Sliding window", 0, max_hour, (0, max_hour))

# Query for values within window
traffic_data_filtered = traffic_data.query("@window_start <= hour <= @window_end")

st.line_chart(traffic_data_filtered, x="hour")
