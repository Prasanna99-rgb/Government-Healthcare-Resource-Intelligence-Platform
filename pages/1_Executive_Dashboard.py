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
    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

df = load_data()

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📊 Executive Healthcare Intelligence Dashboard")

st.markdown("""
### Real-Time Healthcare Decision Support System

A comprehensive executive dashboard for analysing India's healthcare
infrastructure, healthcare accessibility, maternal & child health,
and district healthcare priority.
""")

st.divider()

# ==========================================================
# EXECUTIVE KPIs
# ==========================================================

total_population = int(df["population"].sum())

total_health_centres = int(df["health_centres"].sum())

avg_vaccination = df["vaccination"].mean()

avg_anaemia = df["anaemia"].mean()

avg_female_literacy = df["female_literacy"].mean()

avg_priority_score = df["healthcare_priority_score"].mean()

critical_districts = (
    df["priority_level"] == "Critical"
).sum()

total_states = df["state"].nunique()

# Automatically convert to percentage if data is stored as 0–1

if avg_vaccination <= 1:
    avg_vaccination *= 100

if avg_anaemia <= 1:
    avg_anaemia *= 100

if avg_female_literacy <= 1:
    avg_female_literacy *= 100

# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Population",
        f"{total_population:,}"
    )

with c2:
    st.metric(
        "Health Centres",
        f"{total_health_centres:,}"
    )

with c3:
    st.metric(
        "Average Vaccination",
        f"{avg_vaccination:.1f}%"
    )

with c4:
    st.metric(
        "Average Anaemia",
        f"{avg_anaemia:.1f}%"
    )

c5, c6, c7, c8 = st.columns(4)

with c5:
    st.metric(
        "Female Literacy",
        f"{avg_female_literacy:.1f}%"
    )

with c6:
    st.metric(
        "Priority Score",
        f"{avg_priority_score:.2f}"
    )

with c7:
    st.metric(
        "Critical Districts",
        critical_districts
    )

with c8:
    st.metric(
        "States",
        total_states
    )

st.divider()

# ==========================================================
# STATE PERFORMANCE & HIGH PRIORITY DISTRICTS
# ==========================================================

left, right = st.columns([1.3, 1])

# ==========================================================
# STATE HEALTHCARE PERFORMANCE
# ==========================================================

