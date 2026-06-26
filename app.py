import streamlit as st

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Government Healthcare Resource Intelligence Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.title{
    text-align:center;
    color:#0E4D92;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#555555;
    font-size:20px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.15);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# Header
# ------------------------------

st.markdown(
    "<h1 class='title'>🏥 Government Healthcare Resource Intelligence Platform</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>AI Powered Decision Support System for Healthcare Resource Allocation</p>",
    unsafe_allow_html=True
)

st.divider()

# ------------------------------
# About Project
# ------------------------------

st.header("📌 Project Overview")

st.write("""
This platform analyzes India's healthcare infrastructure using
government datasets and provides data-driven recommendations
for policymakers.

The application combines:

- Healthcare Infrastructure Analysis
- Public Health Indicators
- Healthcare Priority Index
- Policy Recommendation Engine
- Machine Learning Prediction
""")

st.divider()

# ------------------------------
# Features
# ------------------------------

st.header("🚀 Features")

col1,col2,col3=st.columns(3)

with col1:

    st.success("""
    ✅ Executive Dashboard

    ✅ Healthcare Analysis

    ✅ District Insights
    """)

with col2:

    st.info("""
    📊 Healthcare Priority Index

    📈 State Analysis

    🏥 Infrastructure Analysis
    """)

with col3:

    st.warning("""
    🤖 ML Prediction

    📄 District Report

    🏛 Government Recommendations
    """)

st.divider()

# ------------------------------
# Workflow
# ------------------------------

st.header("🔄 Project Workflow")

st.markdown("""

Raw Data

⬇

Data Cleaning

⬇

SQL Analytics

⬇

EDA

⬇

Healthcare Priority Index

⬇

Policy Recommendation Engine

⬇

Machine Learning

⬇

Interactive Dashboard

""")

st.divider()

# ------------------------------
# Technologies
# ------------------------------

st.header("🛠 Tech Stack")

tech1,tech2,tech3,tech4=st.columns(4)

tech1.metric("Language","Python")

tech2.metric("Database","MySQL")

tech3.metric("ML Model","XGBoost")

tech4.metric("Framework","Streamlit")

st.divider()

# ------------------------------
# Sidebar
# ------------------------------

st.sidebar.title("📚 Navigation")

st.sidebar.success("Select a page from the sidebar.")

st.sidebar.info("""
Pages Included

🏠 Home

📊 Executive Dashboard

🏥 Healthcare Analysis

📈 Priority Index

🏛 Recommendation Engine

🤖 ML Prediction

📄 District Report
""")

# ------------------------------
# Footer
# ------------------------------

st.markdown("---")

st.markdown(
"""
<div class='footer'>

Developed by <b>Prasanna Deshmane</b>

Government Healthcare Resource Intelligence Platform

</div>
""",
unsafe_allow_html=True
)
