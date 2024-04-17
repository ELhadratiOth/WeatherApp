import requests



# Base URL for the 7Timer API (astro endpoint)
url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

# Make a request to the 7Timer API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    print(data)


