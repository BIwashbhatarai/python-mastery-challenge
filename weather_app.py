import requests  # Import requests module to handle HTTP requests

# Your OpenWeatherMap API key (replace with your own)
api_key = "086aa7477e4c8be6d719fb083db6988c"

# Base URL for the OpenWeatherMap current weather API
base_url = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch and display the current weather for the given city.

    Args:
        city (str): Name of the city to get weather for.
    """
    # Parameters to send with API request
    params = {
        "q": city,          # City name
        "appid": api_key,   # API key for authentication
        "units": "metric"   # Units in Celsius
    }
    
    # Send GET request to the API with parameters
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        
        main = data['main']     # Main weather data (temp, humidity, etc.)
        weather_desc = data['weather'][0]['description']  # Weather condition description
        temp = main['temp']     # Current temperature in Celsius
        humidity = main['humidity']  # Humidity percentage
        
        # Print formatted weather information
        print(f"\nWeather in {city.title()}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc.capitalize()}")
        print(f"Humidity: {humidity}%\n")
        
    else:
        # If city not found or other error, show this message
        print(f"Error: City {city} not found or API issue")

def main():
    """
    Main function to run the CLI Weather App.
    """
    print("---CLI Weather App---")
    
    # Get city name input from user
    city = input("Enter city name: ").strip()
    
    # Fetch and display the weather for the entered city
    get_weather(city)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
