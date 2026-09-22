import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load("laptop_price_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻"
)

st.title("💻 Laptop Price Prediction")
st.write("Enter the laptop specifications to predict its estimated price.")

# Input fields
ram = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8, step=2)
size_inch = st.number_input("Screen Size (inch)", min_value=10.0, max_value=20.0, value=15.6)
battery_wh = st.number_input("Battery (Wh)", min_value=20, max_value=100, value=50)
weight_kg = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, value=1.6)

brand = st.selectbox(
    "Brand",
    ["Acer", "Apple", "Asus", "Dell", "HP", "Lenovo", "MSI", "Samsung"]
)

category = st.selectbox(
    "Category",
    ["Gaming", "Home", "Student"]
)

cpu = st.selectbox(
    "CPU",
    ["Apple M2", "Intel i3", "Intel i5", "Intel i7",
     "Ryzen 3", "Ryzen 5", "Ryzen 7"]
)

ram_type = st.selectbox(
    "RAM Type",
    ["DDR3", "DDR4", "DDR5", "Unified"]
)

storage = st.selectbox(
    "Storage",
    ["256GB", "512GB", "1TB", "2TB"]
)

ssd = st.selectbox(
    "SSD",
    ["Yes", "No"]
)

ssd_size = st.selectbox(
    "SSD Size",
    ["256GB", "512GB", "1TB", "2TB", "Unknown"]
)

graphics_card = st.selectbox(
    "Graphics Card",
    ["Integrated", "Nvidia", "AMD"]
)

graphics_card_size = st.selectbox(
    "Graphics Card Size",
    ["4GB", "6GB", "8GB", "Unknown"]
)

os = st.selectbox(
    "Operating System",
    ["Windows 10", "Windows 11", "macOS"]
)

# Prediction
if st.button("🔮 Predict Laptop Price"):

    # Create empty input with exactly the same columns as training data
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    # Numerical features
    input_data["ram"] = ram
    input_data["size_inch"] = size_inch
    input_data["battery_wh"] = battery_wh
    input_data["weight_kg"] = weight_kg

    # Categorical features
    values = {
        "brand": brand,
        "category": category,
        "cpu": cpu,
        "ram_type": ram_type,
        "storage": storage,
        "ssd": ssd,
        "ssd_size": ssd_size,
        "graphics_card": graphics_card,
        "graphics_card_size": graphics_card_size,
        "os": os
    }

    for feature, value in values.items():

        column_name = feature + "_" + value

        if column_name in input_data.columns:
            input_data[column_name] = 1

    # Predict
    prediction = model.predict(input_data)[0]

    st.success(
        f"💰 Estimated Laptop Price: ₹{prediction:,.2f}"
    )