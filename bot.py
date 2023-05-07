from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium.webdriver.chrome.service as service

# Constants
file_nomor = "nomor.txt"
MESSAGE_BOX_ELEMENT = 'div[title="Search or start new chat"]'
SEND_BUTTON_ELEMENT = 'div[class="_2xy_p _3XKXx"]'

# Functions
def read(file_nomor):
    ##baca nomor dari file
    with open(file_nomor, mode="r") as file:
        return file.readlines()

def send(driver, phone_number, message):
    ##mengirim pesan dan mencari element message box
    driver.get(f'https://web.whatsapp.com/send?phone={phone_number}')
    time.sleep(5)
    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, MESSAGE_BOX_ELEMENT)))
        message_box = driver.find_element_by_css_selector(By.CSS_SELECTOR,MESSAGE_BOX_ELEMENT)
        message_box.send_keys(message)
        send_button = driver.find_elemnt_by_css_selector(By.CSS_SELECTOR,SEND_BUTTON_ELEMENT)
        send_button.click()
        time.sleep(5)
    except:
        print(f"Error sending message to {phone_number}")

def main():
    ## membaca nomor
    phone_numbers = read(file_nomor)
    ## pesan dari user
    message = input("Masukkan pesan: ")
    ## Inisialisasi driver dan set cookies
    serv = service.Service('C:\chromeDriver\chromedriver.exe')
    driver = webdriver.Chrome(service=serv) 
    driver.get("https://web.whatsapp.com/")
    ## mengirim pesan ke setiap nomor
    for phone_number in phone_numbers:
        send(driver, phone_number, message)
    driver.quit()

if __name__ == '__main__':
    main()
