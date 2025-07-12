import requests

API_KEY = "e29dee0382777f6b20af477bae09810b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"The weather in {city} is {description} with a temperature of {temperature}°C.")
else:
    print("City not found or error with the API.")
