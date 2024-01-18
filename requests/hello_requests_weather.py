#!/usr/bin/env python
#
# hello_requests_weather.py
#


import requests


# Los Angeles
latitude = "34.0549"
longitude = "-118.2426"

weather_api = "https://api.weather.gov/points/" + latitude + "," + longitude

print(weather_api)
result = requests.get(weather_api)

forecast_url = result.json()['properties']['forecast']
print("forecast:" + forecast_url)

result = requests.get(forecast_url)

periods = result.json()['properties']['periods']

for period in periods:
    print(period['name'] + ": " + period['detailedForecast'])
    

