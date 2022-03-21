import json
import os

import requests


def get_by_location(location, latitude, longitude):
    url = "https://api.weatherapi.com/v1/current.json"

    api_key = os.environ.get('weather_api_key')
    if location is not None:
        location_name = location
    elif latitude is not None and longitude is not None:
        location_name = str(latitude) + "," + str(longitude)

    querystring = {"q": location_name, "key": api_key, "aqi": "yes"}

    response = requests.request("GET", url, params=querystring)

    print('Weather Response: ', response.text)
    js = json.loads(response.text)

    return js
