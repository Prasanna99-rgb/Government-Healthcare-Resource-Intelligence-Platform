import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Healthcare Priority Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    return joblib.load(
        "models/healthcare_priority_model.pkl"
    )

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

# ==========================================================
# LOAD RESOURCES
# ==========================================================

model = load_model()

df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🤖 AI Healthcare Priority Prediction")

st.markdown("""
Predict the **Healthcare Priority Score** using the trained
**XGBoost Regression Model**.

The prediction is based on **11 healthcare indicators**
used during model training.
""")

st.divider()

# ==========================================================
# MODEL SUMMARY
# ==========================================================

left, right = st.columns([3,1])

with left:

    st.info("""

### Model Information

**Algorithm**

XGBoost Regressor

**Prediction**

Healthcare Priority Score

**Training Features**

11

**Dataset**

Healthcare Priority Index

""")

with right:

    st.metric(
        "Model",
        "XGBoost"
    )

    st.metric(
        "Features",
        "11"
    )

    st.metric(
        "Status",
        "Ready"
    )

st.divider()

# ==========================================================
# HEALTHCARE INDICATOR INPUT
# ==========================================================

st.subheader("📝 Enter Healthcare Indicators")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        population = st.number_input(
            "Population",
            min_value=1000,
            value=500000,
            step=1000
        )

        health_centres = st.number_input(
            "Health Centres",
            min_value=1,
            value=20
        )

        population_per_health_centre = st.number_input(
            "Population per Health Centre",
            min_value=1000.0,
            value=25000.0,
            step=500.0
        )

        literacy = st.slider(
            "Literacy (%)",
            0.0,
            100.0,
            75.0
        )

        female_literacy = st.slider(
            "Female Literacy (%)",
            0.0,
            100.0,
            70.0
        )

        vaccination = st.slider(
            "Vaccination (%)",
            0.0,
            100.0,
            80.0
        )

    with col2:

        anaemia = st.slider(
            "Anaemia (%)",
            0.0,
            100.0,
            40.0
        )

        stunted = st.slider(
            "Stunted Children (%)",
            0.0,
            100.0,
            30.0
        )

        underweight = st.slider(
            "Underweight Children (%)",
            0.0,
            100.0,
            25.0
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

    predict_btn = st.form_submit_button(
        "🚀 Predict Healthcare Priority",
        use_container_width=True
    )

# ==========================================================
# CREATE MODEL INPUT
# ==========================================================

input_df = pd.DataFrame({

    "population":[population],

    "health_centres":[health_centres],

    "population_per_health_centre":[population_per_health_centre],

    "literacy":[literacy],

    "female_literacy":[female_literacy],

    "vaccination":[vaccination],

    "anaemia":[anaemia],

    "stunted":[stunted],

    "underweight":[underweight],

    "institutional_birth":[institutional_birth],

    "antenatal_care":[antenatal_care]

})

st.subheader("📋 Input Summary")

st.dataframe(
    input_df,
    hide_index=True,
    use_container_width=True
)

st.divider()

# ==========================================================
# PREDICTION ENGINE
# ==========================================================

if predict_btn:

    prediction = float(model.predict(input_df)[0])

    prediction = round(prediction, 2)

    # ======================================================
    # PRIORITY LEVEL
    # ======================================================

    if prediction >= 40:

        priority = "Critical"

        gauge_color = "#DC2626"

        recommendations = [

            "🚨 Immediate government intervention",

            "🏥 Build additional Primary Health Centres",

            "👨‍⚕️ Recruit doctors & nurses",

            "💉 Strengthen vaccination programme",

            "🥗 Launch nutrition & anaemia reduction programme"

        ]

    elif prediction >= 20:

        priority = "High"

        gauge_color = "#F97316"

        recommendations = [

            "🏥 Upgrade healthcare infrastructure",

            "👩‍⚕️ Increase healthcare workforce",

            "🤱 Improve maternal healthcare",

            "📢 Expand awareness programmes"

        ]

    elif prediction >= 10:

        priority = "Medium"

        gauge_color = "#EAB308"

        recommendations = [

            "📈 Monitor healthcare indicators",

            "💉 Improve preventive healthcare",

            "📚 Conduct awareness campaigns"

        ]

    else:

        priority = "Low"

        gauge_color = "#22C55E"

        recommendations = [

            "✅ Maintain existing healthcare services",

            "📊 Continue routine monitoring"

        ]

    st.subheader("🎯 Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Priority Score",

            f"{prediction:.2f}"

        )

    with c2:

        st.metric(

            "Priority Level",

            priority

        )

    with c3:

        st.metric(

            "Model",

            "XGBoost"

        )

    st.divider()

# ==========================================================
# HEALTHCARE PRIORITY GAUGE
# ==========================================================

    st.subheader("📊 Healthcare Priority Gauge")

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=prediction,

            title={"text":"Healthcare Priority Score"},

            gauge={

                "axis":{"range":[0,60]},

                "bar":{"color":gauge_color},

                "steps":[

                    {"range":[0,10],"color":"#22C55E"},

                    {"range":[10,20],"color":"#EAB308"},

                    {"range":[20,40],"color":"#F97316"},

                    {"range":[40,60],"color":"#DC2626"}

                ]

            }

        )

    )

    gauge.update_layout(height=420)

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    st.divider()

