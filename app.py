# import mysql.connector
import functools
import json
import time
import traceback

import googlemaps
import requests
from flask import Flask, g, jsonify, render_template, request
from flask_googlemaps import GoogleMaps
from sqlalchemy import text

import config
import database
import pandas as pd

app = Flask(__name__)
GoogleMaps(app, key=config.MAP_KEY)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = database.connect_to_database()
    return db


# Set up the Google Maps client
gmaps = googlemaps.Client(config.MAP_KEY)

# Search for a location in Dublin
address = "Dublin, Ireland"
geocode_result = gmaps.geocode(address)

# Get the latitude and longitude of the location
lat = geocode_result[0]["geometry"]["location"]["lat"]
lng = geocode_result[0]["geometry"]["location"]["lng"]


@app.route('/')
def index():

    # Fetch the station data from the MySQL database
    query = 'SELECT * FROM station'
    engine = get_db()
    stations = engine.connect().execute(text(query)).fetchall()

    # Fetch the latest available bikes data
    availability_query = 'SELECT number, available_bikes FROM availability ORDER BY last_update DESC'
    availability_data = engine.connect().execute(text(availability_query)).fetchall()
    availability_dict = {item[0]: item[1] for item in availability_data}

    # Set up the markers
    markers = []
    for station in stations:
        available_bikes = availability_dict.get(station[0], 0)
        marker = {
            'number': station[0],
            'position': {'lat': station[7], 'lng': station[8]},
            'title': station[6],
            'weathercode': 10,
            'status': station[9],
            'bike_stands': station[3],
            'available_bikes': available_bikes
        }
        markers.append(marker)

    # Render the template with API key, markers, and specified lat and lng
    return render_template("map.html", api_key=config.MAP_KEY, markers=markers, lat=lat, lng=lng, availability=availability_dict)



@app.route('/data')
def station_data():
    engine = get_db()
    query = 'SELECT * FROM station'
    data = engine.connect().execute(text(query)).fetchall()
    query = request.args.get('query')
    filter_criteria = request.args.get('filter')
    if query and filter_criteria:
        query = f"SELECT * FROM station WHERE {filter_criteria} LIKE '%{query}%'"
        search_results = engine.connect().execute(text(query)).fetchall()
        return render_template('data.html', search_results=search_results)
    else:
        return render_template('data.html')
    

@app.route("/stations")
@functools.lru_cache(maxsize=128)
def get_stations():
    engine = get_db()
    sql = "select * from station;"
    try:
        with engine.connect() as conn:
            rows = conn.execute(text(sql)).fetchall()
            # this has not been print because debug mode
            print('#found {} stations', len(rows), rows, flush=True)
            # app.logger.info('#found {} stations', len(rows), rows) #Another way to print
            # use this formula to turn the rows into a list of dicts
            return jsonify([row._asdict() for row in rows])
    except:
        print(traceback.format_exc())
        return "error in get_stations", 404

<<<<<<< HEAD
# From lecture note, working now. It's showing info of 1 station defined in the link


@app.route("/available/<int:station_id>")
def get_station(station_id):
    engine = get_db()
    data = []
    rows = engine.execute(
        "SELECT * from availability where number = {} order by last_update DESC LIMIT 1;".format(station_id))
    for row in rows:
        data.append(dict(row))
    return jsonify(available=data)

# def new_func():
#     return station_id

# Function to get the longitude of the chosen station


@app.route("/available/<int:station_id>")
def get_lng(station_id):
    engine = get_db()
    lng = engine.execute(
        "SELECT position_lng from availability where number = {} order by last_update DESC LIMIT 1;".format(station_id))
    return lng


@app.route("/available/<int:station_id>")
def get_lat(station_id):
    engine = get_db()
    lat = engine.execute(
        "SELECT position_lat from availability where number = {} order by last_update DESC LIMIT 1;".format(station_id))
    return lat


=======
>>>>>>> main
@app.route("/availability/daily/<int:station_id>")
def get_availability_daily(station_id):
    engine = get_db()
    df = pd.read_sql_query(
        "SELECT * from availability where number = %(number)s", engine, params={"number": station_id})
    df['last_update'] = pd.to_datetime(df.last_update, unit='s')
    df.set_index('last_update', inplace=True)
<<<<<<< HEAD
    res = df[['available_bikes', 'available_bike_stands']
             ].resample('1d').mean()
    daily = jsonify(data=json.dumps(
        list(zip(map(lambda x: x.isoformat(), res.index), res.values.tolist()))))
    return render_template("chart.html", daily=daily)

=======
    res = df[['available_bikes', 'available_bike_stands']].resample('1d').mean()
    daily=jsonify(data=json.dumps(list(zip(map(lambda x:x.isoformat(), res.index),res.values.tolist()))))
    return daily
>>>>>>> main

@app.route("/chart")
def chart():
    return render_template("chart.html")

<<<<<<< HEAD

@app.route('/weather')
def weather():
    LATITUDE = get_lat
    LONGITUDE = get_lng
    r = requests.get(config.WEATHER_URL, params={"latitude": 53.340927, "longitude": -6.262501, "hourly": config.HOURLY,
                                                 "daily": config.DAILY, "current_weather": "true", "timeformat": "unixtime", "timezone": config.TIMEZONE})
    r_text = json.loads(r.text)
    weather = jsonify(available=r_text)
    return weather
    # return f'Weather information: {weather}'.format(weather)


=======
>>>>>>> main
if __name__ == '__main__':
    app.run(debug=True)

# Testing decorators:


def build_regression_model(**kwargs):
    print('building model...')

# build_regression_model()


start = time.time()
build_regression_model()
end = time.time()

print(end-start)
print("took: {} secs".format(end-start))


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        print("")
