import streamlit as st

def load_css():

    st.markdown("""
<style>

/* =========================
   GLOBAL
========================= */

html,
body,
[data-testid="stAppViewContainer"],
.main {

    background: #0B1120 !important;
    color: #F8FAFC !important;

}

[data-testid="stHeader"]{

    background:#0B1120 !important;

}

[data-testid="stToolbar"]{

    background:#0B1120 !important;

}

.block-container{

    background:#0B1120 !important;

    padding-top:2rem;

}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:#F8FAFC !important;
}

/* =========================
   HEADINGS
========================= */

h1{
    color:#FFFFFF !important;
    font-weight:800 !important;
}

h2{
    color:#F8FAFC !important;
    font-weight:700 !important;
}

h3{
    color:#E2E8F0 !important;
    font-weight:600 !important;
}

h4,h5,h6{
    color:#CBD5E1 !important;
}

/* =========================
   TEXT
========================= */

p{
    color:#CBD5E1 !important;
}

label{
    color:#E2E8F0 !important;
}

span{
    color:#E2E8F0;
}

/* =========================
   METRIC CARDS
========================= */

div[data-testid="metric-container"]{

    background:#1E293B;

    border:1px solid #334155;

    border-radius:16px;

    padding:18px;

    box-shadow:0 6px 18px rgba(0,0,0,.35);

}

div[data-testid="metric-container"] label{

    color:#94A3B8 !important;

}

div[data-testid="metric-container"] div{

    color:#FFFFFF !important;

}

/* =========================
   BUTTONS
========================= */

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:700;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* =========================
   DATAFRAME
========================= */

div[data-testid="stDataFrame"]{

    border:1px solid #334155;

    border-radius:12px;

}

/* =========================
   DOWNLOAD BUTTON
========================= */

.stDownloadButton>button{

    background:#059669;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:bold;

}

/* =========================
   SUCCESS / INFO / WARNING
========================= */

div[data-baseweb="notification"]{

    border-radius:12px;

}

/* =========================
   CUSTOM CARDS
========================= */

.blue-card{

    background:#1D4ED8;

    color:white;

    padding:25px;

    border-radius:18px;

    box-shadow:0 10px 25px rgba(0,0,0,.30);

}

.green-card{

    background:#15803D;

    color:white;

    padding:25px;

    border-radius:18px;

    box-shadow:0 10px 25px rgba(0,0,0,.30);

}

.info-card{

    background:#1E293B;

    color:#F8FAFC;

    border:1px solid #334155;

    padding:22px;

    border-radius:18px;

}

.info-card h2,
.info-card h3,
.info-card p{

    color:#F8FAFC !important;

}

/* =========================
   FOOTER
========================= */

.footer{

    background:#111827;

    border:1px solid #334155;

    border-radius:16px;

    padding:20px;

    text-align:center;

    color:#CBD5E1;

}

/* =========================
   PLOTLY
========================= */

.js-plotly-plot{

    border-radius:14px;

}

</style>
""", unsafe_allow_html=True)
