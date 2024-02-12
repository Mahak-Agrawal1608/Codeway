import requests

def get_weather_data(location):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Check if the location is a zip code or city name
    if location.isdigit():
        params = {'zip': location, 'appid': api_key, 'units': 'metric'}
    else:
        params = {'q': location, 'appid': api_key, 'units': 'metric'}

    # Making the API request
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        return data
    else:
        print("Failed to retrieve weather data. Please try again later.")
        return None

def display_weather(data):
    if data is not None:
        print("\nCurrent Weather:")
        print(f"Location: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("No weather data to display.")

def main():
    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather_data(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
