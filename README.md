# AI Decision Support System

This project provides managers with data‑driven recommendations by combining time series forecasting (Prophet) with machine learning interpretability (XGBoost). An interactive Streamlit dashboard allows what‑if simulations.

## Features
- Sales forecasting with Prophet
- Feature importance analysis with XGBoost
- Interactive dashboard with region selection and what‑if slider for marketing spend
- Dynamic recommendations based on forecast trend

## How to run locally
1. Clone this repository.
2. Install dependencies: pip install -r requirements.txt
3. Generate data (if not included): python generate_data.py
4. Train models: python train_model.py and python train_xgboost.py
5. Launch dashboard: streamlit run dashboard/app.py

## Live demo
[Link to deployed app – add when deployed]
