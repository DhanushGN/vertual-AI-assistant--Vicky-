from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service

warnings.simplefilter("ignore")

try:
    url = "https://dictation.io/speech"

    chrome_driver_path = 'chromedriver.exe'
    chrome_options = Options()
    chrome_options.headless = False
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    service = Service(chrome_driver_path)
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Disable UI pop-ups for media access
    chrome_options.add_argument("--use-fake-device-for-media-stream")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    
    try:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div").click()

    except:
        pass
        
    sleep(15)

    # Execute JavaScript to enable microphone access
    driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')
    sleep(1)

    # Click the "Clear" button to reset
    clear_button_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]'
    driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
    sleep(1)

    # Click the start button
    start_button_xpath = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
    driver.find_element(by=By.XPATH, value=start_button_xpath).click()
    print("Microphone is turned on")

except Exception as e:
    print("Error: Unable to configure the ChromeDriver properly.")
    print("To resolve this error, make sure to set up the ChromeDriver correctly.")
    print(e)

# Continuous loop for capturing and writing text
while True:
    # Get the text from the dictation interface
    text_element_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[2]'
    text = driver.find_element(by=By.XPATH, value=text_element_xpath).text

    if len(text) == 0:
        pass
    else:
        # Click the "Clear" button to reset
        driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
        text = text.strip()
        
        # Write the text to a file
        output_file_path = "SpeechRecognition.txt"
        with open(output_file_path, "w") as file_write:
            file_write.write(text)
