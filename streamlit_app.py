import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
season_data = {
    "2000": {
        "total_storms": 15,
        "hurricanes": 8,
        "major_hurricanes": 3,
        "notable_storms": [
            {
                "name": "Hurricane Keith",
                "category": 4,
                "summary": "Caused significant damage in Belize and Mexico."
            },
            {
                "name": "Hurricane Gordon",
                "category": 1,
                "summary": "Brought heavy rainfall and flooding to Florida."
            }
        ]
    },
    "2001": {
        "total_storms": 15,
        "hurricanes": 9,
        "major_hurricanes": 4,
        "notable_storms": [
            {
                "name": "Tropical Storm Allison",
                "category": "Tropical Storm",
                "summary": "Caused severe flooding in Texas; one of the costliest tropical storms."
            },
            {
                "name": "Hurricane Iris",
                "category": 4,
                "summary": "Struck Belize causing severe destruction."
            }
        ]
    },
    "2002": {
        "total_storms": 12,
        "hurricanes": 4,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Lili",
                "category": 4,
                "summary": "Made landfall in Louisiana causing significant damage."
            },
            {
                "name": "Tropical Storm Fay",
                "category": "Tropical Storm",
                "summary": "Brought heavy rains to Texas."
            }
        ]
    },
    "2003": {
        "total_storms": 16,
        "hurricanes": 7,
        "major_hurricanes": 3,
        "notable_storms": [
            {
                "name": "Hurricane Isabel",
                "category": 5,
                "summary": "Caused extensive damage in the Mid-Atlantic U.S."
            },
            {
                "name": "Hurricane Fabian",
                "category": 4,
                "summary": "Struck Bermuda causing significant damage."
            }
        ]
    },
    "2004": {
        "total_storms": 15,
        "hurricanes": 9,
        "major_hurricanes": 6,
        "notable_storms": [
            {
                "name": "Hurricane Charley",
                "category": 4,
                "summary": "Severely impacted Florida's Gulf Coast."
            },
            {
                "name": "Hurricane Ivan",
                "category": 5,
                "summary": "Caused widespread damage from the Caribbean to the U.S."
            },
            {
                "name": "Hurricane Jeanne",
                "category": 3,
                "summary": "Looped over the Atlantic before striking Florida."
            }
        ]
    },
    "2005": {
        "total_storms": 28,
        "hurricanes": 15,
        "major_hurricanes": 7,
        "notable_storms": [
            {
                "name": "Hurricane Katrina",
                "category": 5,
                "summary": "Devastated New Orleans and surrounding areas with catastrophic flooding."
            },
            {
                "name": "Hurricane Rita",
                "category": 5,
                "summary": "Struck the Texas-Louisiana border causing severe damage."
            },
            {
                "name": "Hurricane Wilma",
                "category": 5,
                "summary": "Strongest Atlantic hurricane by pressure; impacted Yucatán and South Florida."
            },
            {
                "name": "Hurricane Stan",
                "category": 1,
                "summary": "Caused deadly flooding and mudslides in Central America, especially Guatemala."
            }
        ]
    },
    "2006": {
        "total_storms": 10,
        "hurricanes": 5,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Ernesto",
                "category": 1,
                "summary": "Affected Haiti, Cuba, and the U.S. East Coast."
            },
            {
                "name": "Hurricane Gordon",
                "category": 3,
                "summary": "Remained mostly over open water; minimal land impact."
            }
        ]
    },
    "2007": {
        "total_storms": 15,
        "hurricanes": 6,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Dean",
                "category": 5,
                "summary": "Made landfall in Mexico; one of the strongest hurricanes to do so."
            },
            {
                "name": "Hurricane Felix",
                "category": 5,
                "summary": "Struck Nicaragua; rapid intensification noted."
            }
        ]
    },
    "2008": {
        "total_storms": 16,
        "hurricanes": 8,
        "major_hurricanes": 5,
        "notable_storms": [
            {
                "name": "Hurricane Gustav",
                "category": 4,
                "summary": "Caused significant damage in the Caribbean and U.S. Gulf Coast."
            },
            {
                "name": "Hurricane Ike",
                "category": 4,
                "summary": "Extensive damage in Texas and parts of the Caribbean."
            }
        ]
    },
    "2009": {
        "total_storms": 9,
        "hurricanes": 3,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Bill",
                "category": 4,
                "summary": "Large storm that remained mostly over open water."
            },
            {
                "name": "Tropical Storm Claudette",
                "category": "Tropical Storm",
                "summary": "Made landfall in the Florida Panhandle."
            }
        ]
    },
    "2010": {
        "total_storms": 19,
        "hurricanes": 12,
        "major_hurricanes": 5,
        "notable_storms": [
            {
                "name": "Hurricane Igor",
                "category": 4,
                "summary": "Affected Newfoundland and Bermuda."
            },
            {
                "name": "Hurricane Tomas",
                "category": 2,
                "summary": "Caused flooding and damage in the Caribbean."
            }
        ]
    },
    "2011": {
        "total_storms": 19,
        "hurricanes": 7,
        "major_hurricanes": 4,
        "notable_storms": [
            {
                "name": "Hurricane Irene",
                "category": 3,
                "summary": "Caused severe flooding and power outages from North Carolina to the northeastern U.S."
            },
            {
                "name": "Hurricane Katia",
                "category": 4,
                "summary": "A powerful Cape Verde hurricane that stayed mostly over open ocean."
            },
            {
                "name": "Hurricane Rina",
                "category": 3,
                "summary": "Briefly became a major hurricane near the Yucatán Peninsula."
            },
            {
                "name": "Tropical Storm Lee",
                "category": "Tropical Storm",
                "summary": "Caused extensive flooding in the Gulf Coast and the northeastern U.S."
            }
        ]
    },
    "2012": {
        "total_storms": 19,
        "hurricanes": 10,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Sandy",
                "category": 3,
                "summary": "Caused extensive damage across the Caribbean and the U.S. East Coast, particularly in New Jersey and New York."
            },
            {
                "name": "Hurricane Isaac",
                "category": 1,
                "summary": "Made landfall in Louisiana, causing significant flooding and power outages."
            }
        ]
    },
    "2013": {
        "total_storms": 14,
        "hurricanes": 2,
        "major_hurricanes": 0,
        "notable_storms": [
            {
                "name": "Tropical Storm Andrea",
                "category": "Tropical Storm",
                "summary": "Brought heavy rain and tornadoes to Florida and the Southeastern U.S."
            },
            {
                "name": "Hurricane Humberto",
                "category": 1,
                "summary": "Briefly reached hurricane strength; remained over the eastern Atlantic with minimal impact."
            }
        ]
    },
    "2014": {
        "total_storms": 8,
        "hurricanes": 6,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Arthur",
                "category": 2,
                "summary": "Made landfall in North Carolina, causing power outages and flooding during the Fourth of July holiday."
            },
            {
                "name": "Hurricane Gonzalo",
                "category": 4,
                "summary": "Struck Bermuda, causing widespread damage and power outages."
            }
        ]
    },
    "2015": {
        "total_storms": 11,
        "hurricanes": 4,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Joaquin",
                "category": 4,
                "summary": "Caused significant damage in the Bahamas and was associated with the sinking of the cargo ship El Faro."
            },
            {
                "name": "Tropical Storm Erika",
                "category": "Tropical Storm",
                "summary": "Caused deadly flooding and landslides in Dominica."
            }
        ]
    },
    "2016": {
        "total_storms": 15,
        "hurricanes": 7,
        "major_hurricanes": 4,
        "notable_storms": [
            {
                "name": "Hurricane Matthew",
                "category": 5,
                "summary": "Caused widespread destruction in Haiti, eastern Cuba, and the southeastern United States."
            },
            {
                "name": "Hurricane Hermine",
                "category": 1,
                "summary": "Made landfall in Florida, ending an 11-year hurricane landfall drought for the state."
            }
        ]
    },
    "2017": {
        "total_storms": 17,
        "hurricanes": 10,
        "major_hurricanes": 6,
        "notable_storms": [
            {
                "name": "Hurricane Harvey",
                "category": 4,
                "summary": "Brought catastrophic flooding to Texas, particularly the Houston area."
            },
            {
                "name": "Hurricane Irma",
                "category": 5,
                "summary": "Caused extensive damage across the Caribbean and Florida."
            },
            {
                "name": "Hurricane Maria",
                "category": 5,
                "summary": "Devastated Puerto Rico, causing a humanitarian crisis."
            }
        ]
    },
    "2018": {
        "total_storms": 15,
        "hurricanes": 8,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Florence",
                "category": 4,
                "summary": "Brought record-breaking rainfall and flooding to the Carolinas."
            },
            {
                "name": "Hurricane Michael",
                "category": 5,
                "summary": "Made landfall in the Florida Panhandle with catastrophic winds and storm surge."
            }
        ]
    },
    "2019": {
        "total_storms": 18,
        "hurricanes": 6,
        "major_hurricanes": 3,
        "notable_storms": [
            {
                "name": "Hurricane Dorian",
                "category": 5,
                "summary": "Devastated the Bahamas with record-breaking winds and storm surge."
            },
            {
                "name": "Tropical Storm Imelda",
                "category": "Tropical Storm",
                "summary": "Caused significant flooding in southeastern Texas."
            }
        ]
    },
    "2020": {
        "total_storms": 30,
        "hurricanes": 13,
        "major_hurricanes": 6,
        "notable_storms": [
            {
                "name": "Hurricane Laura",
                "category": 4,
                "summary": "Struck Louisiana with extreme winds and storm surge."
            },
            {
                "name": "Hurricane Eta",
                "category": 4,
                "summary": "Caused extensive damage in Central America due to heavy rainfall and flooding."
            },
            {
                "name": "Hurricane Iota",
                "category": 5,
                "summary": "Made landfall in Nicaragua, exacerbating the devastation caused by Eta just weeks earlier."
            }
        ]
    },
    "2021": {
        "total_storms": 21,
        "hurricanes": 7,
        "major_hurricanes": 4,
        "notable_storms": [
            {
                "name": "Hurricane Ida",
                "category": 4,
                "summary": "Caused severe damage in Louisiana and catastrophic flooding in the Northeastern U.S."
            },
            {
                "name": "Hurricane Elsa",
                "category": 1,
                "summary": "Affected the Caribbean and the southeastern United States."
            }
        ]
    },
    "2022": {
        "total_storms": 14,
        "hurricanes": 8,
        "major_hurricanes": 2,
        "notable_storms": [
            {
                "name": "Hurricane Fiona",
                "category": 4,
                "summary": "Caused widespread flooding in Puerto Rico and became a powerful storm in Atlantic Canada."
            },
            {
                "name": "Hurricane Ian",
                "category": 5,
                "summary": "One of Florida's most destructive storms; storm surge and wind devastated the Gulf Coast."
            }
        ]
    },
    "2023": {
        "total_storms": 20,
        "hurricanes": 7,
        "major_hurricanes": 3,
        "notable_storms": [
            {
                "name": "Hurricane Idalia",
                "category": 4,
                "summary": "Struck Florida's Big Bend region with powerful storm surge and flooding."
            },
            {
                "name": "Hurricane Lee",
                "category": 5,
                "summary": "Long-tracked major hurricane that impacted parts of the Northeast U.S. and Atlantic Canada."
            },
            {
                "name": "Hurricane Franklin",
                "category": 4,
                "summary": "Stayed offshore but became one of the strongest hurricanes of the season."
            }
        ]
    },
    "2024": {
        "total_storms": 17,
        "hurricanes": 9,
        "major_hurricanes": 4,
        "notable_storms": [
            {
                "name": "Hurricane Beryl",
                "category": 5,
                "summary": "Historic Category 5 hurricane in June; devastated parts of the Windward Islands."
            },
            {
                "name": "Hurricane Helene",
                "category": 4,
                "summary": "Powerful hurricane that struck Florida's Big Bend as a high-end Cat 4."
            },
            {
                "name": "Hurricane Milton",
                "category": 5,
                "summary": "Reached Category 5 intensity before making landfall in Florida at Cat 3."
            }
        ]
    }
}
 

 

