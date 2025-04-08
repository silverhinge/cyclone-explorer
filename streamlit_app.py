import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Page setup
st.set_page_config(page_title="Cyclone Explorer", layout="wide")
st.title("🌀 Cyclone Explorer")
st.markdown("Visualize stylized hurricane structures — cartoon-style storm anatomy.")

# Dropdown
storm = st.selectbox(
    "Select a cyclone:",
    [
        "Hurricane Helene (2024)",
        "Hurricane Milton (2024) - coming soon",
        "Tropical Storm Beryl (2024) - coming soon"
    ]
)

# ---------------------- HELENE - CARTOON DIAGRAM ---------------------- #
if storm == "Hurricane Helene (2024)":
    st.subheader("🎨 Cartoon Diagram: Hurricane Helene")

    st.markdown("""
    This stylized diagram shows the structure of Hurricane Helene at peak intensity.  
    Each ring and spiral represents a key part of the storm — the eye, eyewall, and outer rainbands.
    """)

    # Generate spiral storm structure
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_facecolor("black")

    # Eye
    eye = Circle((0, 0), 5, color="gold", label="Eye")
    ax.add_patch(eye)

    # Eyewall
    for r in np.linspace(7, 10, 5):
        theta = np.linspace(0, 2 * np.pi, 500)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot(x, y, color="darkred", linewidth=2, alpha=0.7)

    # Rainbands as spirals
    for i in range(3):
        theta = np.linspace(0, 4 * np.pi, 1000)
        r = 12 + i * 5 + theta * 0.5
        x = r * np.cos(theta + i * np.pi/3)
        y = r * np.sin(theta + i * np.pi/3)
        ax.plot(x, y, color="skyblue", linewidth=1.5, alpha=0.4)

    # Outer wind field
    outer_rings = [30, 50, 70]
    ring_colors = ["#3355ff", "#2244cc", "#112288"]
    labels = ["Outer Rainband", "Mid Rainband", "Peripheral Winds"]
    for radius, color in zip(outer_rings, ring_colors):
        ring = Circle((0, 0), radius, fill=False, color=color, linewidth=1, linestyle='--', alpha=0.3)
        ax.add_patch(ring)

    # Label zones
    ax.text(0, 0, "👁️", fontsize=18, ha='center', va='center', color="black")
    ax.text(0, -12, "Eyewall", color="white", fontsize=10, ha='center')
    ax.text(0, -40, "Rainbands", color="skyblue", fontsize=10, ha='center')
    ax.text(0, -65, "Wind Field", color="lightgray", fontsize=10, ha='center')

    ax.set_xlim(-80, 80)
    ax.set_ylim(-80, 80)
    ax.axis('off')
    st.pyplot(fig)

    st.info("🌀 Hurricane Helene was a Category 4 hurricane at peak. This graphic is a schematic — not satellite data — but modeled after observed structure.")

# ---------------------- PLACEHOLDERS ---------------------- #
else:
    st.warning("This cyclone’s diagram is coming soon!")
