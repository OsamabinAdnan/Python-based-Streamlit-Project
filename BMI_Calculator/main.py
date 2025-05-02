# Import required libraries
import streamlit as st # Import Streamlit library for creating the web interface

# Configure the Streamlit page settings
st.set_page_config(
    page_title="BMI Calculator",  # Set the browser tab title
    page_icon="🏋️‍♀️",           # Set the browser tab icon
    layout="centered",            # Center the content on the page
)

# Display the main title of the application
st.title("🏋️‍♀️ Body Mass Index (BMI) Calculator ⛹️‍♀️")

# Create a slider for height input (in centimeters)
# Parameters: label, min value, max value, default value
height = st.slider("Enter your height (in cm):", 100, 250, 175)

# Create a slider for weight input (in kilograms)
# Parameters: label, min value, max value, default value
weight = st.slider("Enter your weight (in kg):", 30, 250, 70)

# Calculate BMI using the formula: weight (kg) / height (m)²
# Note: Height is converted from cm to meters by dividing by 100
bmi = weight / ((height / 100) ** 2)

# Display the calculated BMI with 2 decimal places
# Using custom HTML styling for better visual appearance
st.markdown(f"""
<div style = "font-size:24px; text-align: center; font-weight: bold; padding: 20px; margin: 20px 0; background:#4ee247; border-radius: 10px;">
    Your BMI is: <span style="font-size: 32px;">{bmi:.2f}</span>
</div>
""", unsafe_allow_html=True)

# Determine BMI category and display appropriate message with color-coded styling
# Each category has a different background color for visual distinction
if bmi < 18.5:
    # Underweight category - orange background
    st.markdown(f"""
    <div style = "font-size:24px; text-align: center; font-weight: bold; padding: 20px; margin: 20px 0; background:orange; border-radius: 10px;">
        Your are Underweight
    </div>
    """, unsafe_allow_html=True)
elif bmi >= 18.5 and bmi < 25:
    # Normal weight category - light green background
    st.markdown(f"""
    <div style = "font-size:24px; text-align: center; font-weight: bold; padding: 20px; margin: 20px 0; background:lightgreen; border-radius: 10px;">
        Your are Normal weight
    </div>
    """, unsafe_allow_html=True)
elif bmi >= 25 and bmi < 30:
    # Overweight category - pink background
    st.markdown(f"""
    <div style = "font-size:24px; text-align: center; font-weight: bold; padding: 20px; margin: 20px 0; background:pink; border-radius: 10px;">
        Your are Overweight
    </div>
    """, unsafe_allow_html=True)
elif bmi >=30 and bmi < 35:
    # Obese category - red background
    st.markdown(f"""
    <div style = "font-size:24px; text-align: center; font-weight: bold; padding: 20px; margin: 20px 0; background:red; border-radius: 10px;">
        Your are Obese
    </div>
    """, unsafe_allow_html=True)
elif bmi >= 35:
    # Severely obese category - maroon background with white text
    st.markdown(f"""
    <div style = "font-size:24px; text-align: center; font-weight: bold; padding: 20px; margin: 20px 0; background:maroon; border-radius: 10px; color:white;">
        Your are Severely Obese
    </div>
    """, unsafe_allow_html=True)

# Display BMI category reference information
# This section provides a quick reference for all BMI categories
st.write("### **BMI Categories:**")
st.write("1. Underweight: BMI less than 18.5")
st.write("2. Normal weight: BMI between 18.5 and 25")
st.write("3. Overweight: BMI between 25 and 30")
st.write("4. Obese: BMI between 30 and 35")
st.write("5. Severely obese: BMI greater than 35") 
