import webbrowser as web
from time import sleep
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyttsx3
import pywhatkit
import keyboard
import speech_recognition as sr
import os
import pyautogui 
import pyttsx3
import speech_recognition as sr
import os

MASTER="Dhanush"
NICK_NAME="BOSS"
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f":   {audio}")
    print("   ")
    Assistant.runAndWait()


def Takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.......")
        command.pause_threshold=1
        audio = command.listen(source)

        try:
            print("Recongnizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said :{query}")

        except Exception as Error:
            return "none"
        return query.lower()

def openyoutube():
    while True:     
        Speak(f"what you want to search on youtube,sir")
        query=Takecommand()
        if "nothing else" in query:
            break
        else:
            url="https://www.youtube.com/results?search_query="+query     
            web.open(url)
            sleep(5)
            Speak("this is what i found")
            try:
                pywhatkit.playonyt(query)
            except:
                Speak("")
            Speak("This may also help you sir ")
            while True:
                query=Takecommand()
                if 'stop play' in query:
                    keyboard.press_and_release('space')
                elif 'mute unmute' in query:
                     keyboard.press_and_release('m')
                elif 'forward' in query:
                     keyboard.press_and_release('alt+26')
                elif 'backward' in query:
                     keyboard.press_and_release('alt+27')
                elif 'increase volume' in query:
                     keyboard.press_and_release('alt+24')
                elif 'decrease volume' in query:
                     keyboard.press_and_release('alt+25')
                elif 'enable captions' in query:
                     keyboard.press_and_release('c')
                elif 'disable captions' in query:
                     keyboard.press_and_release('c')
                elif 'next video' in query:
                     keyboard.press_and_release('shift+n')
                elif 'previous video' in query:
                     keyboard.press_and_release('shift+p')
                elif 'ok' in query:
                     break
        

openyoutube()