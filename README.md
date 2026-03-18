<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=AI%20Decision%20Support%20System&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=35&desc=For%20Business%20Managers&descAlignY=55&descSize=18" width="100%"/>

<!-- Animated Typing SVG -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=true&width=700&height=80&lines=📈+Forecast+Sales+%7C+Identify+Key+Drivers;🎚️+Simulate+Marketing+Impact+%7C+Get+Recommendations" alt="Typing SVG" />
</a>

<br/>

<!-- Badges Row 1 -->
<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Prophet-0078D4?style=for-the-badge&logo=facebook&logoColor=white" alt="Prophet"/>
  <img src="https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost"/>
</p>

<!-- Badges Row 2 -->
<p>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/github/stars/LuthandoCandlovu/ai-decision-support?style=for-the-badge&color=yellow" alt="Stars"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome"/>
  <img src="https://img.shields.io/badge/Status-Active-00C851?style=for-the-badge" alt="Status"/>
</p>

<!-- Colorful Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

---

## 🌟 Overview

<table>
<tr>
<td width="60%">

> **A data-driven decision engine for modern business managers.**

This project combines the power of **time series forecasting (Prophet)** with **machine learning interpretability (XGBoost)** inside a sleek, interactive **Streamlit** dashboard. Go from raw data to confident decisions in seconds.

**Real-world impact:**
> Imagine a regional manager spotting a predicted sales dip and *instantly* testing how a +10% marketing budget increase could offset it — all before their next meeting. 🚀

</td>
<td width="40%" align="center">

```
┌─────────────────────────┐
│   📊  Sales Forecast    │
│   🔍  Feature Drivers   │
│   🎚️  What-If Simulator │
│   💡  Smart Actions     │
└─────────────────────────┘
```

</td>
</tr>
</table>

---

## ✨ Demo

<div align="center">

