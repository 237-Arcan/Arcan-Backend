# app/core/realtime_dashboard.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from arcanapp.core.predictive_engine import fetch_live_odds

def show_live_odds():
    st_autorefresh(interval=10000, key="datarefresh")
    st.title("ShadowOdds - Live Betting Flow Monitor")
    st.line_chart(fetch_live_odds())
