from api_request.api_request import request_and_save_data

def make_request(location):

    latitude = location["latitude"]
    longitude = location["longitude"]
    location_id = location["location_id"]
    endpoint = "flood"

    url = "https://flood-api.open-meteo.com/v1/flood"
    params = {
        "forecast_days": 1,
        "latitude": latitude,
        "longitude": longitude,
        "timezone": "America/New_York",
        "daily": "river_discharge",
    }

    request_and_save_data(url, params, location_id, endpoint)