> 📽️ *Replace the GIF below with a screen recording of your dashboard in action*  
> *(Recommended tool: [ScreenToGif](https://www.screentogif.com/))*

<img src="images/demo.gif" alt="Dashboard Demo" width="90%" style="border-radius:10px; border: 2px solid #00D9FF;"/>

</div>

---

## 🏗️ Architecture

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║                    🏗️  SYSTEM ARCHITECTURE                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   ┌──────────────────────────────────────────────────────────┐   ║
║   │  👤  USER INTERFACE  (Streamlit Dashboard)               │   ║
║   │  • Region Selector   • What-If Slider   • Plotly Charts  │   ║
║   └────────────────────────┬─────────────────────────────────┘   ║
║                            │                                     ║
║              ┌─────────────▼──────────────┐                      ║
║              │   ⚙️  APPLICATION LAYER    │                      ║
║              │   • Model Loader           │                      ║
║              │   • Forecast Generator     │                      ║
║              │   • Recommendation Engine  │                      ║
║              └──────┬──────────┬──────────┘                      ║
║                     │          │                                  ║
║         ┌───────────▼──┐  ┌───▼────────────┐                     ║
║         │ 🔮  PROPHET  │  │  🤖  XGBOOST   │                     ║
║         │  Time Series │  │  Feature Imp.  │                     ║
║         │  Forecasting │  │  + SHAP Values │                     ║
║         └───────┬──────┘  └──────┬─────────┘                     ║
║                 │                │                                ║
║         ┌───────▼────────────────▼─────────┐                     ║
║         │       📦  DATA LAYER             │                     ║
║         │  CSV (Region, Date, Sales,       │                     ║
║         │       Marketing Spend, Season)   │                     ║
║         └──────────────────────────────────┘                     ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

<div align="center">
<img src="images/architecture.png" alt="Architecture Diagram" width="80%"/>
</div>

---

## ⚡ Features

<div align="center">

| &nbsp; | Feature | Description |
|:------:|---------|-------------|
| 📊 | **Sales Forecasting** | Facebook Prophet predicts the next **30 days** with confidence intervals |
| 🔍 | **Feature Importance** | XGBoost reveals which factors — marketing, seasonality, region — drive sales most |
| 🎚️ | **What-If Simulation** | Real-time slider: adjust marketing spend and see forecast update instantly |
| 📈 | **Interactive Visuals** | Built with Plotly — zoom, pan, and hover for granular insights |
| 💡 | **Smart Recommendations** | Dynamic plain-English advice based on predicted trend and simulation input |
| 🧩 | **Modular Architecture** | Easily extend with new data sources, models, or regions |

</div>

---

## 🚀 Getting Started

<details>
<summary><b>📋 Prerequisites</b> — click to expand</summary>

- Python **3.8** or higher
- Git

</details>

### 🔧 Installation

**1. Clone the repository**
```bash
git clone https://github.com/LuthandoCandlovu/ai-decision-support.git
cd ai-decision-support
```

**2. Create & activate a virtual environment**
```bash
python -m venv venv

# 🪟 Windows
venv\Scripts\activate

# 🍎 macOS / 🐧 Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Generate synthetic data** *(if not already present)*
```bash
python generate_data.py
```

**5. Train models**
```bash
python train_model.py       # 🔮 Prophet models (one per region)
python train_xgboost.py     # 🤖 XGBoost for feature importance
```

**6. Launch the dashboard** 🚀
```bash
streamlit run dashboard/app.py
```

> 🌐 App opens at **http://localhost:8501**

---

## 🖥️ Usage

```
1. 🌍  Select a region from the sidebar
       │
2. 📊  View historical sales + 30-day forecast
       │
3. 🔍  Explore the feature importance chart
       │
4. 🎚️  Adjust the "What-If Simulator" marketing slider
       │
5. 💡  Read the dynamic recommendation at the bottom
```

---

## 🛠️ Tech Stack

<div align="center">

<table>
<tr>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/><br/>Core Language
  </td>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/><br/>Data
  </td>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/><br/>Numerics
  </td>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-Prophet-0078D4?style=for-the-badge&logo=facebook&logoColor=white"/><br/>Forecasting
  </td>
</tr>
<tr>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-XGBoost-189AB4?style=for-the-badge&logoColor=white"/><br/>ML / Features
  </td>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/><br/>Evaluation
  </td>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/><br/>Dashboard
  </td>
  <td align="center" width="110">
    <img src="https://img.shields.io/badge/-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/><br/>Visuals
  </td>
</tr>
</table>

</div>

---

## 🗺️ Roadmap

```
✅  Prophet time-series forecasting
✅  XGBoost feature importance
✅  Interactive Streamlit dashboard
✅  What-If marketing simulator
🔄  SHAP for deeper explainability
🔄  PostgreSQL / BigQuery integration
🔄  Multi-product & multi-region support
🔄  Streamlit Cloud deployment
🔄  User authentication (multi-tenant)
```

---

## 📁 Project Structure

```
ai-decision-support/
│
├── 📂 dashboard/
│   └── app.py                  # Main Streamlit dashboard
│
├── 📂 models/                  # Saved trained models (.joblib)
│
├── 📂 data/                    # Synthetic CSV data
│
├── 📂 images/                  # Screenshots & diagrams
│
├── 🐍 generate_data.py         # Synthetic data generator
├── 🐍 train_model.py           # Prophet training script
├── 🐍 train_xgboost.py         # XGBoost training script
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 📄 License

<div align="center">

Distributed under the **MIT License** — see [`LICENSE`](LICENSE) for full details.

</div>

---

## 📬 Contact

<div align="center">

**Luthando Candlovu**

<a href="https://github.com/LuthandoCandlovu">
  <img src="https://img.shields.io/badge/GitHub-LuthandoCandlovu-181717?style=for-the-badge&logo=github"/>
</a>
&nbsp;
<a href="https://linkedin.com/in/luthando-candlovu">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin"/>
</a>
&nbsp;
<a href="https://github.com/LuthandoCandlovu/ai-decision-support">
  <img src="https://img.shields.io/badge/Project-Repository-FF6B6B?style=for-the-badge&logo=github"/>
</a>

</div>

---

<div align="center">

<!-- Animated Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

**⭐ Found this useful? Give it a star on GitHub! ⭐**

*Built with ❤️ by Luthando Candlovu*

</div>