# ---------------- Cyclone Data ---------------- #
cyclone_data = {
    "Hurricane Katrina (2005)": {
        "category": 5, "max_wind": 175, "min_pressure": 902, "landfall_cat": 3,
        "summary": "Catastrophic storm that flooded New Orleans and devastated the Gulf Coast.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Katrina#/media/File:Katrina_2005-08-28_1700Z.jpg",
        "track": [(23.1, -75.1), (24.5, -76.8), (26.1, -78.3), (27.8, -80.0), (29.5, -89.6)]
    },
    "Hurricane Wilma (2005)": {
        "category": 5, "max_wind": 185, "min_pressure": 882, "landfall_cat": 3,
        "summary": "Strongest Atlantic hurricane on record by pressure. Impacted Yucatán and Florida.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Wilma#/media/File:Wilma_2005-10-19_1345Z.png",
        "track": [(17.0, -79.0), (18.5, -82.0), (19.8, -84.0), (20.9, -86.5), (25.0, -80.0)]
    },
    "Hurricane Rita (2005)": {
        "category": 5, "max_wind": 180, "min_pressure": 895, "landfall_cat": 3,
        "summary": "Powerful Gulf storm following Katrina, landfall near Texas-Louisiana border.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Rita#/media/File:Rita_2005-09-21_1915Z.jpg",
        "track": [(21.5, -75.0), (23.0, -77.0), (24.7, -79.0), (26.5, -91.0), (29.7, -93.6)]
    },
    "Hurricane Isabel (2003)": {
        "category": 5, "max_wind": 165, "min_pressure": 915, "landfall_cat": 2,
        "summary": "Large landfalling hurricane in North Carolina.",
        "track": [(15.0, -45.0), (18.0, -52.0), (22.0, -60.0), (26.0, -68.0), (33.0, -76.5)]
    },
    "Hurricane Ivan (2004)": {
        "category": 5, "max_wind": 165, "min_pressure": 910, "landfall_cat": 3,
        "summary": "Major Gulf storm. Devastated Grenada and struck Alabama.",
        "track": [(10.2, -45.0), (12.5, -55.3), (15.0, -63.5), (20.0, -75.0), (28.0, -87.0)]
    },
    "Hurricane Dean (2007)": {
        "category": 5, "max_wind": 175, "min_pressure": 905, "landfall_cat": 5,
        "summary": "Yucatán landfall at Cat 5 intensity.",
        "track": [(12.0, -50.0), (14.5, -55.0), (16.0, -60.0), (18.0, -70.0), (20.5, -86.0)]
    },
    "Hurricane Irma (2017)": {
        "category": 5, "max_wind": 180, "min_pressure": 914, "landfall_cat": 4,
        "summary": "Destroyed parts of the northern Caribbean and Florida Keys.",
        "track": [(15.3, -50.2), (17.0, -60.5), (19.0, -65.0), (22.0, -72.0), (25.0, -80.0)]
    },
    "Hurricane Maria (2017)": {
        "category": 5, "max_wind": 175, "min_pressure": 908, "landfall_cat": 4,
        "summary": "Devastated Puerto Rico with prolonged outages and flooding.",
        "track": [(13.0, -56.0), (14.5, -60.0), (16.0, -63.0), (17.5, -66.5), (19.0, -69.0)]
    },
    "Hurricane Harvey (2017)": {
        "category": 4, "max_wind": 130, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Catastrophic flooding in Texas. One of the costliest U.S. hurricanes.",
        "track": [(18.0, -75.0), (22.0, -80.0), (25.0, -84.0), (27.5, -89.0), (28.9, -95.0)]
    },
    "Hurricane Michael (2018)": {
        "category": 5, "max_wind": 160, "min_pressure": 919, "landfall_cat": 5,
        "summary": "Destroyed parts of the Florida Panhandle.",
        "track": [(15.0, -75.0), (18.0, -80.0), (21.0, -83.0), (25.0, -85.0), (30.0, -86.5)]
    },
    "Hurricane Dorian (2019)": {
        "category": 5, "max_wind": 185, "min_pressure": 910, "landfall_cat": 1,
        "summary": "Stalled over Grand Bahama with catastrophic winds.",
        "track": [(21.0, -60.0), (23.5, -65.0), (25.0, -70.0), (26.5, -75.0), (27.0, -78.0)]
    },
    "Hurricane Laura (2020)": {
        "category": 4, "max_wind": 150, "min_pressure": 937, "landfall_cat": 4,
        "summary": "Major landfall in Louisiana with extreme wind damage.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Laura#/media/File:Laura_2020-08-26_2300Z.png",
        "track": [(18.0, -70.0), (21.0, -75.0), (24.0, -80.0), (26.5, -87.0), (29.8, -93.3)]
    },
    "Hurricane Ian (2022)": {
        "category": 5, "max_wind": 160, "min_pressure": 936, "landfall_cat": 4,
        "summary": "Devastated SW Florida with storm surge and flooding.",
        "track": [(15.0, -70.0), (17.5, -75.0), (20.0, -80.0), (24.0, -83.0), (26.5, -82.5)]
    },
    "Hurricane Fiona (2022)": {
        "category": 4, "max_wind": 130, "min_pressure": 931, "landfall_cat": 3,
        "summary": "Flooding in Puerto Rico and damage across Atlantic Canada.",
        "track": [(15.5, -52.0), (17.5, -56.0), (19.0, -60.0), (21.0, -65.0), (23.0, -68.0)]
    },
    "Hurricane Sandy (2012)": {
        "category": 3, "max_wind": 115, "min_pressure": 940, "landfall_cat": 1,
        "summary": "Massive hybrid cyclone. Northeast U.S. impact.",
        "track": [(15.0, -75.0), (18.0, -76.0), (22.0, -74.0), (27.0, -71.0), (35.0, -74.0)]
    },
    "Hurricane Helene (2024)": {
        "category": 4, "max_wind": 140, "min_pressure": 920, "landfall_cat": 4,
        "summary": "Struck Florida’s Big Bend region as a powerful Cat 4.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Helene#/media/File:Helene_2024-09-27_0146Z.jpg",
        "track": [(18.0, -58.0), (20.0, -60.0), (23.0, -63.0), (25.5, -67.0), (29.0, -83.5)]
    },
    "Hurricane Milton (2024)": {
        "category": 5, "max_wind": 180, "min_pressure": 897, "landfall_cat": 3,
        "summary": "Peaked at Category 5 before making landfall near Siesta Key, Florida.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Milton#/media/File:Milton_2024-10-07_1920Z.jpg",
        "track": [(18.5, -70.0), (21.0, -72.5), (23.5, -75.0), (25.8, -78.0), (27.3, -82.5)]
    },
    "Hurricane Beryl (2024)": {
        "category": 5, "max_wind": 165, "min_pressure": 926, "landfall_cat": 4,
        "summary": "Historic Category 5 hurricane in June, devastated parts of the Windward Islands.",
        "storm_image_url": "https://en.wikipedia.org/wiki/Hurricane_Beryl#/media/File:Beryl_2024-07-02_1230Z.jpg",
        "track": [(11.5, -52.0), (12.8, -55.0), (14.2, -58.0), (15.5, -61.0), (16.8, -64.0)]
    }
}
def get_goes_sector(lat, lon):
    if -100 <= lon <= -40 and 0 <= lat <= 50:
        return "taw"  # Tropical Atlantic West
    elif -90 <= lon <= -60 and 10 <= lat <= 35:
        return "gm"   # Gulf of America
    elif -75 <= lon <= -55 and 10 <= lat <= 25:
        return "car"  # Caribbean
    elif -140 <= lon <= -100:
        return "ep"   # East Pacific
    else:
        return "gm"   # Default to Gulf


