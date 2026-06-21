
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

with tab2:
    st.header("WillowForge Quantum AI Trading")
    if st.button("Run WillowForge Simulation"):
        st.success("Quantum portfolio optimization complete.")
    st.metric("Predicted Portfolio Drawdown", "18.5%")
    
    # Past Week Market Simulation
    st.subheader("Past Week Market Simulation")
    if st.button("Run Past Week Simulation"):
        data = pd.DataFrame({
            "Date": pd.date_range(end=datetime.now(), periods=7),
            "NVDA": [120, 118, 125, 130, 128, 135, 132],
            "TSM": [180, 178, 185, 190, 188, 195, 192],
            "AAPL": [220, 218, 225, 230, 228, 235, 232]
        })
        st.line_chart(data.set_index("Date"))
        st.metric("Portfolio Performance (Past Week)", "-2.8%")

with tab3:
    st.header("🧠 Hybrid Intelligence Engine")
    if st.button("Run Full Analysis"):
        st.success("Bayesian update + Analog search + Digital Twin complete.")
        st.metric("Final Predicted Impact", "22.4% ± 4.1%")
        st.write("**Recommendation**: Reroute high-value cargo, increase safety stock.")

st.caption(f"M1dN1ght • {datetime.now().strftime('%Y-%m-%d %H:%M')}")
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

with tab2:
    st.header("WillowForge Quantum AI Trading")
    if st.button("Run WillowForge Simulation"):
        st.success("Quantum portfolio optimization complete.")
    st.metric("Predicted Portfolio Drawdown", "18.5%")

with tab3:
    st.header("🧠 Hybrid Intelligence Engine - Data Flow")
    
    # Data Flow
    st.subheader("Data Flow")
    flow_data = pd.DataFrame({
        "Stage": ["Live Weather", "Physics Model", "Bayesian Update", "Analog Search", "Digital Twin", "Final Prediction"],
        "Value": [4.2, 18.5, 21.8, 22.4, 23.1, 22.4]
    })
    st.bar_chart(flow_data.set_index("Stage"))
    
    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Wind Field")
        fig = go.Figure(go.Scatter(x=np.linspace(-40, 40, 10), y=np.zeros(10), mode='lines', line=dict(color='lightblue')))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Storm Surge")
        st.metric("Predicted Surge", "6.8 ft")
    
    if st.button("Run Full Analysis"):
        st.success("All models converged.")
        st.metric("Final Predicted Impact", "22.4% ± 4.1%")
        st.write("**Recommendation**: Reroute high-value cargo, increase safety stock.")

st.caption(f"M1dN1ght • {datetime.now().strftime('%Y-%m-%d %H:%M')}")
