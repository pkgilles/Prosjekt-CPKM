import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load the restaurant data

restaurants = [
    {'Restaurant': 'Maaemo', 'Stjerner': 3, 'Lengdegrad': 59.907647183418746, 'Breddegrad': 10.75813998319409},
    {'Restaurant': 'Renaa', 'Stjerner': 2, 'Lengdegrad': 58.97396191894673, 'Breddegrad': 5.731084322652034},
    {'Restaurant': 'Sketch', 'Stjerner': 2, 'Lengdegrad': 51.512721702120295, 'Breddegrad': -0.14144440934666339},
    {'Restaurant': 'Kontrast', 'Stjerner': 1, 'Lengdegrad': 59.922982017962504, 'Breddegrad': 10.751167162303334},
    {'Restaurant': 'Chapter One', 'Stjerner': 1, 'Lengdegrad': 53.354313, 'Breddegrad': -6.2641001},
    {'Restaurant': 'Middag Paris', 'Stjerner': 1, 'Lengdegrad': 48.86580095415907, 'Breddegrad': 2.3196169323413423},
    {'Restaurant': 'Il Gallo D\'oro', 'Stjerner': 1, 'Lengdegrad': 32.63850818472831, 'Breddegrad': -16.926428884070905},
    {'Restaurant': 'Restaurant Opus', 'Stjerner': 1, 'Lengdegrad': 48.20143884034287, 'Breddegrad': 16.372871288311156},
    {'Restaurant': 'Disfrutar', 'Stjerner': 2, 'Lengdegrad': 41.38782363695626, 'Breddegrad': 2.153204200226883},
    {'Restaurant': 'Alma', 'Stjerner': 2, 'Lengdegrad': 38.71047126916178, 'Breddegrad': -9.141003188669877},
    {'Restaurant': 'Loco', 'Stjerner': 1, 'Lengdegrad': 38.712692233153376, 'Breddegrad': -9.160627528960182},
    {'Restaurant': 'Birdland', 'Stjerner': 1, 'Lengdegrad': 35.67298943958676, 'Breddegrad': 139.76381215596643},
    {'Restaurant': 'Fagn', 'Stjerner': 1, 'Lengdegrad': 63.434117339663665, 'Breddegrad': 10.396440642846406},
    {'Restaurant': 'Statholdergaarden', 'Stjerner': 1, 'Lengdegrad': 59.909576312764315, 'Breddegrad': 10.743158646936871},
    {'Restaurant': 'La Degustation', 'Stjerner': 1, 'Lengdegrad': 50.091098220934434, 'Breddegrad': 14.425738457129478},
    {'Restaurant': 'Adam/Albin', 'Stjerner': 1, 'Lengdegrad': 59.34310282115162, 'Breddegrad': 18.066249963979196},
    {'Restaurant': 'Hyde', 'Stjerner': 1, 'Lengdegrad': 59.919678614026225, 'Breddegrad': 10.748774540864886},
    {'Restaurant': 'Mon Oncle', 'Stjerner': 1, 'Lengdegrad': 59.91716932299051, 'Breddegrad': 10.738994821796187},
    {'Restaurant': 'Ola (Martin Berasategui)', 'Stjerner': 1, 'Lengdegrad': 43.25810595552674, 'Breddegrad': -2.926402002033818},
    {'Restaurant': 'Hakkasan Mayfair', 'Stjerner': 1, 'Lengdegrad': 51.51040318279479, 'Breddegrad': -0.14501570176840065},
    {'Restaurant': 'Da Terra', 'Stjerner': 2, 'Lengdegrad': 51.53058708267891, 'Breddegrad': -0.05591802875661535},
    {'Restaurant': 'formel B', 'Stjerner': 1, 'Lengdegrad': 55.67091959080128, 'Breddegrad': 12.535634144400204},
    {'Restaurant': 'Casona del Judio', 'Stjerner': 1, 'Lengdegrad': 43.46875599502872, 'Breddegrad': -3.828884023477654},
    {'Restaurant': 'Arzak', 'Stjerner': 3, 'Lengdegrad': 43.321816318381906, 'Breddegrad': -1.9492931443615904},
    {'Restaurant': 'Savage', 'Stjerner': 1, 'Lengdegrad': 59.90965741447051, 'Breddegrad': 10.740274627370074},
    {'Restaurant': 'Finnjävel Salonki', 'Stjerner': 1, 'Lengdegrad': 60.17210936992626, 'Breddegrad': 24.932450651381274},
    {'Restaurant': 'Kitchen Table', 'Stjerner': 2, 'Lengdegrad': 51.52051886488125, 'Breddegrad': -0.13604940418496586},
    {'Restaurant': 'Casa de Chá de Boa Nova', 'Stjerner': 2, 'Lengdegrad': 41.203092957202905, 'Breddegrad': -8.714882495958829},
    {'Restaurant': 'Belcanto', 'Stjerner': 2, 'Lengdegrad': 38.71025006629505, 'Breddegrad': -9.141476330999446},
    {'Restaurant': 'Jatak', 'Stjerner': 1, 'Lengdegrad': 55.6871699325071, 'Breddegrad': 12.548033871389647}
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