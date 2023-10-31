import os
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
req_url = f"{BASE_URL}?appid={os.environ['API_KEY']}&q={city}"
res = requests.get(req_url)


def get_data():
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print("Error fetching data.")
