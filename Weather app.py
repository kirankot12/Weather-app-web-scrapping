from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from tkinter import *
import requests 
import json
from datetime import datetime

#Creating the window
root = Tk()
root.geometry("400x400") # size of window
root.resizable(0,0) #creating a fixed size
root.title("Kiran Kot weather app") #title of the window

city_value = StringVar()

def showWeather():
    api_key = "007e1f60df5cfb9c9d589a9b5614cc85"
    city_name = city_value.get()
    weather_url = "https://api.opnweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" +api_key
    
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")
    
    if weather_info["cod"] == 200:
        kelvin = 273
        
        temp = int(weather_info["main"]["temp"] - kelvin )
        feels_like_temp = int(weather_info["main"]["feels_like"] - kelvin )
        pressure = weather_info ["main"]["pressure"]
        humidity = weather_info["main"]["humidity"]
        wind_speed = weather_info["wind"]["speed"] * 3.6 
        sunrise = weather_info["sys"]["sunset"]
        sunset = weather_info["sys"]["sunset"]
        timezone = weather_info [ "timezone"]
        cloudy = weather_info["clouds"]["all"]
        description = weather_info ["weather"][0]["description"]
    
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
    
        weather = f"\nweather of: {city_name}\nTemperature (Celsius): {temp} \nFeels like in (Celsius): {feels_like_temp}\nPressure:{pressure} hPa\nHumidity: {humidity}%\nSunrise at  {sunrise_time} and {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else: 
        weather = f"\n\tweather for '{city_name}' not Found!\n\tKindly Enter valid City name! "
    tfield.insert(INSERT, weather)
    
    def time_format_for_location(utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()
        
city_head = Label(root, text = "enter City name", font = "Arial 12 bold").pack(pady=10)
inp_city = Entry(root, textvariable = city_value, width= 24, font="Arial 14 bold"). pack()

Button(root, command = showWeather, text ="The Weather is:", font ='arial 12 bold').pack(pady=10)
tfield = Text(root, width= 46, height=10)
tfield.pack()
root.mainloop()    
