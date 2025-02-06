# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:23:17 2025

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:20:16 2025

@author: Administrator
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import json
import sys


listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
def weather(city):
    """Fetches weather data for a given city using OpenWeatherMap API."""
    api_key = "bcde558ca3fe60ab9793019b415bcfcf"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"

    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") != 200:  # Check if request was successful
        return f"Sorry, I couldn't find the weather for {city}. Please check the city name."

    try:
        temp_kelvin = data["main"]["temp"]
        temp_celsius = round(temp_kelvin - 273.15, 2)  # Convert Kelvin to Celsius
        return f"The current temperature in {city} is {temp_celsius} degrees Celsius."
    except KeyError:
        return "Weather data is not available at the moment."


def user_commands():
    command = ""  
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'anagha' in command:
                command = command.replace('anagha', '').strip()
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Network error. Please check your internet connection.")
    except Exception as e:
        print(f"Error: {e}")

    return command  

    
    
def run_alexa():
    command = user_commands()
    if 'play a song' in command:
        song = 'Arijit Singh'
        engine_talk('Playing some music')
        print("Playing....")
        pywhatkit.playonyt(song)
    elif 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'what is' in command:
        name = command.replace('what is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'explain' in command:
        name = command.replace('explain' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'tell me the weather' in command:
        engine_talk('Please tell the name of the city')
        city = user_commands()
        weather_api = weather(city)
        engine_talk(weather_api + 'degree fahreneit' )
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')
        print("I didn't hear you properly")
        
while True:
    run_alexa()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    