from dotenv import load_dotenv
import os
import requests
from flask import Flask

app = Flask(__name__)
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
req_url = f"{BASE_URL}?appid={os.getenv('API_KEY')}&q={city}"
res = requests.get(req_url)


def get_data():
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print("Error fetching data.")


@app.route("/weather")
def weather():
    data = get_data()
    return data


if __name__ == "__main__":
    app.run(debug=True)
