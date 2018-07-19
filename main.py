import json
import requests
import apikey
import google_place_api

weather = "no text"
appid = apikey.openweatherapi
city_id = 0
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'lat': google_place_api.lat, 'lon': google_place_api.lon, 'units': 'metric',
                               'lang': 'ru', 'appid': appid})
    data = res.json()
    print(data)
    name = data['name']
    conditions = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    icon = "http://openweathermap.org/img/w/" + str(data['weather'][0]['icon']) + ".png"

    if (temp > 0):
        temp = "+" + str(temp)
    if (temp_min > 0):
        temp_min = "+" + str(temp_min)

    if (temp_max > 0):
        temp_max = "+" + str(temp_max)

    weather = "Сегодня в  <b>" + google_place_api.name + "<b>\n" + "<a href = " + icon + "</a>" + str(
        temp) + "\n" + str(conditions).capitalize() + " от " + str(temp_min) + " до " + str(temp_max)
except Exception as e:
    print(e)
    pass
