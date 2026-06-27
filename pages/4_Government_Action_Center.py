import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Government Action Center",
    page_icon="🏛️",
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

st.title("🏛 Government Action Center")

st.caption(
    "AI Assisted Decision Support for Healthcare Resource Planning"
)

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(df["state"].unique())
)

if state == "All":
    temp = df.copy()
else:
    temp = df[df["state"] == state]

# ==========================================================
# KPI CARDS
# ==========================================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Critical Districts",
        temp[temp["priority_level"]=="Critical"].shape[0]
    )

with c2:
    st.metric(
        "High Priority",
        temp[temp["priority_level"]=="High"].shape[0]
    )

with c3:
    st.metric(
        "Avg Priority Score",
        round(
            temp["healthcare_priority_score"].mean(),
            2
        )
    )

with c4:
    st.metric(
        "Population Covered",
        f"{temp['population'].sum():,.0f}"
    )

st.divider()

# ==========================================================
# PRIORITY OVERVIEW
# ==========================================================

priority = (
    temp["priority_level"]
    .value_counts()
    .reset_index()
)

priority.columns = [
    "Priority",
    "Districts"
]

fig = px.bar(
    priority,
    x="Priority",
    y="Districts",
    color="Priority",
    text_auto=True,
    title="Healthcare Priority Overview"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# AI GOVERNMENT RECOMMENDATIONS
# ==========================================================

st.subheader("🤖 AI Government Recommendations")

top_priority = temp.sort_values(
    "healthcare_priority_score",
    ascending=False
).head(10)

for _, row in top_priority.iterrows():

    population = row["population"]
    existing_centres = row["health_centres"]

    # Target: 1 Health Centre per 25,000 population
    required_centres = max(1, int(population / 25000))

    additional_centres = max(
        0,
        required_centres - existing_centres
    )

    doctor_requirement = additional_centres * 2

    with st.container(border=True):

        st.markdown(f"## 📍 {row['district']} ({row['state']})")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Priority Score",
                f"{row['healthcare_priority_score']:.2f}"
            )

        with c2:
            st.metric(
                "Priority Level",
                row["priority_level"]
            )

        with c3:
            st.metric(
                "Population",
                f"{population:,.0f}"
            )

        st.markdown("### 📋 Recommended Actions")

        if additional_centres > 0:
            st.success(
                f"🏥 Build **{additional_centres}** additional Primary Health Centres"
            )
        else:
            st.info(
                "🏥 Existing Health Centre count is adequate"
            )

        st.write(
            f"👨‍⚕️ Recruit approximately **{doctor_requirement}** doctors"
        )

        if row["vaccination"] < 80:
            st.write(
                "💉 Strengthen vaccination campaign"
            )

        if row["anaemia"] > 50:
            st.write(
                "🥗 Launch district nutrition & anaemia reduction programme"
            )

        if row["female_literacy"] < 70:
            st.write(
                "📚 Improve women's health awareness programmes"
            )

st.divider()

# ==========================================================
# ACTION PRIORITY QUEUE
# ==========================================================

st.subheader("🚨 Government Action Priority Queue")

queue = temp[
    [
        "district",
        "state",
        "priority_level",
        "healthcare_priority_score",
        "vaccination",
        "anaemia",
        "population_per_health_centre"
    ]
].sort_values(
    "healthcare_priority_score",
    ascending=False
)

st.dataframe(
    queue,
    use_container_width=True,
    hide_index=True,
    height=450
)

st.divider()

# ==========================================================
# RESOURCE REQUIREMENT SUMMARY
# ==========================================================

st.subheader("🏥 Estimated Resource Requirement")

critical = temp[
    temp["priority_level"] == "Critical"
]

additional_phc = (
    critical["population"] / 25000
    - critical["health_centres"]
).clip(lower=0).sum()

doctor_requirement = int(additional_phc * 2)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Estimated Additional PHCs",
        int(additional_phc)
    )

with col2:

    st.metric(
        "Estimated Doctors Required",
        doctor_requirement
    )

st.divider()

# ==========================================================
# STATE ACTION SUMMARY
# ==========================================================

st.subheader("📊 State-wise Government Action Summary")

state_action = (
    temp.groupby("state", as_index=False)
    .agg({
        "healthcare_priority_score": "mean",
        "population": "sum",
        "health_centres": "sum",
        "vaccination": "mean",
        "anaemia": "mean"
    })
)

state_action["Recommended_Action"] = state_action.apply(
    lambda x:
    "Immediate Intervention"
    if x["healthcare_priority_score"] >= 40
    else "Strengthen Existing Infrastructure"
    if x["healthcare_priority_score"] >= 20
    else "Maintain Current Services",
    axis=1
)

st.dataframe(
    state_action,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

st.subheader("📋 Executive Summary")

critical = temp[temp["priority_level"] == "Critical"].shape[0]
high = temp[temp["priority_level"] == "High"].shape[0]
avg_vacc = temp["vaccination"].mean()
avg_anaemia = temp["anaemia"].mean()

st.info(f"""
### National Healthcare Status

- 🚨 Critical Districts: **{critical}**
- ⚠️ High Priority Districts: **{high}**
- 💉 Average Vaccination: **{avg_vacc:.1f}%**
- 🩸 Average Anaemia: **{avg_anaemia:.1f}%**

### Recommended National Strategy

1. Prioritize Critical districts first.
2. Expand Primary Health Centre capacity where shortages exist.
3. Strengthen maternal and child healthcare.
4. Increase vaccination coverage in low-performing districts.
5. Continue monitoring Medium and Low priority districts.
""")

st.divider()

# ==========================================================
# DOWNLOAD ACTION PLAN
# ==========================================================

st.subheader("📥 Download Government Action Plan")

csv = state_action.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download State Action Plan",
    data=csv,
    file_name="Government_Action_Plan.csv",
    mime="text/csv"
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "Government Healthcare Resource Intelligence Platform | Government Action Center"
)
