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

def send_msg(n):

    n=n.replace("hey","")
    n=n.replace("vicky","")
    n=n.replace("send","")
    n=n.replace("message","")
    n=n.replace("whatsapp","")
    n=n.replace("to","")
    print(n)
    world='that'
    name_pick =n.find(world)
    content_pick=name_pick+len(world)
    name=n[:name_pick]
    name=name.replace(" ","")
    content=n[content_pick:]
    print(name)
    print(content)
    content=(f"Vicky:- {content}")
    from contact import get_contact_name
    name=get_contact_name(name)
    
    crome_path="C:/Users/dhanu/AppData/Local/Google/Chrome/User Data/Dhanush GN"
    option = webdriver.ChromeOptions()
    option.add_argument(f"--user-data-dir={crome_path}")
    option.binary_location="C:/Program Files/Google/Chrome/Application/chrome.exe"
    option.add_argument('--on-sandbox')
    driver=webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com/')


    wait=WebDriverWait(driver,100)
     
    target=f'"{name}"'
    TEXT=content
    print(target)
    print(TEXT)
    contact_path='//span[contains(@title,'+ target +')]'
    contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()
    msg_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
    msg_box=wait.until(EC.presence_of_element_located((By.XPATH,msg_box_path)))
    msg_box.send_keys(TEXT+Keys.ENTER)
    sleep(10)
    Speak(f"it's delivered {NICK_NAME}")
    
