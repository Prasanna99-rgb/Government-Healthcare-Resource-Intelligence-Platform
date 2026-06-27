import streamlit as st

def apply_styles():

    st.markdown("""
    <style>

    /* ------------------------------------------------ */
    /* Hide Streamlit Default Menu                       */
    /* ------------------------------------------------ */

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    /* ------------------------------------------------ */
    /* Main App                                         */
    /* ------------------------------------------------ */

    .main{
        background-color:#F4F8FC;
    }

    .block-container{
        padding-top:1rem;
        padding-left:2rem;
        padding-right:2rem;
        padding-bottom:2rem;
    }

    /* ------------------------------------------------ */
    /* Hero Section                                     */
    /* ------------------------------------------------ */

    .hero{

        background:linear-gradient(135deg,#0B3C5D,#328CC1);

        padding:35px;

        border-radius:20px;

        color:white;

        text-align:center;

        margin-bottom:25px;

        box-shadow:0 8px 20px rgba(0,0,0,.18);

    }

    .hero h1{

        font-size:42px;

        font-weight:bold;

        margin-bottom:10px;

    }

    .hero p{

        font-size:18px;

    }

    /* ------------------------------------------------ */
    /* Section Card                                     */
    /* ------------------------------------------------ */

    .section{

        background:white;

        border-radius:18px;

        padding:25px;

        margin-bottom:20px;

        box-shadow:0 4px 15px rgba(0,0,0,.08);

    }

    /* ------------------------------------------------ */
    /* KPI Cards                                        */
    /* ------------------------------------------------ */

    div[data-testid="metric-container"]{

        background:white;

        border-radius:15px;

        padding:18px;

        box-shadow:0 4px 15px rgba(0,0,0,.10);

        border-left:6px solid #0B3C5D;

    }

    div[data-testid="metric-container"]:hover{

        transform:translateY(-4px);

        transition:.3s;

    }

    /* ------------------------------------------------ */
    /* Sidebar                                          */
    /* ------------------------------------------------ */

    section[data-testid="stSidebar"]{

        background:#0B3C5D;

    }

    section[data-testid="stSidebar"] *{

        color:white;

    }

    /* ------------------------------------------------ */
    /* Buttons                                          */
    /* ------------------------------------------------ */

    .stButton>button{

        width:100%;

        background:#0B3C5D;

        color:white;

        border:none;

        border-radius:10px;

        font-weight:bold;

        height:45px;

    }

    .stButton>button:hover{

        background:#1976D2;

        color:white;

    }

    /* ------------------------------------------------ */
    /* Download Button                                  */
    /* ------------------------------------------------ */

    .stDownloadButton>button{

        width:100%;

        background:#2E7D32;

        color:white;

        border:none;

        border-radius:10px;

        font-weight:bold;

        height:45px;

    }

    /* ------------------------------------------------ */
    /* Dataframe                                        */
    /* ------------------------------------------------ */

    div[data-testid="stDataFrame"]{

        border-radius:15px;

        overflow:hidden;

    }

    /* ------------------------------------------------ */
    /* Footer                                           */
    /* ------------------------------------------------ */

    .footer{

        text-align:center;

        color:gray;

        font-size:14px;

        margin-top:30px;

    }

    </style>

    """, unsafe_allow_html=True)
