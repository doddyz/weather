# Papier crayon pour cleanup code et minifier la duplication inutile de code répété
# Ajouter séléction de ville avec choix de ville par défaut parmis une liste prédéfinie (voir comment permettre séléction simple de villes)
# Formattage temperatures en entiers avec symbole degré

import streamlit as st
import requests
from weather import *


st.set_page_config(
     page_title='Weather App',
     page_icon=':sunshine:',
     layout='wide',
     initial_sidebar_state='expanded',
 )


st.title('Weather App')

call_url = open_weather_api_call('London')
r = requests.get(call_url)
r_json = r.json()

# st.write(r_json)

current_weather_metrics = get_current_weather_metrics(r_json)
current_weather_temp = current_weather_metrics['temp']
current_weather_wind_speed = current_weather_metrics['wind_speed']

current_weather_description = get_current_weather_description(r_json)
current_weather_icon = current_weather_description['icon']
current_weather_main = current_weather_description['main']
current_weather_description = current_weather_description['description']

# daily_forecast_weather_data = get_daily_weather_forecast_data(r_json)
forecast_weather_data_1 = get_daily_weather_forecast_data_for_day_n(r_json, 1)
forecast_weather_data_2 = get_daily_weather_forecast_data_for_day_n(r_json, 2)
forecast_weather_data_3 = get_daily_weather_forecast_data_for_day_n(r_json, 3)
forecast_weather_data_4 = get_daily_weather_forecast_data_for_day_n(r_json, 4)
forecast_weather_data_5 = get_daily_weather_forecast_data_for_day_n(r_json, 5)
forecast_weather_data_6 = get_daily_weather_forecast_data_for_day_n(r_json, 6)
forecast_weather_data_7 = get_daily_weather_forecast_data_for_day_n(r_json, 7)
forecast_weather_data_8 = get_daily_weather_forecast_data_for_day_n(r_json, 8)

# Current Weather here
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.image(get_weather_icon_url(current_weather_icon))
#     st.subheader(current_weather_description)
#     # st.subheader(current_weather_main)
    
# with col2:
#     st.metric('Temperature', current_weather_temp)

# with col3:
#     st.metric('Wind Speed', current_weather_wind_speed)


col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
# col1, col2, col3 = st.columns(3)

with col1:
    # Need day of week here
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_1['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_1['icon']))
    st.caption(forecast_weather_data_1['description'])
    st.metric('Min', forecast_weather_data_1['min_temp'])
    st.metric('Max', forecast_weather_data_1['max_temp'])

    
with col2:
    # Need day of week here
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_2['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_2['icon']))
    st.caption(forecast_weather_data_2['description'])
    st.metric('Min', forecast_weather_data_2['min_temp'])
    st.metric('Max', forecast_weather_data_2['max_temp'])


with col3:
    # Need day of week here
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_3['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_3['icon']))
    st.caption(forecast_weather_data_3['description'])
    st.metric('Min', forecast_weather_data_3['min_temp'])
    st.metric('Max', forecast_weather_data_3['max_temp'])


with col4:
    # Need day of week here
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_4['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_4['icon']))
    st.caption(forecast_weather_data_4['description'])
    st.metric('Min', forecast_weather_data_4['min_temp'])
    st.metric('Max', forecast_weather_data_4['max_temp'])


with col5:
    # Need day of week here
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_5['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_5['icon']))
    st.caption(forecast_weather_data_3['description'])
    st.metric('Min', forecast_weather_data_3['min_temp'])
    st.metric('Max', forecast_weather_data_3['max_temp'])


with col6:
    # Need day of week here
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_6['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_6['icon']))
    st.caption(forecast_weather_data_6['description'])
    st.metric('Min', forecast_weather_data_6['min_temp'])
    st.metric('Max', forecast_weather_data_6['max_temp'])


with col7:
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_7['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_7['icon']))
    st.caption(forecast_weather_data_7['description'])
    st.metric('Min', forecast_weather_data_7['min_temp'])
    st.metric('Max', forecast_weather_data_7['max_temp'])


with col8:
    st.subheader(get_day_of_week_from_ts(int(forecast_weather_data_8['dt'])))
    st.image(get_weather_icon_url(forecast_weather_data_8['icon']))
    st.caption(forecast_weather_data_8['description'])
    st.metric('Min', forecast_weather_data_8['min_temp'])
    st.metric('Max', forecast_weather_data_8['max_temp'])







