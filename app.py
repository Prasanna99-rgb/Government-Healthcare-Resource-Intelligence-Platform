import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.styles import load_css

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Government Healthcare Resource Intelligence Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A8A,#2563EB);
padding:45px;
border-radius:25px;
text-align:center;
box-shadow:0 10px 35px rgba(0,0,0,.45);
">

<h1 style="color:white;font-size:52px;margin-bottom:10px;">
🏥 Government Healthcare Resource Intelligence Platform
</h1>

<h3 style="color:#E2E8F0;">
AI-Powered Decision Support System for Public Healthcare Planning Across India
</h3>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# ABOUT PLATFORM
# ==========================================================

st.markdown("## 🌍 About the Platform")

st.info("""
This AI-powered platform helps government agencies identify healthcare gaps,
prioritize districts, monitor healthcare performance, and generate
data-driven recommendations for effective resource allocation across India.
""")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# PLATFORM OVERVIEW
# ==========================================================

st.markdown("## 📊 Platform Overview")

total_states = df["state"].nunique()

total_districts = df["district"].nunique()

total_population = int(df["population"].sum())

total_health_centres = int(df["health_centres"].sum())

avg_priority = df["healthcare_priority_score"].mean()

critical = (df["priority_level"] == "Critical").sum()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "🏛 States",
        total_states
    )

    st.metric(
        "👨‍👩‍👧 Population",
        f"{total_population:,}"
    )

with col2:

    st.metric(
        "📍 Districts",
        total_districts
    )

    st.metric(
        "🚨 Critical Districts",
        critical
    )

with col3:

    st.metric(
        "🏥 Health Centres",
        f"{total_health_centres:,}"
    )

    st.metric(
        "📈 Avg Priority Score",
        f"{avg_priority:.2f}"
    )

st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# PLATFORM MODULES
# ==========================================================

st.markdown("## 🚀 Platform Modules")

