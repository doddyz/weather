# Add branch to test daily temperatures feature, papier crayon 1st
# Always minify code before moving on next feature/fix
# Papier crayon pour cleanup code et minifier la duplication inutile de code répété
# Formattage temperatures en entiers avec symbole degré
# Ajouter séléction de ville avec choix de ville par défaut parmis une liste prédéfinie (voir comment permettre séléction simple de villes)


import streamlit as st
import requests
from weather import *


st.set_page_config(
     page_title='Weather App',
     page_icon=':sunshine:',
     layout='wide',
     initial_sidebar_state='collapsed',
 )


st.title('Weather App')

options_sidebar = st.sidebar

with options_sidebar:
    app_lang = st.selectbox('Display lang', ('en', 'fr', 'es'))
    st.markdown('---')
    country = st.selectbox('Countries', COUNTRIES.keys())
    city = st.selectbox('Cities', COUNTRIES[country])
    
    
city_coordinates = get_geo_coordinates(city, country)
call_url = open_weather_api_call(*city_coordinates, lang=app_lang)
r = requests.get(call_url)
r_json = r.json()


cols = st.columns(8)
for i in range(0, 8):
    with cols[i]:
        daily_weather_col_data(r_json, i + 1)







