import pyttsx3
import datetime
MASTER="Dhanush"
NICK_NAME="Boss"
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

def wishme():
     hour=int(datetime.datetime.now().hour)

     if hour>=0 and hour<12:
        Speak("Good morning..,"+NICK_NAME)
     elif hour>=12 and hour<18:
          Speak("Good Afternoon..,"+NICK_NAME)
     else:
          Speak("Good Evening..,"+NICK_NAME)
     Speak("How can i help you")