import json
import requests
import apikey
from datetime import datetime

appid = apikey.openweatherapi
city_id = 0


def weatherapp(text):
    place_query = ""
    place_query = text
    place_apikey = apikey.google_place_api
    lat = "lat"
    lon = "lot"

    # Находим место по названию города с пощью Google Place API
    try:
        place_res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',
                                 params={'query': place_query, 'language': 'ru', 'key': place_apikey})
        place_data = place_res.json()

        lon = json.dumps(place_data['results'][0]['geometry']['location']['lng'])
        lat = json.dumps(place_data['results'][0]['geometry']['location']['lat'])
        place_name = place_data['results'][0]['name']

    except Exception as e:
        print("Error requests: ", e)
    pass

    # По широте и долготе определям погоду местности с  помощью OpenWeatherMap API
    try:
        gradus = b'\xb0'.decode("utf-8", "replace")
        now = datetime.now()
        t = 0
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                           params={'lat': lat, 'lon': lon, 'units': 'metric',
                                   'lang': 'ru', 'appid': appid})
        data = res.json()
        day = "послезавтра"
        if (day == "сегодня"):
            t = 0
        elif (day == "завтра"):
            t = 1
        elif (day == "послезавтра"):
            t = 2
        list = data['list']
        for daily in list:
            name = str(data['city']['name'])
            conditions = str(daily['weather'][0]['description'])
            clouds = str(daily['clouds']['all'])
            wind_speed = str(daily['wind']['speed'])
            temp = daily['main']['temp']
            humi = str(daily['main']['humidity'])
            date = str(daily['dt_txt'])
            date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            im = "https://i.pinimg.com/originals/97/1b/02/971b02d5aacc22155dd10202c918cd16.gif"
            if (temp > 0):
                temp = "+" + str(temp)
            weather = "Error 007"
            if date.hour == 12 and date.day == now.day + t:
                weather = str(
                    date.date()) + " в  " + place_name + "\n" + conditions.capitalize() + "\nТемпература: " + str(
                    temp) + " " + gradus + " C \nВлажность: " + humi + " %\nОблачность: " + clouds + " %\nСкорость ветра: " + wind_speed + " м/с\n<a href = '" + im + "'>.</a>\n\n"
                print(weather)
                break
        return weather

    except Exception as e:
        print(e)
        pass