st.markdown(
    "Navigate through powerful analytics modules designed for healthcare planning and decision-making."
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div style="background:#1E293B;
padding:25px;
border-radius:18px;
border:1px solid #334155;
margin-bottom:20px;">

<h3 style="color:#60A5FA;">📊 Executive Dashboard</h3>

<p style="color:#CBD5E1;">
National healthcare KPIs, infrastructure monitoring,
priority districts and executive decision support.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#1E293B;
padding:25px;
border-radius:18px;
border:1px solid #334155;
margin-bottom:20px;">

<h3 style="color:#34D399;">🏥 Infrastructure Analysis</h3>

<p style="color:#CBD5E1;">
Healthcare centres, infrastructure gaps,
population coverage and accessibility analysis.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#1E293B;
padding:25px;
border-radius:18px;
border:1px solid #334155;">

<h3 style="color:#FBBF24;">📍 District Intelligence</h3>

<p style="color:#CBD5E1;">
District-wise healthcare performance,
ranking and priority assessment.
</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div style="background:#1E293B;
padding:25px;
border-radius:18px;
border:1px solid #334155;
margin-bottom:20px;">

<h3 style="color:#A78BFA;">🤖 AI Prediction</h3>

<p style="color:#CBD5E1;">
Predict Healthcare Priority Score using
XGBoost Machine Learning model.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#1E293B;
padding:25px;
border-radius:18px;
border:1px solid #334155;
margin-bottom:20px;">

<h3 style="color:#FB7185;">📈 Resource Optimization</h3>

<p style="color:#CBD5E1;">
Identify resource shortages and recommend
optimal healthcare allocation strategies.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#1E293B;
padding:25px;
border-radius:18px;
border:1px solid #334155;">

<h3 style="color:#22D3EE;">📄 Reports & Insights</h3>

<p style="color:#CBD5E1;">
Generate executive reports, download datasets
and visualize healthcare intelligence.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# SYSTEM ARCHITECTURE
# ==========================================================

st.markdown("## 🏗️ Platform Architecture")

st.markdown("""
<div style="
background:#1E293B;
padding:25px;
border-radius:20px;
border:1px solid #334155;
">

<h3 style="color:#60A5FA;">Healthcare Intelligence Workflow</h3>

<br>

<h4 style="color:#F8FAFC;">
📂 Healthcare Dataset
</h4>

<p style="color:#CBD5E1;">
⬇
</p>

<h4 style="color:#F8FAFC;">
🧹 Data Cleaning & Feature Engineering
</h4>

<p style="color:#CBD5E1;">
⬇
</p>

<h4 style="color:#F8FAFC;">
📊 Healthcare Priority Index
</h4>

<p style="color:#CBD5E1;">
⬇
</p>

<h4 style="color:#F8FAFC;">
🤖 XGBoost AI Prediction
</h4>

<p style="color:#CBD5E1;">
⬇
</p>

<h4 style="color:#F8FAFC;">
📈 Executive Decision Dashboard
</h4>

<p style="color:#CBD5E1;">
⬇
</p>

<h4 style="color:#22C55E;">
🏥 Government Resource Allocation
</h4>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# KEY FEATURES
# ==========================================================

st.markdown("## ⭐ Platform Highlights")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
### 📊 Analytics

✔ Executive Dashboard

✔ State Analysis

✔ District Analysis

✔ Infrastructure Gap

✔ Interactive Charts
""")

with c2:

    st.info("""
### 🤖 AI Intelligence

✔ XGBoost Prediction

✔ Priority Score

✔ Risk Classification

✔ AI Recommendations

✔ Decision Support
""")

with c3:

    st.warning("""
### 🚀 Business Value

✔ Government Planning

✔ Resource Allocation

✔ Healthcare Monitoring

✔ Public Health Insights

✔ Policy Support
""")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# QUICK STATISTICS
# ==========================================================

st.markdown("## 📈 Platform Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📍 Districts", df["district"].nunique())

with col2:
    st.metric("🏛 States", df["state"].nunique())

with col3:
    st.metric("🏥 Health Centres", f"{int(df['health_centres'].sum()):,}")

with col4:
    st.metric("🤖 AI Model", "XGBoost")


# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.markdown("## 💻 Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
border:1px solid #334155;
">
<h2>🐍</h2>
<h4 style="color:#60A5FA;">Python</h4>
<p style="color:#CBD5E1;">Data Processing</p>
</div>
""", unsafe_allow_html=True)

with tech2:
    st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
border:1px solid #334155;
">
<h2>📊</h2>
<h4 style="color:#22C55E;">Streamlit</h4>
<p style="color:#CBD5E1;">Interactive Dashboard</p>
</div>
""", unsafe_allow_html=True)

with tech3:
    st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
border:1px solid #334155;
">
<h2>🤖</h2>
<h4 style="color:#F59E0B;">XGBoost</h4>
<p style="color:#CBD5E1;">Machine Learning</p>
</div>
""", unsafe_allow_html=True)

with tech4:
    st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
border:1px solid #334155;
">
<h2>📈</h2>
<h4 style="color:#A855F7;">Plotly</h4>
<p style="color:#CBD5E1;">Interactive Visualizations</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# DEVELOPER
# ==========================================================

st.markdown("## 👨‍💻 Developer")

st.markdown("""
<div style="
background:linear-gradient(135deg,#1E293B,#0F172A);
padding:30px;
border-radius:20px;
border:1px solid #334155;
">

<h2 style="color:white;">
Prasanna Deshmane
</h2>

<h4 style="color:#60A5FA;">
Data Analyst | Python | SQL | Machine Learning | Streamlit
</h4>

<p style="color:#CBD5E1;">
This project demonstrates AI-powered healthcare analytics for
government decision-making using real-world healthcare data,
interactive dashboards, and machine learning.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:20px;
background:#111827;
border-radius:15px;
border:1px solid #334155;
">

<h3 style="color:white;">
🏥 Government Healthcare Resource Intelligence Platform
</h3>

<p style="color:#CBD5E1;">
AI-Powered Decision Support System for Public Healthcare Planning
</p>

<p style="color:#94A3B8;">
Built with ❤️ using Streamlit • Python • XGBoost • Plotly
</p>

</div>
""", unsafe_allow_html=True)
