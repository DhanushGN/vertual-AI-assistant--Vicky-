import wikipedia
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

Speak("hello")

def wiki(query):
    query=query.replace("wikipedia","")
    query=query.replace("vicky","")
    query=query.replace("hey","")
    result=wikipedia.summary(query, sentences=2)
    Speak(result)
