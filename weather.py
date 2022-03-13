# https://openweathermap.org/api/one-call-api#data
# See how to exclude parts exclude={part}
# See how to store these in secrets, and where it goes when deploying web app

import json
import pandas as pd
import requests
import streamlit as st
from datetime import datetime

OPENWEATHER_API_KEY = '3506e11b30813c5348ea977b1fb394a8'

BASE_API_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall?'

BASE_GEO_API_CALL_URL = 'http://api.openweathermap.org/geo/1.0/direct?'

BASE_ICON_URL = 'http://openweathermap.org/img/wn/'

COUNTRIES = {'GB': ['London', 'Manchester'], 'FR': ['Paris'], 'ES': ['Madrid']}

# CITIES = {'London': {'lat': '51.5118529', 'lon': '-0.1987003'}}

def get_geo_coordinates(city_name, country_code):
    # try without limit param 1st
     geo_api_call_url = BASE_GEO_API_CALL_URL + f'q={city_name},{country_code}&appid={OPENWEATHER_API_KEY}'
     r = requests.get(geo_api_call_url)
     r_json = r.json()
     return r_json[0]['lat'], r_json[0]['lon']


@st.cache
def open_weather_api_call(lat, lon, lang='en', units='metric'):
    # lat = CITIES[city]['lat']
    # lon = CITIES[city]['lon']
    return BASE_API_CALL_URL + f'lat={lat}&lon={lon}&units={units}&lang={lang}&appid={OPENWEATHER_API_KEY}'


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
        forecast_weather_data_day_n['temp']['min'],
        'max_temp':
        forecast_weather_data_day_n['temp']['max'],
        'description':
        forecast_weather_data_day_n['weather'][0]['description'],
        'icon':
        forecast_weather_data_day_n['weather'][0]['icon'],
        
                
        }


def get_weather_icon_url(icon_code):
    return BASE_ICON_URL + icon_code + '@2x.png'


def get_day_of_week_from_ts(ts):
    # return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return datetime.utcfromtimestamp(ts).strftime('%a')


