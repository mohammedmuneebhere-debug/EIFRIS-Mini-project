# app/main.py

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from utils.forecast import forecast_disaster
from utils.routes import recommend_routes
from utils.alerts import send_alert_sms
from utils.resources import allocate_resources
from utils.chain_detector import load_chain_rules, detect_disaster_chain

st.set_page_config(page_title="DisasterAware AI", layout="wide")

# Initialize session state
if "analyze_clicked" not in st.session_state:
    st.session_state.analyze_clicked = False

st.title("🌐 DisasterAware AI")
st.markdown("A Unified Disaster Response System")

# 📍 Step 1: Input location
location = st.text_input("Enter Location (City or Region)", "Region A")

# 🧠 Analyze button
if st.button("🧠 Analyze Risk"):
    st.session_state.analyze_clicked = True

# 🔁 Display only after click
if st.session_state.analyze_clicked:
    # 🔮 Step 2: Predict disaster
    forecast = forecast_disaster(location)
    st.subheader("🔮 Predicted Disaster")
    st.markdown(f"""
    - **Type:** {forecast['type']}
    - **Severity:** {forecast['severity']}
    - **Impact Zones:** {', '.join(forecast['impact_zones'])}
    """)

    # 🛣️ Step 3: Recommend routes
    routes = recommend_routes(location, forecast["impact_zones"])
    st.subheader("🛣️ Safe Evacuation Routes")
    for i, route in enumerate(routes, 1):
        st.markdown(f"**{i}.** {route}")

    # 🗺️ Step 4: Map
    m = folium.Map(location=[17.40, 78.47], zoom_start=6)
    for zone in forecast["impact_zones"]:
        folium.Marker(
            [17.40, 78.47], tooltip=f"Impact Zone: {zone}", icon=folium.Icon(color="red")
        ).add_to(m)
    st.subheader("📍 Impact Zone Map")
    st_folium(m, width=700, height=500)

    # 📩 Step 5: Send SMS alert
    if st.button("📩 Send SMS Alert"):
        send_alert_sms(f"Disaster Alert for {forecast['type']} - Take shelter!", location)
        st.success("📩 Alert sent to affected region.")

    # 🚑 Step 6: Allocate resources
    df = pd.read_csv("data/sample_disaster_data.csv")
    allocation = allocate_resources(df, {"ambulances": 10, "boats": 5, "shelters": 6})
    st.subheader("🚑 Resource Allocation Plan")
    for region, resources in allocation.items():
        st.markdown(f"**📍 {region}**")
        for item in resources:
            st.markdown(f"- {item}")

    # 🔗 Step 7: Disaster chain detection
    chain_rules = load_chain_rules("data/chain_detection_rules.json")
    chains = detect_disaster_chain(df, chain_rules)
    st.subheader("⚠️ Disaster Chain Warnings")
    if chains:
        for alert in chains:
            st.warning(alert)
    else:
        st.success("✅ No disaster chains detected.")

# 🔁 Optional: Reset button
if st.button("🔄 Reset"):
    st.session_state.analyze_clicked = False
