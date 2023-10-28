import datetime
import pyttsx3

MASTER="Dhanush"
NICK_NAME="Boss"
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',160)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f":   {audio}")
    print("   ")
    Assistant.runAndWait()

def time():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    Speak(f"{NICK_NAME}, it's {strTime}")