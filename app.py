import streamlit as st
import pandas as pd
import pickle

# --- Page Config ---
st.set_page_config(page_title=" Crop Yield Prediction", page_icon="🌱", layout="centered")

# --- Load model once ---
@st.cache_resource
def load_model():
    with open("crop_yield_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# --- Title and Instructions ---
st.title("🌾 Crop Yield Prediction System")
st.markdown("Provide environmental and crop details to predict expected yield (tons/hectare).")

# --- Input Fields in Two Columns ---
col1, col2 = st.columns(2)

with col1:
    region = st.selectbox("🌍 Region", ["North", "South", "East", "West"])
    soil_type = st.selectbox("🪨 Soil Type", ["Clay", "Sandy", "Loam", "Silt", "Peaty", "Chalky"])
    crop = st.selectbox("🌱 Crop", ["Wheat", "Rice", "Maize", "Barley", "Soybean", "Cotton"])
    rainfall = st.number_input("🌧 Rainfall (mm)", min_value=0.0, step=1.0)
    fertilizer = st.selectbox("🧪 Fertilizer Used", ["True", "False"])

with col2:
    temperature = st.number_input("🌡 Temperature (°C)", min_value=-10.0, step=0.1)
    irrigation = st.selectbox("💧 Irrigation Used", ["True", "False"])
    weather = st.selectbox("⛅ Weather Condition", ["Sunny", "Rainy", "Cloudy"])
    days_to_harvest = st.number_input("📅 Days to Harvest", min_value=1, step=1)

# --- Initialize Prediction History ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- Prediction Button ---
if st.button("🔮 Predict Yield"):
    # Prepare input DataFrame
    input_data = pd.DataFrame({
        'Region': [region],
        'Soil_Type': [soil_type],
        'Crop': [crop],
        'Rainfall_mm': [rainfall],
        'Temperature_Celsius': [temperature],
        'Fertilizer_Used': [fertilizer == "True"],
        'Irrigation_Used': [irrigation == "True"],
        'Weather_Condition': [weather],
        'Days_to_Harvest': [days_to_harvest]
    })

    # Predict yield
    predicted_yield = model.predict(input_data)[0]

    # Display results
    st.success(f"🌱 Predicted Crop Yield: **{predicted_yield:.2f} tons/hectare**")
    
    # Add latest entry to top and keep only last 5
    st.session_state.history.insert(0, [region, crop, predicted_yield])
    st.session_state.history = st.session_state.history[:5]

# --- Show Prediction History ---
if st.session_state.history:
    st.subheader("📜 Prediction History (Last 5)")
    
    # Convert to DataFrame and add 1-based Index
    df_history = pd.DataFrame(st.session_state.history, columns=["Region", "Crop", "Predicted Yield (t/ha)"])
    df_history.index = range(1, len(df_history) + 1)
    st.dataframe(df_history, use_container_width=True)

    # --- Clear History Button ---
    if st.button("🗑 Clear History"):
        st.session_state.history.clear()
        st.rerun()
