import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="District Intelligence Report",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

st.title("📋 District Intelligence Report")

st.markdown("""
Generate a detailed healthcare intelligence report for any district.

The report includes:

- 🏥 Healthcare Infrastructure
- 👶 Maternal & Child Health
- 💉 Vaccination
- 📊 Priority Score
- 🤖 Government Recommendations
""")

st.divider()

# ==========================================================
# DISTRICT SELECTION
# ==========================================================

state = st.sidebar.selectbox(
    "Select State",
    sorted(df["state"].unique())
)

districts = sorted(
    df[df["state"] == state]["district"].unique()
)

district = st.sidebar.selectbox(
    "Select District",
    districts
)

report = df[
    (df["state"] == state) &
    (df["district"] == district)
].iloc[0]

st.header(f"📍 {district}")

st.caption(state)

st.divider()

# ==========================================================
# EXECUTIVE KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Population",
        f"{report['population']:,.0f}"
    )

with k2:
    st.metric(
        "Health Centres",
        int(report["health_centres"])
    )

with k3:
    st.metric(
        "Priority Score",
        f"{report['healthcare_priority_score']:.2f}"
    )

with k4:
    st.metric(
        "Priority Level",
        report["priority_level"]
    )

st.divider()

# ==========================================================
# HEALTHCARE PROFILE
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("🏥 Healthcare Infrastructure")

    infrastructure = pd.DataFrame({

        "Indicator":[
            "Healthcare Density",
            "Healthcare Rank",
            "Population / Health Centre",
            "Electricity Access (%)",
            "Clean Fuel (%)",
            "Health Insurance (%)"
        ],

        "Value":[
            report["healthcare_density"],
            report["healthcare_rank"],
            f"{report['population_per_health_centre']:,.0f}",
            f"{report['electricity']:.1f}",
            f"{report['clean_fuel']:.1f}",
            f"{report['health_insurance']:.1f}"
        ]

    })

    st.dataframe(
        infrastructure,
        hide_index=True,
        use_container_width=True
    )

with right:

    st.subheader("👩 Maternal & Child Healthcare")

    maternal = pd.DataFrame({

        "Indicator":[
            "Female Literacy (%)",
            "Vaccination (%)",
            "Antenatal Care (%)",
            "Institutional Birth (%)",
            "Stunted (%)",
            "Underweight (%)",
            "Anaemia (%)"
        ],

        "Value":[
            report["female_literacy"],
            report["vaccination"],
            report["antenatal_care"],
            report["institutional_birth"],
            report["stunted"],
            report["underweight"],
            report["anaemia"]
        ]

    })

    st.dataframe(
        maternal,
        hide_index=True,
        use_container_width=True
    )

st.divider()

# ==========================================================
# DISTRICT HEALTH SCORECARD
# ==========================================================

st.subheader("📊 District Health Scorecard")

scorecard = pd.DataFrame({

    "Indicator":[
        "Vaccination",
        "Female Literacy",
        "Institutional Birth",
        "Health Insurance",
        "Electricity",
        "Clean Fuel"
    ],

    "Percentage":[
        report["vaccination"],
        report["female_literacy"],
        report["institutional_birth"],
        report["health_insurance"],
        report["electricity"],
        report["clean_fuel"]
    ]

})

fig = px.bar(

    scorecard,

    x="Indicator",

    y="Percentage",

    color="Percentage",

    text_auto=".1f",

    title="District Healthcare Performance Indicators"

)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# HEALTHCARE PRIORITY GAUGE
# ==========================================================

st.subheader("🎯 Healthcare Priority Gauge")

priority_score = report["healthcare_priority_score"]

if report["priority_level"] == "Critical":
    gauge_color = "#DC2626"
elif report["priority_level"] == "High":
    gauge_color = "#F97316"
elif report["priority_level"] == "Medium":
    gauge_color = "#EAB308"
else:
    gauge_color = "#22C55E"

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=priority_score,
        title={"text": "Healthcare Priority Score"},
        gauge={
            "axis": {"range": [0, 60]},
            "bar": {"color": gauge_color},
            "steps": [
                {"range": [0, 10], "color": "#22C55E"},
                {"range": [10, 20], "color": "#EAB308"},
                {"range": [20, 40], "color": "#F97316"},
                {"range": [40, 60], "color": "#DC2626"}
            ]
        }
    )
)

fig.update_layout(height=420)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# AI GOVERNMENT RECOMMENDATIONS
# ==========================================================

st.subheader("🤖 AI Government Recommendations")

recommendations = []

if report["priority_level"] == "Critical":

    recommendations = [
        "🚨 Immediate budget allocation required",
        "🏥 Establish additional Primary Health Centres",
        "👨‍⚕️ Recruit doctors and nurses",
        "💉 Conduct intensive vaccination campaigns",
        "🥗 Strengthen nutrition and anaemia reduction programmes"
    ]

elif report["priority_level"] == "High":

    recommendations = [
        "🏥 Upgrade healthcare infrastructure",
        "👩‍⚕️ Increase healthcare workforce",
        "🤱 Improve maternal healthcare services",
        "📢 Strengthen preventive healthcare programmes"
    ]

elif report["priority_level"] == "Medium":

    recommendations = [
        "📈 Continue monitoring health indicators",
        "💉 Improve preventive healthcare coverage",
        "📚 Conduct health awareness campaigns"
    ]

else:

    recommendations = [
        "✅ Maintain existing healthcare services",
        "📊 Continue routine performance monitoring"
    ]

for item in recommendations:
    st.success(item)

st.divider()

# ==========================================================
# DOWNLOAD DISTRICT REPORT
# ==========================================================

st.subheader("📥 Download District Report")

district_report = pd.DataFrame([report])

csv = district_report.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download District Intelligence Report",
    data=csv,
    file_name=f"{district}_Healthcare_Report.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption("""
Government Healthcare Resource Intelligence Platform

District Intelligence Report • Streamlit • Python • Plotly • XGBoost

© 2026
""")
