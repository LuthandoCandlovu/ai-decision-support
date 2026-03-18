import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
from prophet import Prophet
import numpy as np

st.set_page_config(layout="wide")
st.title("AI Decision Support System")

@st.cache_data
def load_data():
    return pd.read_csv('data/sales_data.csv', parse_dates=['date'])

df = load_data()

# Load XGBoost model and feature importance
@st.cache_resource
def load_xgboost():
    model = joblib.load('models/xgboost_model.pkl')
    # We'll compute feature importance from model
    return model

xgb_model = load_xgboost()
feature_names = ['marketing_spend', 'month', 'quarter', 'region_North', 'region_South', 'region_West']
importance = xgb_model.feature_importances_
feat_imp = pd.DataFrame({'feature': feature_names, 'importance': importance}).sort_values('importance', ascending=False)

# Sidebar controls
region = st.sidebar.selectbox("Select Region", df['region'].unique())
st.sidebar.markdown("---")
st.sidebar.subheader("What-If Simulator")
marketing_change = st.sidebar.slider(
    "Adjust future marketing spend (%)", 
    min_value=-50, max_value=50, value=0, step=5
)

# Filter data for selected region
region_df = df[df['region'] == region].copy()

# --- Historical Sales ---
st.subheader(f"Historical Sales - {region}")
fig1 = px.line(region_df, x='date', y='sales', title='Sales Over Time')
st.plotly_chart(fig1, use_container_width=True)

# --- Prophet Forecast ---
model = joblib.load(f'models/prophet_{region}.pkl')
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Apply what-if adjustment to forecast (simplistic: scale forecast by marketing change)
# In reality, you'd retrain or use a more sophisticated model, but this demonstrates the concept.
adjustment_factor = 1 + marketing_change / 100.0
forecast['yhat'] = forecast['yhat'] * adjustment_factor
forecast['yhat_lower'] = forecast['yhat_lower'] * adjustment_factor
forecast['yhat_upper'] = forecast['yhat_upper'] * adjustment_factor

st.subheader("30-Day Forecast (with what-if adjustment)")
fig2 = px.line(forecast, x='ds', y='yhat', title='Forecasted Sales')
# Add confidence interval
fig2.add_trace(go.Scatter(
    x=forecast['ds'].tolist() + forecast['ds'][::-1].tolist(),
    y=forecast['yhat_upper'].tolist() + forecast['yhat_lower'][::-1].tolist(),
    fill='toself',
    fillcolor='rgba(0,100,80,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    showlegend=False
))
st.plotly_chart(fig2, use_container_width=True)

# --- Feature Importance from XGBoost ---
st.subheader("What Drives Sales? (XGBoost Feature Importance)")
fig3 = px.bar(feat_imp, x='importance', y='feature', orientation='h', 
              title='Feature Importance', color='importance')
st.plotly_chart(fig3, use_container_width=True)

# --- Recommendation (enhanced with what-if) ---
last_30_avg = forecast['yhat'].iloc[-30:].mean()
previous_30_avg = forecast['yhat'].iloc[-60:-30].mean() if len(forecast) > 60 else last_30_avg
trend = "up" if last_30_avg > previous_30_avg else "down"

if trend == "down":
    base_rec = "⚠️ **Forecast Alert:** Sales are predicted to decline."
else:
    base_rec = "✅ **Positive Outlook:** Sales are forecasted to grow."

if marketing_change > 0:
    action = f"You simulated a **+{marketing_change}%** increase in marketing. This could boost sales further."
elif marketing_change < 0:
    action = f"You simulated a **{marketing_change}%** decrease in marketing. This may reduce sales."
else:
    action = "No change simulated."

rec = f"{base_rec} {action}"

st.subheader("Recommendation")
st.info(rec)

# Show raw data if needed
with st.expander("Show raw forecast data"):
    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30))
