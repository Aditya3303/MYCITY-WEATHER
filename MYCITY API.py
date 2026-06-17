import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"   # "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print("Error:", data.get("message", "Unable to fetch weather data"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Replace with your own API key from OpenWeatherMap
    API_KEY = "YOUR_API_KEY_HERE"
    city_name = input("Enter city name: ")
    get_weather(city_name, API_KEY)
