import streamlit as st

# Title and description
st.title("🌍 Unit Converter App")
st.markdown("### Instantly convert values between Length, Weight, and Time units")
st.write("Welcome! Choose a category, select a conversion type, enter a value, and get the result instantly.")

# Category selection
category = st.selectbox("🔘 Select Category", ["Length", "Weight", "Time"])

# Conversion options based on selected category
if category == "Length":
    conversion_type = st.selectbox("📏 Select Conversion Type", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    conversion_type = st.selectbox("⚖️ Select Conversion Type", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    conversion_type = st.selectbox("⏱️ Select Conversion Type", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours"
    ])

# Value input
value = st.number_input("✏️ Enter value to convert", min_value=0.0, format="%.2f")

# Conversion function
def convert_units(category, value, conversion_type):
    if category == "Length":
        if conversion_type == "Kilometers to Miles":
            return value * 0.621371, "miles"
        elif conversion_type == "Miles to Kilometers":
            return value / 0.621371, "kilometers"

    elif category == "Weight":
        if conversion_type == "Kilograms to Pounds":
            return value * 2.20462, "pounds"
        elif conversion_type == "Pounds to Kilograms":
            return value / 2.20462, "kilograms"

    elif category == "Time":
        conversions = {
            "Seconds to Minutes": (value / 60, "minutes"),
            "Minutes to Seconds": (value * 60, "seconds"),
            "Minutes to Hours": (value / 60, "hours"),
            "Hours to Minutes": (value * 60, "minutes"),
            "Hours to Days": (value / 24, "days"),
            "Days to Hours": (value * 24, "hours"),
        }
        return conversions.get(conversion_type, (0, ""))

    return 0, ""

# Button to trigger conversion
if st.button("🔄 Convert"):
    result, unit = convert_units(category, value, conversion_type)
    st.success(f"✅ Result: {result:.2f} {unit}")
#footer
st.write("© Created by Humema Israr")