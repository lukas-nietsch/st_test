import streamlit as st
import folium
# Create a Folium map
m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)
 
# Display the map in Streamlit
st.pydeck_chart(m)
