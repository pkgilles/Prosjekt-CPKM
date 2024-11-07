import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load the restaurant data
data = pd.read_csv(r'C:\Python\Restliste.csv', sep=';', index_col=False)

# Set up the Streamlit app
st.markdown("<h1 style='text-align: center;'>Christina og Per Kristians Michelin-reise</h1>", unsafe_allow_html=True)
st.write("Her er alle restaurantene vi har besøkt:")

# Filter selection for star ratings
stjernevalg = st.multiselect(
    "Velg antall stjerner for restauranter å vise:",
    options=[1, 2, 3],
    default=[1, 2, 3]
)

# Filter data based on selected star ratings
filtered_data = data[data['Stjerner'].isin(stjernevalg)]

# Create a folium map centered over Europe with a dark theme
m = folium.Map(location=[54.5260, 15.2551], zoom_start=4, tiles="CartoDB dark_matter")

# Define the color to match the filter boxes
marker_color = "#1abc9c"  # Same as the primary color in config.toml

# Add a marker for each restaurant in the filtered data
for idx, row in filtered_data.iterrows():
    popup_content = f"""
    <div style="width: 250px; font-size: 16px; background-color: #333333; color: #e0e0e0; padding: 10px; border-radius: 5px;">
        <strong>{row['Restaurant']}</strong><br>
        Stjerner: {row['Stjerner']}
    </div>
    """
    
    folium.Marker(
        location=[row['Lengdegrad'], row['Breddegrad']],
        popup=folium.Popup(popup_content, max_width=300),
        icon=folium.Icon(icon="star", icon_color=marker_color, color="white", prefix="fa")  # Green star icon
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=1450)

# Display summary statistics below the map
total_restaurants = filtered_data.shape[0]
total_stars = filtered_data['Stjerner'].sum()

st.write("### Oppsummering:")
st.write(f"Antall restauranter besøkt: {total_restaurants}")
st.write(f"Totalt antall stjerner: {total_stars}")