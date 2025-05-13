import streamlit as st

st.set_page_config(page_title="🔄 Unit Converter", layout="wide")
st.title("🔄 Unit Converter")

# Custom CSS for background, text colors and input box styling
st.markdown(
    """
    <style>
    /* Background and text colors for the app */
    .stApp {
        background-color:rgb(143, 139, 142);  /* light blue */
        color: white;  /* navy blue text */
    }
    /* Style the text input box */
    selectbox[type="text"] {
        background-color: white !important;
         color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.write("### Convert weight, length, temperature, and more easily!✨")
st.markdown("Enter your units here and get outstanding conversion results instantly!🚀")

category = st.selectbox("✅ Select the category of units you want to convert", ["Weight", "Length", "Temperature", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084

    elif category == "Weight":
        if unit == "Kilograms to Grams":
            return value * 1000
        elif unit == "Grams to Kilograms":
            return value / 1000
        elif unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Pounds":
            return value / 453.592
        elif unit == "Pounds to Grams":
            return value * 453.592

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return value * 1.8 + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) / 1.8
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) / 1.8 + 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 1.8 + 32

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Minutes to Days":
            return value / 1440
        elif unit == "Days to Minutes":
            return value * 1440

# Show appropriate unit options based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Grams", "Grams to Kilograms", "Kilograms to Pounds", "Pounds to Kilograms", "Grams to Pounds", "Pounds to Grams"])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius", "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours", "Minutes to Days", "Days to Minutes"])

value = st.number_input("🔢 Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is: **{result:.2f}**")
    else:
        st.error("Conversion not supported or invalid input.")
