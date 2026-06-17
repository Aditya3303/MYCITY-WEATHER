import requests

# Lucknow coordinates
lat, lon = 26.8467, 80.9462
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weathercode,windspeed_10m&timezone=auto"

response = requests.get(url)
data = response.json()

print("Temperature:", data["current"]["temperature_2m"], "°C")
print("Weather code:", data["current"]["weathercode"])
print("Wind speed:", data["current"]["windspeed_10m"], "km/h")
