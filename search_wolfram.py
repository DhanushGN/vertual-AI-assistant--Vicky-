import pyttsx3
import wolframalpha

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

def wolf(n):
    n=n.replace("hey","")
    n=n.replace("vicky","")
    n=n.replace("search","")
    n=n.replace("wolfram","")
    n=n.replace("in","")
    api_key="8U2J99-WAWGEVQAJ3"
    request=wolframalpha.Client(api_key)
    request=request.query(n)
 
    try:
          answer=next(request.results).text
          Speak(answer)

    except:
         Speak("I can't receive anything")
