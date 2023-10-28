from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyttsx3
import speech_recognition as sr
import os
from bs4 import BeautifulSoup
import time
def check_unread_messages():
    crome_path = "C:/Users/dhanu/AppData/Local/Google/Chrome/User Data/Dhanush GN"
    option = webdriver.ChromeOptions()
    option.add_argument(f"--user-data-dir={crome_path}")
    option.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    option.add_argument('--on-sandbox')
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com/')

    wait = WebDriverWait(driver, 100)

    unread_senders = []

    while True:
        
    
                try:
                    # Check for unread messages
                    chats = driver.find_elements(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div')
                    for chat in chats:
                        # Check if the chat is unread by looking for an unread indicator
                        if chat.find_element(By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span'):
                            sender_name = chat.find_element(By.XPATH, './/span[@title]')
                            sender_name = sender_name.get_attribute('title')
                            unread_senders.append(sender_name)

                    # Delay for a few seconds to allow the page to load
                    time.sleep(3)

                    # Scroll to load more chats (adjust as needed)
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", driver.find_element(By.XPATH, '//*[@id="pane-side"]'))
                    time.sleep(2)  # Wait for new chats to load

                except KeyboardInterrupt:
                    break
                
                return unread_senders

if __name__ == "__main__":
    unread_senders = check_unread_messages()
    if unread_senders:
        print("Unread messages from the following senders:")
        for sender in unread_senders:
            print(sender)
    else:
        print("No unread messages found.")
