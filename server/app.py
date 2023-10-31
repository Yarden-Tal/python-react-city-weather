import requests

API_KEY = "8e59e93c6389a0acf65adb7526ecfd26"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
req_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
res = requests.get(req_url)


def get_data():
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print("Error fetching data.")
