import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Executive Healthcare Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

    percentage_columns = [
        "female_literacy",
        "antenatal_care",
        "institutional_birth",
        "vaccination",
        "stunted",
        "underweight",
        "anaemia"
    ]

    for col in percentage_columns:

        if df[col].max() <= 1:

            df[col] = df[col] * 100

    return df


df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📊 Executive Healthcare Intelligence Dashboard")

st.markdown("""
### Real-Time Healthcare Decision Support System

National Healthcare Intelligence Dashboard for monitoring
healthcare infrastructure, vaccination, maternal & child
health and district healthcare priority across India.
""")

st.divider()

# ==========================================================
# EXECUTIVE KPI CARDS
# ==========================================================

population = int(df["population"].sum())

health_centres = int(df["health_centres"].sum())

vaccination = df["vaccination"].mean()

anaemia = df["anaemia"].mean()

female_literacy = df["female_literacy"].mean()

priority_score = df["healthcare_priority_score"].mean()

critical_districts = (
    df["priority_level"] == "Critical"
).sum()

states = df["state"].nunique()

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Population",
        f"{population:,}"
    )

with k2:
    st.metric(
        "Health Centres",
        f"{int(health_centres):,}"
    )

with k3:
    st.metric(
        "Vaccination",
        f"{vaccination:.1f}%"
    )

with k4:
    st.metric(
        "Anaemia",
        f"{anaemia:.1f}%"
    )

k5, k6, k7, k8 = st.columns(4)

with k5:
    st.metric(
        "Female Literacy",
        f"{female_literacy:.1f}%"
    )

with k6:
    st.metric(
        "Priority Score",
        f"{priority_score:.2f}"
    )

with k7:
    st.metric(
        "Critical Districts",
        critical_districts
    )

with k8:
    st.metric(
        "States",
        states
    )

st.divider()

# ==========================================================
# STATE PERFORMANCE & HIGH PRIORITY DISTRICTS
# ==========================================================

left, right = st.columns([1.35, 1])

# ==========================================================
# STATE HEALTHCARE PERFORMANCE
# ==========================================================

