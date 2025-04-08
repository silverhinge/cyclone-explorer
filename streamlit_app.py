import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# ---------------- Cyclone Data ---------------- #
cyclone_data = {
    "Hurricane Katrina (2005)": {
        "category": 5, "max_wind": 175, "min_pressure": 902, "landfall_cat": 3,
        "summary": "Catastrophic storm that flooded New Orleans and devastated the Gulf Coast.",
        "track": [(23.1, -75.1), (24.5, -76.8), (26.1, -78.3), (27.8, -80.0), (29.5, -89.6)]
    },
    "Hurricane Wilma (2005)": {
        "category": 5, "max_wind": 185, "min_pressure": 882, "landfall_cat": 3,
        "summary": "Strongest Atlantic hurricane on record by pressure. Impacted Yucatán and Florida.",
        "track": [(17.0, -79.0), (18.5, -82.0), (19.8, -84.0), (20.9, -86.5), (25.0, -80.0)]
    },
    "Hurricane Rita (2005)": {
        "category": 5, "max_wind": 180, "min_pressure": 895, "landfall_cat": 3,
        "summary": "Powerful Gulf storm following Katrina, landfall near Texas-Louisiana border.",
        "track": [(21.5, -75.0), (23.0, -77.0), (24.7, -79.0), (26.5, -91.0), (29.7, -93.6)]
    },
    "Hurricane Isabel (2003)": {
        "category": 5, "max_wind": 165, "min_pressure": 915, "landfall_cat": 2,
        "summary": "Large landfalling hurricane in North Carolina."
    },
    "Hurricane Ivan (2004)": {
        "category": 5, "max_wind": 165, "min_pressure": 910, "landfall_cat": 3,
        "summary": "Major Gulf storm. Devastated Grenada and struck Alabama."
    },
    "Hurricane Dean (2007)": {
        "category": 5, "max_wind": 175, "min_pressure": 905, "landfall_cat": 5,
        "summary": "Yucatán landfall at Cat 5 intensity."
    },
    "Hurricane Irma (2017)": {
        "category": 5, "max_wind": 180, "min_pressure": 914, "landfall_cat": 4,
        "summary": "Destroyed parts of the northern Caribbean and Florida Keys."
    },
    "Hurricane Maria (2017)": {
        "category": 5, "max_wind": 175, "min_pressure": 908, "landfall_cat": 4,
        "summary": "Devastated Puerto Rico with prolonged outages and flooding."
    },
    "Hurricane Harvey (2017)": {
        "category": 4, "max_wind": 130, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Catastrophic flooding in Texas. One of the costliest U.S. hurricanes."
    },
    "Hurricane Michael (2018)": {
        "category": 5, "max_wind": 160, "min_pressure": 919, "landfall_cat": 5,
        "summary": "Destroyed parts of the Florida Panhandle."
    },
    "Hurricane Dorian (2019)": {
        "category": 5, "max_wind": 185, "min_pressure": 910, "landfall_cat": 1,
        "summary": "Stalled over Grand Bahama with catastrophic winds."
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
        "summary": "Flooding in Puerto Rico and damage across Atlantic Canada."
    },
    "Hurricane Sandy (2012)": {
        "category": 3, "max_wind": 115, "min_pressure": 940, "landfall_cat": 1,
        "summary": "Massive hybrid cyclone. Northeast U.S. impact."
    },
    "Hurricane Helene (2024)": {
        "category": 4, "max_wind": 140, "min_pressure": 920, "landfall_cat": 4,
        "summary": "Struck Florida’s Big Bend region as a powerful Cat 4.",
        "track": [(18.0, -58.0), (20.0, -60.0), (23.0, -63.0), (25.5, -67.0), (29.0, -83.5)]
    },
    "Hurricane Milton (2024)": {
        "category": 5, "max_wind": 180, "min_pressure": 897, "landfall_cat": 3,
        "summary": "Peaked at Category 5 before making landfall near Siesta Key, Florida.",
        "track": [(18.5, -70.0), (21.0, -72.5), (23.5, -75.0), (25.8, -78.0), (27.3, -82.5)]
    },
    "Hurricane Beryl (2024)": {
        "category": 5, "max_wind": 165, "min_pressure": 926, "landfall_cat": 4,
        "summary": "Historic Category 5 hurricane in June, devastated parts of the Windward Islands.",
        "track": [(11.5, -52.0), (12.8, -55.0), (14.2, -58.0), (15.5, -61.0), (16.8, -64.0)]
    }
}


# ---------------- App Layout ---------------- #
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
mode = st.selectbox("Choose a mode:", ["Explore One Cyclone", "Compare Two Cyclones"])

