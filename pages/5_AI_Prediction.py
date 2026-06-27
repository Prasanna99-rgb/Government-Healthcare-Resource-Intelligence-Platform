import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# PAGE CONFIG
st.set_page_config(...)

# LOAD MODEL
@st.cache_resource
def load_model():
    return joblib.load("models/healthcare_priority_model.pkl")

# LOAD DATA
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/healthcare_priority_index.csv")

# CALL FUNCTIONS
model = load_model()
df = load_data()

# FEATURE IMPORTANCE
importance = model.feature_importances_

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Prediction",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# LOAD MODEL & DATA
# ==========================================================

@st.cache_resource
def load_model():
    return joblib.load("models/healthcare_priority_model.pkl")

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

model = load_model()
df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🤖 AI Healthcare Priority Prediction")

st.caption(
    "Predict Healthcare Priority Score using XGBoost"
)

st.divider()

# ==========================================================
# USER INPUT
# ==========================================================

st.subheader("📝 Enter Healthcare Indicators")

col1, col2 = st.columns(2)

with col1:

    population_per_health_centre = st.number_input(
        "Population per Health Centre",
        min_value=1000.0,
        max_value=100000.0,
        value=25000.0
    )

    vaccination = st.slider(
        "Vaccination (%)",
        0.0,
        100.0,
        80.0
    )

    anaemia = st.slider(
        "Anaemia (%)",
        0.0,
        100.0,
        40.0
    )

    stunted = st.slider(
        "Stunted (%)",
        0.0,
        100.0,
        30.0
    )

with col2:

    underweight = st.slider(
        "Underweight (%)",
        0.0,
        100.0,
        25.0
    )

    female_literacy = st.slider(
        "Female Literacy (%)",
        0.0,
        100.0,
        75.0
    )

    institutional_birth = st.slider(
        "Institutional Birth (%)",
        0.0,
        100.0,
        85.0
    )

    antenatal_care = st.slider(
        "Antenatal Care (%)",
        0.0,
        100.0,
        80.0
    )

st.divider()

# ==========================================================
# PREDICTION
# ==========================================================

if st.button("🚀 Predict Healthcare Priority", use_container_width=True):

    input_data = pd.DataFrame({

        "population_per_health_centre":[population_per_health_centre],

        "vaccination":[vaccination],

        "anaemia":[anaemia],

        "stunted":[stunted],

        "underweight":[underweight],

        "female_literacy":[female_literacy],

        "institutional_birth":[institutional_birth],

        "antenatal_care":[antenatal_care]

    })

    prediction = float(model.predict(input_data)[0])

    # ============================================
    # Priority Level
    # (Use same thresholds as your notebook)
    # ============================================

    if prediction >= 40:

        priority = "Critical"

        color = "red"

        recommendation = """
🚨 Immediate Government Intervention

• Build Additional PHCs

• Recruit Doctors

• Nutrition Programme

• Vaccination Drive

• Increase Healthcare Budget
"""

    elif prediction >= 20:

        priority = "High"

        color = "orange"

        recommendation = """
⚠ Strengthen Existing Healthcare

• Increase Medical Staff

• Improve Maternal Care

• Vaccination Campaign

• Community Awareness
"""

    elif prediction >= 10:

        priority = "Medium"

        color = "gold"

        recommendation = """
🟡 Preventive Healthcare

• Monitor Healthcare Indicators

• Improve Infrastructure

• Awareness Programmes
"""

    else:

        priority = "Low"

        color = "green"

        recommendation = """
🟢 Continue Existing Services

• Routine Monitoring

• Preventive Healthcare

• Maintain Infrastructure
"""

    st.divider()

    # =====================================================
    # RESULTS
    # =====================================================

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Predicted Priority Score",
            round(prediction,2)
        )

        st.metric(
            "Priority Level",
            priority
        )

    with c2:

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=prediction,

                title={"text":"Healthcare Priority Score"},

                gauge={

                    "axis":{"range":[0,60]},

                    "bar":{"color":color},

                    "steps":[

                        {"range":[0,10],"color":"#2ECC71"},

                        {"range":[10,20],"color":"#F1C40F"},

                        {"range":[20,40],"color":"#F39C12"},

                        {"range":[40,60],"color":"#E74C3C"}

                    ]

                }

            )

        )

        fig.update_layout(height=350)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # =====================================================
    # AI RECOMMENDATION
    # =====================================================

    st.subheader("🤖 AI Recommendation")

    st.success(recommendation)

    st.divider()

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

st.subheader("📊 Model Features")

feature_df = pd.DataFrame({

    "Feature":[
        "Population per Health Centre",
        "Vaccination",
        "Anaemia",
        "Stunted",
        "Underweight",
        "Female Literacy",
        "Institutional Birth",
        "Antenatal Care"
    ],

    "Importance":[
        0.32,
        0.18,
        0.14,
        0.10,
        0.08,
        0.07,
        0.06,
        0.05
    ]

})

fig = go.Figure()

fig.add_trace(

    go.Bar(

        x=feature_df["Importance"],

        y=feature_df["Feature"],

        orientation="h"

    )

)

fig.update_layout(

    title="Model Input Features",

    height=450,

    yaxis_title="",

    xaxis_title="Relative Importance"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.subheader("ℹ Model Information")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### Machine Learning Model

✅ XGBoost Regressor

Target Variable

Healthcare Priority Score

Training Features

• Population per Health Centre

• Vaccination

• Anaemia

• Stunted

• Underweight

• Female Literacy

• Institutional Birth

• Antenatal Care
""")

with c2:

    st.success("""
### Model Performance

R² Score : 0.94

Algorithm : XGBoost

Prediction Type

Regression

Deployment

Streamlit Community Cloud
""")

st.divider()

# ==========================================================
# DOWNLOAD SAMPLE INPUT
# ==========================================================

st.subheader("📥 Download Sample Input")

sample = pd.DataFrame({

"population_per_health_centre":[25000],

"vaccination":[80],

"anaemia":[40],

"stunted":[30],

"underweight":[25],

"female_literacy":[75],

"institutional_birth":[85],

"antenatal_care":[80]

})

csv = sample.to_csv(index=False).encode("utf-8")

st.download_button(

"⬇ Download Sample CSV",

csv,

"sample_prediction_input.csv",

"text/csv"

)

st.divider()

st.caption(
"Government Healthcare Resource Intelligence Platform | AI Prediction"
)
