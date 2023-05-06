from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
from webdriver_manager.chrome import ChromeDriverManager

# Constants
file_nomor = "nomor.txt"
CHROMEDRIVER_PATH = "C:\chromeDriver\chromedriver.exe"
MESSAGE_BOX_XPATH = '//div[@class="_3FRCZ copyable-text selectable-text"][@data-tab="6"]'
SEND_BUTTON_XPATH = '//button[@class="_3M-N-"]'

# Functions
def get_cookies(driver):
    ##Get WhatsApp web cookies
    driver.get('https://web.whatsapp.com/')
    input("Scan QR code kemudian tekan enter ")
    pickle.dump(driver.get_cookies(), open('cookies.pkl', 'wb'))
    return pickle.load(open('cookies.pkl', 'rb'))

def set_cookies(driver, cookies):
    ##Set WhatsApp web cookies
    for cookie in cookies:
        driver.add_cookie(cookie)

def read(file_nomor):
    ##baca nomor dari file
    with open(file_nomor, mode="r") as file:
        return file.readlines()

def send(driver, phone_number, message):
    ##mengirim pesan dan mencari element message box
    driver.get(f'https://web.whatsapp.com/send?phone={phone_number}')
    time.sleep(5)
    try:
        wait = WebDriverWait(driver, 25)
        wait.until(EC.presence_of_element_located((By.XPATH, MESSAGE_BOX_XPATH)))
        message_box = driver.find_element_by_xpath(MESSAGE_BOX_XPATH)
        message_box.send_keys(message)
        send_button = driver.find_element_by_xpath(SEND_BUTTON_XPATH)
        send_button.click()
        time.sleep(5)
    except Exception:
        print(f"Error sending message to {phone_number}")

def main():
    ## membaca nomor
    phone_numbers = read(file_nomor)
    ## pesan dari user
    message = input("Masukkan pesan: ")
    ## Inisialisasi driver dan set cookies
    driver = webdriver.Chrome(ChromeDriverManager().install())
    set_cookies(driver, get_cookies(driver))
    ## mengirim pesan ke setiap nomor
    for phone_number in phone_numbers:
        send(driver, phone_number, message)
    driver.quit()

if __name__ == '__main__':
    main()
