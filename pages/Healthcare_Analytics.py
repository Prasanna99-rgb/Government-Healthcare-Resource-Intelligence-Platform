import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Healthcare Analytics",
    page_icon="📈",
    layout="wide"
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

st.title("📈 Healthcare Analytics Dashboard")

st.caption(
    "Comprehensive Healthcare Performance Analytics Across India"
)

st.divider()

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

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

# ==========================================================
# KPI SECTION
# ==========================================================

k1,k2,k3,k4,k5 = st.columns(5)

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
        "Female Literacy",
        f"{temp['female_literacy'].mean():.1f}%"
    )

with k5:
    st.metric(
        "Priority Score",
        f"{temp['healthcare_priority_score'].mean():.2f}"
    )

st.divider()

# ==========================================================
# STATE HEALTHCARE COMPARISON
# ==========================================================

st.subheader("🏆 State Healthcare Comparison")

state_summary = (
    temp.groupby("state", as_index=False)
    .agg({
        "population": "sum",
        "health_centres": "sum",
        "vaccination": "mean",
        "anaemia": "mean",
        "healthcare_priority_score": "mean"
    })
)

state_summary = state_summary.sort_values(
    "healthcare_priority_score"
)

fig = px.bar(
    state_summary,
    x="state",
    y="healthcare_priority_score",
    color="healthcare_priority_score",
    text_auto=".2f",
    title="Average Healthcare Priority Score by State"
)

fig.update_layout(
    height=550,
    xaxis_title="State",
    yaxis_title="Priority Score"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# POPULATION vs HEALTH CENTRES
# ==========================================================

st.subheader("🏥 Infrastructure Gap Analysis")

fig = px.scatter(
    temp,
    x="population",
    y="health_centres",
    color="priority_level",
    size="population_per_health_centre",
    hover_name="district",
    hover_data=[
        "state",
        "vaccination",
        "anaemia"
    ],
    title="Population vs Healthcare Infrastructure"
)

fig.update_layout(height=650)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# HEALTHCARE DENSITY
# ==========================================================

st.subheader("📊 Healthcare Density Distribution")

density = (
    temp["healthcare_density"]
    .value_counts()
    .reset_index()
)

density.columns = [
    "Healthcare Density",
    "District Count"
]

fig = px.pie(
    density,
    names="Healthcare Density",
    values="District Count",
    hole=0.45,
    title="Healthcare Density Classification"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# BEST & WORST STATES
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("🥇 Best Performing States")

    best = state_summary.nsmallest(
        10,
        "healthcare_priority_score"
    )[[
        "state",
        "healthcare_priority_score",
        "vaccination"
    ]]

    st.dataframe(
        best,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("🚨 States Needing Attention")

    worst = state_summary.nlargest(
        10,
        "healthcare_priority_score"
    )[[
        "state",
        "healthcare_priority_score",
        "anaemia"
    ]]

    st.dataframe(
        worst,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================================================
# VACCINATION ANALYSIS
# ==========================================================

st.subheader("💉 Vaccination Coverage Analysis")

vaccination_state = (
    temp.groupby("state", as_index=False)["vaccination"]
    .mean()
    .sort_values("vaccination", ascending=False)
)

fig = px.bar(
    vaccination_state,
    x="state",
    y="vaccination",
    color="vaccination",
    text_auto=".1f",
    title="Average Vaccination Coverage by State"
)

fig.update_layout(height=550)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# ANAEMIA ANALYSIS
# ==========================================================

st.subheader("🩸 Anaemia Burden Analysis")

anaemia_state = (
    temp.groupby("state", as_index=False)["anaemia"]
    .mean()
    .sort_values("anaemia", ascending=False)
)

fig = px.bar(
    anaemia_state,
    x="state",
    y="anaemia",
    color="anaemia",
    text_auto=".1f",
    title="Average Anaemia Burden by State"
)

fig.update_layout(height=550)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# MATERNAL HEALTH
# ==========================================================

st.subheader("🤱 Maternal Healthcare")

maternal = temp.groupby("state", as_index=False).agg({
    "antenatal_care":"mean",
    "institutional_birth":"mean"
})

fig = px.scatter(
    maternal,
    x="antenatal_care",
    y="institutional_birth",
    size="institutional_birth",
    color="institutional_birth",
    hover_name="state",
    title="Antenatal Care vs Institutional Birth"
)

fig.update_layout(height=600)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# FEMALE LITERACY
# ==========================================================

st.subheader("📚 Female Literacy")

fig = px.box(
    temp,
    x="priority_level",
    y="female_literacy",
    color="priority_level",
    title="Female Literacy by Priority Level"
)

fig.update_layout(height=550)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# PRIORITY DISTRIBUTION
# ==========================================================

st.subheader("🎯 Healthcare Priority Distribution")

priority = (
    temp["priority_level"]
    .value_counts()
    .reset_index()
)

priority.columns = [
    "Priority",
    "Districts"
]

fig = px.pie(
    priority,
    names="Priority",
    values="Districts",
    hole=0.5,
    title="District Priority Classification"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# CORRELATION ANALYSIS
# ==========================================================

st.subheader("📊 Correlation Analysis")

corr_cols = [
    "population",
    "health_centres",
    "population_per_health_centre",
    "vaccination",
    "anaemia",
    "female_literacy",
    "antenatal_care",
    "institutional_birth",
    "healthcare_priority_score"
]

corr = temp[corr_cols].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Healthcare Indicator Correlation Matrix"
)

fig.update_layout(height=650)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

st.subheader("🧠 Executive Insights")

highest = temp.loc[
    temp["healthcare_priority_score"].idxmax()
]

lowest = temp.loc[
    temp["healthcare_priority_score"].idxmin()
]

col1, col2 = st.columns(2)

with col1:

    st.error(f"""
### 🚨 Highest Priority District

**District:** {highest['district']}

**State:** {highest['state']}

**Priority Score:** {highest['healthcare_priority_score']:.2f}

**Vaccination:** {highest['vaccination']:.1f}%

**Anaemia:** {highest['anaemia']:.1f}%

**Healthcare Density:** {highest['healthcare_density']}
""")

with col2:

    st.success(f"""
### 🏆 Best Performing District

**District:** {lowest['district']}

**State:** {lowest['state']}

**Priority Score:** {lowest['healthcare_priority_score']:.2f}

**Vaccination:** {lowest['vaccination']:.1f}%

**Anaemia:** {lowest['anaemia']:.1f}%

**Healthcare Density:** {lowest['healthcare_density']}
""")

st.divider()

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

st.subheader("📥 Download Analytics Data")

csv = temp.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Analytics Report",
    data=csv,
    file_name="Healthcare_Analytics_Report.csv",
    mime="text/csv"
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "Government Healthcare Resource Intelligence Platform | Healthcare Analytics Dashboard"
)