# ---------------- EXPLORE ONE ---------------- #
if mode == "Explore One Cyclone":
    st.header("🌀 Explore One Cyclone")

    cyclone_options = ["Select Cyclone"] + list(cyclone_data.keys())
    selected = st.selectbox("Select a Cyclone", cyclone_options)

    if selected != "Select Cyclone":
        data = cyclone_data[selected]

        st.subheader(selected)
        st.markdown(f"**Summary:** {data['summary']}")
        st.markdown(f"**Category:** {data['category']}  |  **Max Wind:** {data['max_wind']} mph  |  **Min Pressure:** {data['min_pressure']} mb  |  **Landfall Cat:** {data['landfall_cat']}")

        st.markdown("### 🌀 Cyclone Structure & Track")

        col_map1, col_map2 = st.columns(2)
        
        with col_map1:
            st.markdown("**Wind Field Rings**")
            m1 = folium.Map(location=data['track'][-1], zoom_start=6, tiles='cartodbpositron')
            folium.CircleMarker(
                location=data['track'][-1],
                radius=8,
                popup=f"Eye: {data['min_pressure']} mb, {data['max_wind']} mph",
                color="black",
                fill=True
            ).add_to(m1)
            folium.Circle(location=data['track'][-1], radius=60000, color="orange", fill=False, popup="34 kt Wind Radius").add_to(m1)
            folium.Circle(location=data['track'][-1], radius=40000, color="red", fill=False, popup="50 kt Wind Radius").add_to(m1)
            folium.Circle(location=data['track'][-1], radius=25000, color="darkred", fill=False, popup="64 kt Wind Radius").add_to(m1)
            st_folium(m1, width=350, height=350)
        
        with col_map2:
            st.markdown("**Track Map**")
            m2 = folium.Map(location=data['track'][0], zoom_start=5, tiles='cartodbpositron')
            folium.PolyLine(data['track'], color="blue").add_to(m2)
            folium.Marker(data['track'][0], popup="Start").add_to(m2)
            folium.Marker(data['track'][-1], popup="End").add_to(m2)
            st_folium(m2, width=350, height=350)


        st.markdown("### 📉 Central Pressure Evolution")
        hours = np.arange(0, 96, 6)
        pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data['category'] * 20 + 10))
        fig, ax = plt.subplots()
        ax.plot(hours, pressure, color='blue')
        ax.set_xlabel("Hours")
        ax.set_ylabel("Pressure (mb)")
        ax.set_title("Central Pressure Over Time")
        ax.invert_yaxis()
        st.pyplot(fig)

        st.markdown("### 🌬️ Wind Field Cross-Section")
        radii = np.linspace(0, 200, 200)
        wind_profile = data['max_wind'] * np.exp(-radii / 50)
        fig2, ax2 = plt.subplots()
        ax2.plot(radii, wind_profile, color='orange')
        ax2.set_xlabel("Distance from Eye (km)")
        ax2.set_ylabel("Wind Speed (mph)")
        ax2.set_title("Wind Speed by Radius")
        st.pyplot(fig2)

# ---------------- COMPARE TWO ---------------- #
if mode == "Compare Two Cyclones":
    st.header("🌪️ Storm Comparison Mode")

    options = ["Select Cyclone"] + list(cyclone_data.keys())
    col = st.columns(2)
    storm_a = col[0].selectbox("Select Storm A", options, index=0, key="a")
    storm_b = col[1].selectbox("Select Storm B", options, index=0, key="b")

    if storm_a != "Select Cyclone" and storm_b != "Select Cyclone":
        data_a = cyclone_data[storm_a]
        data_b = cyclone_data[storm_b]

        st.markdown("### 🗺️ Track Maps")
        col1, col2 = st.columns(2)
        with col1:
            m1 = folium.Map(location=data_a['track'][0], zoom_start=5, tiles='cartodbpositron')
            folium.PolyLine(data_a['track'], color="blue").add_to(m1)
            folium.Marker(data_a['track'][0], popup="Start").add_to(m1)
            folium.Marker(data_a['track'][-1], popup="End").add_to(m1)
            st.markdown(f"**{storm_a}**")
            st_folium(m1, width=350, height=250)

        with col2:
            m2 = folium.Map(location=data_b['track'][0], zoom_start=5, tiles='cartodbpositron')
            folium.PolyLine(data_b['track'], color="red").add_to(m2)
            folium.Marker(data_b['track'][0], popup="Start").add_to(m2)
            folium.Marker(data_b['track'][-1], popup="End").add_to(m2)
            st.markdown(f"**{storm_b}**")
            st_folium(m2, width=350, height=250)

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
        col3, col4 = st.columns(2)
        hours = np.arange(0, 96, 6)

        with col3:
            pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data_a['category'] * 20 + 10))
            fig, ax = plt.subplots()
            ax.plot(hours, pressure, color='blue')
            ax.set_title(f"{storm_a} Pressure")
            ax.invert_yaxis()
            st.pyplot(fig)

        with col4:
            pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data_b['category'] * 20 + 10))
            fig, ax = plt.subplots()
            ax.plot(hours, pressure, color='darkred')
            ax.set_title(f"{storm_b} Pressure")
            ax.invert_yaxis()
            st.pyplot(fig)

        st.markdown("### 🌬️ Wind Field Cross-Section")
        col5, col6 = st.columns(2)
        radii = np.linspace(0, 200, 200)

        with col5:
            wind_a = data_a['max_wind'] * np.exp(-radii / 50)
            fig, ax = plt.subplots()
            ax.plot(radii, wind_a, color='orange')
            ax.set_title(f"{storm_a} Wind Field")
            st.pyplot(fig)

        with col6:
            wind_b = data_b['max_wind'] * np.exp(-radii / 50)
            fig, ax = plt.subplots()
            ax.plot(radii, wind_b, color='purple')
            ax.set_title(f"{storm_b} Wind Field")
            st.pyplot(fig)
