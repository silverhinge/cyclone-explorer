import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Page config
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
st.markdown("Welcome to Cyclone Explorer — a live dashboard for visualizing historical and current tropical cyclones.")

# Dropdown Menu
storm = st.selectbox(
    "Select a cyclone:",
    [
        "Hurricane Helene (2024)",
        "Hurricane Milton (2024) - coming soon",
        "Tropical Storm Beryl (2024) - coming soon"
    ]
)

# ---------------------- HURRICANE HELENE ---------------------- #
if storm == "Hurricane Helene (2024)":
    st.subheader("📌 Hurricane Helene – September 2024")

    st.markdown("""
    **Overview:**  
    Hurricane Helene made landfall in the Big Bend region of Florida in late September 2024 as a Category 4 hurricane, with sustained winds of 140 mph and a central pressure near 920 mb.  
    The storm caused widespread wind damage, record-breaking rainfall, and coastal flooding across Florida and inland states.
    """)

    # INTERACTIVE STRUCTURAL MAP
    st.markdown("### 🌀 Interactive Storm Structure Map")

    m = folium.Map(location=[29.0, -83.5], zoom_start=6, tiles='cartodbpositron')

    # Eye
    folium.CircleMarker(
        location=[29.0, -83.5],
        radius=8,
        popup="👁️ Eye: Central pressure ~920 mb\nMax winds ~140 mph",
        color="black",
        fill=True,
        fill_color="black",
        tooltip="Storm Eye"
    ).add_to(m)

    # Wind radii zones
    folium.Circle(
        location=[29.0, -83.5],
        radius=60000,  # ~60 km
        color="orange",
        fill=False,
        popup="🌬️ 34 kt Wind Radius (~60 km)",
        tooltip="34 kt zone"
    ).add_to(m)

    folium.Circle(
        location=[29.0, -83.5],
        radius=40000,
        color="red",
        fill=False,
        popup="🌬️ 50 kt Wind Radius (~40 km)",
        tooltip="50 kt zone"
    ).add_to(m)

    folium.Circle(
        location=[29.0, -83.5],
        radius=25000,
        color="darkred",
        fill=False,
        popup="🌬️ 64 kt Wind Radius (~25 km)",
        tooltip="64 kt zone"
    ).add_to(m)

    # Rainbands (as extended rings)
    rainband_radii = [90000, 120000, 150000]
    colors = ["#88f", "#66c", "#44a"]
    labels = ["Outer Rainband", "Mid Rainband", "Deep Convection"]

    for radius, color, label in zip(rainband_radii, colors, labels):
        folium.Circle(
            location=[29.0, -83.5],
            radius=radius,
            color=color,
            fill=False,
            popup=f"🌧️ {label}",
            tooltip=label
        ).add_to(m)

    # Display map
    st_data = st_folium(m, width=700, height=500)

    # STRUCTURAL CHARTS
    st.markdown("### 📊 Structural Diagrams")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Central Pressure Evolution (mb)**")
        hours = np.arange(0, 96, 6)
        pressure = 1010 - (np.sin(hours / 96 * np.pi) * 90 + 5)
        fig1, ax1 = plt.subplots()
        ax1.plot(hours, pressure, color='blue', linewidth=2)
        ax1.set_xlabel("Hours Since Formation")
        ax1.set_ylabel("Pressure (mb)")
        ax1.set_title("Central Pressure Drop")
        ax1.invert_yaxis()
        ax1.grid(True)
        st.pyplot(fig1)

    with col2:
        st.markdown("**Wind Field at Peak Intensity (mph)**")
        radii_km = np.linspace(0, 200, 200)
        wind_speed = 140 * np.exp(-radii_km / 50)
        fig2, ax2 = plt.subplots()
        ax2.plot(radii_km, wind_speed, color='darkred')
        ax2.set_xlabel("Distance from Eye (km)")
        ax2.set_ylabel("Wind Speed (mph)")
        ax2.set_title("Wind Field Cross-Section")
        ax2.grid(True)
        st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Rainband Structure (top-down schematic)**")
        theta = np.linspace(0, 2 * np.pi, 300)
        radii = [40, 80, 120, 160]
        fig3, ax3 = plt.subplots()
        for r in radii:
            ax3.plot(r * np.cos(theta), r * np.sin(theta), alpha=0.6)
        ax3.set_title("Rainbands")
        ax3.set_aspect("equal")
        ax3.set_xticks([])
        ax3.set_yticks([])
        st.pyplot(fig3)

    with col4:
        st.markdown("**Spaghetti Ensemble Track (mock)**")
        fig4, ax4 = plt.subplots()
        for i in range(10):
            offset = np.random.normal(0, 1.2, 10)
            lat = np.linspace(20, 30, 10) + offset
            lon = np.linspace(-80, -70, 10) + offset
            ax4.plot(lon, lat, alpha=0.5)
        ax4.set_xlabel("Longitude")
        ax4.set_ylabel("Latitude")
        ax4.set_title("Model Spread (Simulated)")
        ax4.grid(True)
        st.pyplot(fig4)

# ---------------------- PLACEHOLDER FOR FUTURE STORMS ---------------------- #
else:
    st.warning("This storm’s visuals are coming soon! Stay tuned as we add more 2024–2025 systems.")
