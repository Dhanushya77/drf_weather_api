from django.shortcuts import render
import requests
import math, datetime
# Create your views here.

def index(req):
    city_name = 'kochi'
    if req.method == 'POST':
        city_name = req.POST['city']
        api_key = '360e4bc3865e745ec844bd7ec054ca11'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        weather = requests.get(url)
        weather_data = weather.json()
        try:
            data={
                'city':city_name,
                'description':weather_data['weather'][0]['description'],
            }
        except:
            city_name = 'kochi'
            
    api_key = '360e4bc3865e745ec844bd7ec054ca11'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    weather = requests.get(url)
    weather_data = weather.json()
    dt_object = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    dt_object1 = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    data={
        'city':city_name,
        'description':weather_data['weather'][0]['description'],
        'temp':math.floor(weather_data['main']['temp']-273.15),
        'temp_min':math.floor(weather_data['main']['temp_min']-273.15),
        'temp_max':math.floor(weather_data['main']['temp_max']-273.15),
        'wind':weather_data['wind']['speed'],
        'sunrise':dt_object.strftime('%H:%M:%S'),
        'sunset':dt_object1.strftime('%H:%M:%S'),
    }
    return render(req,'index.html',{'data':data})