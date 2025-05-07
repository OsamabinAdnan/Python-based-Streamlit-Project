import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import requests
import plotly.express as px

# Load environment variables from .env file
load_dotenv()

# Get GitHub token from environment variable
token = os.getenv('GITHUB_TOKEN')
# Set headers for GitHub API requests
headers = {'Authorization': f'token {token}'} if token else {}

# Streamlit config
st.set_page_config(
    page_title= 'GitHub Profile Analyzer',
    page_icon= ':🖥:',
    layout= 'centered',
)

st.title('GitHub Profile Analyzer')

username = st.text_input('Enter GitHub username')

if username:
    # Make GitHub API requests for user
    user_url = f'https://api.github.com/users/{username}'
    # Make GitHub API requests for user's repositories
    repo_url = f'https://api.github.com/users/{username}/repos?per_page=50'

    # 
    user_response = requests.get(user_url, headers=headers)
    repos_respnse = requests.get(repo_url, headers=headers)



