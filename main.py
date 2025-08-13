import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary 
import requests
from gtts import gTTS
import pygame
import time
import pyjokes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime 
import re
import os
import google.generativeai as genai

#pip install pocketsphinx
recognizer = sr.Recognizer()    #It helps to take speech recognition functionality
engine=pyttsx3.init()

genai.configure(api_key="AI........................................Jk")
model = genai.GenerativeModel(model_name="gemini-2.0-flash")
weather_api_key = "85....................d62"
def speak(text):
    print(f"[🗣️ Jarvis will say]: {text[:100]}...")  # print first 100 chars

    try:
        if len(text.strip()) == 0:
            raise ValueError("Empty text passed to speak()")

        # Limit max length for gTTS
        if len(text) > 500:
            text = text[:500]  # gTTS fails on very long text

        tts = gTTS(text)
        tts.save('temp.mp3')

        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove("temp.mp3")

    except Exception as e:
        print(f"[TTS Error]: {e}")
        print("[🛑 Falling back to pyttsx3]")
        engine.say(text)
        engine.runAndWait()



def clean_response(text):
    # Remove asterisks, markdown, and HTML tags
    text = re.sub(r'\*+', '', text)  # Remove asterisks
    text = re.sub(r'<[^>]*>', '', text)  # Remove HTML tags like <a>, <b>
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove markdown links [text](url)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&')
    return text.strip()


def aiProcess(command):
     try:
          chat = model.start_chat()
          response = chat.send_message(command)
          clean_text = clean_response(response.text)  # clean it before returning
          return clean_text

     except Exception as e:
       print(f"[Gemini error]:{e}")
       return "Sorry, something went wrong with AI."
     
def change_volume(command):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if "mute" in command:
        volume.SetMute(1, None)
        speak("System volume muted.")
    elif "unmute" in command:
        volume.SetMute(0, None)
        speak("System volume unmuted.")
    elif "increase" in command or "up" in command:
        current = volume.GetMasterVolumeLevelScalar()
        new_volume = min(current + 0.1, 1.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        speak("Volume increased.")
    elif "decrease" in command or "down" in command:
        current = volume.GetMasterVolumeLevelScalar()
        new_volume = max(current - 0.1, 0.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        speak("Volume decreased.")
    elif "set volume to" in command:
        try:
            level = int(command.split("set volume to")[-1].strip().split()[0])
            if 0 <= level <= 100:
                volume.SetMasterVolumeLevelScalar(level / 100.0, None)
                speak(f"Volume set to {level} percent.")
            else:
                speak("Please say a number between 0 and 100.")
        except:
            speak("Sorry, I couldn't understand the volume level.")

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Sorry, I couldn't find weather for {city}."

        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]
        wind = data["wind"]["speed"]

        report = f"Weather in {city} is {weather_desc}. Temperature is {temp}°C. Humidity is {humidity}%. Wind speed is {wind} m/s."
        return report

    except Exception as e:
        print(f"[❌ Weather Error]: {str(e)}")
        return "Sorry, I couldn't fetch the weather."




def processcommand(c):
    c = c.lower()
    response = ""

    if "open google" in c:
        webbrowser.open("https://google.com")
        response = "Opening Google..."

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        response = "Opening Facebook..."

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube..."

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        response = "Opening LinkedIn..."

    elif "joke" in c:
        joke = pyjokes.get_joke()
        print(f"[😂 Joke]: {joke}")
        speak(joke)
        response = joke

    elif "play song" in c:
      song_list = "\n".join([f"- {name}" for name in musiclibrary.music.keys()])
      response = f"Here are the available songs:\n{song_list}\nPlease say the name of the song."
      speak(response)
      with sr.Microphone() as source:
        audio = recognizer.listen(source)
        song_name = recognizer.recognize_google(audio).lower()
        found = False
        for title, url in musiclibrary.music.items():
            if song_name in title.lower():
                speak(f"Playing {title}")
                webbrowser.open(url)
                found = True
                break
        if not found:
            speak(f"Sorry, I couldn't find the song {song_name}")

    elif "volume" in c or "mute" in c:
        change_volume(c)
        response = "Volume command executed."
        

    elif "weather in" in c:
        city = c.split("weather in")[-1].strip()
        response = get_weather(city)
       

    elif "time" in c:
        now = datetime.now().strftime("%I:%M %p")
        response = f"The time is {now}"
       

    elif "date" in c:
        today = datetime.now().strftime("%A, %d %B %Y")
        response = f"Today is {today}"
        

    else:
        print("[🤖 Asking Gemini]:", c)
        response = aiProcess(c)
        print("[✅ Gemini said]:", response)

    return response

def run_jarvis_loop():
    speak("Initializing Jarvis.......")
    while True:
        try:  
            with sr.Microphone() as source:
                print("Listening for Jarvis...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
                trigger = recognizer.recognize_google(audio)
            if trigger.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    command_audio = recognizer.listen(source,timeout=5)
                    command = recognizer.recognize_google(command_audio)
                    processcommand(command)
        except sr.UnknownValueError:
                print("Could not understand audio.")
        except sr.RequestError as e:
                print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {str(e)}")
