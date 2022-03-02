import os

import requests
from datetime import datetime as dt
from dotenv import load_dotenv
load_dotenv()

todays_date = dt.now().strftime("%d/%m/%Y")
todays_time = dt.now().strftime("%H:%M:%S")

APP_ID = os.environ["NUTRIX_APP_ID"]
API_KEY = os.environ["NUTRIX_API_KEY"]
nutritionix_exercise_endpoint = os.environ["NUTRIX_END"]
sheety_endpoint = os.environ["SHEET_END"]
headers_sheety = {
    "Authorization": "Bearer " + os.environ["AUTH_TOKEN"],
}
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": "cycled 3 miles",
    "gender": "male",
    "weight_kg": 90.7,
    "height_cm": 177.8,
    "age": 30
}

exercise_response = requests.post(url=nutritionix_exercise_endpoint, json=params, headers=nutritionix_headers)
data = exercise_response.json()

sheety_params = {
    "sheet1": {
        "date": todays_date,
        "time": todays_time,
        "exercise": data["exercises"][0]["user_input"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
    }
}
print(sheety_params)
# response = requests.get(url=sheety_endpoint, auth=('Bl4ckSt4ff', 'thisfuckinsucks'))
# print(response.text)

sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers_sheety)
print(sheety_response.text)

