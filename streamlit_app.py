import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# ---------------- CYCLONE DATA ---------------- #
cyclone_data = {
    "Hurricane Katrina (2005)": {
        "category": 5, "max_wind": 175, "min_pressure": 902, "landfall_cat": 3,
        "summary": "Catastrophic storm that flooded New Orleans and devastated the Gulf Coast."
    },
    "Hurricane Wilma (2005)": {
        "category": 5, "max_wind": 185, "min_pressure": 882, "landfall_cat": 3,
        "summary": "Strongest Atlantic hurricane on record by minimum pressure."
    },
    "Hurricane Irma (2017)": {
        "category": 5, "max_wind": 180, "min_pressure": 914, "landfall_cat": 4,
        "summary": "Destroyed parts of the northern Caribbean and Florida Keys."
    },
    "Hurricane Maria (2017)": {
        "category": 5, "max_wind": 175, "min_pressure": 908, "landfall_cat": 4,
        "summary": "Devastated Puerto Rico with prolonged power outages and flooding."
    },
    "Hurricane Harvey (2017)": {
        "category": 4, "max_wind": 130, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Catastrophic flooding in Texas. One of the costliest U.S. hurricanes."
    },
    "Hurricane Dorian (2019)": {
        "category": 5, "max_wind": 185, "min_pressure": 910, "landfall_cat": 1,
        "summary": "Destroyed Grand Bahama with Category 5 winds and prolonged stall."
    },
    "Hurricane Laura (2020)": {
        "category": 4, "max_wind": 150, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Major landfall in Louisiana with extreme wind damage."
    },
    "Hurricane Ian (2022)": {
        "category": 5, "max_wind": 160, "min_pressure": 936, "landfall_cat": 4,
        "summary": "Devastated SW Florida with storm surge and flooding."
    },
    "Hurricane Fiona (2022)": {
        "category": 4, "max_wind": 130, "min_pressure": 931, "landfall_cat": 3,
        "summary": "Significant flooding in Puerto Rico and Atlantic Canada."
    },
    "Hurricane Helene (2024)": {
        "category": 4, "max_wind": 140, "min_pressure": 920, "landfall_cat": 4,
        "summary": "Struck Big Bend Florida as a destructive Category 4 hurricane."
    },
    "Hurricane Milton (2024)": {
        "category": 5, "max_wind": 180, "min_pressure": 897, "landfall_cat": 3,
        "summary": "Made landfall near Siesta Key, Florida. Peaked at Cat 5."
    },
    "Hurricane Beryl (2024)": {
        "category": 5, "max_wind": 165, "min_pressure": 926, "landfall_cat": 4,
        "summary": "First Category 5 hurricane in June. Devastated parts of the Windward Islands."
    },
    "Hurricane Isabel (2003)": {
        "category": 5, "max_wind": 165, "min_pressure": 915, "landfall_cat": 2,
        "summary": "Large, powerful storm that made landfall in North Carolina."
    },
    "Hurricane Ivan (2004)": {
        "category": 5, "max_wind": 165, "min_pressure": 910, "landfall_cat": 3,
        "summary": "Major hurricane that impacted Grenada and the U.S. Gulf Coast."
    },
    "Hurricane Dean (2007)": {
        "category": 5, "max_wind": 175, "min_pressure": 905, "landfall_cat": 5,
        "summary": "Made landfall in Mexico's Yucatan Peninsula at peak intensity."
    },
    "Hurricane Michael (2018)": {
        "category": 5, "max_wind": 160, "min_pressure": 919, "landfall_cat": 5,
        "summary": "Devastated the Florida Panhandle with catastrophic winds and surge."
    },
    "Hurricane Sandy (2012)": {
        "category": 3, "max_wind": 115, "min_pressure": 940, "landfall_cat": 1,
        "summary": "Massive hybrid storm that impacted the northeastern U.S. coast."
    }
}

# ---------------- UI ---------------- #
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
mode = st.selectbox("Choose a mode:", ["Explore One Cyclone", "Compare Two Cyclones"])

# ---------------- COMPARE ---------------- #
if mode == "Compare Two Cyclones":
    st.header("🌪️ Storm Comparison Mode")

    storm_options = ["Select Cyclone"] + list(cyclone_data.keys())
    col_pick = st.columns(2)
    storm_a = col_pick[0].selectbox("Select Storm A", storm_options, index=0, key="a")
    storm_b = col_pick[1].selectbox("Select Storm B", storm_options, index=0, key="b")

    if storm_a != "Select Cyclone" and storm_b != "Select Cyclone":
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

        for col, storm, data, color in zip([col1, col2], [storm_a, storm_b], [data_a, data_b], ['blue', 'darkred']):
            pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data['category'] * 20 + 10))
            fig, ax = plt.subplots()
            ax.plot(hours, pressure, color=color)
            ax.set_title(f"{storm} Pressure")
            ax.invert_yaxis()
            st.pyplot(fig)

        st.markdown("### 🌬️ Wind Field Cross-Section")
        col3, col4 = st.columns(2)
        radii = np.linspace(0, 200, 200)

        for col, storm, data, color in zip([col3, col4], [storm_a, storm_b], [data_a, data_b], ['orange', 'purple']):
            winds = data['max_wind'] * np.exp(-radii / 50)
            fig, ax = plt.subplots()
            ax.plot(radii, winds, color=color)
            ax.set_title(f"{storm} Wind Field")
            st.pyplot(fig)

# ---------------- EXPLORE ---------------- #
elif mode == "Explore One Cyclone":
    storm = st.selectbox("Select a cyclone to explore:", ["Hurricane Helene (2024)", "Hurricane Milton (2024)", "Hurricane Beryl (2024)"])

    if storm == "Hurricane Helene (2024)":
        loc, wind, pressure, category = [29.0, -83.5], 140, 920, 4
    elif storm == "Hurricane Milton (2024)":
        loc, wind, pressure, category = [27.3, -82.5], 180, 897, 5
    elif storm == "Hurricane Beryl (2024)":
        loc, wind, pressure, category = [15.5, -61.0], 165, 926, 5

    st.subheader(f"{storm}")
    m = folium.Map(location=loc, zoom_start=6, tiles='cartodbpositron')
    folium.CircleMarker(location=loc, radius=8, popup=f"👁️ Eye: {pressure} mb, {wind} mph", color="black", fill=True).add_to(m)
    folium.Circle(location=loc, radius=60000, color="orange", fill=False, popup="34 kt Wind Radius").add_to(m)
    folium.Circle(location=loc, radius=40000, color="red", fill=False, popup="50 kt Wind Radius").add_to(m)
    folium.Circle(location=loc, radius=25000, color="darkred", fill=False, popup="64 kt Wind Radius").add_to(m)
    st_folium(m, width=700, height=500)

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
