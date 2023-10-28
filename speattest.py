import pyttsx3
import speech_recognition as sr
import os

MASTER="Dhanush"
NICK_NAME="BOSS"
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[2].id)
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
    

query=Takecommand()
Speak(f"what you want to search on youtube,sir")