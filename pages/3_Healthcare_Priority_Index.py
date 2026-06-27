import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Healthcare Priority Index",
    page_icon="🎯",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

df = load_data()

# =====================================================
# PAGE TITLE
# =====================================================

st.title("🎯 Healthcare Priority Index")

st.caption(
    "AI-Based Healthcare Priority Classification for Government Decision Support"
)

st.divider()

# =====================================================
# FILTERS
# =====================================================

state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(df["state"].unique())
)

if state == "All":
    temp = df.copy()
else:
    temp = df[df["state"] == state]

district = st.sidebar.selectbox(
    "Select District",
    ["All"] + sorted(temp["district"].unique())
)

if district != "All":
    temp = temp[temp["district"] == district]

# =====================================================
# KPI SECTION
# =====================================================

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "Average Priority Score",
        f"{temp['healthcare_priority_score'].mean():.2f}"
    )

with c2:

    st.metric(
        "Critical Districts",
        temp[temp["priority_level"]=="Critical"].shape[0]
    )

with c3:

    st.metric(
        "High Priority",
        temp[temp["priority_level"]=="High"].shape[0]
    )

with c4:

    st.metric(
        "Medium / Low",
        temp[
            temp["priority_level"].isin(
                ["Medium","Low"]
            )
        ].shape[0]
    )

st.divider()

# ==========================================================
# PRIORITY DISTRIBUTION
# ==========================================================

st.subheader("🚦 Healthcare Priority Distribution")

col1, col2 = st.columns(2)

with col1:

    priority = (
        temp["priority_level"]
        .value_counts()
        .reset_index()
    )

    priority.columns = [
        "Priority Level",
        "Districts"
    ]

    fig = px.pie(
        priority,
        names="Priority Level",
        values="Districts",
        hole=0.45,
        color="Priority Level",
        color_discrete_map={
            "Critical":"#d62728",
            "High":"#ff7f0e",
            "Medium":"#f1c40f",
            "Low":"#2ca02c"
        }
    )

    fig.update_layout(height=500)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.histogram(

        temp,

        x="healthcare_priority_score",

        nbins=30,

        color="priority_level",

        title="Priority Score Distribution"

    )

    fig.update_layout(height=500)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# TOP PRIORITY DISTRICTS
# ==========================================================

st.subheader("🚨 Top 20 High Priority Districts")

top20 = (

    temp

    .sort_values(

        "healthcare_priority_score",

        ascending=False

    )

    .head(20)

)

fig = px.bar(

    top20,

    x="healthcare_priority_score",

    y="district",

    orientation="h",

    color="priority_level",

    text_auto=".2f",

    hover_data=[

        "state",

        "vaccination",

        "anaemia",

        "health_centres"

    ]

)

fig.update_layout(

    height=700,

    yaxis_title="",

    xaxis_title="Healthcare Priority Score"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# PRIORITY LEADERBOARD
# ==========================================================

st.subheader("🏆 District Priority Leaderboard")

leaderboard = temp[[
    "district",
    "state",
    "healthcare_priority_score",
    "priority_level",
    "vaccination",
    "anaemia",
    "health_centres"
]].sort_values(
    "healthcare_priority_score",
    ascending=False
)

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True,
    height=500
)

st.divider()

# ==========================================================
# GOVERNMENT INTERVENTION CENTER
# ==========================================================

st.subheader("🏛 Government Intervention Center")

critical = temp.sort_values(
    "healthcare_priority_score",
    ascending=False
).head(10)

for _, row in critical.iterrows():

    if row["priority_level"] == "Critical":

        recommendation = [
            "🏥 Build additional Primary Health Centres",
            "👨‍⚕️ Recruit specialist doctors & nurses",
            "💉 Strengthen vaccination campaigns",
            "🥗 Launch nutrition & anaemia reduction programs",
            "💰 Allocate emergency healthcare funding"
        ]

    elif row["priority_level"] == "High":

        recommendation = [
            "🏥 Upgrade existing healthcare facilities",
            "👩‍⚕️ Increase healthcare workforce",
            "🤱 Improve maternal healthcare services",
            "📢 Conduct public health awareness campaigns"
        ]

    elif row["priority_level"] == "Medium":

        recommendation = [
            "📈 Monitor healthcare indicators",
            "💉 Improve preventive healthcare coverage",
            "📚 Strengthen health education initiatives"
        ]

    else:

        recommendation = [
            "✅ Maintain existing healthcare services",
            "📊 Continue routine monitoring"
        ]

    with st.expander(f"📍 {row['district']} ({row['state']})"):

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Priority Score",
                round(row["healthcare_priority_score"], 2)
            )

            st.metric(
                "Priority Level",
                row["priority_level"]
            )

        with c2:

            st.metric(
                "Vaccination %",
                round(row["vaccination"], 1)
            )

            st.metric(
                "Anaemia %",
                round(row["anaemia"], 1)
            )

        st.markdown("### Recommended Government Actions")

        for rec in recommendation:
            st.write(rec)

st.divider()

# ==========================================================
# DISTRICT SEARCH
# ==========================================================

st.subheader("🔍 District Search")

selected = st.selectbox(
    "Select District",
    sorted(df["district"].unique())
)

district_data = df[df["district"] == selected].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
### {district_data['district']}

**State:** {district_data['state']}

**Priority Level:** {district_data['priority_level']}

**Priority Score:** {district_data['healthcare_priority_score']:.2f}
""")

with col2:

    st.success(f"""
### Healthcare Indicators

Vaccination : {district_data['vaccination']:.1f} %

Anaemia : {district_data['anaemia']:.1f} %

Health Centres : {district_data['health_centres']}

Female Literacy : {district_data['female_literacy']:.1f} %
""")

st.divider()

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

csv = temp.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Priority Report",
    csv,
    "Healthcare_Priority_Report.csv",
    "text/csv"
)

st.divider()

st.caption(
    "Government Healthcare Resource Intelligence Platform | Healthcare Priority Index"
)
