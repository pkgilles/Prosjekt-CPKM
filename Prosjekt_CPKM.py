import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load the restaurant data
# Breddegrad = latitude, Lengdegrad = longitude
restaurants = [
    {'Restaurant': 'Maaemo', 'Stjerner': 3, 'Breddegrad': 59.907647183418746, 'Lengdegrad': 10.75813998319409, 'Besøk': 2, 'Sum stjerner': 6},
    {'Restaurant': 'Renaa', 'Stjerner': 2, 'Breddegrad': 58.97396191894673, 'Lengdegrad': 5.731084322652034, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Sketch', 'Stjerner': 2, 'Breddegrad': 51.512721702120295, 'Lengdegrad': -0.14144440934666339, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Kontrast', 'Stjerner': 2, 'Breddegrad': 59.922982017962504, 'Lengdegrad': 10.751167162303334, 'Besøk': 2, 'Sum stjerner': 3},
    {'Restaurant': 'Chapter One', 'Stjerner': 1, 'Breddegrad': 53.354313, 'Lengdegrad': -6.2641001, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Middag Paris', 'Stjerner': 1, 'Breddegrad': 48.86580095415907, 'Lengdegrad': 2.3196169323413423, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Il Gallo D\'oro', 'Stjerner': 1, 'Breddegrad': 32.63850818472831, 'Lengdegrad': -16.926428884070905, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Restaurant Opus', 'Stjerner': 1, 'Breddegrad': 48.20143884034287, 'Lengdegrad': 16.372871288311156, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Disfrutar', 'Stjerner': 2, 'Breddegrad': 41.38782363695626, 'Lengdegrad': 2.153204200226883, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Alma', 'Stjerner': 2, 'Breddegrad': 38.71047126916178, 'Lengdegrad': -9.141003188669877, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Loco', 'Stjerner': 1, 'Breddegrad': 38.712692233153376, 'Lengdegrad': -9.160627528960182, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Birdland', 'Stjerner': 1, 'Breddegrad': 35.67298943958676, 'Lengdegrad': 139.76381215596643, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Fagn', 'Stjerner': 1, 'Breddegrad': 63.434117339663665, 'Lengdegrad': 10.396440642846406, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Statholdergaarden', 'Stjerner': 1, 'Breddegrad': 59.909576312764315, 'Lengdegrad': 10.743158646936871, 'Besøk': 2, 'Sum stjerner': 2},
    {'Restaurant': 'La Degustation', 'Stjerner': 1, 'Breddegrad': 50.091098220934434, 'Lengdegrad': 14.425738457129478, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Adam/Albin', 'Stjerner': 1, 'Breddegrad': 59.34310282115162, 'Lengdegrad': 18.066249963979196, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Hyde', 'Stjerner': 1, 'Breddegrad': 59.919678614026225, 'Lengdegrad': 10.748774540864886, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Mon Oncle', 'Stjerner': 1, 'Breddegrad': 59.91716932299051, 'Lengdegrad': 10.738994821796187, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Ola (Martin Berasategui)', 'Stjerner': 1, 'Breddegrad': 43.25810595552674, 'Lengdegrad': -2.926402002033818, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Hakkasan Mayfair', 'Stjerner': 1, 'Breddegrad': 51.51040318279479, 'Lengdegrad': -0.14501570176840065, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Da Terra', 'Stjerner': 2, 'Breddegrad': 51.53058708267891, 'Lengdegrad': -0.05591802875661535, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'formel B', 'Stjerner': 1, 'Breddegrad': 55.67091959080128, 'Lengdegrad': 12.535634144400204, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Casona del Judio', 'Stjerner': 1, 'Breddegrad': 43.46875599502872, 'Lengdegrad': -3.828884023477654, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Arzak', 'Stjerner': 3, 'Breddegrad': 43.321816318381906, 'Lengdegrad': -1.9492931443615904, 'Besøk': 1, 'Sum stjerner': 3},
    {'Restaurant': 'Savage', 'Stjerner': 1, 'Breddegrad': 59.90965741447051, 'Lengdegrad': 10.740274627370074, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Finnjävel Salonki', 'Stjerner': 1, 'Breddegrad': 60.17210936992626, 'Lengdegrad': 24.932450651381274, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Kitchen Table', 'Stjerner': 2, 'Breddegrad': 51.52051886488125, 'Lengdegrad': -0.13604940418496586, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Casa de Chá de Boa Nova', 'Stjerner': 2, 'Breddegrad': 41.203092957202905, 'Lengdegrad': -8.714882495958829, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Belcanto', 'Stjerner': 2, 'Breddegrad': 38.71025006629505, 'Lengdegrad': -9.141476330999446, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Jatak', 'Stjerner': 1, 'Breddegrad': 55.6871699325071, 'Lengdegrad': 12.548033871389647, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Ricard Camarena', 'Stjerner': 2, 'Breddegrad': 39.48578556565042, 'Lengdegrad': -0.38364874472450533, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Yugen', 'Stjerner': 2, 'Breddegrad': 34.66494703388733, 'Lengdegrad': 135.52174529818703, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Velrosier', 'Stjerner': 1, 'Breddegrad': 35.0026325147605, 'Lengdegrad': 135.76882619820134, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'Florilege', 'Stjerner': 2, 'Breddegrad': 35.66174874281927, 'Lengdegrad': 139.74353242706522, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'Restaurant 212', 'Stjerner': 2, 'Breddegrad': 52.365882, 'Lengdegrad': 4.900279, 'Besøk': 1, 'Sum stjerner': 2},
    {'Restaurant': 'À L\'aise', 'Stjerner': 1, 'Breddegrad': 59.929166, 'Lengdegrad': 10.709721, 'Besøk': 1, 'Sum stjerner': 1},
    {'Restaurant': 'La Scène', 'Stjerner': 2, 'Breddegrad': 48.872063, 'Lengdegrad': 2.314564, 'Besøk': 1, 'Sum stjerner': 2},
]

data = pd.DataFrame(restaurants)

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
m = folium.Map(location=[60, 40], zoom_start=4, tiles="CartoDB dark_matter")

# Define the color to match the filter boxes
marker_color = "#1abc9c"  # Same as the primary color in config.toml

# Add a marker for each restaurant in the filtered data
for idx, row in filtered_data.iterrows():
    popup_content = f"""
    <div style="width: 250px; font-size: 16px; background-color: #333333; color: #e0e0e0; padding: 10px; border-radius: 5px;">
        <strong>{row['Restaurant']}</strong><br>
        Stjerner: {row['Stjerner']}<br>
        Besøk: {row['Besøk']}<br>
        Totalt: {row['Sum stjerner']}
    </div>
    """
    folium.Marker(
        location=[row['Breddegrad'], row['Lengdegrad']],
        popup=folium.Popup(popup_content, max_width=300),
        icon=folium.Icon(icon="star", icon_color=marker_color, color="white", prefix="fa")  # Green star icon
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=1450)

# Display summary statistics below the map
total_restaurants = filtered_data.shape[0]
total_stars = filtered_data['Sum stjerner'].sum()
total_unique_stars = filtered_data['Stjerner'].sum()
total_visits = filtered_data['Besøk'].sum()

st.write("### Oppsummering:")
st.write(f"Antall restauranter besøkt: {total_restaurants}")
st.write(f"Totalt antall stjerner: {total_stars}")
st.write(f"Totalt unike stjerner: {total_unique_stars}")
st.write(f"Totalt besøk: {total_visits}")
