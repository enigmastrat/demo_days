import requests


def fetchWeather(lat, lon):
    response =  requests.get(f"https://api.weather.gov/points/{lat},{lon}")  .json()
    x = response["@context"][1]["@version"]
    return x


if __name__ == "__main__":
    print(fetchWeather('33','-112'))


