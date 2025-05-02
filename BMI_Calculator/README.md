# BMI Calculator

A simple and interactive BMI (Body Mass Index) calculator built with Streamlit.

## 🚀 Features

- Interactive sliders for height and weight input
- Real-time BMI calculation
- Visual feedback with color-coded messages
- BMI category classification
- Reference information for BMI categories

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.7 or higher
- Streamlit library

## 🛠️ Installation

1. Clone this repository or download the source code
2. Install the required packages:

```bash
pip install streamlit
```

## 💻 Usage

1. Run the application using the following command:

```bash
streamlit run main.py
```

2. The application will open in your default web browser
3. Use the sliders to input your height (in cm) and weight (in kg)
4. Your BMI will be calculated automatically and displayed along with your BMI category

## 📊 BMI Categories

The application classifies BMI into the following categories:

- Underweight: BMI < 18.5
- Normal weight: BMI between 18.5 and 24.9
- Overweight: BMI between 25 and 29.9
- Obese: BMI between 30 and 34.9
- Severely obese: BMI ≥ 35

## 🎨 UI Components

- Height slider: Range 100-250 cm
- Weight slider: Range 30-200 kg
- BMI result display
- Category information
- Reference information section

## 🔧 Technical Details

- Built with Streamlit for the user interface
- Uses simple mathematical formula for BMI calculation: weight (kg) / height (m)²
- Responsive design with centered layout
- Custom page configuration with emoji icons

## 🔗 Live App

[BMI Calculator](https://bmicalculatorapp-osamabinadnan.streamlit.app/) from Osama bin Adnan

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Created by Osama Bin Adnan

---

*Note: This BMI calculator is for informational purposes only and should not be used as a substitute for professional medical advice.*
