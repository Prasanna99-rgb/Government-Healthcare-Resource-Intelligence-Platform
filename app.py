import streamlit as st
import pandas as pd
from PIL import Image

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Government Healthcare Resource Intelligence Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-bottom:1rem;
padding-left:2rem;
padding-right:2rem;
}

.main{
background-color:#F4F8FC;
}

.hero{

background:linear-gradient(135deg,#0B3C5D,#328CC1);

padding:35px;

border-radius:20px;

color:white;

text-align:center;

box-shadow:0px 8px 20px rgba(0,0,0,.15);

}

.hero h1{

font-size:44px;

font-weight:700;

}

.hero p{

font-size:20px;

opacity:.95;

}

.card{

background:white;

padding:20px;

border-radius:15px;

box-shadow:0 4px 12px rgba(0,0,0,.08);

border-left:6px solid #0B3C5D;

}

.section{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0 2px 10px rgba(0,0,0,.08);

margin-bottom:20px;

}

.footer{

text-align:center;

font-size:15px;

color:gray;

padding-top:30px;

}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.image(
    "https://img.icons8.com/color/96/hospital-3.png",
    width=80
)

st.sidebar.title("Healthcare Platform")

st.sidebar.success(
    "Government Decision Support System"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Platform Modules

🏠 Home

📊 Executive Dashboard

🏥 Healthcare Analysis

🗺 India Healthcare Map

📈 Healthcare Priority Index

🏛 Government Action Center

🤖 ML Prediction

📄 District Report

""")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Built using

Python

Streamlit

Plotly

MySQL

XGBoost
"""
)

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown("""

<div class="hero">

<h1>

🏥 Government Healthcare Resource Intelligence Platform

</h1>

<p>

AI Powered Decision Support System for Public Healthcare Planning

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------------
# INTRODUCTION
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("📌 About This Platform")

st.write("""

The Government Healthcare Resource Intelligence Platform is an AI-powered analytics solution designed to support data-driven healthcare planning across India.

The platform integrates healthcare infrastructure, demographic statistics, and public health indicators to identify districts that require immediate attention and generate actionable recommendations for policymakers.

""")

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# PLATFORM FEATURES
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("🚀 Platform Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
### 📊 Analytics

- Executive Dashboard
- State Analysis
- District Analysis
- Healthcare Infrastructure
- Population Insights
- Health Indicators
""")

with col2:

    st.markdown("""
### 🏥 Healthcare Intelligence

- Vaccination Analysis
- Anaemia Analysis
- Child Nutrition
- Maternal Health
- Female Literacy
- Priority Index
""")

with col3:

    st.markdown("""
### 🤖 AI Decision Support

- Government Recommendation
- XGBoost Prediction
- District Ranking
- Priority Score
- Download Reports
- Decision Support
""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# PROJECT WORKFLOW
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("🔄 End-to-End Analytics Workflow")

st.code("""

Raw Government Datasets
          │
          ▼
Data Cleaning & Integration
          │
          ▼
SQL Business Analytics
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Healthcare Priority Index
          │
          ▼
Government Recommendation Engine
          │
          ▼
Machine Learning (XGBoost)
          │
          ▼
Interactive Streamlit Dashboard

""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# TECH STACK
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("🛠 Technology Stack")

c1,c2,c3,c4,c5,c6 = st.columns(6)

with c1:
    st.metric("Language","Python")

with c2:
    st.metric("Database","MySQL")

with c3:
    st.metric("EDA","Pandas")

with c4:
    st.metric("Visualization","Plotly")

with c5:
    st.metric("Machine Learning","XGBoost")

with c6:
    st.metric("Framework","Streamlit")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# WHY THIS PROJECT
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("🎯 Why This Platform?")

left,right = st.columns(2)

with left:

    st.success("""

✔ Identify healthcare resource gaps

✔ Compare district performance

✔ Detect high-risk districts

✔ Improve healthcare planning

✔ Monitor public health indicators

✔ Assist government decision making

""")

with right:

    st.info("""

✔ AI-powered recommendations

✔ Interactive dashboards

✔ Healthcare Priority Index

✔ Machine Learning predictions

✔ Downloadable reports

✔ Executive insights

""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# PAGE GUIDE
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("📂 Explore the Platform")

page1,page2,page3 = st.columns(3)

with page1:

    st.info("""

🏠 Home

📊 Executive Dashboard

🏥 Healthcare Analysis

""")

with page2:

    st.warning("""

🗺 India Healthcare Map

📈 Priority Index

🏛 Action Center

""")

with page3:

    st.success("""

🤖 ML Prediction

📄 District Report

⬇ Download Reports

""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# PROJECT STATISTICS
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("📈 Project Statistics")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Datasets","3")

with col2:
    st.metric("States","36+")

with col3:
    st.metric("Districts","700+")

with col4:
    st.metric("ML Model","XGBoost")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# INTERVIEW HIGHLIGHTS
# ---------------------------------------------------------

st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("⭐ Highlights")

st.write("""

This project demonstrates:

• End-to-End Data Analytics

• SQL Business Analysis

• Exploratory Data Analysis

• Healthcare Decision Intelligence

• Feature Engineering

• Machine Learning (XGBoost)

• Policy Recommendation Engine

• Interactive Streamlit Dashboard

• Downloadable Reports

• Government Decision Support

""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.markdown("""

<div class="footer">

<h3>Government Healthcare Resource Intelligence Platform</h3>

Developed by <b>Prasanna Deshmane</b>

Python • MySQL • Streamlit • Plotly • XGBoost

</div>

""",unsafe_allow_html=True)