with left:

    st.subheader("🏆 State Healthcare Performance")

    state_summary = (

        df.groupby("state", as_index=False)

        .agg(

            Average_Priority=("healthcare_priority_score", "mean"),

            Population=("population", "sum"),

            Health_Centres=("health_centres", "sum"),

            Vaccination=("vaccination", "mean")

        )

        .sort_values(

            "Average_Priority",

            ascending=False

        )

    )

    fig = px.bar(

        state_summary.head(10),

        x="Average_Priority",

        y="state",

        orientation="h",

        color="Average_Priority",

        text_auto=".2f",

        color_continuous_scale="Reds",

        title="Top 10 States by Healthcare Priority Score"

    )

    fig.update_layout(

        height=550,

        yaxis_title="",

        xaxis_title="Average Priority Score",

        coloraxis_showscale=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ==========================================================
# TOP PRIORITY DISTRICTS
# ==========================================================

with right:

    st.subheader("🚨 Highest Risk Districts")

    top10 = (

        df.sort_values(

            "healthcare_priority_score",

            ascending=False

        )

        .head(10)

    )

    for _, row in top10.iterrows():

        st.error(f"""
### 🚨 {row['district']}

**State:** {row['state']}

**Priority Score:** {row['healthcare_priority_score']:.2f}

**Vaccination:** {row['vaccination']:.1f}%

**Anaemia:** {row['anaemia']:.1f}%

**Healthcare Density:** {row['healthcare_density']}

**Priority Level:** {row['priority_level']}
""")

st.divider()

# ==========================================================
# HEALTHCARE INFRASTRUCTURE GAP ANALYSIS
# ==========================================================

st.subheader("🏥 Healthcare Infrastructure Gap Analysis")

gap_df = (
    df.sort_values(
        "population_per_health_centre",
        ascending=False
    )
    .head(20)
)

fig = px.bar(

    gap_df,

    x="district",

    y="population_per_health_centre",

    color="healthcare_density",

    hover_data=[
        "state",
        "population",
        "health_centres",
        "priority_level"
    ],

    title="Top 20 Districts with Highest Infrastructure Gap"

)

fig.update_layout(

    height=600,

    xaxis_title="District",

    yaxis_title="Normalized Infrastructure Gap",

    xaxis_tickangle=-45

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# VACCINATION vs ANAEMIA ANALYSIS
# ==========================================================

st.subheader("💉 Vaccination vs Anaemia Intelligence")

fig = px.scatter(

    df,

    x="vaccination",

    y="anaemia",

    color="priority_level",

    size="population",

    hover_name="district",

    hover_data=[
        "state",
        "healthcare_density",
        "healthcare_priority_score"
    ],

    title="Vaccination Coverage vs Anaemia"

)

fig.update_layout(

    height=650,

    xaxis_title="Vaccination (%)",

    yaxis_title="Anaemia (%)"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# STATE HEALTHCARE OVERVIEW
# ==========================================================

st.subheader("🗺️ State Healthcare Overview")

state_df = (

    df.groupby("state", as_index=False)

    .agg({

        "healthcare_priority_score":"mean",

        "vaccination":"mean",

        "anaemia":"mean",

        "female_literacy":"mean"

    })

)

fig = px.imshow(

    state_df.set_index("state"),

    aspect="auto",

    color_continuous_scale="RdYlGn_r",

    labels=dict(

        x="Healthcare Indicator",

        y="State",

        color="Value"

    ),

    title="State-wise Healthcare Indicators"

)

fig.update_layout(

    height=700

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# HEALTHCARE DENSITY DISTRIBUTION
# ==========================================================

st.subheader("🏥 Healthcare Density Distribution")

density_df = (

    df["healthcare_density"]

    .value_counts()

    .reset_index()

)

density_df.columns = [

    "Healthcare Density",

    "Districts"

]

fig = px.pie(

    density_df,

    names="Healthcare Density",

    values="Districts",

    hole=0.45,

    title="District Distribution by Healthcare Density"

)

fig.update_traces(

    textposition="inside",

    textinfo="percent+label"

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
# PRIORITY LEVEL DISTRIBUTION
# ==========================================================

st.subheader("📊 Priority Level Distribution")

priority_df = (

    df["priority_level"]

    .value_counts()

    .reset_index()

)

priority_df.columns = [

    "Priority Level",

    "Districts"

]

fig = px.bar(

    priority_df,

    x="Priority Level",

    y="Districts",

    color="Priority Level",

    text_auto=True,

    title="Healthcare Priority Levels Across Districts"

)

fig.update_layout(

    height=500,

    xaxis_title="Priority Level",

    yaxis_title="Number of Districts",

    showlegend=False

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

st.subheader("📌 Executive Healthcare Insights")

highest_priority = df.loc[
    df["healthcare_priority_score"].idxmax()
]

lowest_priority = df.loc[
    df["healthcare_priority_score"].idxmin()
]

highest_vaccination = df.loc[
    df["vaccination"].idxmax()
]

highest_anaemia = df.loc[
    df["anaemia"].idxmax()
]

best_healthcare = df.loc[
    df["healthcare_rank"].idxmin()
]

worst_healthcare = df.loc[
    df["healthcare_rank"].idxmax()
]

left, right = st.columns(2)

with left:

    st.success(f"""
### 🟢 Positive Highlights

🏥 **Best Healthcare District**

**{best_healthcare['district']}**
({best_healthcare['state']})

Healthcare Density:
**{best_healthcare['healthcare_density']}**

Healthcare Rank:
**{int(best_healthcare['healthcare_rank'])}**

---

💉 **Highest Vaccination**

**{highest_vaccination['district']}**
({highest_vaccination['state']})

Vaccination:
**{highest_vaccination['vaccination']:.1f}%**
""")

with right:

    st.error(f"""
### 🔴 Districts Requiring Immediate Attention

🚨 **Highest Priority District**

**{highest_priority['district']}**
({highest_priority['state']})

Priority Score:
**{highest_priority['healthcare_priority_score']:.2f}**

---

🩸 **Highest Anaemia**

**{highest_anaemia['district']}**
({highest_anaemia['state']})

Anaemia:
**{highest_anaemia['anaemia']:.1f}%**

---

🏥 **Lowest Healthcare Rank**

**{worst_healthcare['district']}**
({worst_healthcare['state']})

Healthcare Density:
**{worst_healthcare['healthcare_density']}**

Healthcare Rank:
**{int(worst_healthcare['healthcare_rank'])}**
""")

st.divider()

# ==========================================================
# DOWNLOAD DATASET
# ==========================================================

st.subheader("📥 Download Dashboard Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Healthcare Intelligence Dataset",
    data=csv,
    file_name="Healthcare_Intelligence_Dataset.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption("""
Government Healthcare Resource Intelligence Platform

Executive Healthcare Dashboard

Built with Streamlit • Plotly • Python • XGBoost
""")
