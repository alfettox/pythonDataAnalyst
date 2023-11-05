# simple computer program that can predict whether it will rain tomorrow based on today's weather conditions. You'll use a simplified model that makes predictions based on two factors: temperature and humidity. Here's what you need to do:

# Collect data

# Day	Temperature (°C)	Humidity (%)	Will It Rain Tomorrow?
# 1	            28	            70	                    No
# 2	            22	            85	                    Yes
# 3	            30	            60	                    No
# 4	            18	            95	                    Yes
# 5	            25	            75	                    No

# Step 1: Gather Data
data = [
    (28, 70, "N"),
    (22, 85, "Y"),
    (30, 60, "N"),
    (18, 95, "Y"),
    (25, 75, "N")
]

def predict_weather(temperature, humidity):
    if temperature > 25 and humidity > 80:
        return "Y"  # rain
    else:
        return "N"   # won't rain

t = int(input("Insert temperature: "))
h = int(input("Insert humidity: "))

prediction = predict_weather(t, h)

print(f"Prediction: Will it rain tomorrow? {prediction}")