with left:

    st.subheader("🏆 State Healthcare Performance")

    state_summary = (
        df.groupby("state", as_index=False)
        .agg(
            Priority_Score=("healthcare_priority_score", "mean"),
            Vaccination=("vaccination", "mean"),
            Health_Centres=("health_centres", "sum"),
            Population=("population", "sum")
        )
        .sort_values(
            "Priority_Score",
            ascending=False
        )
    )

    # Convert percentage columns if stored between 0–1
    if state_summary["Vaccination"].max() <= 1:
        state_summary["Vaccination"] *= 100

    fig = px.bar(

        state_summary.head(10),

        x="Priority_Score",

        y="state",

        orientation="h",

        color="Priority_Score",

        text_auto=".2f",

        title="Top 10 States by Healthcare Priority Score"

    )

    fig.update_layout(

        height=520,

        yaxis_title="",

        xaxis_title="Healthcare Priority Score",

        coloraxis_showscale=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ==========================================================
# HIGHEST PRIORITY DISTRICTS
# ==========================================================

with right:

    st.subheader("🚨 Highest Priority Districts")

    top10 = (

        df.sort_values(

            "healthcare_priority_score",

            ascending=False

        )

        .head(10)

    )

    for _, row in top10.iterrows():

        vaccination = row["vaccination"]

        anaemia = row["anaemia"]

        if vaccination <= 1:
            vaccination *= 100

        if anaemia <= 1:
            anaemia *= 100

        st.error(f"""
### 📍 {row['district']}

**State:** {row['state']}

**Priority Score:** {row['healthcare_priority_score']:.2f}

**Vaccination:** {vaccination:.1f}%

**Anaemia:** {anaemia:.1f}%

**Health Centres:** {int(row['health_centres'])}

**Priority Level:** {row['priority_level']}
""")

st.divider()

# ==========================================================
# HEALTHCARE INFRASTRUCTURE GAP ANALYSIS
# ==========================================================

st.subheader("🏥 Healthcare Infrastructure Gap Analysis")

gap_df = (
    df.nlargest(
        20,
        "population_per_health_centre"
    )
    .sort_values(
        "population_per_health_centre"
    )
)

fig = px.bar(

    gap_df,

    x="population_per_health_centre",

    y="district",

    orientation="h",

    color="population_per_health_centre",

    hover_data=[
        "state",
        "population",
        "health_centres"
    ],

    text_auto=".0f",

    title="Top 20 Districts with Highest Population per Health Centre"

)

fig.update_layout(

    height=650,

    xaxis_title="Population per Health Centre",

    yaxis_title="District",

    coloraxis_showscale=False

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# VACCINATION vs ANAEMIA INTELLIGENCE
# ==========================================================

st.subheader("💉 Vaccination vs Anaemia Intelligence")

scatter_df = df.copy()

if scatter_df["vaccination"].max() <= 1:
    scatter_df["vaccination"] *= 100

if scatter_df["anaemia"].max() <= 1:
    scatter_df["anaemia"] *= 100

fig = px.scatter(

    scatter_df,

    x="vaccination",

    y="anaemia",

    size="population",

    color="healthcare_priority_score",

    hover_name="district",

    hover_data=[

        "state",

        "health_centres",

        "population_per_health_centre"

    ],

    title="Vaccination Coverage vs Anaemia Burden"

)

fig.update_layout(

    height=650,

    xaxis_title="Vaccination (%)",

    yaxis_title="Anaemia (%)",

    coloraxis_colorbar_title="Priority Score"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ==========================================================
# STATE HEALTHCARE HEATMAP
# ==========================================================

st.subheader("🗺️ State Healthcare Priority Heatmap")

state_df = (

    df.groupby("state", as_index=False)

    .agg({

        "healthcare_priority_score":"mean",

        "vaccination":"mean",

        "anaemia":"mean",

        "female_literacy":"mean"

    })

)

# Convert percentage columns if required

for col in ["vaccination","anaemia","female_literacy"]:

    if state_df[col].max() <= 1:

        state_df[col] = state_df[col] * 100

heatmap = px.imshow(

    state_df.set_index("state"),

    labels=dict(

        x="Healthcare Indicator",

        y="State",

        color="Value"

    ),

    aspect="auto",

    color_continuous_scale="RdYlGn_r",

    title="State-wise Healthcare Indicators"

)

heatmap.update_layout(

    height=700

)

st.plotly_chart(

    heatmap,

    use_container_width=True

)

st.divider()

# ==========================================================
# PRIORITY LEVEL DISTRIBUTION
# ==========================================================

st.subheader("📊 District Priority Distribution")

priority_count = (

    df["priority_level"]

    .value_counts()

    .reset_index()

)

priority_count.columns = [

    "Priority Level",

    "Districts"

]

pie = px.pie(

    priority_count,

    names="Priority Level",

    values="Districts",

    hole=0.45,

    title="Distribution of Healthcare Priority Levels"

)

pie.update_traces(

    textposition="inside",

    textinfo="percent+label"

)

pie.update_layout(

    height=500

)

st.plotly_chart(

    pie,

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
    df["healthcare_density"].idxmax()
]

worst_healthcare = df.loc[
    df["healthcare_density"].idxmin()
]

c1, c2 = st.columns(2)

with c1:

    st.success(f"""
### 🟢 Key Positive Insights

🏥 Best Healthcare Density

**{best_healthcare['district']}**
({best_healthcare['state']})

Healthcare Density:
**{best_healthcare['healthcare_density']:.2f}**

---

💉 Highest Vaccination

**{highest_vaccination['district']}**
({highest_vaccination['state']})

Vaccination:
**{highest_vaccination['vaccination']:.1f}%**
""")

with c2:

    st.error(f"""
### 🔴 Immediate Attention Required

🚨 Highest Priority District

**{highest_priority['district']}**
({highest_priority['state']})

Priority Score:
**{highest_priority['healthcare_priority_score']:.2f}**

---

🩸 Highest Anaemia

**{highest_anaemia['district']}**
({highest_anaemia['state']})

Anaemia:
**{highest_anaemia['anaemia']:.1f}%**

---

🏥 Lowest Healthcare Density

**{worst_healthcare['district']}**
({worst_healthcare['state']})

Healthcare Density:
**{worst_healthcare['healthcare_density']:.2f}**

st.divider()

# ==========================================================
# DATA DOWNLOAD
# ==========================================================

st.subheader("📥 Download Dashboard Data")

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

st.markdown("---")

st.caption("""

Government Healthcare Resource Intelligence Platform

Executive Healthcare Intelligence Dashboard

Developed using

• Python

• Streamlit

• Plotly

• XGBoost

© 2026

""")
