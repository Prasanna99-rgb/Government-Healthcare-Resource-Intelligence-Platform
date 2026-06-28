import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from utils.styles import load_css


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="Government Healthcare Resource Intelligence Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
# -------------------------------
# LOAD DATA
# -------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

df = load_data()
# ==========================================================
# PREMIUM UI
# ==========================================================

st.markdown("""
<style>

/* Hide Streamlit Components */

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* App */

.stApp{
background:#F4F8FC;
}

/* Hero */

.hero{

background:linear-gradient(135deg,#0B3C5D,#1565C0);

padding:40px;

border-radius:22px;

color:white;

box-shadow:0px 12px 25px rgba(0,0,0,.20);

margin-bottom:25px;

}

.hero h1{

font-size:46px;

font-weight:700;

}

.hero p{

font-size:19px;

opacity:.95;

}

/* KPI */

div[data-testid="metric-container"]{

background:white;

padding:20px;

border-radius:18px;

border-left:6px solid #1565C0;

box-shadow:0px 6px 18px rgba(0,0,0,.12);

transition:.3s;

}

div[data-testid="metric-container"]:hover{

transform:translateY(-6px);

}

/* Cards */

.card{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0px 6px 16px rgba(0,0,0,.10);

margin-bottom:20px;

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:#082B4A;

}

section[data-testid="stSidebar"] *{

color:white;

}

/* Buttons */

.stButton>button{

background:#1565C0;

color:white;

border:none;

border-radius:10px;

height:45px;

width:100%;

font-weight:bold;

}

.stButton>button:hover{

background:#0D47A1;

}

/* Download */

.stDownloadButton>button{

background:#2E7D32;

color:white;

border-radius:10px;

width:100%;

height:45px;

font-weight:bold;

}

</style>

""",unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""

<div class="hero">

<h1>🏥 Government Healthcare Resource Intelligence Platform</h1>

<p>
AI-Powered Decision Support System for Public Healthcare Planning Across India
</p>

</div>

""", unsafe_allow_html=True)

st.markdown("### 🇮🇳 About the Platform")

st.info("""
This platform helps government agencies identify healthcare gaps,
prioritize districts, analyze public health indicators, and generate
AI-driven recommendations for better healthcare resource allocation.
""")

st.divider()

# ==========================================================
# PLATFORM STATISTICS
# ==========================================================

st.subheader("📊 Platform Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "States",
        df["state"].nunique()
    )

with col2:
    st.metric(
        "Districts",
        df["district"].nunique()
    )

with col3:
    st.metric(
        "Health Centres",
        f"{int(df['health_centres'].sum()):,}"
    )

with col4:
    st.metric(
        "Population",
        f"{int(df['population'].sum()):,}"
    )

st.divider()

# ==========================================================
# PLATFORM MODULES
# ==========================================================

st.subheader("🚀 Platform Modules")

c1,c2,c3 = st.columns(3)

with c1:

    st.success("""

### 📊 Analytics

✔ Executive Dashboard

✔ State Comparison

✔ District Ranking

✔ Healthcare Infrastructure

""")

with c2:

    st.info("""

### 🤖 AI Intelligence

✔ Priority Index

✔ XGBoost Prediction

✔ Recommendation Engine

✔ Risk Classification

""")

with c3:

    st.warning("""

### 🏛 Government

✔ Policy Support

✔ Healthcare Planning

✔ Resource Allocation

✔ Download Reports

""")

st.divider()

# ==========================================================
# WHY THIS PROJECT
# ==========================================================

st.subheader("🎯 Why This Project Matters")

st.markdown("""

- Identify healthcare resource gaps across districts

- Prioritize government investments

- Improve vaccination coverage analysis

- Detect high-risk healthcare regions

- Support evidence-based policy decisions

- Provide AI-powered recommendations

""")

st.divider()

# ==========================================================
# SYSTEM ARCHITECTURE
# ==========================================================

st.subheader("🏗️ System Architecture")

st.code("""

Government Datasets
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Healthcare Master Dataset
        │
        ├────────► SQL Analytics
        │
        ├────────► EDA
        │
        ├────────► Healthcare Priority Index
        │
        ├────────► AI Recommendation Engine
        │
        └────────► XGBoost Prediction
                     │
                     ▼
          Streamlit Decision Support Platform

""")

st.divider()

# ==========================================================
# END TO END WORKFLOW
# ==========================================================

st.subheader("📈 Analytics Workflow")

workflow = px.funnel(
    y=[
        "Government Data",
        "Data Cleaning",
        "Feature Engineering",
        "SQL Analysis",
        "EDA",
        "Priority Index",
        "Machine Learning",
        "Decision Support Dashboard"
    ],
    x=[100,92,85,78,70,60,48,35]
)

workflow.update_layout(height=500)

st.plotly_chart(
    workflow,
    use_container_width=True
)

st.divider()

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.subheader("🛠 Technology Stack")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.info("""
### Backend

• Python

• Pandas

• NumPy

• Joblib
""")

with c2:
    st.info("""
### Database

• MySQL

• SQL Analytics

• Views

• Window Functions
""")

with c3:
    st.info("""
### Visualization

• Streamlit

• Plotly

• Interactive Dashboard
""")

with c4:
    st.info("""
### AI / ML

• XGBoost

• Scikit-learn

• Prediction Engine
""")

st.divider()

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.subheader("⭐ Project Highlights")

left,right = st.columns(2)

with left:

    st.success("""
✔ Government Decision Support

✔ Healthcare Resource Planning

✔ AI Recommendation Engine

✔ District Intelligence

✔ Interactive Dashboards

✔ Healthcare Priority Ranking

✔ Policy Recommendation
""")

with right:

    st.success("""
✔ Machine Learning

✔ SQL Analytics

✔ Feature Engineering

✔ Streamlit Deployment

✔ Download Reports

✔ Executive Insights

✔ Production Ready
""")

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""

---

### 👨‍💻 Developed By

**Prasanna Deshmane**

Government Healthcare Resource Intelligence Platform

Python • MySQL • Streamlit • Plotly • XGBoost

Designed for Data Analyst Portfolio & Interviews

""")
