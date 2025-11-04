import sys
import json
import requests
import pathlib
from pprint import pp

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": "42.3751",
    "longitude": "-71.1056",
    "timezone": "America/New_York",
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "dew_point_2m",
        "apparent_temperature",
        "precipitation_probability",
        "precipitation",
        "rain",
        "showers",
        "snowfall",
        "snow_depth",
        "wind_speed_10m",
        "weather_code",
        "visibility",
        "wind_direction_10m",
        "wind_gusts_10m",
        "cloud_cover",
        "et0_fao_evapotranspiration",
    ],
    "daily": [
        "daylight_duration",
        "sunshine_duration",
        "sunrise",
        "sunset",
        "weather_code",
        "uv_index_clear_sky_max",
        "uv_index_max",
        "et0_fao_evapotranspiration",
    ]
}
cities = {
    "cambridge,ma,usa": {
        "latitude": "42.3751",
        "longitude": "-71.1056",
    },
}

def make_request():
    try:
        resp = requests.get(url=url, params=params)
        resp.raise_for_status
        if resp.status_code != 200: 
            raise requests.exceptions.HTTPError
        content = json.loads(resp.content)
        fp = pathlib.Path("C:/Users/sammy/projects/portfolio/weather_cheddr-weddr/test_data/payload.json")
        with open(fp, "w") as f:
            json.dump(content, f)

    except requests.exceptions.HTTPError as err:
        print("API request failed. Error details: ", err)

    except Exception as err:
        print("An error occurred. Error details: ", err)