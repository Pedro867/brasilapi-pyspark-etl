import os
import json
import requests

URL_API = "https://brasilapi.com.br/api/banks/v1"
DIR_PATH = "./data_lake/bronze"
FILE_NAME = "banks_raw.json"

def get_and_save_data():

    os.makedirs(DIR_PATH, exist_ok=True)

    print(f"Getting data from: {URL_API} ...")

    response = requests.get(URL_API)

    if response.status_code == 200:
        data = response.json()
        complete_path = os.path.join(DIR_PATH, FILE_NAME)

        with open(complete_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))

        print(f"Success! {len(data)} records saved on {complete_path}")
    else:
        print(f"Request error. Status code = {response.status_code}")

if __name__ == "__main__":
    get_and_save_data()