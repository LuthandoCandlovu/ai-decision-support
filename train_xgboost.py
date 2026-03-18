import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import xgboost as xgb
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Create weekly aggregates
df['week'] = df['date'].dt.isocalendar().week
df['year'] = df['date'].dt.year

weekly = df.groupby(['region', 'year', 'week']).agg({
    'sales': 'sum',
    'marketing_spend': 'sum',
    'date': 'min'  # for reference
}).reset_index()

# Add seasonality features
weekly['month'] = weekly['date'].dt.month
weekly['quarter'] = weekly['date'].dt.quarter

# One-hot encode region
weekly = pd.get_dummies(weekly, columns=['region'], prefix='region')

# Features and target
feature_cols = ['marketing_spend', 'month', 'quarter'] + [c for c in weekly.columns if 'region_' in c]
X = weekly[feature_cols]
y = weekly['sales']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'XGBoost MAE: {mae:.2f}')

# Feature importance
importance = model.feature_importances_
feat_imp = pd.Series(importance, index=feature_cols).sort_values(ascending=False)

# Plot
plt.figure(figsize=(10,6))
feat_imp.plot(kind='bar')
plt.title('Feature Importance')
plt.tight_layout()
plt.savefig('models/feature_importance.png')
print('Feature importance plot saved to models/feature_importance.png')

# Save model
joblib.dump(model, 'models/xgboost_model.pkl')
print('XGBoost model saved.')
