import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------
# Load Data
# ---------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/healthcare_priority_index.csv")

df = load_data()

# ---------------------------------
# Header
# ---------------------------------

st.title("📊 Executive Healthcare Dashboard")
st.write("National Healthcare Resource Overview")

st.divider()

# ---------------------------------
# KPI Cards
# ---------------------------------

total_population = int(df["population"].sum())
total_states = df["state"].nunique()
total_districts = df["district"].nunique()
total_health_centres = int(df["health_centres"].sum())

avg_vaccination = round(df["vaccination"].mean(),2)
avg_anaemia = round(df["anaemia"].mean(),2)
avg_literacy = round(df["literacy"].mean(),2)
avg_priority = round(df["healthcare_priority_score"].mean(),2)

col1,col2,col3,col4 = st.columns(4)

col1.metric("👨‍👩‍👧 Population",f"{total_population:,}")
col2.metric("🏥 Health Centres",f"{total_health_centres:,}")
col3.metric("🗺 States",total_states)
col4.metric("📍 Districts",total_districts)

st.divider()

col5,col6,col7,col8 = st.columns(4)

col5.metric("💉 Avg Vaccination",f"{avg_vaccination}%")
col6.metric("🩸 Avg Anaemia",f"{avg_anaemia}%")
col7.metric("📚 Avg Literacy",f"{avg_literacy}%")
col8.metric("🏥 Avg Priority Score",avg_priority)

st.divider()

# ---------------------------------
# Population by State
# ---------------------------------

st.subheader("State-wise Population")

state_pop = (
    df.groupby("state")["population"]
    .sum()
    .reset_index()
    .sort_values("population",ascending=False)
)

fig = px.bar(
    state_pop,
    x="state",
    y="population",
    color="population",
    title="Population by State"
)

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------
# Health Centres by State
# ---------------------------------

st.subheader("Health Centres by State")

health = (
    df.groupby("state")["health_centres"]
    .sum()
    .reset_index()
    .sort_values("health_centres",ascending=False)
)

fig = px.bar(
    health,
    x="state",
    y="health_centres",
    color="health_centres",
    title="Health Centres"
)

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------
# Priority Level Distribution
# ---------------------------------

st.subheader("Healthcare Priority Distribution")

fig = px.pie(
    df,
    names="priority_level",
    title="Priority Level"
)

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------
# Top Priority Districts
# ---------------------------------

st.subheader("Top 20 Critical Districts")

top = df.sort_values(
    "healthcare_priority_score",
    ascending=False
).head(20)

st.dataframe(
    top[
        [
            "district",
            "state",
            "healthcare_priority_score",
            "priority_level"
        ]
    ],
    use_container_width=True
)

# ---------------------------------
# Top Vaccination States
# ---------------------------------

st.subheader("Average Vaccination by State")

vacc = (
    df.groupby("state")["vaccination"]
    .mean()
    .reset_index()
    .sort_values("vaccination",ascending=False)
)

fig = px.bar(
    vacc,
    x="state",
    y="vaccination",
    color="vaccination"
)

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------
# Highest Anaemia States
# ---------------------------------

st.subheader("Average Anaemia by State")

anaemia = (
    df.groupby("state")["anaemia"]
    .mean()
    .reset_index()
    .sort_values("anaemia",ascending=False)
)

fig = px.bar(
    anaemia,
    x="state",
    y="anaemia",
    color="anaemia"
)

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------
# Footer
# ---------------------------------

st.divider()

st.caption("Government Healthcare Resource Intelligence Platform")
