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
@app.route('/wishMe')
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!") 
  
    assname =("Daisy 1 point o")
    speak("I am your Virtual  Assistant")
    speak(assname)
    return redirect('command.html')
def usrname():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome Mister")
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
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

import json 

@app.route('/command')
def command():
	return render_template('command.html')
	

@app.route('/answer', methods=['POST'])
def answer():
	# if command == "who are you":
	#     answer = ("I am yappola \_(^^)_/")
	#     return render_template('command.html',answer=answer)






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
    app.run(debug=True,host="127.0.0.1",port=8679)
	clear = lambda: os.system('cls')
	wishMe()
	usrname()
     
 
