import streamlit as st

def load_css():

    st.markdown("""

<style>

/* ==========================================================
GENERAL
========================================================== */

html, body, [class*="css"]{

    background:#F8FAFC;
    color:#0F172A;
    font-family:'Segoe UI',sans-serif;

}

/* ==========================================================
HEADINGS
========================================================== */

h1{
    color:#0F172A !important;
    font-weight:700;
}

h2{
    color:#1E293B !important;
    font-weight:700;
}

h3{
    color:#334155 !important;
    font-weight:600;
}

p{
    color:#475569 !important;
    font-size:17px;
}

/* ==========================================================
SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{

    background:#0F172A;

}

section[data-testid="stSidebar"] *{

    color:white !important;

}

/* ==========================================================
METRIC CARDS
========================================================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:15px;

    border:1px solid #E2E8F0;

    box-shadow:0 4px 15px rgba(0,0,0,.08);

}

/* ==========================================================
BUTTON
========================================================== */

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    padding:12px;

    font-weight:bold;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* ==========================================================
DATAFRAME
========================================================== */

div[data-testid="stDataFrame"]{

    border-radius:12px;

    border:1px solid #CBD5E1;

}

/* ==========================================================
SUCCESS
========================================================== */

div[data-testid="stAlert"]{

    border-radius:12px;

}

/* ==========================================================
BLUE CARD
========================================================== */

.blue-card{

    background:#2563EB;

    color:white;

    padding:25px;

    border-radius:18px;

    box-shadow:0 10px 25px rgba(0,0,0,.15);

}

/* ==========================================================
GREEN CARD
========================================================== */

.green-card{

    background:#22C55E;

    color:white;

    padding:20px;

    border-radius:18px;

}

/* ==========================================================
INFO CARD
========================================================== */

.info-card{

    background:white;

    color:#0F172A;

    border:1px solid #E2E8F0;

    border-radius:18px;

    padding:20px;

    box-shadow:0 6px 20px rgba(0,0,0,.08);

}

/* ==========================================================
FOOTER
========================================================== */

.footer{

    background:white;

    border-radius:15px;

    border:1px solid #CBD5E1;

    padding:20px;

    color:#334155;

    text-align:center;

    margin-top:40px;

}

</style>

""",unsafe_allow_html=True)
