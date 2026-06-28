import streamlit as st
import pandas as pd
import numpy as np
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
# PAGE HEADER
# ==========================================================

st.title("🤖 AI Healthcare Priority Prediction")

st.markdown("""
Predict the **Healthcare Priority Score** of any district using the
trained **XGBoost Regression Model**.

Adjust the healthcare indicators below and instantly receive:

- 🎯 Predicted Healthcare Priority Score
- 🚦 Priority Classification
- 🏛 Government Recommendation
- 📊 Feature Importance
""")

st.divider()

# ==========================================================
# MODEL INFORMATION
# ==========================================================

left, right = st.columns([3,1])

with left:

    st.info(
        """
**Model Used:** XGBoost Regressor

**Prediction Target:** Healthcare Priority Score

**Model Performance**

• R² Score : **0.94**

• MAE : **1.08**

• RMSE : **1.93**
"""
    )

with right:

    st.metric(
        "Model",
        "XGBoost"
    )

    st.metric(
        "Features",
        "8"
    )

    st.metric(
        "Status",
        "Ready"
    )

st.divider()

# ==========================================================
# HEALTHCARE INPUT FORM
# ==========================================================

st.subheader("📝 Healthcare Indicator Input")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        population_per_health_centre = st.number_input(
            "Population per Health Centre",
            min_value=1000.0,
            max_value=100000.0,
            value=25000.0,
            step=500.0,
            help="Average population served by one health centre."
        )

        vaccination = st.slider(
            "Vaccination Coverage (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=0.5
        )

        anaemia = st.slider(
            "Anaemia (%)",
            min_value=0.0,
            max_value=100.0,
            value=40.0,
            step=0.5
        )

        stunted = st.slider(
            "Stunted Children (%)",
            min_value=0.0,
            max_value=100.0,
            value=30.0,
            step=0.5
        )

    with col2:

        underweight = st.slider(
            "Underweight Children (%)",
            min_value=0.0,
            max_value=100.0,
            value=25.0,
            step=0.5
        )

        female_literacy = st.slider(
            "Female Literacy (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=0.5
        )

        institutional_birth = st.slider(
            "Institutional Birth (%)",
            min_value=0.0,
            max_value=100.0,
            value=85.0,
            step=0.5
        )

        antenatal_care = st.slider(
            "Antenatal Care (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=0.5
        )

    predict_btn = st.form_submit_button(
        "🚀 Predict Healthcare Priority",
        use_container_width=True
    )

# ==========================================================
# CREATE INPUT DATAFRAME
# ==========================================================

input_df = pd.DataFrame({

    "population_per_health_centre":[population_per_health_centre],

    "vaccination":[vaccination],

    "anaemia":[anaemia],

    "stunted":[stunted],

    "underweight":[underweight],

    "female_literacy":[female_literacy],

    "institutional_birth":[institutional_birth],

    "antenatal_care":[antenatal_care]

})

st.subheader("📋 Input Summary")

st.dataframe(
    input_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# PREDICTION ENGINE
# ==========================================================

if predict_btn:

    # ------------------------------------------------------
    # PREDICT HEALTHCARE PRIORITY SCORE
    # ------------------------------------------------------

    prediction = float(model.predict(input_df)[0])

    prediction = round(prediction, 2)

    # ------------------------------------------------------
    # PRIORITY CLASSIFICATION
    # (Use the same thresholds as your notebook)
    # ------------------------------------------------------

    if prediction >= 40:

        priority = "Critical"

        badge = "🔴"

        gauge_color = "#DC2626"

        recommendation = [
            "Increase healthcare budget immediately",
            "Construct additional Primary Health Centres",
            "Recruit doctors, nurses and specialists",
            "Launch emergency vaccination campaign",
            "Strengthen nutrition & anaemia programmes"
        ]

    elif prediction >= 20:

        priority = "High"

        badge = "🟠"

        gauge_color = "#F97316"

        recommendation = [
            "Upgrade existing healthcare facilities",
            "Increase medical workforce",
            "Improve maternal healthcare",
            "Expand preventive healthcare programmes",
            "Increase public health awareness"
        ]

    elif prediction >= 10:

        priority = "Medium"

        badge = "🟡"

        gauge_color = "#EAB308"

        recommendation = [
            "Monitor healthcare indicators regularly",
            "Improve preventive healthcare",
            "Strengthen awareness programmes",
            "Review healthcare resources periodically"
        ]

    else:

        priority = "Low"

        badge = "🟢"

        gauge_color = "#22C55E"

        recommendation = [
            "Maintain existing healthcare infrastructure",
            "Continue preventive healthcare",
            "Perform routine monitoring",
            "Focus on long-term healthcare planning"
        ]

    # ------------------------------------------------------
    # PREDICTION RESULTS
    # ------------------------------------------------------

    st.subheader("🎯 Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Healthcare Priority Score",
            f"{prediction:.2f}"
        )

    with c2:

        st.metric(
            "Priority Level",
            f"{badge} {priority}"
        )

    with c3:

        st.metric(
            "Model Used",
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

            number={"suffix":""},

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

        for item in recommendation:

            st.write(f"✅ {item}")

    with right:

        st.info(f"""
### Risk Summary

Priority Level

**{priority}**

Predicted Score

**{prediction:.2f}**

Model

**XGBoost Regression**
""")

    st.divider()

# ==========================================================
# INPUT vs PREDICTION
# ==========================================================

    st.subheader("📋 Prediction Summary")

    result = input_df.copy()

    result["Predicted Priority Score"] = prediction

    result["Priority Level"] = priority

    st.dataframe(

        result,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

# ==========================================================
# XGBOOST FEATURE IMPORTANCE
# ==========================================================

st.subheader("📈 XGBoost Feature Importance")

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

    "Importance": model.feature_importances_

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

    title="Feature Importance Learned by XGBoost",

    height=500,

    xaxis_title="Importance",

    yaxis_title="",

    template="plotly_white"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.subheader("🏆 Model Performance")

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "R² Score",
        "0.9414"
    )

with m2:

    st.metric(
        "MAE",
        "1.0813"
    )

with m3:

    st.metric(
        "RMSE",
        "1.9257"
    )

st.success("""
### Model Summary

✔ Best Performing Model : **XGBoost Regression**

✔ Higher accuracy than Random Forest

✔ Captures complex healthcare relationships

✔ Suitable for decision-support systems

✔ Successfully deployed using Streamlit
""")

st.divider()

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

st.subheader("📥 Download Prediction Report")

if predict_btn:

    report = result.copy()

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="⬇ Download Prediction Report",

        data=csv,

        file_name="Healthcare_Priority_Prediction_Report.csv",

        mime="text/csv",

        use_container_width=True

    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
"""
Government Healthcare Resource Intelligence Platform

AI Prediction Module • XGBoost • Streamlit • Plotly

© 2026
"""
)
