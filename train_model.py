import pandas as pd
from prophet import Prophet
import joblib
import os

# Load data
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Ensure models directory exists
os.makedirs('models', exist_ok=True)

# Train one model per region
for region in df['region'].unique():
    region_df = df[df['region'] == region][['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})
    
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
    model.fit(region_df)
    
    # Save model
    joblib.dump(model, f'models/prophet_{region}.pkl')
    print(f"Model for {region} saved.")
