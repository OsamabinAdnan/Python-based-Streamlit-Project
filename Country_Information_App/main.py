import requests  # For making HTTP requests to the API
from dotenv import load_dotenv  # For loading environment variables from a .env file
import os  # For accessing environment variables and file system operations
import streamlit as st  # For building the web app interface

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key for the Countries API from environment variables
my_api_key = os.getenv('COUNTRIES_API_KEY')

# Function to fetch country data from the API
def fetch_country_data(country_name):
    # Construct the API URL with the country name and API key
    url = f"https://countryapi.io/api/name/{country_name}?apikey={my_api_key}"
    # Make a GET request to the API
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # If the response data is empty, return None
        if not data:
            return None

        # Extract the first country's data from the response
        country_data = list(data.values())[0]
        # Extract specific fields from the country data
        name = country_data.get('name', 'N/A')  # Country name
        official_name = country_data.get('official_name', 'N/A')  # Official name
        capital = country_data.get('capital', 'N/A')  # Capital city
        region = country_data.get('region', 'N/A')  # Region
        population = country_data.get('population', 'N/A')  # Population
        area = country_data.get('area', 'N/A')  # Area in square kilometers
        currencies = country_data.get('currencies', {})  # Currencies
        flag = country_data.get('flag', {}).get('large', '')  # URL of the country's flag
        languages = country_data.get('languages', {})  # Languages spoken
        timezones = country_data.get('timezones', ['N/A'])[0]  # Timezones
        calling_code = country_data.get('callingCode', 'N/A')  # Calling code
        alpha2_code = country_data.get('alpha2Code', 'N/A')  # Alpha-2 code
        alpha3_code = country_data.get('alpha3Code', 'N/A')  # Alpha-3 code

        # Return all extracted data as a tuple
        return name, official_name, capital, region, population, area, currencies, flag, languages, timezones, calling_code, alpha2_code, alpha3_code
    
    else:
        # If the response status code is not 200, return None
        return None

# Main function to define the Streamlit app
def main():
    # Set the page configuration for the Streamlit app
    st.set_page_config(
        page_title="Country Information App",  # Title of the app
        page_icon="🌍",  # Icon for the app
        layout="centered",  # Layout of the app
    )
    # Display the app title with custom styling
    st.markdown(
        "<h1 style='text-align: center; color: #4ee247;'>🌎 Country Information App 🗺️</h1>",
        unsafe_allow_html=True
    )
    # Add a horizontal line
    st.markdown("---")
    # Display a prompt for the user to enter a country name
    st.markdown("### 📥 Enter a country name to get started")
    # Input field for the user to enter a country name
    country_name = st.text_input("Enter a country name:")
    # If the user has entered a country name
    if country_name:
        # Fetch country information using the fetch_country_data function
        country_info = fetch_country_data(country_name)
        # If country information is successfully retrieved
        if country_info:
            # Unpack the returned tuple into individual variables
            name, official_name, capital, region, population, area, currencies, flag, languages, timezones, calling_code, alpha2_code, alpha3_code = country_info

            # Display the country details
            st.markdown("## 📌 Country Details")
            with st.container():
                # Create two columns for displaying the flag and details side by side
                col1, col2 = st.columns([3, 3])
                with col1:
                    # Display the country's flag
                    st.image(flag, caption="Country Flag", width=300)
                with col2:
                    # Display the country's name and other details
                    st.markdown(f"### 🏷️ {name}")
                    st.markdown(f"**Official Name:** {official_name}")
                    st.markdown(f"**Capital:** {capital}")
                    st.markdown(f"**Region:** {region}")
                    st.markdown(f"**Population:** {population:,} people")
                    st.markdown(f"**Area:** {area:,} km²")

            # Add a horizontal line
            st.markdown("---")
            # Display currency and language information
            st.markdown("### 💱 Currency & Language Info")
            # Display the list of currencies with their names and codes
            st.markdown(f"**Currencies:** {', '.join([f'{v['name']} ({k})' for k, v in currencies.items()])}")
            # Display the symbol of the first currency in the list
            st.markdown(f"**Currency Symbol:** {list(currencies.values())[0]['symbol']}")
            # Display the list of languages spoken in the country
            st.markdown(f"**Languages:** {', '.join(languages.values())}")

            # Add another horizontal line
            st.markdown("---")
            # Display miscellaneous information
            st.markdown("### 🌐 Miscellaneous")
            st.markdown(f"**Timezones:** {timezones}")
            st.markdown(f"**Calling Code:** {calling_code}")
            st.markdown(f"**Alpha-2 Code:** {alpha2_code}")
            st.markdown(f"**Alpha-3 Code:** {alpha3_code}")
        
        else:
            # Display an error message if the country is not found
            st.error("❌ Country not found. Please enter a valid country name.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
