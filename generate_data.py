import pandas as pd
import numpy as np
from datetime import datetime

np.random.seed(42)

# Date range
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)
dates = pd.date_range(start_date, end_date, freq='D')

# Regions
regions = ['North', 'South', 'West']
data = []

for region in regions:
    # Base trend: slight growth over time
    trend = np.linspace(100, 200, len(dates)) if region == 'North' else \
            np.linspace(80, 160, len(dates)) if region == 'South' else \
            np.linspace(120, 220, len(dates))
    
    # Seasonality: weekly pattern + yearly spike in November/December
    seasonal = 10 * np.sin(2 * np.pi * dates.dayofyear / 365) + \
               20 * np.sin(2 * np.pi * dates.dayofweek / 7)
    
    # Marketing spend: start as float to allow later addition of noise
    marketing = 50.0 + 20.0 * (dates.dayofweek >= 5).astype(float) + \
                30.0 * ((dates.month == 11) | (dates.month == 12)).astype(float)
    marketing += np.random.normal(0, 5, len(dates))   # now works
    
    # Sales = base + seasonality + effect of marketing + noise
    sales = trend + seasonal + 0.8 * marketing + np.random.normal(0, 15, len(dates))
    sales = np.maximum(sales, 0)  # no negative sales
    
    for i, date in enumerate(dates):
        data.append({
            'date': date,
            'region': region,
            'sales': sales[i],
            'marketing_spend': marketing[i]
        })

df = pd.DataFrame(data)
df.to_csv('data/sales_data.csv', index=False)
print("Data generated and saved to data/sales_data.csv")
