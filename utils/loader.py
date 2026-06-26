import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

MODEL_DIR = BASE_DIR / "models"

# ============================================================
# Load Main Dataset
# ============================================================

@st.cache_data(show_spinner=False)
def load_master_data():

    try:

        df = pd.read_csv(
            DATA_DIR / "final_healthcare_master.csv"
        )

        return df

    except Exception as e:

        st.error(f"Error loading master dataset\n\n{e}")

        return pd.DataFrame()

# ============================================================
# Load Priority Dataset
# ============================================================

@st.cache_data(show_spinner=False)
def load_priority_data():

    try:

        df = pd.read_csv(
            DATA_DIR / "healthcare_priority_index.csv"
        )

        return df

    except Exception as e:

        st.error(f"Error loading priority dataset\n\n{e}")

        return pd.DataFrame()

# ============================================================
# Load XGBoost Model
# ============================================================

@st.cache_resource(show_spinner=False)
def load_model():

    try:

        model = joblib.load(

            MODEL_DIR / "healthcare_priority_model.pkl"

        )

        return model

    except Exception as e:

        st.error(f"Unable to load ML model\n\n{e}")

        return None

# ============================================================
# Get States
# ============================================================

def get_states(df):

    return sorted(

        df["state"]

        .dropna()

        .unique()

    )

# ============================================================
# Get Districts
# ============================================================

def get_districts(df,state):

    return sorted(

        df[df["state"]==state]["district"]

        .dropna()

        .unique()

    )

# ============================================================
# Filter Dataset
# ============================================================

def filter_dataset(

    df,

    state="All",

    district="All"

):

    temp = df.copy()

    if state!="All":

        temp = temp[

            temp["state"]==state

        ]

    if district!="All":

        temp = temp[

            temp["district"]==district

        ]

    return temp

# ============================================================
# KPI Calculator
# ============================================================

def calculate_kpis(df):

    kpis = {

        "Population":int(df["population"].sum()),

        "Health Centres":int(df["health_centres"].sum()),

        "States":df["state"].nunique(),

        "Districts":df["district"].nunique(),

        "Vaccination":round(df["vaccination"].mean(),2),

        "Anaemia":round(df["anaemia"].mean(),2),

        "Literacy":round(df["literacy"].mean(),2),

        "Priority":round(df["healthcare_priority_score"].mean(),2)

    }

    return kpis

# ============================================================
# Top Priority Districts
# ============================================================

def top_priority(df,n=20):

    return (

        df

        .sort_values(

            "healthcare_priority_score",

            ascending=False

        )

        .head(n)

    )

# ============================================================
# Lowest Priority Districts
# ============================================================

def lowest_priority(df,n=20):

    return (

        df

        .sort_values(

            "healthcare_priority_score"

        )

        .head(n)

    )

# ============================================================
# State Summary
# ============================================================

def state_summary(df):

    return (

        df

        .groupby("state")

        .agg({

            "population":"sum",

            "health_centres":"sum",

            "vaccination":"mean",

            "anaemia":"mean",

            "healthcare_priority_score":"mean"

        })

        .reset_index()

    )

# ============================================================
# District Summary
# ============================================================

def district_summary(df,district):

    return (

        df[

            df["district"]==district

        ]

    )
