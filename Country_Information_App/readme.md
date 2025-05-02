# 🌍 Country Information App 🗺️

A sleek and responsive web application built using **Python** and **Streamlit**, which fetches detailed information about any country using the `countryapi.io` API.

---

## 📦 Features

- 🔍 Search for any country by name
- 🏳️ View national flag
- 🏙 Get capital, region, and area
- 👨‍👩‍👧‍👦 View population
- 💱 Currency details including symbol
- 🗣 List of official languages
- 🌐 Timezone, calling code, alpha codes
- ✅ Clean UI with responsive layout using Streamlit

---

## 🖥️ Live App Link

[Country Information App](https://countryinformationapp-osamabinadnan.streamlit.app/)

---

## 🚀 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **Backend**: Python
- **API**: [countryapi.io](https://countryapi.io/)
- **Environment Management**: `python-dotenv`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/OsamabinAdnan/Project-4-Assignments_OsamabinAdnan/tree/main/Assignment_01_online_class_projects/
cd Online Class Project 09 Python Streamlit Web App - Country Information Cards
```
### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate # on Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```
Or manually:

```bash
pip install streamlit requests python-dotenv
```

### 4. Get a Free API Key from [countryapi.io](https://countryapi.io/)

- Sign up and grab your API key.

### 5. Create a .env File

``` bash
COUNTRIES_API_KEY=your_api_key_here
```

### 6. Run the App

```bash
streamlit run app.py
```

Replace `app.py` with your file name if different.

## 📂 Project Structure

```bash
.
├── app.py               # Main application file
├── .gitignore           # Ignore sensitive files like API keys
├── requirements.txt     # Python dependencies | pip freeze > requirements.txt ==> This command will write all packages with versions in this file
└── README.md            # You're reading it!

```

## How It Works

* The user enters a country name.
* The app sends a GET request to countryapi.io API.
* On a successful response:
    - It parses and displays the flag, capital, population, currency, languages, and more.
* The interface is made interactive and responsive using Streamlit's layout features.

## 📌 Example Output

* Country: Pakistan
* Capital: Islamabad
* Population: 220,892,331
* Currency: Pakistani Rupee (PKR) – Symbol: ₨
* Languages: English, Urdu
* Region: Asia
* Flag: 🇵🇰