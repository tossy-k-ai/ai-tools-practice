import requests

def get_location(city):
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

        res = requests.get(url)
        data = res.json()

        if "results" not in data:
            return None,None
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]

        return lat, lon

    except Exception:
        return None, None
    
def get_weather(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        res = requests.get(url)
        data = res.json()

        if"current_weather" not in data:
            return None,None,"取得失敗"

        temp = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]
        code = data["current_weather"]["weathercode"]

        weather_map = {
            0: "快晴",
            1: "晴れ",
            2: "くもり",
            3: "曇り",
            45: "霧",
            61: "雨",
            71: "雪",
        }

        weather = weather_map.get(code, "不明")

        return temp, wind, weather
    except Exception:
        return None,None,"エラー"
city = input("都市名: ")

lat, lon = get_location(city)

if lat is None:
    print("都市が見つかりません")
else:
    temp, wind, weather = get_weather(lat, lon)

    if temp is None:
        print("天気取得失敗")
    else:
        print(f"{city}の天気")
        print(f"気温: {temp}℃")
        print(f"風速: {wind}km/h")
        print(f"天気: {weather}")