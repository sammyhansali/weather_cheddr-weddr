import sys
import json
import requests
from pprint import pp

def main():
    weather_forecast_url = "https://api.open-meteo.com/v1/forecast"
    wf_params = {
        "latitude": "42.3751",
        "longitude": "-71.1056",
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
    historical_weather_url = "https://archive-api.open-meteo.com/v1/archive"
    hw_params = {
        "latitude": "42.3751",
        "longitude": "-71.1056",
        "start_date": "2025-01-01",
        "end_date": "2025-02-01",
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
    
    try:
        resp = requests.get(url=weather_forecast_url, params=wf_params)
        # resp = requests.get(url=historical_weather_url, params=hw_params)
        resp.raise_for_status
        if resp.status_code != 200: 
            raise requests.exceptions.HTTPError
        content = json.loads(resp.content)
        pp(content)
    except requests.exceptions.HTTPError as err:
        print("API request failed. Error details: ", err)
    

if __name__ == "__main__":
    main()
