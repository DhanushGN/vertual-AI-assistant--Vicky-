from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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


def send__call(n):
    Speak("Working on it")
    n=n.replace("send","")
    n=n.replace("call","")
    n=n.replace("voice","")
    n=n.replace("to","")
    n=n.replace("vicky","")
    n=n.replace("hey","")
    world='that'
    name_pick =n.find(world)
    content_pick=name_pick+len(world)
    name=n[:name_pick]
    name=name.replace(" ","")
    content=n[content_pick:]
    print(name)
    print(content)
    if name=="dhanush":
        to_num="+917022634688"
    account_sid='AC03e4a03c45528b93a336f3cc1bdf08b8'
    auth_token='837405295f6510412eacab3d53005495'
    client=Client(account_sid,auth_token)
    message=client.calls \
            .create(
                twiml=f'<Response><Say>hey i am Vicky virtual assistent, dhanush leaved as voice message to you that is -{content}</Say></Response>',
                from_='+12055649250',
                to=to_num     
                )
    Speak(f"it's delivered {NICK_NAME}")