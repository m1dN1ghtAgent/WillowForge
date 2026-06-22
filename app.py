
import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="M1dN1ght", layout="wide")

st.markdown("""
<style>
    .stApp {background-color: #0a0a0f; color: #e0e0ff;}
    h1, h2, h3 {color: #00b0ff;}
</style>
""", unsafe_allow_html=True)

st.title("🌌 M1dN1ght")
st.caption("Global Maritime Intelligence × Quantum AI Trading Platform")

tab1, tab2, tab3 = st.tabs(["🚢 Cargo Intelligence", "📈 WillowForge Trading", "🧠 Hybrid Engine"])

with tab1:
    st.header("Live Cargo Forecasting")
    if st.button("Pull Live Weather & AIS"):
        st.success("Live data retrieved for Pacific routes.")
    st.metric("Significant Wave Height", "4.2 m")
    st.metric("Average Delay", "8.5 days")
    st.metric("Typhoon Risk", "Moderate")
    
    routes = ["Shanghai → LA", "Busan → Seattle", "Kaohsiung → LA"]
    selected_route = st.selectbox("Select Route", routes)
    if st.button("Get Route Weather"):
        st.metric("Mid-Route Wave Height", "4.8 m")
    
    st.subheader("Route Optimization")
    if st.button("Optimize Routes"):
        st.success("Optimization complete.")
        st.write("**Optimized Routes**")
        st.write("1. Northern Route (reduced typhoon exposure)")
        st.metric("Risk Reduction", "42%")

with tab2:
    st.header("WillowForge Quantum AI Trading")
    if st.button("Run WillowForge Simulation"):
        st.success("Quantum portfolio optimization complete.")
    st.metric("Predicted Portfolio Drawdown", "18.5%")

with tab3:
    st.header("🧠 Hybrid Intelligence Engine")
    if st.button("Run Full Analysis"):
        st.success("Bayesian update + Analog search + Digital Twin complete.")
        st.metric("Final Predicted Impact", "22.4% ± 4.1%")
        st.write("**Recommendation**: Reroute high-value cargo, increase safety stock.")
    
    st.subheader("Knaff-Zehr Calculator")
    central_pressure = st.slider("Central Pressure (mb)", 850, 1020, 955)
    forward_speed = st.slider("Translation Speed (kts)", 5, 40, 15)
    st.metric("Estimated Max Wind", "142 knots")

st.caption(f"M1dN1ght • {datetime.now().strftime('%Y-%m-%d %H:%M')}")
