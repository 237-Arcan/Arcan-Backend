import streamlit as st
from streamlit_autorefresh import st_autorefresh
from modules.shadow.odds_analyzer import fetch_live_odds

def show_live_odds():
    st.title("ShadowOdds Live Dashboard")
    st_autorefresh(interval=5000)
    live_data = fetch_live_odds()
    if live_data is not None:
        st.line_chart(live_data)
    else:
        st.warning("Aucune donnée de cote en direct disponible.")
