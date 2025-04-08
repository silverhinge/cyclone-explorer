import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------- COMPARISON MODE -------------------- #
if mode == "Compare Two Cyclones":
    st.header("🌪️ Storm Comparison Mode")

    col_pick = st.columns(2)
    with col_pick[0]:
        storm_a = st.selectbox("Select Storm A", list(cyclone_data.keys()), key="a")
    with col_pick[1]:
        storm_b = st.selectbox("Select Storm B", list(cyclone_data.keys()), key="b")

    data_a = cyclone_data[storm_a]
    data_b = cyclone_data[storm_b]

    # ---------- STAT COMPARISON TABLE ---------- #
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

    # ---------- STRUCTURE VISUALS ---------- #
    st.markdown("### 📉 Central Pressure Evolution")
    col1, col2 = st.columns(2)

    with col1:
        hours = np.arange(0, 96, 6)
        pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data_a['category'] * 20 + 10))
        fig1, ax1 = plt.subplots()
        ax1.plot(hours, pressure, color='blue')
        ax1.set_title(f"{storm_a} Pressure")
        ax1.set_xlabel("Hours Since Formation")
        ax1.set_ylabel("Pressure (mb)")
        ax1.invert_yaxis()
        ax1.grid(True)
        st.pyplot(fig1)

    with col2:
        pressure = 1010 - (np.sin(hours / 96 * np.pi) * (data_b['category'] * 20 + 10))
        fig2, ax2 = plt.subplots()
        ax2.plot(hours, pressure, color='darkred')
        ax2.set_title(f"{storm_b} Pressure")
        ax2.set_xlabel("Hours Since Formation")
        ax2.set_ylabel("Pressure (mb)")
        ax2.invert_yaxis()
        ax2.grid(True)
        st.pyplot(fig2)

    st.markdown("### 🌬️ Wind Field Cross-Section")
    col3, col4 = st.columns(2)

    with col3:
        radii = np.linspace(0, 200, 200)
        winds = data_a['max_wind'] * np.exp(-radii / 50)
        fig3, ax3 = plt.subplots()
        ax3.plot(radii, winds, color='orange')
        ax3.set_title(f"{storm_a} Wind Field")
        ax3.set_xlabel("Distance from Eye (km)")
        ax3.set_ylabel("Wind Speed (mph)")
        st.pyplot(fig3)

    with col4:
        winds = data_b['max_wind'] * np.exp(-radii / 50)
        fig4, ax4 = plt.subplots()
        ax4.plot(radii, winds, color='purple')
        ax4.set_title(f"{storm_b} Wind Field")
        ax4.set_xlabel("Distance from Eye (km)")
        ax4.set_ylabel("Wind Speed (mph)")
        st.pyplot(fig4)

    st.markdown("### 🌧️ Rainband Schematic (Simplified)")
    col5, col6 = st.columns(2)
    theta = np.linspace(0, 2 * np.pi, 300)

    with col5:
        radii_a = [40, 80, 120, 160]
        fig5, ax5 = plt.subplots()
        for r in radii_a:
            ax5.plot(r * np.cos(theta), r * np.sin(theta), alpha=0.6)
        ax5.set_title(f"{storm_a} Rainbands")
        ax5.set_aspect("equal")
        ax5.axis('off')
        st.pyplot(fig5)

    with col6:
        radii_b = [40, 80, 120, 160]
        fig6, ax6 = plt.subplots()
        for r in radii_b:
            ax6.plot(r * np.cos(theta), r * np.sin(theta), alpha=0.6)
        ax6.set_title(f"{storm_b} Rainbands")
        ax6.set_aspect("equal")
        ax6.axis('off')
        st.pyplot(fig6)

# -------------------- DEFAULT SINGLE STORM EXPLORER -------------------- #
else:
    st.info("Use the mode selector to explore a single cyclone. Full interactive explorer to be restored below this section.")
