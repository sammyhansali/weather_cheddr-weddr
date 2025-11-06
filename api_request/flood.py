import sys
import json
import requests
import pathlib
from pprint import pp

url = "https://flood-api.open-meteo.com/v1/flood"
params = {
	"forecast_days": 1,
	"latitude": 42.3751,
	"longitude": -71.1056,
	"timezone": "America/New_York",
	"daily": "river_discharge",
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