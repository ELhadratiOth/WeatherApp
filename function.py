import requests

def getCurrentLocation(latitude, longitude):
    weatherApiUrl = f"https://api.open-meteo.com/v1/dwd-icon?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weather_code,is_day&timezone=auto&forecast_hours=24"
    getting_weather= requests.get(weatherApiUrl)
    currentWeather = getting_weather.json()
    print(currentWeather)
    # print('getCurrentLocation')
    return currentWeather


def oganiseData(latitude, longitude):
    currentWeather = getCurrentLocation(latitude, longitude)
    time =  currentWeather['hourly']['time'][::4]
    tmp = currentWeather['hourly']['temperature_2m'][::4]
    tmp_code = currentWeather['hourly']['weather_code'][::4]
    is_day= currentWeather['hourly']['is_day'][::4]
    time_local = currentWeather['utc_offset_seconds']
    # print(tmp_code)
    dataDic = {
        'time': time ,
        'tmp': tmp ,
        'tmp_code': tmp_code ,
        'is_day' : is_day ,
        'time_local' : time_local
    }
    # print('oganiseData')

    return dataDic

def setImg( latitude, longitude):
    dataDic = oganiseData(latitude, longitude)
    img =[]
    for data , isday in zip(dataDic['tmp_code'] ,dataDic['is_day'])  :
        if int(data) == 0 :
            if int(isday) == 0 :
                img.append("./static/1n.png")
            else :
                img.append("./static/1.png")
        elif int(data) in [1,2,3]:
            if int(isday) == 0 :
                img.append("./static/2n.png")
            else :
                img.append("./static/2.png")
        elif int(data) in [56,67 ,51,53,55 ,45,48] :
            if int(isday) == 0 :
                img.append("./static/3n.png")
            else :
                img.append("./static/3.png")
        elif int(data) in [61,63,65] :
            if int(isday) == 0 :
                img.append("./static/4n.png")
            else :
                img.append("./static/4.png")
        elif int(data) in [66,67]:
            if int(isday) == 0 :
                img.append("./static/6710.png")
        elif int(data) in [71,73] :
            if int(isday) == 0 :
                img.append("./static/5n.png")
            else :
                img.append("./static/5.png")
        elif int(data) in [75,77] :
            if int(isday) == 0 :
                img.append("./static/911n.png")
            else :
                img.append("./static/911.png")
        elif int(data) in [80,81,82,85,86] :
            if int(isday) == 0 :
                img.append("./static/8n.png")
            else :
                img.append("./static/8.png")
    dataDic['img']= img
    # print(img)
    # print('setImg')

    return dataDic

def actuall_dataCompli():
    url = "http://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    # print(data)
    latitude = data['loc'].split(',')[0]
    longitude = data['loc'].split(',')[1]
    region = data['region']
    city = data['city']
    return latitude, longitude, region, city
def getCurrentWeather(latitude, longitude):
    weatherApiUrl = f"https://api.open-meteo.com/v1/dwd-icon?latitude={latitude}&longitude={longitude}&current=temperature_2m,is_day,weather_code&timezone=auto"

    getting_weather= requests.get(weatherApiUrl)
    if getting_weather.status_code == 200:
        currentWeather = getting_weather.json()
        # print(currentWeather)
        lastT = currentWeather['current']['temperature_2m']
        code_lastT = currentWeather['current']['weather_code']
        is_day = currentWeather['current']['is_day']

        return lastT , code_lastT , is_day
    else :
            # print("error de connexion")
            return


def outputCurrentT(latitude, longitude):
    img = ""
    lastT , code_lastT , isday  = getCurrentWeather(latitude, longitude)
    # print(code_lastT)
    # print(lastT)
    if int(code_lastT) == 0:
        if isday == 0 :
            img = "./static/1n.png"
        else :
            img = "./static/1.png"
    elif int(code_lastT) in [1, 2, 3]:
        if isday == 0 :
            img = "./static/2n.png"
        else :
            img = "./static/2.png"
    elif int(code_lastT) in [56, 67, 51, 53, 55, 45, 48]:
        if isday == 0 :
            img = "./static/3n.png"
        else :
            img = "./static/3.png"
    elif int(code_lastT) in [61, 63, 65]:
        if isday == 0:
            img = "./static/4n.png"
        else:
            img = "./static/4.png"
    elif int(code_lastT) in [66, 67]:
         img = "./static/6710.png"
    elif int(code_lastT) in [71, 73]:
        if isday == 0:
            img = "./static/5n.png"
        else:
            img = "./static/5.png"
    elif int(code_lastT) in [75, 77]:
        if isday == 0:
            img = "./static/911n.png"
        else:
            img = "./static/911.png"
    elif int(code_lastT) in [80, 81, 82, 85, 86]:
        if isday == 0:
            img = "./static/8n.png"
        else:
            img = "./static/8.png"

    return str(lastT).split('.')[0] , img

def getAirQuality(aqi):
    if aqi <= 20:
        return "Good", "Enjoy outdoor activities!" , '#1F8A70'
    elif aqi <= 50:
        return "Fair", "Acceptable, though some may be sensitive." , '#219C90'
    elif aqi <= 100:
        return "Moderate", "Sensitive individuals may experience symptoms." , '#FFC700'
    elif aqi <= 150:
        return "Poor", "Effects possible for sensitive people." ,'#FF9800'
    elif aqi <= 250:
        return "Very Poor", "Health alert: serious effects possible." , "#DD5746"
    else:
        return "Extremely Poor", "Emergency conditions. High risk for everyone." , "#E72929"

def AirDetails(latitude, longitude):
    weatherApiUrl = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longitude}&current=european_aqi,us_aqi,pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&timezone=auto&forecast_days=1"
    getting_weather= requests.get(weatherApiUrl)
    currentWeather = getting_weather.json()
    # print(currentWeather)
    aqi = int( (currentWeather['current']['european_aqi'] + currentWeather['current']['us_aqi']) / 2 )

    pm10 = currentWeather['current']['pm10']
    pm2_5 = currentWeather['current']['pm2_5']
    carbon_monoxide = currentWeather['current']['carbon_monoxide']
    nitrogen_dioxide = currentWeather['current']['nitrogen_dioxide']
    sulphur_dioxide = currentWeather['current']['sulphur_dioxide']
    ozone = currentWeather['current']['ozone']
    time = currentWeather['current']['time'].split('T')[1]
    unity = currentWeather['current_units']['pm10']


    type , message , color = getAirQuality(aqi)
    return aqi , pm10 , pm2_5 , carbon_monoxide , nitrogen_dioxide , sulphur_dioxide , ozone , type , message , time , unity , color





