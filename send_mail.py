import smtplib
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


def send_email(n):
    Speak("Working on it")
    n=n.replace("send","")
    n=n.replace("mail","")
    n=n.replace("to","")
    n=n.replace("vicky","")
    n=n.replace("hey","")
    world='that'
    name_pick =n.find(world)
    content_pick=name_pick+len(world)
    name=n[:name_pick]
    name=name.replace(" ","")
    content=n[content_pick:]
    if name=="dhanush":
        to="dhanushdhanu7484@gmail.com"

    # Email configuration
    sender_email = "dhanushgn7484@outlook.com"
    sender_password = "Dhanush@7484"
    recipient_email = to
    subject = "Subject of the email"
    message = content

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        Speak(f"it's delivered {NICK_NAME}")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Quit the server
        server.quit()
    

