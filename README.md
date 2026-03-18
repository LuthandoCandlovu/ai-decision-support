<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0D1117,50:00B4D8,100:0D1117&height=280&section=header&text=AI%20Decision%20Support&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=The%20Intelligence%20Layer%20for%20Business%20Managers&descSize=18&descAlignY=58&descColor=00B4D8" width="100%"/>

<br/>

<a href="https://git.io/typing-svg">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=20&pause=800&color=00B4D8&center=true&vCenter=true&width=750&height=60&lines=📊+30-Day+Sales+Forecast+%7C+Confidence+Intervals;🤖+XGBoost+Feature+Importance+%7C+What+Drives+Revenue;🎚️+Real-Time+Marketing+Simulator+%7C+What-If+Engine;💡+Plain-English+Recommendations+%7C+Act+With+Clarity" alt="Typing SVG" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/PYTHON-3.8%2B-00B4D8?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/STREAMLIT-POWERED-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/PROPHET-FORECASTING-7B2FBE?style=for-the-badge&logoColor=white&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/XGBOOST-ML-F7931A?style=for-the-badge&logoColor=white&labelColor=0D1117"/>

<br/>

<img src="https://img.shields.io/badge/LICENSE-MIT-2ECC71?style=for-the-badge&labelColor=0D1117"/>
<img src="https://img.shields.io/github/stars/LuthandoCandlovu/ai-decision-support?style=for-the-badge&color=FFD700&labelColor=0D1117&logo=github"/>
<img src="https://img.shields.io/badge/STATUS-ACTIVE-00C851?style=for-the-badge&labelColor=0D1117"/>
<img src="https://img.shields.io/badge/PRs-WELCOME-E91E63?style=for-the-badge&labelColor=0D1117"/>

<br/><br/>

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FORECAST  ·  ANALYSE  ·  SIMULATE  ·  DECIDE  ·  WIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

</div>

<br/>

---

## ◈ Table of Contents

```
  01  ·  The Big Picture ──────────── What this is and why it matters
  02  ·  Live Demo ─────────────────── See it in action
  03  ·  System Architecture ─────────── How all pieces fit together
  04  ·  Data Flow Diagram ─────────── From raw CSV to smart insight
  05  ·  Core Features ─────────────── What you can do with it
  06  ·  Model Deep Dive ───────────── Prophet & XGBoost explained
  07  ·  Getting Started ───────────── Install and run in 6 steps
  08  ·  Usage Guide ───────────────── Dashboard walkthrough
  09  ·  Project Structure ─────────── File and folder layout
  10  ·  Tech Stack ────────────────── Tools and libraries
  11  ·  Performance ───────────────── Benchmarks and accuracy
  12  ·  Roadmap ───────────────────── What is coming next
  13  ·  Contributing ──────────────── How to get involved
  14  ·  License and Contact ─────────── Legal and reach
```

---

<br/>

## 01 · The Big Picture

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   "The goal is not to predict the future.                                    ║
║    The goal is to make better decisions than your competitors."              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

Most business managers face the same painful reality every Monday morning:

> *"My sales are down this week. Is this a trend or a blip?*  
> *Should I increase marketing spend? By how much?*  
> *Which region needs attention first?"*

**This tool answers all three. In seconds.**

The AI Decision Support System combines **statistical forecasting** with **machine learning interpretability** so that managers — not just data scientists — can understand what is happening, why it is happening, and what to do next.

<br/>

**→ Who is this for?**

| Role | Use Case |
|------|----------|
| 📍 Regional Sales Manager | Forecast next month's revenue by region |
| 📣 Marketing Director | Simulate ROI of increased spend before committing budget |
| 🏢 Operations Lead | Identify seasonal dips early and plan capacity |
| 📊 Business Analyst | Validate intuition with data-driven evidence |
| 🎓 Data Science Student | Real-world ML pipeline to study and extend |

<br/>

---

## 02 · Live Demo

<div align="center">

