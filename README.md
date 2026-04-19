# Player Performance Dashboard

Exploratory analysis and playstyle clustering of 28,000+
football players using Transfermarkt data.

## Live demo
[Open dashboard on Streamlit](https://player-dashboard-vwzmlfztpi4ixvulgzawv9.streamlit.app/)

## What this project does
- Loads and cleans Transfermarkt player + appearance data
- Engineers per-90 minute performance features
- Clusters players into 5 playstyle groups using K-Means
- Visualises results with interactive Plotly charts
- Deploys as a live Streamlit web app

## Key findings
- K-Means with K=4 identified distinct archetypes:
  Forwards, midfielders,
  Defenders, and Goalkeepers
- Goals per 90 varies 4x between Goal scorers (0.52)
  and Defensive anchors (0.04)
- Market value correlates strongly with minutes ratio
  (r=0.61) — consistent starters are worth more

## Tech stack
- Python 3.11
- pandas, numpy — data loading and feature engineering
- seaborn, matplotlib — exploratory visualisation
- scikit-learn — StandardScaler, KMeans, PCA
- Plotly — interactive dashboard charts
- Streamlit — web app deployment

## How to run locally
1. Clone the repo
   git clone https://github.com/Bahaa-Edd/player-dashboard

2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate    # Windows
   source venv/bin/activate # Mac/Linux

3. Install dependencies
   pip install -r requirements.txt

4. Download the dataset from Kaggle
   https://www.kaggle.com/datasets/davidcariboo/player-scores
   Place the CSV files in the data/ folder

5. Run the notebooks in order (01 through 05)

6. Launch the Streamlit app
   streamlit run app.py

## Project structure
player-dashboard/
├── notebooks/
│   ├── 01_data_loading_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_clustering.ipynb
│   └── 05_dashboard.ipynb
├── app.py
└── requirements.txt
