import sys
import json
import requests
import pathlib
from pprint import pp

url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
	"forecast_days": 1,
	"latitude": 42.3751,
	"longitude": -71.1056,
	"timezone": "America/New_York",
	"hourly": [
        "pm10", 
        "pm2_5", 
        "carbon_monoxide", 
        "carbon_dioxide", 
        "nitrogen_dioxide", 
        "sulphur_dioxide", 
        "ozone", 
        "aerosol_optical_depth", 
        "dust", 
        "uv_index", 
        "uv_index_clear_sky", 
        "methane",
    ],
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