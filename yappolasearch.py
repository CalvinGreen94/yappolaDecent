import numpy as np
from flask import send_file
from flask import Flask, session,abort,request, jsonify, render_template,redirect,url_for,flash,redirect
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler as mini
import wolframalpha
import wikipedia
import os
import stripe
import datetime
import subprocess
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import webbrowser
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from espeakng import ESpeakNG 
import wave 
# import pyaudio 
# import StringIO
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
daisy = 'dAIsy'
app = Flask(__name__)
app.secret_key = "You Come t0 m3 0n th3 dai 0f mah dAUghterZZzz wedDinng BITCH!"
pub_key ='pk_live_2pO0yUvt9xKyjAo9rca8Vkc600FWtgJuqZ'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
app_id = "5PL6G8-KRH7PUAAH5"
@app.route('/wishMe')
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!") 
  
    assname =("Yappola 1 point o")
    speak("I am your Virtual  Assistant")
    speak(assname)
    return redirect('command.html')
def usrname():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome ", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, ")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 10
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice. Try again") 
        return "None"
     
    return query

import json 

@app.route('/command')
def command():
	return render_template('command.html')
	

@app.route('/answer', methods=['POST'])
def answer():
    command=request.form['Talk to yappola:']
	#
        while True:
		try:
		    app_id = "5PL6G8-KRH7PUAAH5"
		    client = wolframalpha.Client(app_id)
	            res = client.query(command)
		    answers = next(res.results).text 
		    answers = str(answers) 
		    voice = speak("The answer is "+answers)
		except:
				try:
					command=command.split(' ')
					command = command.join(command[2:]) #input[2:]
					answers = wikipedia.summary(command) 
					voice = speak("Searching for Command "+command)
				except:
					answers = 'I dont know the answer' 
					voice = speak(answers)
		break
	return render_template('command.html',answers=answers) #files=files,url=url filename=filename


# # @app.route('/home')
# # def home():
# # 	return render_template('command.html')#code=301

