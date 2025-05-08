# GitHub Profile Analyzer

A powerful Streamlit-based web application that provides comprehensive analysis and visualization of GitHub profiles and repositories.

## Live Link

![Github Profile Analyzer]()

## 🌟 Features

- **Profile Overview**
  - User profile information display
  - Avatar and bio integration
  - Key metrics (followers, following, public repos)

- **Repository Analysis**
  - Comprehensive repository listing with creation dates
  - Star and fork statistics
  - Language distribution analysis

- **Interactive Visualizations**
  1. **Top Repositories Tab**
     - Bar chart of most starred repositories
     - Top 10 repositories visualization

  2. **Language Analysis Tab**
     - Pie chart of language distribution
     - Tabular view of top languages

  3. **Repository Insights Tab**
     - Total stars and forks metrics
     - Fork ratio analysis
     - Most forked repositories visualization

  4. **Activity Stats Tab**
     - Repository creation timeline
     - Repository size distribution
     - Activity patterns over time

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- GitHub Personal Access Token (for API authentication)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/github-profile-analyzer.git
   cd github-profile-analyzer
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your GitHub token:
   ```
   GITHUB_TOKEN=your_github_token_here
   ```

### Running the Application

Run the Streamlit application:
```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📊 Usage

1. Enter any GitHub username in the input field
2. View comprehensive profile information
3. Explore different analysis tabs:
   - Check top repositories
   - Analyze language distribution
   - View repository insights
   - Track activity patterns

## 🛠️ Technical Stack

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Python-dotenv**: Environment variable management
- **Requests**: API interactions

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

- **Osama bin Adnan**
  - GitHub: [@OsamabinAdnan](https://github.com/OsamabinAdnan)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/github-profile-analyzer/issues).

## ⭐ Show your support

Give a ⭐️ if this project helped you!