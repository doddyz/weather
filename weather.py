# Altair Chart refinements: add tooltips, Format datetime as wanted, slant axis labels data, Finally maybe mix into a single combo chart all information, colouring each chart type differently
# See how to exclude parts exclude={part}
# See how to store these in secrets, and where it goes when deploying web app
# https://openweathermap.org/api/one-call-api#data

import json
import altair as alt
import pandas as pd
import requests
import streamlit as st
from datetime import datetime

OPENWEATHER_KEY = st.secrets['openweather_key']

BASE_API_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall?'

BASE_GEO_API_CALL_URL = 'http://api.openweathermap.org/geo/1.0/direct?'

BASE_ICON_URL = 'http://openweathermap.org/img/wn/'

COUNTRIES = {'GB': ['London', 'Manchester'], 'FR': ['Paris', 'Vincennes', 'Bordeaux'], 'TG': ['Lomé', 'Aneho'], 'ES': ['Madrid', 'Málaga', 'Granada', 'Córdoba']}

# CITIES = {'London': {'lat': '51.5118529', 'lon': '-0.1987003'}}

def get_geo_coordinates(city_name, country_code):
    # try without limit param 1st
     geo_api_call_url = BASE_GEO_API_CALL_URL + f'q={city_name},{country_code}&appid={OPENWEATHER_KEY}'
     r = requests.get(geo_api_call_url)
     r_json = r.json()
     return r_json[0]['lat'], r_json[0]['lon']


@st.cache
def open_weather_api_call(lat, lon, lang='en', units='metric'):
    return BASE_API_CALL_URL + f'lat={lat}&lon={lon}&units={units}&lang={lang}&appid={OPENWEATHER_KEY}'


def get_current_weather_metrics(call_json):
    # returns dict of current weather main parameters including desc + icon
    # Add if as rain/snow params not always there
    return {
        'temp':
        call_json['current']['temp'],
        'wind_speed':
        call_json['current']['wind_speed'],
        # 'rain':
        # call_json['current']['rain'],
        # 'snow':
        # call_json['current']['snow']
    }


def get_current_weather_description(call_json):
    # returns dict of current weather main parameters including desc + icon
    return call_json['current']['weather'][0]
    

def get_daily_weather_forecast_data(call_json):
    # returns dict of current weather main parameters including desc + icon
    # Add if as rain/snow params not always there
    return call_json['daily']


def get_daily_weather_forecast_data_for_day_n(call_json, n):
    forecast_weather_data_day_n = get_daily_weather_forecast_data(call_json)[n - 1]
    return {
        'dt':
        forecast_weather_data_day_n['dt'],
        'temp':
        forecast_weather_data_day_n['temp'],
        'wind_speed':
        forecast_weather_data_day_n['wind_speed'],
        'min_temp':
        '{0:.0f}'.format(forecast_weather_data_day_n['temp']['min']),
        'max_temp':
         '{0:.0f}'.format(forecast_weather_data_day_n['temp']['max']),
        'description':
        forecast_weather_data_day_n['weather'][0]['description'],
        'icon':
        forecast_weather_data_day_n['weather'][0]['icon'],
        
                
        }


def daily_weather_col_data(r_json, day_n):
     forecast_weather_data = get_daily_weather_forecast_data_for_day_n(r_json, day_n)
     st.subheader(get_day_of_week_from_ts(int(forecast_weather_data['dt'])))
     st.image(get_weather_icon_url(forecast_weather_data['icon']))
     st.caption(forecast_weather_data['description'])
     st.metric('Max', forecast_weather_data['max_temp'])
     st.metric('Min', forecast_weather_data['min_temp'])


def get_hourly_weather_forecast_data(call_json):
    # returns dict of hourly weather data
    return call_json['hourly']

# For now only interested in next 24 hours hourly data
def get_hourly_weather_forecast_data_as_df(call_json):
    # returns dict of hourly weather data
    df = pd.DataFrame(call_json['hourly'])

    # Add a column to transform dt unix timestamps as date time objects that we can then parse as we wish

    df['Date'] = df['dt'].map(datetime.fromtimestamp)

    # df['Tmp2'] = df['Date'].map(lambda x: x.strftime('%A %H:%M'));
    
    # To make our hours start at 1 rather than 0
    # Verify we're using right hours by converting the unix timestamp first
    df.index += 1

    # df = df.set_index('Tmp2')
    return df[:24]


def draw_hourly_temp_chart(df):

     base = alt.Chart(df).encode(
        x='Date',
        y='temp',
        tooltip='temp'
        
    )
         
     line = base.mark_line()

     points = base.mark_point(filled=True, size=40)
     chart = line + points

     return chart


def draw_hourly_precipitation_proba_chart(df):
     return alt.Chart(df).mark_bar().encode(
          x='Date:T',
          y='pop:Q',
     )

     

def get_weather_icon_url(icon_code):
    return BASE_ICON_URL + icon_code + '@2x.png'


def get_day_of_week_from_ts(ts):
    # return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return datetime.utcfromtimestamp(ts).strftime('%a')