if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1",port=8888)
	# clear = lambda: os.system('cls')
     
 #    # This Function will clean any
 #    # command before execution of this python file
 #    clear()
	# wishMe()
 #    usrname()
     
 #    while True:
         
 #        query = takeCommand().lower()
 #        if 'wikipedia' in query:
 #            speak('Searching Wikipedia...')
 #            query = query.replace("wikipedia", "")
 #            results = wikipedia.summary(query, sentences = 3)
 #            speak("According to Wikipedia")
 #            print(results)
 #            speak(results)
 
 #        elif 'open youtube' in query:
 #            speak("Here you go to Youtube\n")
 #            webbrowser.open("youtube.com")
 
 #        elif 'open google' in query:
 #            speak("Here you go to Google\n")
 #            webbrowser.open("google.com")
 
 #        elif 'open stackoverflow' in query:
 #            speak("Here you go to Stack Over flow.Happy coding")
 #            webbrowser.open("stackoverflow.com")  
 
 #        elif 'play music' in query or "play song" in query:
 #            speak("Here you go with music")
 #            # music_dir = "G:\\Song"
 #            music_dir = "C:\\Users\\...\\Music"
 #            songs = os.listdir(music_dir)
 #            print(songs)   
 #            random = os.startfile(os.path.join(music_dir, songs[1]))
 
 #        elif 'the time' in query:
 #            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
 #            speak(f"Sir, the time is {strTime}")
 
 #        elif 'open opera' in query:
 #            codePath = r"C:\\Users\\....."
 #            os.startfile(codePath)
 

 
 #        elif 'how are you' in query:
 #            speak("I am fine, Thank you")
 #            speak("How are you,")
 
 #        elif 'fine' in query or "good" in query:
 #            speak("It's good to know that your fine")
 
 #        elif "change my name to" in query:
 #            query = query.replace("change my name to", "")
 #            assname = query
 
 #        elif "change name" in query:
 #            speak("What would you like to call me")
 #            assname = takeCommand()
 #            speak("Thanks for naming me")
 
 #        elif "what's your name" in query or "What is your name" in query:
 #            speak("My friends call me")
 #            speak(assname)
 #            print("My friends call me", assname)
 
 #        elif 'exit' in query:
 #            speak("Thanks for giving me your time")
 #            exit()
 
 #        elif "who made you" in query or "who created you" in query:
 #            speak("I have been created by Yappola.")
             
 #        elif 'joke' in query:
 #            speak(pyjokes.get_joke())
             
 #        elif "calculate" in query:
             
 #            
 #            client = wolframalpha.Client(app_id)
 #            indx = query.lower().split().index('calculate')
 #            query = query.split()[indx + 1:]
 #            res = client.query(' '.join(query))
 #            answer = next(res.results).text
 #            print("The answer is " + answer)
 #            speak("The answer is " + answer)
 
 #        elif 'search' in query or 'play' in query:
             
 #            query = query.replace("search", "")
 #            query = query.replace("play", "")         
 #            webbrowser.open(query)
 
 #        elif "who i am" in query:
 #            speak("If you talk then definitely your human.")
 
 #        elif "why you came to world" in query:
 #            speak("Thanks to Gaurav. further It's a secret")
 
 #        elif 'power point presentation' in query:
 #            speak("opening Power Point presentation")
 #            power = r"C:\\Users\\..."
 #            os.startfile(power)
 
 #        elif 'is love' in query:
 #            speak("It is 7th sense that destroy all other senses")
 
 #        elif "who are you" in query:
 #            speak("I am your virtual assistant created by Yappola")
 
 #        elif 'reason for you' in query:
 #            speak("I was created as to enhance NLP by Yappola ")
 
 #        elif 'change background' in query:
 #            ctypes.windll.user32.SystemParametersInfoW(20,
 #                                                       0,
 #                                                       "Location of wallpaper",
 #                                                       0)
 #            speak("Background changed successfully")
 
 #        elif 'open bluestack' in query:
 #            appli = r"C:\\ProgramData\\....."
 #            os.startfile(appli)
 
 
         
 #        elif 'lock window' in query:
 #                speak("locking the device")
 #                ctypes.windll.user32.LockWorkStation()
 
 #        elif 'shutdown system' in query:
 #                speak("Hold On a Sec ! Your system is on its way to shut down")
 #                subprocess.call('shutdown / p /f')
                 
 #        elif 'empty recycle bin' in query:
 #            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
 #            speak("Recycle Bin Recycled")
 
 #        elif "don't listen" in query or "stop listening" in query:
 #            speak("for how much time you want to stop jarvis from listening commands")
 #            a = int(takeCommand())
 #            time.sleep(a)
 #            print(a)
 
 #        elif "where is" in query:
 #            query = query.replace("where is", "")
 #            location = query
 #            speak("User asked to Locate")
 #            speak(location)
 #            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
 #        elif "camera" in query or "take a photo" in query:
 #            ec.capture(0, "Jarvis Camera ", "img.jpg")
 
 #        elif "restart" in query:
 #            subprocess.call(["shutdown", "/r"])
             
 #        elif "hibernate" in query or "sleep" in query:
 #            speak("Hibernating")
 #            subprocess.call("shutdown / h")
 
 #        elif "log off" in query or "sign out" in query:
 #            speak("Make sure all the application are closed before sign-out")
 #            time.sleep(5)
 #            subprocess.call(["shutdown", "/l"])
 
 #        elif "write a note" in query:
 #            speak("What should i write, sir")
 #            note = takeCommand()
 #            file = open('jarvis.txt', 'w')
 #            speak("Sir, Should i include date and time")
 #            snfm = takeCommand()
 #            if 'yes' in snfm or 'sure' in snfm:
 #                strTime = datetime.datetime.now().strftime("% H:% M:% S")
 #                file.write(strTime)
 #                file.write(" :- ")
 #                file.write(note)
 #            else:
 #                file.write(note)
         
 
 #        elif "update assistant" in query:
 #            speak("After downloading file please replace this file with the downloaded one")
 #            url = '# url after uploading file'
 #            r = requests.get(url, stream = True)
             
 #            with open("Voice.py", "wb") as Pypdf:
                 
 #                total_length = int(r.headers.get('content-length'))
                 
 #                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
 #                                       expected_size =(total_length / 1024) + 1):
 #                    if ch:
 #                      Pypdf.write(ch)
                     
 #        # NPPR9-FWDCX-D2C8J-H872K-2YT43
 #        elif "daisy" in query:
             
 #            wishMe()
 #            speak("Yappola 1 point o in your service")
 #            speak(assname)
 
 #        elif "weather" in query:
             
 #            # Google Open weather website
 #            # to get API of Open weather
 #            api_key = "Api key"
 #            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
 #            speak(" City name ")
 #            print("City name : ")
 #            city_name = takeCommand()
 #            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
 #            response = requests.get(complete_url)
 #            x = response.json()
             
 #            if x["cod"] != "404":
 #                y = x["main"]
 #                current_temperature = y["temp"]
 #                current_pressure = y["pressure"]
 #                current_humidiy = y["humidity"]
 #                z = x["weather"]
 #                weather_description = z[0]["description"]
 #                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
 #            else:
 #                speak(" City Not Found ")
             

 #        elif "wikipedia" in query:
 #            webbrowser.open("wikipedia.com")
 
 #        elif "Good Morning" in query:
 #            speak("A warm" +query)
 #            speak("How are you Mister")
 #            speak(assname)
 
 #        # most asked question from google Assistant
 #        elif "will you be my gf" in query or "will you be my bf" in query:  
 #            speak("I'm not sure about, may be you should give me some time")
 
 #        elif "how are you" in query:
 #            speak("I'm fine, glad you asked me that")
 
 #        elif "i love you" in query:
 #            speak("It's hard to understand")
 
 #        elif "what is" in query or "who is" in query:
             
 #            # Use the same API key
 #            # that we have generated earlier
 #            client = wolframalpha.Client(app_id)
 #            res = client.query(query)
             
 #            try:
 #                print(next(res.results).text)
 #                speak(next(res.results).text)
 #            except StopIteration:
 #                print ("No results")
 
 
