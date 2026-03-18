<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06080f,50:4c78ff,100:9b6dff&height=220&section=header&text=AI%20Decision%20Support&fontSize=54&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Sales+Forecasting+%7C+Feature+Importance+%7C+What-If+Simulation&descSize=17&descAlignY=58&descColor=a0b4ff" width="100%"/>

</div>

<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=16&pause=1000&color=4C78FF&center=true&vCenter=true&width=800&height=48&lines=📊+30-Day+Sales+Forecast+with+95%25+Confidence+Intervals;🤖+XGBoost+Feature+Importance+%7C+What+Drives+Revenue;🎚️+Real-Time+Marketing+Simulator+%7C+Under+100ms;💡+Plain-English+Recommendations+%7C+Act+With+Clarity;🚀+Built+with+Prophet+%2B+XGBoost+%2B+Streamlit" alt="Typing SVG"/>
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.8+-4c78ff?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1120)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=0d1120)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-9b6dff?style=for-the-badge&logoColor=white&labelColor=0d1120)
![XGBoost](https://img.shields.io/badge/XGBoost-00D4AA?style=for-the-badge&logoColor=0d1120&labelColor=0d1120)
![License](https://img.shields.io/badge/License-MIT-ff7b3a?style=for-the-badge&labelColor=0d1120)
![Stars](https://img.shields.io/github/stars/LuthandoCandlovu/ai-decision-support?style=for-the-badge&color=ffd700&labelColor=0d1120&logo=github)

</div>

---

## 🧭 Overview

Most business managers face the same painful reality every Monday morning:

> *"My sales are down. Is this a trend or a blip? Should I increase marketing spend? By how much? Which region needs attention first?"*

**This tool answers all three — in seconds.**

The AI Decision Support System combines **statistical forecasting (Prophet)** with **machine learning interpretability (XGBoost)** inside an interactive Streamlit dashboard. Managers — not just data scientists — can understand what is happening, why it is happening, and what to do next.

<br/>

| Role | Use Case |
|------|----------|
| 📍 Regional Sales Manager | Forecast next month's revenue by region |
| 📣 Marketing Director | Simulate ROI of increased spend before committing |
| 🏢 Operations Lead | Identify seasonal dips early and plan capacity |
| 📊 Business Analyst | Validate intuition with data-driven evidence |
| 🎓 Data Science Student | Real-world ML pipeline to study and extend |

---

## 🖥️ Live Dashboard

<div align="center">
<img src="https://github.com/user-attachments/assets/eb879ca6-a6fc-41f2-a653-22e3718163fc" width="100%" alt="AI Decision Support Dashboard"/>
</div>

---

## 🏗️ System Architecture

> A clean 5-layer design — each layer has **one responsibility**, making the system testable and easy to extend.

```
┌─────────────────────────────────────────────────────────────┐
│                    🖥️  PRESENTATION LAYER                    │
│           Streamlit Dashboard · Sidebar · Sliders            │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    ⚙️  APPLICATION LAYER                     │
│     forecast_engine.py · recommendation.py · chart_builder   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                      🧠  MODEL LAYER                         │
│         Prophet (per region)  ·  XGBoost (global)            │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                       📦  DATA LAYER                         │
│                       sales_data.csv                         │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Components | Responsibility |
|-------|-----------|----------------|
| 🖥️ Presentation | Streamlit dashboard, sidebar, sliders | User interaction & rendering |
| ⚙️ Application | `forecast_engine.py`, `recommendation.py`, `chart_builder.py` | Business logic |
| 🧠 Model | Prophet (per region), XGBoost (global) | Inference & explainability |
| 📦 Data | `sales_data.csv` | Training & prediction input |

---

## ⚡ Data Flow — What-If Pipeline

> From slider drag to updated forecast: **under 100ms**. Here is exactly how.

```
 User drags slider
        │
        ▼
 ┌─────────────────┐
 │  st.slider()    │  new_spend = base × 1.20
 │  on_change()    │  fires immediately
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ forecast_engine │  future_df["marketing_spend"] = new_spend
 │      .py        │  inject spend delta into future frame
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ model.predict() │  returns yhat · yhat_lower · yhat_upper
 │  Prophet model  │  loaded from prophet_North.json
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │recommendation   │  trend analysis → plain-English action
 │      .py        │  "North trending up +8.3% ..."
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │st.plotly_chart()│  chart redraws in browser
 │   browser UI    │  ⚡ total time: < 100ms
 └─────────────────┘
```

---

## 🛠️ Technology Stack

<div align="center">

| Tool | Version | Role |
|------|---------|------|
| ![Python](https://img.shields.io/badge/Python-4c78ff?style=flat-square&logo=python&logoColor=white) **Python** | 3.8+ | Core language |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) **Streamlit** | latest | Dashboard UI & real-time widgets |
| ![Prophet](https://img.shields.io/badge/Prophet-9b6dff?style=flat-square&logoColor=white) **Prophet** | v1.1.5 | Time-series forecasting |
| ![XGBoost](https://img.shields.io/badge/XGBoost-00D4AA?style=flat-square&logoColor=white) **XGBoost** | v1.7.6 | Feature importance & gradient boosting |
| ![Plotly](https://img.shields.io/badge/Plotly-4c78ff?style=flat-square&logo=plotly&logoColor=white) **Plotly** | latest | Interactive charts (zoom, hover, export) |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) **Pandas** | latest | Data manipulation |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) **NumPy** | latest | Numerical computing |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-f7931e?style=flat-square&logo=scikit-learn&logoColor=white) **scikit-learn** | latest | Evaluation utilities |
| **Joblib** | latest | Model serialisation & persistence |

</div>

---

## ✨ Core Features

### 📊 Feature 1 — 30-Day Sales Forecast

Prophet generates a forward forecast with a **95% confidence interval** so managers see both the best estimate and the uncertainty band.

```python
model = Prophet(
    seasonality_mode        = 'multiplicative',
    yearly_seasonality      = True,
    weekly_seasonality      = True,
    changepoint_prior_scale = 0.05,
    interval_width          = 0.95   # 95% confidence
)
model.add_regressor('marketing_spend')
model.fit(train_df)
forecast = model.predict(future_df)
```

| Output Column | Description |
|--------------|-------------|
| `yhat` | Point forecast — best estimate |
| `yhat_lower` | Lower 95% confidence bound |
| `yhat_upper` | Upper 95% confidence bound |
| `trend` | Underlying direction without seasonality |

<br/>

### 🔍 Feature 2 — Feature Importance (XGBoost)

Tells managers exactly **which factors drive sales** — so budget decisions are based on data, not gut feeling.

| Feature | Score | Meaning |
|---------|:-----:|---------|
| 💰 Marketing Spend | **0.42** | Biggest controllable lever |
| 📅 Month of Year | 0.28 | Strong seasonal patterns |
| 🗺️ Region | 0.16 | Geography drives real differences |
| 🎉 Holiday Flag | 0.09 | Events have measurable impact |
| 📆 Day of Week | 0.05 | Minor weekly variation |

<br/>

### 🎚️ Feature 3 — What-If Marketing Simulator

Drag the slider. Watch the forecast update. No reload. No waiting. **Results in under 100ms.**

```
  Base spend:   $10,000
  Adjusted:     $12,000  (+20%)
  ─────────────────────────────
  Forecast Δ:   +$4,200 / month
  ROI:          ×3.5
  Confidence:   HIGH  ●●●○
```

<br/>

### 💡 Feature 4 — Smart Recommendations

Every session closes with a plain-English action. No jargon. Just the next move.

> *"North region trending up +8.3%. Current momentum strong. Maintain +20% marketing spend to sustain the trajectory."*

<br/>

### 📈 Feature 5 — Interactive Plotly Charts

Zoom · Pan · Hover for exact values · Export PNG — all built-in. Five regions selectable from the sidebar. Charts update on every interaction.

---

## 🚀 Getting Started

### Requirements

```
Python 3.8+  ·  Git  ·  ~500 MB disk  ·  8 GB RAM recommended
```

### Installation

```bash
# 1 — Clone
git clone https://github.com/LuthandoCandlovu/ai-decision-support.git
cd ai-decision-support

# 2 — Virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3 — Dependencies
pip install -r requirements.txt

# 4 — Generate synthetic data
python generate_data.py

# 5 — Train models
python train_model.py           # Prophet — one per region (~85s)
python train_xgboost.py         # XGBoost — global model (~12s)

# 6 — Launch dashboard
streamlit run dashboard/app.py
```

> 🌐 Opens at **http://localhost:8501**

<details>
<summary><b>📦 Full dependency list</b></summary>

```
streamlit      Dashboard framework
prophet        Time-series forecasting
xgboost        Feature importance & ML
pandas         Data manipulation
numpy          Numerics
plotly         Interactive charts
scikit-learn   Evaluation utilities
joblib         Model persistence
shap           Explainability (planned)
```

</details>

---

## 📖 Usage

| Step | Action | What Happens |
|:----:|--------|-------------|
| 1 | Select region (sidebar) | All charts switch to that region's model |
| 2 | Read the historical trend | Blue line = past actual sales |
| 3 | Study the forecast ribbon | Orange dashed = prediction · shaded = 95% CI |
| 4 | Check feature importance | See what actually drives the numbers |
| 5 | Drag marketing spend slider | Forecast updates in real-time |
| 6 | Read the recommendation | Plain-English action ready for your team |

---

## 📁 Project Structure

```
ai-decision-support/
│
├── 📂 dashboard/
│   ├── app.py                  ← Streamlit entry point
│   ├── forecast_engine.py      ← Prophet inference + spend delta
│   ├── recommendation.py       ← Plain-English action generator
│   └── chart_builder.py        ← Plotly chart factory
│
├── 📂 models/
│   ├── prophet_North.json
│   ├── prophet_South.json
│   ├── prophet_East.json
│   ├── prophet_West.json
│   ├── prophet_Central.json
│   └── xgboost_global.joblib
│
├── 📂 data/
│   └── sales_data.csv
│
├── 📂 notebooks/
│   ├── 01_explore_data.ipynb
│   ├── 02_prophet_analysis.ipynb
│   └── 03_xgboost_shap.ipynb
│
├── 🐍 generate_data.py
├── 🐍 train_model.py
├── 🐍 train_xgboost.py
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 📊 Performance

**Accuracy** — 20% held-out test set:

| Model | MAE | RMSE | Score |
|-------|----:|-----:|------:|
| Prophet | $812 | $1,043 | MAPE **5.8%** |
| XGBoost | $724 | $988 | R² **0.91** |

**Runtime** — MacBook Pro M1, 8 GB RAM:

| Task | Time |
|------|-----:|
| Prophet training (5 regions) | ~85 sec |
| XGBoost training | ~12 sec |
| Dashboard cold start | ~4 sec |
| Forecast per query | < 200ms |
| Slider What-If update | **< 100ms** ⚡ |

---

## 🗺️ Roadmap

| Status | Feature |
|:------:|---------|
| ✅ | Prophet forecasting per region |
| ✅ | XGBoost feature importance |
| ✅ | Streamlit interactive dashboard |
| ✅ | Real-time What-If slider |
| ✅ | Smart recommendations engine |
| 🔄 | SHAP waterfall explainability plots |
| 🔄 | Multi-product support |
| 🔄 | Anomaly detection alerts |
| 📅 | PDF export of forecasts |
| 📅 | PostgreSQL / BigQuery connector |
| 📅 | Streamlit Cloud deployment |
| 📅 | Multi-tenant user authentication |
| 📅 | Automated weekly retraining |

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# → Open a Pull Request on GitHub
```

Ideas welcome: SHAP plots · new region data · unit tests · new chart types · translations

---

## 📜 License & Contact

**MIT License — free to use, modify, and distribute.**

<div align="center">

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-@LuthandoCandlovu-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1120)](https://github.com/LuthandoCandlovu)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1120)](https://linkedin.com/in/luthando-candlovu)
&nbsp;
[![View Project](https://img.shields.io/badge/View_Project-4C78FF?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1120)](https://github.com/LuthandoCandlovu/ai-decision-support)

<br/><br/>

> ⭐ If this project helped you — a star on GitHub takes 2 seconds and means a lot.

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:9b6dff,50:4c78ff,100:06080f&height=120&section=footer&text=Built+with+precision.+Designed+with+purpose.&fontSize=14&fontColor=a0b4ff&fontAlignY=65" width="100%"/>

</div>