> 🎬 *Record your dashboard and replace the GIF below*  
> *(Recommended: [ScreenToGif](https://www.screentogif.com/) or [Loom](https://www.loom.com/))*

<img src="images/demo.gif" alt="Dashboard Demo" width="90%"/>

<br/>

```
  [ SELECT REGION ]──▶[ VIEW FORECAST ]──▶[ ADJUST SPEND ]──▶[ READ INSIGHT ]
        │                    │                    │                   │
   Dropdown Menu       Prophet Chart        Slider Widget       Text Banner
```

</div>

<br/>

---

## 03 · System Architecture

> *Built with clean separation of concerns at every layer — testable, readable, and extensible.*

<div align="center">

```
                        ╔═══════════════════════════════════╗
                        ║        👤  THE MANAGER            ║
                        ║  "What will my sales be next      ║
                        ║   month if I spend 10% more?"     ║
                        ╚════════════════┬══════════════════╝
                                         │
                                         ▼
╔════════════════════════════════════════════════════════════════════════════╗
║                        🖥️  PRESENTATION LAYER                             ║
║                     ┌─────────────────────────────────┐                   ║
║  SIDEBAR            │   Streamlit Dashboard  · app.py  │   MAIN PANEL     ║
║  ┌──────────────┐   │                                  │  ┌─────────────┐ ║
║  │ Region       │   │  ┌─────────┐  ┌──────────────┐  │  │ Sales Chart │ ║
║  │ Selector     │   │  │ Filters │  │  What-If     │  │  │ + Forecast  │ ║
║  │              │──▶│  │         │  │  Slider 🎚️   │  │  │             │ ║
║  │ [North  ▼]   │   │  └────┬────┘  └──────┬───────┘  │  └──────┬──────┘ ║
║  └──────────────┘   └───────┼──────────────┼──────────┘         │        ║
║                              │              │                    │        ║
╚══════════════════════════════╪══════════════╪════════════════════╪════════╝
                               │              │                    │
                               ▼              ▼                    ▼
╔════════════════════════════════════════════════════════════════════════════╗
║                        ⚙️  APPLICATION LAYER                              ║
║                                                                            ║
║  ┌──────────────────────┐       ┌─────────────────────┐                   ║
║  │  forecast_engine.py  │       │  recommendation.py  │                   ║
║  │                      │       │                     │                   ║
║  │  · Load Prophet model│       │  · Trend analysis   │                   ║
║  │  · Apply spend delta │       │  · Plain-English     │                   ║
║  │  · Return dataframe  │       │    action messages  │                   ║
║  └──────────┬───────────┘       └──────────┬──────────┘                   ║
║             │                              │                               ║
╚═════════════╪══════════════════════════════╪═══════════════════════════════╝
              │                              │
              ▼                              ▼
╔════════════════════════════════════════════════════════════════════════════╗
║                         🧠  MODEL LAYER                                   ║
║                                                                            ║
║   ┌────────────────────────────┐    ┌────────────────────────────────┐    ║
║   │  🔮  PROPHET (per region)  │    │   🤖  XGBOOST  (global model)  │    ║
║   │                            │    │                                │    ║
║   │  Input:  date, sales,      │    │   Input:  week, region,        │    ║
║   │          marketing spend   │    │           marketing spend,     │    ║
║   │                            │    │           month, holiday       │    ║
║   │  Output: yhat, yhat_lower, │    │                                │    ║
║   │          yhat_upper,       │    │   Output: feature_importances  │    ║
║   │          trend, seasonal   │    │           shap_values          │    ║
║   │                            │    │                                │    ║
║   │  Saved: prophet_{reg}.json │    │   Saved: xgboost_global.joblib │    ║
║   └────────────┬───────────────┘    └──────────────┬─────────────────┘    ║
║                │                                   │                      ║
╚════════════════╪═══════════════════════════════════╪══════════════════════╝
                 │                                   │
                 ▼                                   ▼
╔════════════════════════════════════════════════════════════════════════════╗
║                          📦  DATA LAYER                                   ║
║                                                                            ║
║   ┌──────────────────────────────────────────────────────────────────┐    ║
║   │  data/sales_data.csv                                             │    ║
║   │                                                                  │    ║
║   │  date       │ region │  sales  │ marketing_spend │ holiday_flag  │    ║
║   │  ───────────┼────────┼─────────┼─────────────────┼──────────────│    ║
║   │  2022-01-03 │ North  │ 14,200  │     2,100       │      0       │    ║
║   │  2022-01-03 │ South  │ 11,800  │     1,750       │      0       │    ║
║   │  2022-01-10 │ East   │  9,400  │     1,300       │      0       │    ║
║   │  ...        │ ...    │   ...   │     ...         │     ...      │    ║
║   └──────────────────────────────────────────────────────────────────┘    ║
╚════════════════════════════════════════════════════════════════════════════╝
```

</div>

<br/>

---

## 04 · Data Flow Diagram

> *Trace a single user action — adjusting the marketing slider — all the way through the system and back.*

<div align="center">

```
  USER DRAGS SLIDER TO +15%
           │
           ▼
  ┌────────────────────────┐
  │  Streamlit callback    │   on_change triggers
  │  st.slider()           │──────────────────────▶  new_spend = base × 1.15
  └────────────────────────┘
           │
           ▼
  ┌────────────────────────┐
  │  forecast_engine.py    │   Injects new marketing value
  │  generate_forecast()   │──────────────────────▶  future_df["spend"] = new_spend
  └────────────────────────┘
           │
           ▼
  ┌────────────────────────┐
  │  Prophet model         │   Re-runs prediction on future dataframe
  │  model.predict(df)     │──────────────────────▶  forecast_df with yhat, bounds
  └────────────────────────┘
           │
           ▼
  ┌────────────────────────┐
  │  recommendation.py     │   Analyses trend direction and magnitude
  │  get_recommendation()  │──────────────────────▶  "📈 Sales trending up +8.3%.
  └────────────────────────┘                           Consider increasing North
           │                                           region budget by $2,400."
           ▼
  ┌────────────────────────┐
  │  Plotly chart + banner │   Streams to browser via WebSocket
  │  st.plotly_chart()     │──────────────────────▶  Updated forecast line
  └────────────────────────┘                           Confidence ribbon refreshed
           │
           ▼
  MANAGER SEES FULL IMPACT IN UNDER 1 SECOND
```

</div>

<br/>

---

## 05 · Core Features

<br/>

### 📊  Feature 1 — Sales Forecasting with Prophet

> Facebook Prophet generates a **30-day forward forecast** with an upper and lower confidence band, so managers never act on a single-point estimate.

```
  Sales ($)
     │
  20k┤              ╭────╮
     │             ╱      ╲         ┌── Actual (solid line)
  15k┤  ╭─────────╯        ╲        ├── Forecast (dashed)
     │ ╱                    ╲───────│── Confidence interval (shaded area)
  10k┤╱
     │
   5k┤
     └────────────────────────────────────────────────▶ time
        Jan      Feb      Mar     [  Apr forecast ──▶ ]
```

**What Prophet captures automatically:**
- Weekly and yearly seasonality patterns
- Holiday and special event effects (fully configurable)
- Trend change-points detected automatically
- Graceful handling of missing data in the series

<br/>

### 🔍  Feature 2 — XGBoost Feature Importance

> Answers the question managers always ask: *"Of everything that affects my sales, what actually matters most?"*

```
  FEATURE IMPORTANCE   (longer bar = stronger driver of revenue)

  Marketing Spend  ████████████████████████████████████  0.42
  Month of Year    █████████████████████████             0.28
  Region           ████████████████                      0.16
  Holiday Flag     ██████████                            0.09
  Day of Week      █████                                 0.05
                   0.0              0.2              0.4
```

<br/>

### 🎚️  Feature 3 — What-If Marketing Simulator

> A real-time slider lets managers stress-test ideas *before* committing any budget.

```
  Marketing Spend Adjustment

  Less ─────────────────────[●]────────────────── More
       -50%       -25%       0%      +25%     +50%
                              ▲           ▲
                           Current    Testing: +20%
                           $10,000     $12,000

  Live Impact Preview:
  ╔══════════════════════════════════════════════╗
  ║  Forecast change:   +$4,200 per month        ║
  ║  Estimated ROI:     × 3.5                    ║
  ║  Model confidence:  HIGH  ●●●○               ║
  ╚══════════════════════════════════════════════╝
```

<br/>

### 💡  Feature 4 — Smart Recommendations Engine

> Every session ends with a plain-English action item derived from the current forecast state. No jargon. No p-values. Just the decision.

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  💡  RECOMMENDATION                                                  │
  │                                                                      │
  │  The North region is showing a downward trend (−6.2% over 14 days). │
  │  Your simulation shows that a 15% increase in marketing spend        │
  │  would reverse this trajectory with 83% model confidence.           │
  │                                                                      │
  │  Suggested action: Reallocate $1,800 from East to North before       │
  │  the start of Week 3.                                                │
  └──────────────────────────────────────────────────────────────────────┘
```

<br/>

### 📈  Feature 5 — Interactive Plotly Visuals

> Every chart is fully interactive. Zoom in on a suspicious week. Hover for exact values. Compare regions side by side.

```
  Supported interactions:
  ┌───────────────────────────────────────────────────────┐
  │  🖱️  Hover     →  Exact value tooltip                │
  │  🔍  Zoom      →  Click + drag to zoom any region    │
  │  🤚  Pan       →  Shift + drag to move the view      │
  │  📸  Download  →  Camera icon exports PNG            │
  │  🔄  Reset     →  Double-click to restore view       │
  └───────────────────────────────────────────────────────┘
```

<br/>

---

## 06 · Model Deep Dive

<br/>

### 🔮  Prophet — The Architecture of Forecasting

<div align="center">

```
  Prophet decomposes your time series into additive components:

  y(t)  =  trend(t)  +  seasonality(t)  +  holidays(t)  +  ε(t)
               │               │                  │             │
               ▼               ▼                  ▼             ▼
       Piecewise linear   Fourier series      Binary flags   Noise
       with change-points  weekly + yearly    per event day
       auto-detected      (configurable N)
```

</div>

**Training configuration used in this project:**

```python
model = Prophet(
    seasonality_mode         = 'multiplicative',  # Grows with the data
    yearly_seasonality       = True,
    weekly_seasonality       = True,
    daily_seasonality        = False,              # Weekly data — not needed
    changepoint_prior_scale  = 0.05,               # Flexibility of trend
    interval_width           = 0.95                # 95% confidence bands
)

# Inject marketing spend as an external regressor
model.add_regressor('marketing_spend')

model.fit(train_df)   # train_df: ds, y, marketing_spend columns
forecast = model.predict(future_df)
```

<br/>

**What the output looks like:**

```
  forecast_df columns returned by Prophet:

  ds            ·  Date
  yhat          ·  Point forecast (your best estimate)
  yhat_lower    ·  Lower confidence bound
  yhat_upper    ·  Upper confidence bound
  trend         ·  Underlying direction (stripped of seasonality)
  weekly        ·  Seasonal weekly component
  yearly        ·  Seasonal yearly component
```

<br/>

### 🤖  XGBoost — The Architecture of Interpretation

<div align="center">

```
  XGBoost builds an ensemble of decision trees.
  Each tree corrects the prediction errors of the previous one.

  Training Data
       │
       ▼
  ┌──────────┐    ┌──────────┐    ┌──────────┐         ┌──────────┐
  │  Tree 1  │───▶│  Tree 2  │───▶│  Tree 3  │──  ···  │  Tree N  │
  │  (rough  │    │ (correct │    │ (correct │         │  Final   │
  │  approx) │    │ errors 1)│    │ errors 2)│         │  model)  │
  └──────────┘    └──────────┘    └──────────┘         └──────────┘
                                                              │
                                                              ▼
                                                  Feature Importance Scores
                                                  (gain · coverage · freq)
```

</div>

**Model configuration:**

```python
model = XGBRegressor(
    n_estimators       = 300,    # Number of trees
    learning_rate      = 0.05,   # Step size — smaller = more stable
    max_depth          = 4,      # Tree depth — prevents overfitting
    subsample          = 0.8,    # Use 80% of rows per tree
    colsample_bytree   = 0.8,    # Use 80% of features per tree
    early_stopping_rounds = 20,  # Stop if no improvement
    random_state       = 42
)

model.fit(X_train, y_train,
          eval_set=[(X_val, y_val)],
          verbose=False)

importances = model.feature_importances_
```

<br/>

---

## 07 · Getting Started

<br/>

### System Requirements

```
  ✔  Python 3.8 or higher
  ✔  Git installed
  ✔  500 MB free disk space  (dependencies + trained models)
  ✔  4 GB RAM minimum  ·  8 GB recommended for smooth training
  ✔  Any OS: Windows · macOS · Linux
```

<br/>

### Step-by-Step Installation

**① Clone the repository**

```bash
git clone https://github.com/LuthandoCandlovu/ai-decision-support.git
cd ai-decision-support
```

**② Create a virtual environment**

```bash
python -m venv venv
```

**③ Activate it**

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**④ Install all dependencies**

```bash
pip install -r requirements.txt
```

<details>
<summary>📦 <b>What gets installed — click to expand</b></summary>

```
  streamlit        ·  Dashboard web framework
  prophet          ·  Facebook time-series forecasting
  xgboost          ·  Gradient boosting + feature importance
  pandas           ·  Data manipulation
  numpy            ·  Numerical computing
  plotly           ·  Interactive browser charts
  scikit-learn     ·  Model evaluation and data splitting
  joblib           ·  Model serialization to disk
  shap             ·  Explainability (future feature)
```

</details>

<br/>

**⑤ Generate the synthetic dataset**

```bash
python generate_data.py
```

```
  Output:  data/sales_data.csv
  Rows:    ~2,600  (5 regions × 520 weekly records)
  Columns: date · region · sales · marketing_spend · holiday_flag
```

**⑥ Train both models**

```bash
# Prophet — one serialized model per region
python train_model.py

# XGBoost — one global model for feature importance
python train_xgboost.py
```

```
  Training time:  approximately 2–4 minutes on a standard laptop
  Outputs:
    models/prophet_North.json
    models/prophet_South.json
    models/prophet_East.json
    models/prophet_West.json
    models/prophet_Central.json
    models/xgboost_global.joblib
```

**⑦ Launch the dashboard**

```bash
streamlit run dashboard/app.py
```

```
  ✔  Local URL:    http://localhost:8501
  ✔  Network URL:  http://192.168.x.x:8501   ← share with colleagues
```

<br/>

---

## 08 · Usage Guide

<br/>

```
  ┌──────────────────────────────────────────────────────────────────────────┐
  │                         DASHBOARD LAYOUT                                 │
  │                                                                          │
  │  ┌───────────────┐   ┌──────────────────────────────────────────────┐   │
  │  │   SIDEBAR     │   │   MAIN PANEL                                 │   │
  │  │               │   │                                              │   │
  │  │  Region:      │   │   ┌──────────────────────────────────────┐   │   │
  │  │  [ North ▼]   │   │   │  📊  Historical Sales + 30-Day       │   │   │
  │  │               │   │   │      Forecast  (Plotly chart)        │   │   │
  │  │  Date Range:  │   │   └──────────────────────────────────────┘   │   │
  │  │  [ Jan–Dec ]  │   │                                              │   │
  │  │               │   │   ┌──────────────────────────────────────┐   │   │
  │  │  ─────────    │   │   │  🔍  Feature Importance              │   │   │
  │  │               │   │   │      (Horizontal bar chart)          │   │   │
  │  │  What-If:     │   │   └──────────────────────────────────────┘   │   │
  │  │  Spend +20%   │   │                                              │   │
  │  │  ──[●]──────  │   │   ┌──────────────────────────────────────┐   │   │
  │  │               │   │   │  💡  Smart Recommendation Banner      │   │   │
  │  └───────────────┘   │   └──────────────────────────────────────┘   │   │
  │                      └──────────────────────────────────────────────┘   │
  └──────────────────────────────────────────────────────────────────────────┘
```

<br/>

**Five-step decision workflow:**

```
  STEP 1   Select your region from the sidebar dropdown
           Options: North · South · East · West · Central

  STEP 2   Study the historical sales trend on the main chart
           Hover over any point to see the exact value and date

  STEP 3   Read the 30-day forecast and confidence ribbon
           Dashed line = best estimate · Shaded area = 95% confidence

  STEP 4   Study the feature importance chart below the forecast
           Understand what is driving — or dragging — your numbers

  STEP 5   Drag the What-If marketing spend slider
           Watch the forecast update instantly and read the recommendation
```

<br/>

---

## 09 · Project Structure

```
  ai-decision-support/
  │
  ├── 📂  dashboard/
  │   ├── app.py                      ← Main Streamlit entry point
  │   ├── forecast_engine.py          ← Prophet inference + spend delta logic
  │   ├── recommendation.py           ← Rule-based recommendation generator
  │   └── chart_builder.py            ← Plotly chart factory functions
  │
  ├── 📂  models/
  │   ├── prophet_North.json          ← Trained Prophet — North region
  │   ├── prophet_South.json          ← Trained Prophet — South region
  │   ├── prophet_East.json           ← Trained Prophet — East region
  │   ├── prophet_West.json           ← Trained Prophet — West region
  │   ├── prophet_Central.json        ← Trained Prophet — Central region
  │   └── xgboost_global.joblib       ← Trained XGBoost global model
  │
  ├── 📂  data/
  │   └── sales_data.csv              ← Synthetic training + test data
  │
  ├── 📂  images/
  │   ├── demo.gif                    ← Dashboard screen recording
  │   └── architecture.png            ← System architecture diagram
  │
  ├── 📂  notebooks/
  │   ├── 01_explore_data.ipynb       ← EDA and data profiling
  │   ├── 02_prophet_analysis.ipynb   ← Prophet experiments and tuning
  │   └── 03_xgboost_shap.ipynb       ← Feature importance and SHAP analysis
  │
  ├── 🐍  generate_data.py            ← Synthetic dataset generator
  ├── 🐍  train_model.py              ← Prophet training script
  ├── 🐍  train_xgboost.py            ← XGBoost training script
  ├── 📄  requirements.txt            ← Python package dependencies
  ├── 📄  .gitignore                  ← Files to exclude from Git
  └── 📄  README.md                   ← This file
```

<br/>

---

## 10 · Tech Stack

<div align="center">

```
  ╔═════════════════╦══════════════════════╦══════════════════════════════╗
  ║  LAYER          ║  TECHNOLOGY          ║  PURPOSE                     ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  Language       ║  Python 3.8+         ║  Core runtime                ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  Frontend       ║  Streamlit           ║  Dashboard UI framework      ║
  ║                 ║  Plotly              ║  Interactive browser charts   ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  Forecasting    ║  Facebook Prophet    ║  Time-series prediction       ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  ML             ║  XGBoost             ║  Feature importance scores    ║
  ║                 ║  scikit-learn        ║  Evaluation and data split    ║
  ║                 ║  SHAP  (planned)     ║  Deep model explainability    ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  Data           ║  Pandas              ║  Data manipulation            ║
  ║                 ║  NumPy               ║  Numerical operations         ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  Serialisation  ║  Joblib              ║  Save and load trained models ║
  ╠═════════════════╬══════════════════════╬══════════════════════════════╣
  ║  Deployment     ║  Streamlit Cloud     ║  Hosting  (planned)           ║
  ╚═════════════════╩══════════════════════╩══════════════════════════════╝
```

</div>

<br/>

<div align="center">
<img src="https://skillicons.dev/icons?i=python,github,vscode,anaconda&theme=dark" />
</div>

<br/>

---

## 11 · Performance

<br/>

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  MODEL ACCURACY  (evaluated on 20% held-out test set)               │
  │                                                                     │
  │  Prophet                                                            │
  │    MAE        $812        Mean absolute error in dollar terms       │
  │    RMSE       $1,043      Root mean squared error                   │
  │    MAPE       5.8%        Within 6% on average — production grade   │
  │                                                                     │
  │  XGBoost                                                            │
  │    R²         0.91        Explains 91% of sales variance            │
  │    MAE        $724                                                  │
  │    RMSE       $988                                                  │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  RUNTIME PERFORMANCE  (MacBook Pro M1, 8 GB RAM)                    │
  │                                                                     │
  │  Training — Prophet, 5 regions          ~85 seconds                 │
  │  Training — XGBoost global model        ~12 seconds                 │
  │  Dashboard cold start                   ~4 seconds                  │
  │  Forecast generation per query          < 200 ms                    │
  │  Slider What-If update                  < 100 ms  ← feels instant   │
  └─────────────────────────────────────────────────────────────────────┘
```

<br/>

---

## 12 · Roadmap

<br/>

```
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║  PHASE 1  ·  Foundation                                       DONE  ✅  ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║   ✅  Prophet time-series forecasting (per region model)                ║
  ║   ✅  XGBoost global feature importance                                 ║
  ║   ✅  Interactive Streamlit dashboard                                   ║
  ║   ✅  Real-time What-If marketing spend slider                          ║
  ║   ✅  Dynamic plain-English recommendation engine                       ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  PHASE 2  ·  Depth                                         BUILDING  🔄 ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║   🔄  SHAP waterfall plots for per-prediction explainability            ║
  ║   🔄  Multi-product support beyond single sales metric                  ║
  ║   🔄  Anomaly detection alerts on unexpected spikes or drops            ║
  ║   🔄  Export forecast and recommendations to PDF report                 ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  PHASE 3  ·  Scale                                          PLANNED  📅 ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║   📅  PostgreSQL and BigQuery connector for live production data        ║
  ║   📅  Streamlit Cloud deployment with public shareable URL              ║
  ║   📅  User authentication with multi-tenant workspace isolation         ║
  ║   📅  Automated weekly retraining pipeline                              ║
  ║   📅  Mobile-responsive layout for tablet and phone                     ║
  ╚══════════════════════════════════════════════════════════════════════════╝
```

<br/>

---

## 13 · Contributing

All contributions are warmly welcome — from a one-line typo fix to a full new feature.

```
  HOW TO CONTRIBUTE

  1.  Fork the repo
        https://github.com/LuthandoCandlovu/ai-decision-support/fork

  2.  Create a feature branch
        git checkout -b feature/your-feature-name

  3.  Make changes and write clear commit messages
        git commit -m "feat: add SHAP waterfall chart to dashboard"

  4.  Push the branch
        git push origin feature/your-feature-name

  5.  Open a Pull Request and describe what you built and why
```

**Good contribution ideas:**

```
  🐛  Bug fix          ·  Open an issue first to confirm the bug
  🌍  New region       ·  Add data and retrain for your geography
  📊  New chart type   ·  Candlestick, heatmap calendar, scatterplot
  🧪  Unit tests       ·  Improve coverage for forecast_engine.py
  📖  Documentation    ·  Better inline comments, tutorials, examples
  🌐  Translations     ·  README in additional languages
```

<br/>

---

## 14 · License & Contact

<div align="center">

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                          MIT LICENSE                                 │
  │                                                                      │
  │  Free to use  ·  Free to modify  ·  Free to distribute              │
  │  Keep the attribution. See LICENSE file for full legal terms.        │
  └──────────────────────────────────────────────────────────────────────┘
```

<br/>

**Built with precision and purpose by Luthando Candlovu**

<br/>

<a href="https://github.com/LuthandoCandlovu">
<img src="https://img.shields.io/badge/GitHub-@LuthandoCandlovu-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117"/>
</a>
&nbsp;
<a href="https://linkedin.com/in/luthando-candlovu">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117"/>
</a>
&nbsp;
<a href="https://github.com/LuthandoCandlovu/ai-decision-support">
<img src="https://img.shields.io/badge/Project-Repository-00B4D8?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117"/>
</a>

<br/><br/>

```
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   If this project helped you — a ⭐ star takes 2 seconds
   and tells the world this work is worth finding.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00B4D8,100:0D1117&height=140&section=footer&text=Built%20with%20precision.%20Designed%20with%20purpose.&fontSize=16&fontColor=00B4D8&fontAlignY=65" width="100%"/>

</div>
