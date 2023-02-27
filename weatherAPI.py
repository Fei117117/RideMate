import sqlalchemy as sqla
import traceback
import datetime
import time
import requests
import json
from pprint import pprint

# Getting station data using Station API
APIKEY="dc37139a1f5e7dbb1220eb237bc420120b3381f4"
NAME="Dublin"
STATIONS_URL="https://api.jcdecaux.com/vls/v1/stations" 

r=requests.get(STATIONS_URL,params={"apiKey":APIKEY,"contract":NAME})
stations=json.loads(r.text)

# From station position getting the weather information there

# Creating a dictionary of station and its weather data: Station number is the key, weather data is the value

weather_station = {}

WEATHER_URL="https://api.open-meteo.com/v1/forecast"

for station in stations:
    LATITUDE = station['position']['lat']
    LONGITUDE = station['position']['lng']
    weather=requests.get(WEATHER_URL,params={"latitude":LATITUDE,"longitude":LONGITUDE,"hourly":"temperature_2m","hourly":"precipitation_probability","hourly":"precipitation","hourly":"weathercode","hourly":"windspeed_10m","current_weather":"true","timeformat":"unixtime"})
    weather_dict=json.loads(weather.text)
    
    # Filling the weather_station dictionary:
    weather_station[station['number']]=weather_dict

pprint(weather_station[42])
