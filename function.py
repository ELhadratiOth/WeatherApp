import json
from urllib.request import urlopen
import requests
import time

# def actuall_data():
#     url="http://ipinfo.io/json"
#     response = urlopen(url)
#     data = json.load(response)
#     print(data)
#     latitude=data['loc'].split(',')[0]
#     longitude=data['loc'].split(',')[1]
#     return latitude , longitude

def getCurrentLocation(latitude, longitude):
    weatherApiUrl = f"https://api.open-meteo.com/v1/dwd-icon?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weather_code&forecast_days=1"
    getting_weather= requests.get(weatherApiUrl)
    currentWeather = getting_weather.json()
    print(currentWeather)
    print('getCurrentLocation')

    return currentWeather


def oganiseData(latitude, longitude):
    currentWeather = getCurrentLocation(latitude, longitude)
    time = currentWeather['hourly']['time'][::3]
    tmp = currentWeather['hourly']['temperature_2m'][::3]
    tmp_code = currentWeather['hourly']['weather_code'][::3]
    print(tmp_code)
    dataDic = {
        'time': time ,
        'tmp': tmp ,
        'tmp_code': tmp_code
    }
    print('oganiseData')

    return dataDic

def setImg( latitude, longitude):
    dataDic = oganiseData(latitude, longitude)
    img =[]
    for data in dataDic['tmp_code'] :
        if int(data) == 0 :
            img.append("./static/1.png")
        elif int(data) in [1,2,3]:
            img.append("./static/2.png")
        elif int(data) in [56,67 ,51,53,55 ,45,48] :
            img.append("./static/3.png")
        elif int(data) in [61,63,65] :
            img.append("./static/4.png")
        elif int(data) in [66,67]:
            img.append("./static/6710.png")
        elif int(data) in [71,73] :
            img.append("./static/5.png")
        elif int(data) in [75,77] :
            img.append("./static/911.png")
        elif int(data) in [80,81,82,85,86] :
            img.append("./static/8.png")
    dataDic['img']= img
    print(img)
    print('setImg')

    return dataDic

def actuall_dataCompli():
    url="http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    print(data)
    latitude=data['loc'].split(',')[0]
    longitude=data['loc'].split(',')[1]
    region = data['region']
    city = data['city']
    return latitude , longitude , region , city
def getCurrentWeather(latitude, longitude):
    weatherApiUrl = f"https://api.open-meteo.com/v1/dwd-icon?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code&forecast_days=1"
    getting_weather= requests.get(weatherApiUrl)
    currentWeather = getting_weather.json()
    print(currentWeather)
    lastT = currentWeather['current']['temperature_2m']
    code_lastT = currentWeather['current']['weather_code']


    return lastT , code_lastT


def outputCurrentT(latitude, longitude):
    img = ""
    lastT , code_lastT  = getCurrentWeather(latitude, longitude)
    print(code_lastT)
    print(lastT)
    if int(code_lastT) == 0:
        img = "./static/1.png"
    elif int(code_lastT) in [1, 2, 3]:
        img = "./static/2.png"
    elif int(code_lastT) in [56, 67, 51, 53, 55, 45, 48]:
        img = "./static/3.png"
    elif int(code_lastT) in [61, 63, 65]:
         img = "./static/4.png"
    elif int(code_lastT) in [66, 67]:
         img = "./static/6710.png"
    elif int(code_lastT) in [71, 73]:
         img = "./static/5.png"
    elif int(code_lastT) in [75, 77]:
         img = "./static/911.png"
    elif int(code_lastT) in [80, 81, 82, 85, 86]:
         img = "./static/8.png"
    print("imaff" , img)
    print('outputCurrentT')

    return str(lastT).split('.')[0] , img


# lastT , img = outputCurrentT()
# print(lastT , img)






