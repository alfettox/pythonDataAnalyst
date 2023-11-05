import requests
from decouple import config
import matplotlib.pyplot as plt

api_key = config('API_KEY')

def fetch_weather_data(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

city = 'Montreal,ca'
weather_data = fetch_weather_data(api_key, city)

# Extract historical temperature and humidity data
historical_data = weather_data['list']

# Lists to store historical data
dates = []
temperatures = []
humidities = []

# Process historical data
for entry in historical_data:
    date = entry['dt_txt']
    temperature = entry['main']['temp'] - 273.15  # Convert to Celsius
    humidity = entry['main']['humidity']

    dates.append(date)
    temperatures.append(temperature)
    humidities.append(humidity)

# Create a line plot for historical temperatures
plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='blue', label='Temperature (°C)')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')

# Create a line plot for historical humidities
plt.plot(dates, humidities, marker='o', linestyle='-', color='green', label='Humidity (%)')
plt.ylabel('Humidity (%)')

plt.title('Historical Weather Data for Montreal')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Use today's data to estimate the probability of rain tomorrow
today_data = weather_data['list'][0]
today_temperature = today_data['main']['temp'] - 273.15
today_humidity = today_data['main']['humidity']

# Perform your prediction for tomorrow's weather based on today's data
# For example, you can use a simple rule like if today's temperature is high and humidity is high, predict rain tomorrow.

# Example: If temperature is above 25°C and humidity is above 80%, predict rain tomorrow
if today_temperature > 25 and today_humidity > 80:
    prediction = "It will rain tomorrow."
else:
    prediction = "It won't rain tomorrow."

print(f"Today's Prediction: {prediction}")

plt.show()
