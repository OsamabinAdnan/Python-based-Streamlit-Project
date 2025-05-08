# Import required libraries
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import requests
import plotly.express as px
import base64
from pathlib import Path

# Load environment variables from .env file for secure credential management
load_dotenv()

# Get GitHub token from environment variable for API authentication
token = os.getenv('GITHUB_TOKEN')
# Set up headers for GitHub API requests with token if available
headers = {'Authorization': f'token {token}'} if token else {}

# Configure Streamlit page settings
st.set_page_config(
    page_title= 'GitHub Profile Analyzer',
    page_icon= '📊',
    layout= 'centered',
)

# Main title of the application
st.title('GitHub Profile Analyzer')

# Input field for GitHub username
username = st.text_input('Enter GitHub username')

if username:
    # API endpoints for user data and repositories
    user_url = f'https://api.github.com/users/{username}'
    repo_url = f'https://api.github.com/users/{username}/repos?per_page=50'

    # Make API requests to GitHub
    user_response = requests.get(user_url, headers=headers)
    repos_respnse = requests.get(repo_url, headers=headers)

    # Check if the API requests were successful
    if user_response.status_code == 200 and repos_respnse.status_code == 200:
        user_data = user_response.json()
        repos_data = repos_respnse.json()

        # Display user profile information
        st.header('Profile Header')
        st.subheader(f"**{user_data['name']} (@{user_data['login']})**")
        st.image(user_data['avatar_url'], width=100)

        # Show user bio if available
        if user_data.get('bio'):
            st.write(user_data['bio'])
        
        # Display key profile metrics
        st.markdown(
            f"**Followers:** {user_data['followers']} | " 
            f"**Following:** {user_data['following']} | "
            f"**Public Repos:** {user_data['public_repos']}"
        )

        # Repository Analysis Section
        st.header('Repositories Overview')

        # Convert repository data to DataFrame for analysis
        repo_df = pd.DataFrame(repos_data)

        if not repo_df.empty:
            # Select relevant columns for analysis
            repo_df = repo_df[['name', 'stargazers_count', 'forks_count', 'language', 'html_url', 'created_at', 'size', 'fork']]
            # Format creation date for better readability
            repo_df['created_at'] = pd.to_datetime(repo_df['created_at']).dt.strftime('%B %d, %Y')
            # Sort repositories by stars (most popular first)
            repo_df = repo_df.sort_values(by='stargazers_count', ascending=False)
            st.dataframe(repo_df)
            
            # Create tabs for different analysis views
            tab1, tab2, tab3, tab4 = st.tabs([
                'Top Repositories', 
                'Language Analysis', 
                'Repository Insights',
                'Activity Stats'
            ])

            # Tab 1: Visualize top repositories by stars
            with tab1:
                st.subheader('Top 10 Repositories by Stars')
                top_repos = repo_df.head(10)

                # Create horizontal bar chart for top repos
                fig1 = px.bar(
                    top_repos,
                    x='stargazers_count',
                    y='name',
                    orientation='h',
                    labels={"stargazers_count": "Stars", "name": "Repository"},
                    color='stargazers_count',
                )
                st.plotly_chart(fig1, use_container_width=True)
            
            # Tab 2: Analyze programming languages used
            with tab2:
                st.subheader('🧠 Language Distribution')
                col1, col2 = st.columns(2)
                
                # Create pie chart for language distribution
                with col1:
                    language_count = repo_df['language'].dropna().value_counts().reset_index()
                    language_count.columns = ['Language', 'Count']
                    fig2 = px.pie(
                        language_count,
                        values='Count',
                        names='Language',
                        title='Language Usage'
                    )
                    st.plotly_chart(fig2, use_container_width=True)
                
                # Display language statistics in table format
                with col2:
                    st.subheader("Top Languages")
                    st.table(language_count.head())

            # Tab 3: Show repository statistics and insights
            with tab3:
                st.subheader('📊 Repository Statistics')
                
                # Display key metrics in columns
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    total_stars = repo_df['stargazers_count'].sum()
                    st.metric("Total Stars", total_stars)
                
                with col2:
                    total_forks = repo_df['forks_count'].sum()
                    st.metric("Total Forks", total_forks)
                
                with col3:
                    fork_ratio = (repo_df['fork'].sum() / len(repo_df)) * 100
                    st.metric("Fork Ratio", f"{fork_ratio:.1f}%")
                
                # Visualize most forked repositories
                st.subheader("Most Forked Repositories")
                top_forked = repo_df.nlargest(5, 'forks_count')[['name', 'forks_count']]
                fig3 = px.bar(
                    top_forked,
                    x='name',
                    y='forks_count',
                    title='Top 5 Most Forked Repositories'
                )
                st.plotly_chart(fig3, use_container_width=True)

            # Tab 4: Show repository activity over time
            with tab4:
                st.subheader('📈 Repository Activity')
                
                # Analyze repository creation timeline
                timeline_df = pd.DataFrame(repos_data)[['created_at']]
                timeline_df['created_at'] = pd.to_datetime(timeline_df['created_at'])
                
                # Group repositories by creation year
                yearly_repos = timeline_df.groupby(timeline_df['created_at'].dt.year).size().reset_index()
                yearly_repos.columns = ['Year', 'Number of Repositories']
                
                # Create timeline visualization
                fig4 = px.line(
                    yearly_repos,
                    x='Year',
                    y='Number of Repositories',
                    title='Repository Creation Timeline',
                    markers=True
                )
                st.plotly_chart(fig4, use_container_width=True)
                
                # Show repository size distribution
                st.subheader("Repository Size Distribution")
                fig5 = px.histogram(
                    repo_df,
                    x='size',
                    title='Repository Size Distribution (KB)',
                    nbins=20
                )
                st.plotly_chart(fig5, use_container_width=True)
        else:
            st.warning('No repositories found for this user.')
    else:
        st.warning('Invalid GitHub username.')
else:
    st.warning('Please enter a GitHub username.')


# Footer section with attribution
def img_to_base64(img_path):
    """Convert an image file to base64 string for embedding in HTML"""
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load and prepare profile image for footer
img_path = Path(__file__).parent / "assets" / "osama.png"
img_base64 = img_to_base64(str(img_path))

# Add footer separator and content
st.markdown("---")
st.markdown(
    f'<div style="display: flex; align-items: center; justify-content: center;">'
    f'<p>Built with ❤️ by '
    f'<a href="https://github.com/OsamabinAdnan">Osama bin Adnan</a> '
    f'<img src="data:image/png;base64,{img_base64}" style="width: 50px; height: 50px; border-radius: 50%; margin-left: 5px;">'
    f'</p></div>', 
    unsafe_allow_html=True
)