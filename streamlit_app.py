import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# ---------------- Cyclone Data for Comparison ---------------- #
cyclone_data = {
    "Hurricane Katrina (2005)": {"category": 5, "max_wind": 175, "min_pressure": 902, "landfall_cat": 3,
        "summary": "Catastrophic storm that flooded New Orleans and devastated the Gulf Coast."},
    "Hurricane Wilma (2005)": {"category": 5, "max_wind": 185, "min_pressure": 882, "landfall_cat": 3,
        "summary": "Strongest Atlantic hurricane on record by pressure. Impacted Yucatan and Florida."},
    "Hurricane Rita (2005)": {"category": 5, "max_wind": 180, "min_pressure": 895, "landfall_cat": 3,
        "summary": "Powerful Gulf storm following Katrina, landfall near Texas-Louisiana border."},
    "Hurricane Irma (2017)": {"category": 5, "max_wind": 180, "min_pressure": 914, "landfall_cat": 4,
        "summary": "Destroyed parts of the northern Caribbean and Florida Keys."},
    "Hurricane Maria (2017)": {"category": 5, "max_wind": 175, "min_pressure": 908, "landfall_cat": 4,
        "summary": "Devastated Puerto Rico with prolonged outages and flooding."},
    "Hurricane Harvey (2017)": {"category": 4, "max_wind": 130, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Catastrophic flooding in Texas. One of the costliest U.S. hurricanes."},
    "Hurricane Dorian (2019)": {"category": 5, "max_wind": 185, "min_pressure": 910, "landfall_cat": 1,
        "summary": "Stalled over Grand Bahama with catastrophic winds."},
    "Hurricane Laura (2020)": {"category": 4, "max_wind": 150, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Major landfall in Louisiana with extreme wind damage."},
    "Hurricane Ian (2022)": {"category": 5, "max_wind": 160, "min_pressure": 936, "landfall_cat": 4,
        "summary": "Devastated SW Florida with storm surge and flooding."},
    "Hurricane Fiona (2022)": {"category": 4, "max_wind": 130, "min_pressure": 931, "landfall_cat": 3,
        "summary": "Flooding in Puerto Rico and damage across Atlantic Canada."},
    "Hurricane Helene (2024)": {"category": 4, "max_wind": 140, "min_pressure": 920, "landfall_cat": 4,
        "summary": "Struck Florida’s Big Bend region as a powerful Cat 4."},
    "Hurricane Milton (2024)": {"category": 5, "max_wind": 180, "min_pressure": 897, "landfall_cat": 3,
        "summary": "Cat 5 peak, landfall near Siesta Key, Florida."},
    "Hurricane Beryl (2024)": {"category": 5, "max_wind": 165, "min_pressure": 926, "landfall_cat": 4,
        "summary": "Historic Cat 5 in June. Devastated the Windward Islands."},
    "Hurricane Isabel (2003)": {"category": 5, "max_wind": 165, "min_pressure": 915, "landfall_cat": 2,
        "summary": "Large landfalling hurricane in North Carolina."},
    "Hurricane Ivan (2004)": {"category": 5, "max_wind": 165, "min_pressure": 910, "landfall_cat": 3,
        "summary": "Major Gulf storm. Devastated Grenada and struck Alabama."},
    "Hurricane Dean (2007)": {"category": 5, "max_wind": 175, "min_pressure": 905, "landfall_cat": 5,
        "summary": "Yucatan landfall at Cat 5 intensity."},
    "Hurricane Michael (2018)": {"category": 5, "max_wind": 160, "min_pressure": 919, "landfall_cat": 5,
        "summary": "Destroyed parts of the Florida Panhandle."},
    "Hurricane Sandy (2012)": {"category": 3, "max_wind": 115, "min_pressure": 940, "landfall_cat": 1,
        "summary": "Massive hybrid cyclone. Northeast U.S. impact."}
}

# ---------------- App Layout ---------------- #
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
mode = st.selectbox("Choose a mode:", ["Explore One Cyclone", "Compare Two Cyclones"])

# ---------------- Compare Two Cyclones ---------------- #
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

# ---------------- Explore One Cyclone ---------------- #
elif mode == "Explore One Cyclone":
    storm = st.selectbox("Select a cyclone to explore:", [
        "Hurricane Helene (2024)",
        "Hurricane Milton (2024)",
        "Hurricane Beryl (2024)",
        "Hurricane Katrina (2005)",
        "Hurricane Wilma (2005)",
        "Hurricane Rita (2005)"
    ])

    storm_info = {
        "Hurricane Helene (2024)": {
            "loc": [29.0, -83.5], "wind": 140, "pressure": 920, "category": 4,
            "summary": "Struck Florida's Big Bend region as a powerful Category 4 hurricane."
        },
        "Hurricane Milton (2024)": {
            "loc": [27.3, -82.5], "wind": 180, "pressure": 897, "category": 5,
            "summary": "Peaked at Category 5 before making landfall near Siesta Key, Florida."
        },
        "Hurricane Beryl (2024)": {
            "loc": [15.5, -61.0], "wind": 165, "pressure": 926, "category": 5,
            "summary": "Historic Category 5 in June, striking the Windward Islands."
        },
        "Hurricane Katrina (2005)": {
            "loc": [29.5, -89.6], "wind": 175, "pressure": 902, "category": 5,
            "summary": "Massive flooding in New Orleans. One of the costliest disasters in U.S. history."
        },
        "Hurricane Wilma (2005)": {
            "loc": [20.5, -87.0], "wind": 185, "pressure": 882, "category": 5,
            "summary": "Strongest Atlantic hurricane by pressure. Yucatán and Florida landfalls."
        },
        "Hurricane Rita (2005)": {
            "loc": [29.7, -93.6], "wind": 180, "pressure": 895, "category": 5,
            "summary": "Followed Katrina with major landfall near TX-LA border."
        }
    }

    data = storm_info[storm]
    loc, wind, pressure, category, summary = data["loc"], data["wind"], data["pressure"], data["category"], data["summary"]

    st.subheader(storm)
    st.markdown(f"**Summary:** {summary}")
    st.markdown(f"**Peak Wind:** {wind} mph &nbsp;&nbsp; | &nbsp;&nbsp; **Min Pressure:** {pressure} mb &nbsp;&nbsp; | &nbsp;&nbsp; **Category:** {category}")

    st.markdown("### 🌍 Storm Structure Map")
    m = folium.Map(location=loc, zoom_start=6, tiles='cartodbpositron')
    folium.CircleMarker(location=loc, radius=8, popup=f"Eye: {pressure} mb, {wind} mph", color="black", fill=True).add_to(m)
    folium.Circle(location=loc, radius=60000, color="orange", fill=False, popup="34 kt Wind Radius").add_to(m)
    folium.Circle(location=loc, radius=40000, color="red", fill=False, popup="50 kt Wind Radius").add_to(m)
    folium.Circle(location=loc, radius=25000, color="darkred", fill=False, popup="64 kt Wind Radius").add_to(m)
    st_folium(m, width=700, height=500)

    st.markdown("### 📉 Central Pressure Drop")
    hours = np.arange(0, 96, 6)
    p_curve = 1010 - (np.sin(hours / 96 * np.pi) * (category * 20 + 10))
    fig, ax = plt.subplots()
    ax.plot(hours, p_curve, color='blue')
    ax.set_title(f"{storm} Central Pressure Evolution")
    ax.set_xlabel("Hours Since Formation")
    ax.set_ylabel("Pressure (mb)")
    ax.invert_yaxis()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("### 🌬️ Wind Field Cross-Section")
    radii_km = np.linspace(0, 200, 200)
    wind_profile = wind * np.exp(-radii_km / 50)
    fig2, ax2 = plt.subplots()
    ax2.plot(radii_km, wind_profile, color='crimson')
    ax2.set_title(f"{storm} Wind Speed by Distance")
    ax2.set_xlabel("Distance from Eye (km)")
    ax2.set_ylabel("Wind Speed (mph)")
    ax2.grid(True)
    st.pyplot(fig2)
