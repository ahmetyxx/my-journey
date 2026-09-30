import requests
import os

API_KEY=os.getenv("API_KEY")
MY_LAT="41.021694"
MY_LNG="29.251581"


def wheather_condition(lat,lon):
    response=requests.get(
        url="http://api.openweathermap.org/data/2.5/forecast",
        params={
            "lat":lat,
            "lon":lon,
            "appid":API_KEY,
            "cnt":4,     
        }
    )
    return response.json()

def is_raining(lat,lon):
    response=wheather_condition(lat=lat,lon=lon)
    for forecast in response["list"]:
        if int(forecast["weather"][0]["id"])<700:
            return True
    else:
        return False
    

print(is_raining(MY_LAT,MY_LNG))