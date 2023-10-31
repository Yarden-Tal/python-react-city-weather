from flask import Flask
from app import get_data

app = Flask(__name__)


@app.route("/weather")
def weather():
    data = get_data()
    return data


if __name__ == "__main__":
    app.run(debug=True)