# ---------------- App Layout ---------------- #
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
mode = st.selectbox("Choose a mode:", ["Explore One Cyclone", "Compare Two Cyclones", "Explore Hurricane Seasons"])

# ---------------- EXPLORE ONE ---------------- #
if mode == "Explore One Cyclone":
    st.header("🌀 Explore One Cyclone")

    cyclone_options = ["Select Cyclone"] + list(cyclone_data.keys())
    selected = st.selectbox("Select a Cyclone", cyclone_options)

    if selected != "Select Cyclone":
        data = cyclone_data[selected]
       # --- Cyclone Image and Name ---
        col_img, col_title = st.columns([1, 3])
        
        with col_img:
            if "storm_image_url" in data:
                st.image(data["storm_image_url"], caption="Satellite View", use_container_width=True)
            else:
                st.markdown("🖼️ *Image Not Available*")
        
        with col_title:
            st.subheader(selected)
            st.markdown(f"**Summary:** {data['summary']}")
            st.markdown(f"**Category:** {data['category']}  |  **Max Wind:** {data['max_wind']} mph  |  **Min Pressure:** {data['min_pressure']} mb  |  **Landfall Cat:** {data['landfall_cat']}")

        st.markdown("### 🌀 Cyclone Structure & Track")
        
        col_map1, col_map2 = st.columns(2)
        
        with col_map1:
            st.markdown("**Wind Field Rings**")
            if "track" in data:
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
            else:
                st.info("Wind field visualization not available for this cyclone.")
        
        with col_map2:
            st.markdown("**Track Map**")
            if "track" in data:
                m2 = folium.Map(location=data['track'][0], zoom_start=5, tiles='cartodbpositron')
                folium.PolyLine(data['track'], color="blue").add_to(m2)
                folium.Marker(data['track'][0], popup="Start").add_to(m2)
                folium.Marker(data['track'][-1], popup="End").add_to(m2)
                st_folium(m2, width=350, height=350)
            else:
                st.info("Track data not available for this cyclone.")
        


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
        if "track" in data:
            lat, lon = data["track"][-1]
            sector = get_goes_sector(lat, lon)
    
        st.markdown("### 🛰️ Satellite Loops")
        sat_type = st.selectbox("Satellite Type", ["Infrared", "Visible", "Water Vapor"])
    
        channel_map = {
            "Infrared": "13",
            "Visible": "02",
            "Water Vapor": "09"
        }
    
        channel = channel_map[sat_type]
        url = f"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/{sector}/{channel}/GOES16-{sector.upper()}-{channel}-900x540.gif"
    
        st.image(url, caption=f"{sat_type} Satellite Loop", use_container_width=True)


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
        st.markdown("### 🌬️ Wind Field Rings")
        col_wind1, col_wind2 = st.columns(2)
        
        with col_wind1:
            st.markdown(f"**{storm_a}**")
            if "track" in data_a:
                m_wind1 = folium.Map(location=data_a['track'][-1], zoom_start=6, tiles='cartodbpositron')
                folium.CircleMarker(
                    location=data_a['track'][-1],
                    radius=8,
                    popup=f"Eye: {data_a['min_pressure']} mb, {data_a['max_wind']} mph",
                    color="black",
                    fill=True
                ).add_to(m_wind1)
                folium.Circle(location=data_a['track'][-1], radius=60000, color="orange", fill=False, popup="34 kt Wind Radius").add_to(m_wind1)
                folium.Circle(location=data_a['track'][-1], radius=40000, color="red", fill=False, popup="50 kt Wind Radius").add_to(m_wind1)
                folium.Circle(location=data_a['track'][-1], radius=25000, color="darkred", fill=False, popup="64 kt Wind Radius").add_to(m_wind1)
                st_folium(m_wind1, width=350, height=350)
            else:
                st.info("Wind field visualization not available for this cyclone.")
        
        with col_wind2:
            st.markdown(f"**{storm_b}**")
            if "track" in data_b:
                m_wind2 = folium.Map(location=data_b['track'][-1], zoom_start=6, tiles='cartodbpositron')
                folium.CircleMarker(
                    location=data_b['track'][-1],
                    radius=8,
                    popup=f"Eye: {data_b['min_pressure']} mb, {data_b['max_wind']} mph",
                    color="black",
                    fill=True
                ).add_to(m_wind2)
                folium.Circle(location=data_b['track'][-1], radius=60000, color="orange", fill=False, popup="34 kt Wind Radius").add_to(m_wind2)
                folium.Circle(location=data_b['track'][-1], radius=40000, color="red", fill=False, popup="50 kt Wind Radius").add_to(m_wind2)
                folium.Circle(location=data_b['track'][-1], radius=25000, color="darkred", fill=False, popup="64 kt Wind Radius").add_to(m_wind2)
                st_folium(m_wind2, width=350, height=350)
            else:
                st.info("Wind field visualization not available for this cyclone.")
        

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
        # --- Satellite Viewer ---
        if "track" in data:
            lat, lon = data["track"][-1]
            sector = get_goes_sector(lat, lon)
        
            st.markdown("### 🛰️ Satellite Loops")
            sat_type = st.selectbox("Satellite Type", ["Infrared", "Visible", "Water Vapor"])
        
            channel_map = {
                "Infrared": "13",
                "Visible": "02",
                "Water Vapor": "09"
            }
        
            channel = channel_map[sat_type]
            url = f"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/{sector}/{channel}/GOES16-{sector.upper()}-{channel}-900x540.gif"
        
            st.image(url, caption=f"{sat_type} Satellite Loop", use_container_width=True)
        else:
            st.info("Satellite visualization not available for this cyclone.")

            
if mode == "Explore Hurricane Seasons":
    st.header("🌊 Explore Hurricane Seasons")

    # Dropdown to select a season
    season_options = ["Select Season"] + [str(year) for year in range(2000, 2025)]
    selected_season = st.selectbox("Select a Season", season_options, index=0)

    if selected_season != "Select Season":
        data = season_data[selected_season]

        # Display season statistics
        st.markdown(f"## {selected_season} Hurricane Season")
        st.markdown(f"**Total Named Storms:** {data['total_storms']}")
        st.markdown(f"**Hurricanes:** {data['hurricanes']}")
        st.markdown(f"**Major Hurricanes:** {data['major_hurricanes']}")

        # Display notable storms
        st.markdown("### Notable Storms")
        for storm in data['notable_storms']:
            st.markdown(f"**{storm['name']}** (Category {storm['category']}): {storm['summary']}")

