# Add temperature degree symbol to all shown temperatures
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


# st.write(get_hourly_weather_forecast_data(r_json))

df = get_hourly_weather_forecast_data_as_df(r_json)

# df

# df.to_csv('export.csv')


cols = st.columns(8)
for i in range(0, 8):
    with cols[i]:
        daily_weather_col_data(r_json, i + 1)

st.markdown('---')

st.altair_chart(draw_hourly_temp_chart(df), use_container_width=True)

st.altair_chart(draw_hourly_precipitation_proba_chart(df), use_container_width=True)

# st.bar_chart(df[['pop']])






