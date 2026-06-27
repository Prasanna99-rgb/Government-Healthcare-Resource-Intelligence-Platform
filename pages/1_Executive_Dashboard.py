import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

df = load_data()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Dashboard Filters")

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

    temp = temp[
        temp["district"] == district
    ]

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.markdown("""

# 📊 Executive Healthcare Intelligence Dashboard

Real-time Healthcare Decision Support System

""")

st.divider()

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

k1,k2,k3,k4 = st.columns(4)

with k1:

    st.metric(

        "Population",

        f"{temp['population'].sum():,.0f}"

    )

with k2:

    st.metric(

        "Health Centres",

        f"{temp['health_centres'].sum():,.0f}"

    )

with k3:

    st.metric(

        "Vaccination",

        f"{temp['vaccination'].mean():.1f}%"

    )

with k4:

    st.metric(

        "Anaemia",

        f"{temp['anaemia'].mean():.1f}%"

    )

k5,k6,k7,k8 = st.columns(4)

with k5:

    st.metric(

        "Female Literacy",

        f"{temp['female_literacy'].mean():.1f}%"

    )

with k6:

    st.metric(

        "Priority Score",

        round(

            temp["healthcare_priority_score"].mean(),

            2

        )

    )

with k7:

    st.metric(

        "Critical Districts",

        temp[
            temp["priority_level"]=="Critical"
        ].shape[0]

    )

with k8:

    st.metric(

        "States",

        temp["state"].nunique()

    )

st.divider()

# ==========================================================
# STATE HEALTHCARE LEADERBOARD
# ==========================================================

st.subheader("🏆 State Healthcare Performance")

state_summary = (
    temp.groupby("state")
    .agg({
        "healthcare_priority_score":"mean",
        "vaccination":"mean",
        "anaemia":"mean",
        "health_centres":"sum"
    })
    .reset_index()
)

state_summary = state_summary.sort_values(
    "healthcare_priority_score"
)

fig = px.bar(

    state_summary,

    x="healthcare_priority_score",

    y="state",

    orientation="h",

    color="healthcare_priority_score",

    text_auto=".2f",

    title="Healthcare Priority Ranking (Lower is Better)"

)

fig.update_layout(

    height=650,

    yaxis_title="",

    xaxis_title="Priority Score"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# GOVERNMENT RISK DASHBOARD
# ==========================================================

st.subheader("🚨 Highest Risk Districts")

critical = (

    temp

    .sort_values(

        "healthcare_priority_score",

        ascending=False

    )

    .head(10)

)

for _,row in critical.iterrows():

    with st.container(border=True):

        c1,c2 = st.columns([4,1])

        with c1:

            st.markdown(f"""

### 🚨 {row['district']}

**State:** {row['state']}

Priority Score : **{row['healthcare_priority_score']:.2f}**

Vaccination : **{row['vaccination']:.1f}%**

Anaemia : **{row['anaemia']:.1f}%**

Health Centres : **{row['health_centres']}**

""")

        with c2:

            st.error("Critical")

st.divider()

# ==========================================================
# INFRASTRUCTURE GAP ANALYSIS
# ==========================================================

st.subheader("🏥 Healthcare Infrastructure Gap Analysis")

fig = px.scatter(

    temp,

    x="population",

    y="health_centres",

    size="population_per_health_centre",

    color="priority_level",

    hover_name="district",

    hover_data=[

        "state",

        "vaccination",

        "anaemia"

    ],

    title="Population vs Healthcare Infrastructure"

)

fig.update_layout(height=650)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# VACCINATION vs ANAEMIA
# ==========================================================

st.subheader("💉 Vaccination vs Anaemia Intelligence")

fig = px.scatter(

    temp,

    x="vaccination",

    y="anaemia",

    color="priority_level",

    size="population",

    hover_name="district",

    trendline="ols"

)

fig.update_layout(height=650)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# PRIORITY SCORE GAUGE
# ==========================================================

st.subheader("🎯 National Healthcare Priority Gauge")

score = temp["healthcare_priority_score"].mean()

fig = go.Figure(

    go.Indicator(

        mode="gauge+number",

        value=score,

        title={"text":"Average Priority Score"},

        gauge={

            "axis":{"range":[None,100]},

            "bar":{"color":"darkred"},

            "steps":[

                {"range":[0,25],"color":"lightgreen"},

                {"range":[25,50],"color":"yellow"},

                {"range":[50,75],"color":"orange"},

                {"range":[75,100],"color":"red"}

            ]

        }

    )

)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# GOVERNMENT ACTION CENTER
# ==========================================================

st.subheader("🏛 Government Action Center")

top5 = temp.sort_values(
    "healthcare_priority_score",
    ascending=False
).head(5)

for _, row in top5.iterrows():

    if row["priority_level"] == "Critical":

        recommendation = """
✅ Build additional Primary Health Centres

✅ Deploy specialist doctors

✅ Increase vaccination drives

✅ Launch anaemia & nutrition campaign

✅ Allocate emergency healthcare budget
"""

    elif row["priority_level"] == "High":

        recommendation = """
✅ Strengthen existing hospitals

✅ Recruit healthcare workers

✅ Improve maternal healthcare

✅ Increase health awareness
"""

    else:

        recommendation = """
✅ Maintain current healthcare services

✅ Continue preventive healthcare

✅ Monitor district performance
"""

    with st.expander(f"📍 {row['district']} ({row['state']})"):

        st.write(f"**Priority Level:** {row['priority_level']}")
        st.write(f"**Priority Score:** {row['healthcare_priority_score']:.2f}")
        st.write(f"**Vaccination:** {row['vaccination']:.1f}%")
        st.write(f"**Anaemia:** {row['anaemia']:.1f}%")

        st.markdown("### Recommended Government Actions")
        st.success(recommendation)

st.divider()

# ==========================================================
# BEST & WORST DISTRICTS
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("🏆 Best Performing Districts")

    best = temp.nsmallest(
        10,
        "healthcare_priority_score"
    )[[
        "district",
        "state",
        "healthcare_priority_score"
    ]]

    st.dataframe(
        best,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("🚨 High Priority Districts")

    worst = temp.nlargest(
        10,
        "healthcare_priority_score"
    )[[
        "district",
        "state",
        "healthcare_priority_score"
    ]]

    st.dataframe(
        worst,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

csv = temp.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Executive Report",
    csv,
    "Executive_Healthcare_Report.csv",
    "text/csv"
)

st.divider()

st.caption(
    "Government Healthcare Resource Intelligence Platform | Executive Dashboard"
)