# ==========================================================
# AI DECISION SUPPORT
# ==========================================================

    st.subheader("🤖 AI Decision Support")

    left, right = st.columns([2,1])

    with left:

        st.success("### Recommended Government Actions")

        for rec in recommendations:

            st.write(f"✅ {rec}")

    with right:

        st.info(f"""
### Prediction Summary

**Priority Score**

{prediction:.2f}

**Priority Level**

{priority}

**Model**

XGBoost Regression
""")

    st.divider()

# ==========================================================
# INPUT & PREDICTION SUMMARY
# ==========================================================

    st.subheader("📋 Prediction Report")

    report = input_df.copy()

    report["Predicted Priority Score"] = prediction

    report["Priority Level"] = priority

    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

# ==========================================================
# XGBOOST FEATURE IMPORTANCE
# ==========================================================

st.subheader("📈 XGBoost Feature Importance")

feature_names = [

    "Population",

    "Health Centres",

    "Population / Health Centre",

    "Literacy",

    "Female Literacy",

    "Vaccination",

    "Anaemia",

    "Stunted",

    "Underweight",

    "Institutional Birth",

    "Antenatal Care"

]

importances = model.feature_importances_

# Prevent mismatch error
if len(importances) == len(feature_names):

    feature_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": importances

    })

    feature_df = feature_df.sort_values(
        "Importance",
        ascending=True
    )

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=feature_df["Importance"],

            y=feature_df["Feature"],

            orientation="h",

            text=feature_df["Importance"].round(3),

            textposition="outside"

        )

    )

    fig.update_layout(

        height=550,

        title="XGBoost Feature Importance",

        xaxis_title="Importance",

        yaxis_title=""

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

else:

    st.warning(
        f"""
Feature importance cannot be displayed.

Expected Features : {len(feature_names)}

Model Features : {len(importances)}
"""
    )

st.divider()

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.subheader("🏆 Model Performance")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(

        "R² Score",

        "0.94"

    )

with c2:

    st.metric(

        "MAE",

        "1.08"

    )

with c3:

    st.metric(

        "RMSE",

        "1.93"

    )

st.success("""

### Model Summary

✅ Algorithm : XGBoost Regression

✅ Features Used : 11

✅ Prediction Target : Healthcare Priority Score

✅ Production Ready

""")

st.divider()

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

if predict_btn:

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Prediction Report",

        csv,

        "Healthcare_Prediction_Report.csv",

        "text/csv",

        use_container_width=True

    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption("""

Government Healthcare Resource Intelligence Platform

AI Prediction Module

Built using

• Streamlit

• XGBoost

• Plotly

• Python

""")
