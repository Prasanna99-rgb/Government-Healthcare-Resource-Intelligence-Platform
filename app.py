import streamlit as st

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Government Healthcare Resource Intelligence Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F4F8FB;
}

.block-container{
    padding-top:1rem;
}

.hero{
    background:linear-gradient(90deg,#0F4C81,#2E86C1);
    padding:35px;
    border-radius:15px;
    color:white;
    text-align:center;
}

.metric-box{
    background:white;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #0F4C81;
    box-shadow:0px 4px 12px rgba(0,0,0,0.12);
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Hero Section
# ----------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🏥 Government Healthcare Resource Intelligence Platform</h1>

<h4>
AI Powered Decision Support System for Healthcare Planning
</h4>

<p>
Healthcare Analytics • Machine Learning • Government Policy Recommendation
</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------
# About Project
# ----------------------------------------------------

st.header("📌 About the Project")

st.write("""

The **Government Healthcare Resource Intelligence Platform**
is an end-to-end healthcare analytics solution built using
real Indian government datasets.

The objective is to help policymakers identify districts
requiring immediate healthcare investment by combining:

- Healthcare Infrastructure
- Census Data
- NFHS Health Indicators
- Healthcare Priority Index
- Policy Recommendation Engine
- Machine Learning Prediction

""")

st.divider()

# ----------------------------------------------------
# Project Workflow
# ----------------------------------------------------

st.header("🔄 Project Workflow")

st.markdown("""

```text
Raw Government Datasets

↓

Data Cleaning & Integration

↓

SQL Business Analytics

↓

Exploratory Data Analysis

↓

Healthcare Priority Index

↓

Government Policy Recommendation

↓

Machine Learning Prediction

↓

Interactive Streamlit Dashboard
```

""")

st.divider()

# ----------------------------------------------------
# Core Modules
# ----------------------------------------------------

st.header("🚀 Platform Modules")

col1,col2,col3=st.columns(3)

with col1:

    st.info("""

### 📊 Executive Dashboard

✔ KPIs

✔ State Analysis

✔ District Analysis

✔ Infrastructure Overview

""")

with col2:

    st.success("""

### 🏥 Healthcare Intelligence

✔ Vaccination

✔ Anaemia

✔ Maternal Health

✔ Child Nutrition

✔ Healthcare Priority Index

""")

with col3:

    st.warning("""

### 🤖 AI Decision Support

✔ Policy Recommendation

✔ Healthcare Ranking

✔ XGBoost Prediction

✔ District Report

""")

st.divider()

# ----------------------------------------------------
# Technology Stack
# ----------------------------------------------------

st.header("🛠 Technology Stack")

c1,c2,c3,c4,c5=st.columns(5)

with c1:
    st.metric("Language","Python")

with c2:
    st.metric("Database","MySQL")

with c3:
    st.metric("Analytics","Pandas")

with c4:
    st.metric("ML","XGBoost")

with c5:
    st.metric("Framework","Streamlit")

st.divider()

# ----------------------------------------------------
# Project Highlights
# ----------------------------------------------------

st.header("⭐ Project Highlights")

left,right=st.columns(2)

with left:

    st.success("""

### Analytics

✅ SQL Analytics

✅ Healthcare KPIs

✅ Government Insights

✅ State Comparison

✅ District Ranking

✅ Public Health Analysis

""")

with right:

    st.success("""

### AI Features

✅ Healthcare Priority Index

✅ Government Recommendation Engine

✅ Predictive Analytics

✅ XGBoost Model

✅ Downloadable Reports

✅ Interactive Dashboard

""")

st.divider()

# ----------------------------------------------------
# Dashboard Navigation
# ----------------------------------------------------

st.header("📂 Dashboard Navigation")

st.markdown("""

Use the **left sidebar** to explore the platform.

### Available Pages

🏠 Home

📊 Executive Dashboard

🏥 Healthcare Analysis

📍 India Healthcare Map

📈 Healthcare Priority Index

🏛 Government Action Center

🤖 ML Prediction

📄 District Report

""")

st.divider()

# ----------------------------------------------------
# Why This Project?
# ----------------------------------------------------

st.header("🎯 Why This Project Matters")

st.write("""

India has thousands of healthcare facilities distributed
across hundreds of districts.

This platform helps identify

- Healthcare resource gaps

- Districts needing investment

- Vaccination deficiencies

- Maternal healthcare issues

- Child nutrition concerns

- High-risk districts requiring immediate government action

""")

st.divider()

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.markdown("""

<div class="footer">

Developed by <b>Prasanna Deshmane</b>

Government Healthcare Resource Intelligence Platform

Python • MySQL • Machine Learning • Streamlit

</div>

""",unsafe_allow_html=True)
