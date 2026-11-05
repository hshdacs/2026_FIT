import requests
import pandas as pd
import datetime as dt
import time

#filename = "weather.json" # test, ob die Daten in Ordn
#df = pd.read_json( filename )

#url = "http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&date=2020:2021"
#url = "https://api.openweathermap.org/data/2.5/weather?q=Heidelberg,de&units=metric&APPID=8903a345e1b9134f8001e71b8748a08f"

def date_only(date):
    return date.strftime("%Y-%m-%d")

def time_only(date):
    return date.strftime("%H:%M:%S")

def convert_epoch_to_datetime(epoch_time):
    # Convert epoch time to a datetime object
    return dt.datetime.fromtimestamp(epoch_time)

def getWeather(stadt):
    url = "https://api.openweathermap.org/data/2.5/weather"
    url += "?q=" + stadt + ",de"
    url += "&units=metric"
    url += "&appid=8903a345e1b9134f8001e71b8748a08f"
    response = requests.get(url)
    return response.json()


df = pd.DataFrame()
for s in ["Heidelberg", "Mannheim", "Worms", "Sinsheim", "Stuttgart"]:
    raw_data = getWeather(s)    
    if "main" in raw_data:
        data = raw_data["main"]
        data["date"] = date_only(convert_epoch_to_datetime(raw_data["dt"]))
        data["sunrise"] = time_only(convert_epoch_to_datetime(raw_data["sys"]["sunrise"]))
        data["sunset"] = time_only(convert_epoch_to_datetime(raw_data["sys"]["sunset"]))
        data["wind speed"] = raw_data["wind"]["speed"]
        data["wind deg"] = raw_data["wind"]["deg"]
        df[s] = data

print( df )
print( df.describe() )
df.to_csv("wetter.csv")