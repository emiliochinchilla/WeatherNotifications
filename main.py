import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

#OneWeather API
API_KEY = os.getenv("API_KEY")
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.getenv("account_sid") #Twilio
auth_token = os.getenv("auth_token")
print(API_KEY, account_sid, auth_token)

parameters = {
    "lat" : 0,
    "lon" : 0,
    "cnt": 4,
    "appid" : API_KEY
}


response = requests.get(END_POINT, params=parameters)
response.raise_for_status()

weather_data = response.json()

# weather_code_list = [weather["weather"][0]["id"] for weather in weather_data["list"]]
# print(weather_code_list)

will_rain = False

for weather in weather_data["list"]:
     if weather["weather"][0]["id"] < 700:
         will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+506"
    )
    print(message.status)