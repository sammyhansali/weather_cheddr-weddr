import os
import json
import requests
import pathlib
import datetime

def request_and_save_data(url, params, location_id, endpoint):
    today = datetime.date.today().strftime('%m%d%Y')
    fp = pathlib.Path(f"test_data/{location_id}-{today}-{endpoint}.json")
    if os.path.exists(fp):
        return
    try:
        resp = requests.get(url=url, params=params)

        resp.raise_for_status
        if resp.status_code != 200: 
            raise requests.exceptions.HTTPError
        content = json.loads(resp.content)
        
        with open(fp, "w") as f:
            json.dump(content, f)

    except requests.exceptions.HTTPError as err:
        print("API request failed. Error details: ", err)

    except Exception as err:
        print("An error occurred. Error details: ", err)