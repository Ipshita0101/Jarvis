import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import tkinter as tk
from tkinter import StringVar, Label, scrolledtext


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening") 

    speak("i am Jarvis Mam.Please tell me how may I help you")               

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        Query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {Query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return"None"
    return Query


if __name__=="__main__":
   # speak("Hi i am jarvis")
    wishme()
    while True:
    # if 1:
        Query = takecommand().lower()
    # logic for executing task based on task

        if 'wikipedia' in Query:
            speak("Searching wikipedia.....")
            Query = Query.replace("wikipedia", " ")
            results = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in Query:
            webbrowser.open("youtube.com")

        elif 'open google' in Query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in Query:
            webbrowser.open("stackoverflow.com")   

        elif  'open browser' in Query:
            browserPath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(browserPath)

        elif 'open whatsapp' in Query:
            appPath = "C:\\Users\\dell\\OneDrive\\Desktop\\WhatsApp.lnk"
            os.startfile(appPath) 


        elif 'the time' in Query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the is time {strTime}")    
        
        elif 'open code' in Query:
            codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

