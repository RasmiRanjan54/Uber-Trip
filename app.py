import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("best_model.pkl", "rb"))

# Title
st.title("🚖 Smart Uber Demand Prediction System")

st.write("Predict ride demand based on time inputs")

# User Inputs
hour = st.slider("Select Hour (0-23)", 0, 23)
day = st.slider("Select Day (1-31)", 1, 31)
weekday = st.slider("Select Weekday (0=Mon, 6=Sun)", 0, 6)
month = st.slider("Select Month (1-12)", 1, 12)

# Prediction
if st.button("Predict Demand"):
    
    data = np.array([[hour, day, weekday, month]])
    prediction = model.predict(data)[0]

    st.success(f"Predicted Trips: {int(prediction)}")

    # Surge Pricing Logic
    if prediction > 200:
        st.error("🚀 High Surge Pricing")
    elif prediction > 100:
        st.warning("⚡ Medium Surge Pricing")
    else:
        st.info("🟢 Low Surge Pricing")