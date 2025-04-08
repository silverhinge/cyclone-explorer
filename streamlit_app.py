import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# ---------------- CYCLONE DATA ---------------- #
cyclone_data = {
    "Hurricane Katrina (2005)": {
        "category": 5,
        "max_wind": 175,
        "min_pressure": 902,
        "landfall_cat": 3,
        "summary": "Catastrophic storm that flooded New Orleans and devastated the Gulf Coast."
    },
    "Hurricane Wilma (2005)": {
        "category": 5,
        "max_wind": 185,
        "min_pressure": 882,
        "landfall_cat": 3,
        "summary": "Strongest hurricane on record in the Atlantic basin by pressure."
    },
    "Hurricane Irma (2017)": {
        "category": 5,
        "max_wind": 180,
        "min_pressure": 914,
        "landfall_cat": 4,
        "summary": "Destroyed parts of the northern Caribbean and Florida Keys."
    },
    "Hurricane Helene (2024)": {
        "category": 4,
        "max_wind": 140,
        "min_pressure": 920,
        "landfall_cat": 4,
        "summary": "Struck Big Bend Florida region as a destructive Category 4 hurricane."
    },
    "Hurricane Milton (2024)": {
        "category": 5,
        "max_wind": 180,
        "min_pressure": 897,
        "landfall_cat": 3,
        "summary": "Made landfall near Siesta Key, Florida. Peaked with Cat 5 strength."
    },
    "Tropical Storm Beryl (2024)": {
        "category": 1,
        "max_wind": 65,
        "min_pressure": 994,
        "landfall_cat": 1,
        "summary": "Weak but persistent storm early in the 2024 season."
    }
}

# ---------------- PAGE SETUP ---------------- #
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
mode = st.selectbox("Choose a mode:", ["Explore One Cyclone", "Compare Two Cyclones"])

# ---------------- COMPARE MODE ---------------- #
if mode == "Compare Two Cyclones":
    st.header("🌪️ Storm Comparison Mode")

    col_pick = st.columns(2)
    with col_pick[0]:
        storm_a = st.selectbox("Select Storm A", list(cyclone_data.keys()), key="a")
    with col_pick[1]:
        storm_b = st.selectbox("Select Storm B", list(cyclone_data.keys()), key="b")

    data_a = cyclone_data[storm_a]
    data_b = cyclone_data[storm_b]

    st.markdown("### 📊 Key Cyclone Stats")
    stats_table = f"""
    | Metric            | {storm_a} | {storm_b} |
    |-------------------|------------------|------------------|
    | **Peak Category** | Cat {data_a['category']} | Cat {data_b['category']} |
    | **Max Wind (mph)**| {data_a['max_wind']} | {data_b['max_wind']} |
    | **Min Pressure**  | {data_a['min_pressure']} mb | {data_b['min_pressure']} mb |
    | **Landfall Cat**  | Cat {data_a['landfall_cat']} | Cat {data_b['landfall_cat']} |
    | **Summary**       | {data_a['summary']} | {data_b['summary']} |
    """
    st.markdown(stats_table)

    st.markdown("### 📉 Central Pressure Evolution")
    col1, col2 = st.columns(2)
    hours = np.arange(0, 96, 6)

    with col1:
        pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data_a['category'] * 20 + 10))
        fig1, ax1 = plt.subplots()
        ax1.plot(hours, pressure, color='blue')
        ax1.set_title(f"{storm_a} Pressure")
        ax1.invert_yaxis()
        st.pyplot(fig1)

    with col2:
        pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data_b['category'] * 20 + 10))
        fig2, ax2 = plt.subplots()
        ax2.plot(hours, pressure, color='darkred')
        ax2.set_title(f"{storm_b} Pressure")
        ax2.invert_yaxis()
        st.pyplot(fig2)

    st.markdown("### 🌬️ Wind Field Cross-Section")
    col3, col4 = st.columns(2)
    radii = np.linspace(0, 200, 200)

    with col3:
        winds = data_a['max_wind'] * np.exp(-radii / 50)
        fig3, ax3 = plt.subplots()
        ax3.plot(radii, winds, color='orange')
        ax3.set_title(f"{storm_a} Wind Field")
        st.pyplot(fig3)

    with col4:
        winds = data_b['max_wind'] * np.exp(-radii / 50)
        fig4, ax4 = plt.subplots()
        ax4.plot(radii, winds, color='purple')
        ax4.set_title(f"{storm_b} Wind Field")
        st.pyplot(fig4)

# ---------------- EXPLORE MODE ---------------- #
elif mode == "Explore One Cyclone":
    storm = st.selectbox("Select a cyclone to explore:", ["Hurricane Helene (2024)", "Hurricane Milton (2024)", "Tropical Storm Beryl (2024)"])

    if storm == "Hurricane Helene (2024)":
        loc = [29.0, -83.5]
        wind = 140
        pressure = 920
        category = 4
    elif storm == "Hurricane Milton (2024)":
        loc = [27.3, -82.5]
        wind = 180
        pressure = 897
        category = 5
    elif storm == "Tropical Storm Beryl (2024)":
        loc = [17.5, -61.8]
        wind = 65
        pressure = 994
        category = 1

    st.subheader(f"{storm}")
    m = folium.Map(location=loc, zoom_start=6, tiles='cartodbpositron')

    folium.CircleMarker(location=loc, radius=8, popup=f"👁️ Eye: {pressure} mb, {wind} mph", color="black", fill=True).add_to(m)
    folium.Circle(location=loc, radius=60000, color="orange", fill=False, popup="34 kt Wind Radius").add_to(m)
    folium.Circle(location=loc, radius=40000, color="red", fill=False, popup="50 kt Wind Radius").add_to(m)
    folium.Circle(location=loc, radius=25000, color="darkred", fill=False, popup="64 kt Wind Radius").add_to(m)

    st_data = st_folium(m, width=700, height=500)

    st.markdown("### 📉 Central Pressure Drop")
    hours = np.arange(0, 96, 6)
    p_curve = 1010 - (np.sin(hours / 96 * np.pi) * (category * 20 + 10))
    fig, ax = plt.subplots()
    ax.plot(hours, p_curve, color='blue')
    ax.set_title(f"{storm} Central Pressure")
    ax.set_xlabel("Hours Since Formation")
    ax.set_ylabel("Pressure (mb)")
    ax.invert_yaxis()
    st.pyplot(fig)

# ---------------- END ---------------- #
