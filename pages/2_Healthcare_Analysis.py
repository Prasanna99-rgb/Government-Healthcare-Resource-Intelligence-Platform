import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Healthcare Analysis",
    page_icon="🏥",
    layout="wide"
)

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/healthcare_priority_index.csv"
    )

df = load_data()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("🔍 Filters")

# ---------------- State ----------------

states = sorted(df["state"].unique())

selected_state = st.sidebar.selectbox(

    "Select State",

    ["All States"] + states

)

# ---------------- District ----------------

if selected_state == "All States":

    districts = sorted(df["district"].unique())

else:

    districts = sorted(

        df[df["state"] == selected_state]["district"].unique()

    )

selected_district = st.sidebar.selectbox(

    "Select District",

    ["All Districts"] + districts

)

# ----------------------------------------------------
# Apply Filters
# ----------------------------------------------------

filtered_df = df.copy()

if selected_state != "All States":

    filtered_df = filtered_df[
        filtered_df["state"] == selected_state
    ]

if selected_district != "All Districts":

    filtered_df = filtered_df[
        filtered_df["district"] == selected_district
    ]

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🏥 Healthcare Infrastructure Analysis")

st.write(
"""
Explore India's healthcare infrastructure,
public health indicators,
and district-level healthcare performance.
"""
)

st.divider()

# ----------------------------------------------------
# KPI Calculations
# ----------------------------------------------------

total_population = int(filtered_df["population"].sum())

total_health_centres = int(filtered_df["health_centres"].sum())

total_states = filtered_df["state"].nunique()

total_districts = filtered_df["district"].nunique()

avg_vaccination = round(

filtered_df["vaccination"].mean(),

2

)

avg_anaemia = round(

filtered_df["anaemia"].mean(),

2

)

avg_literacy = round(

filtered_df["literacy"].mean(),

2

)

avg_priority = round(

filtered_df["healthcare_priority_score"].mean(),

2

)

# ----------------------------------------------------
# KPI Row 1
# ----------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric(

        "👨 Population",

        f"{total_population:,}"

    )

with col2:

    st.metric(

        "🏥 Health Centres",

        f"{total_health_centres:,}"

    )

with col3:

    st.metric(

        "🗺 States",

        total_states

    )

with col4:

    st.metric(

        "📍 Districts",

        total_districts

    )

# ----------------------------------------------------
# KPI Row 2
# ----------------------------------------------------

col5,col6,col7,col8 = st.columns(4)

with col5:

    st.metric(

        "💉 Avg Vaccination",

        f"{avg_vaccination}%"

    )

with col6:

    st.metric(

        "🩸 Avg Anaemia",

        f"{avg_anaemia}%"

    )

with col7:

    st.metric(

        "📚 Avg Literacy",

        f"{avg_literacy}%"

    )

with col8:

    st.metric(

        "🏥 Priority Score",

        avg_priority

    )

st.divider()

# ----------------------------------------------------
# Dataset Preview
# ----------------------------------------------------

st.subheader("📋 Filtered Dataset")

st.dataframe(

    filtered_df,

    use_container_width=True,

    height=400

)

st.divider()


# =====================================================
# Population Analysis
# =====================================================

st.header("📊 Population Analysis")

col1, col2 = st.columns(2)

# -----------------------------------------------------
# State-wise Population
# -----------------------------------------------------

with col1:

    state_population = (
        filtered_df.groupby("state")["population"]
        .sum()
        .reset_index()
        .sort_values("population", ascending=False)
    )

    fig = px.bar(
        state_population,
        x="state",
        y="population",
        color="population",
        title="State-wise Population"
    )

    fig.update_layout(xaxis_title="", yaxis_title="Population")

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Top 20 Population Districts
# -----------------------------------------------------

with col2:

    top_population = (
        filtered_df
        .sort_values("population", ascending=False)
        .head(20)
    )

    fig = px.bar(
        top_population,
        x="district",
        y="population",
        color="population",
        title="Top 20 Most Populated Districts"
    )

    fig.update_layout(xaxis_title="", yaxis_title="Population")

    st.plotly_chart(fig, use_container_width=True)

st.divider()


# =====================================================
# Healthcare Infrastructure
# =====================================================

st.header("🏥 Healthcare Infrastructure")

col1, col2 = st.columns(2)

# -----------------------------------------------------
# Health Centres by State
# -----------------------------------------------------

with col1:

    centres = (
        filtered_df.groupby("state")["health_centres"]
        .sum()
        .reset_index()
        .sort_values("health_centres", ascending=False)
    )

    fig = px.bar(
        centres,
        x="state",
        y="health_centres",
        color="health_centres",
        title="Health Centres by State"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Population Pressure
# -----------------------------------------------------

with col2:

    pressure = (
        filtered_df
        .sort_values(
            "population_per_health_centre",
            ascending=False
        )
        .head(20)
    )

    fig = px.bar(
        pressure,
        x="district",
        y="population_per_health_centre",
        color="population_per_health_centre",
        title="Population Per Health Centre"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =====================================================
# Highest Healthcare Pressure
# =====================================================

st.header("🚨 Highest Healthcare Pressure Districts")

critical = (
    filtered_df
    .sort_values(
        "healthcare_priority_score",
        ascending=False
    )
    .head(20)
)

fig = px.bar(

    critical,

    x="district",

    y="healthcare_priority_score",

    color="priority_level",

    title="Top 20 Priority Districts"

)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =====================================================
# Best Healthcare Districts
# =====================================================

st.header("🏆 Best Healthcare Infrastructure")

best = (
    filtered_df
    .sort_values(
        "population_per_health_centre"
    )
    .head(20)
)

st.dataframe(

best[
[
"district",
"state",
"health_centres",
"population_per_health_centre"
]
],

use_container_width=True

)


# =====================================================
# Worst Healthcare Districts
# =====================================================

st.header("⚠ Worst Healthcare Infrastructure")

worst = (
    filtered_df
    .sort_values(
        "population_per_health_centre",
        ascending=False
    )
    .head(20)
)

st.dataframe(

worst[
[
"district",
"state",
"health_centres",
"population_per_health_centre"
]
],

use_container_width=True

)

st.divider()


st.info("""

### 📌 Business Insights

• High population districts require additional healthcare infrastructure.

• Districts with high population per health centre indicate healthcare resource shortages.

• States with low numbers of health centres should receive priority funding.

• The highest priority districts should be considered for new PHCs, additional doctors, and healthcare investments.

""")
