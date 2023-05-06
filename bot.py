from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

file_nomor = "nomor.txt"
CHROMEDRIVER_PATH = "C:\chromeDriver"
MESSAGE_BOX_XPATH = '//div[@class="_3FRCZ copyable-text selectable-text"][@data-tab="6"]'
SEND_BUTTON_XPATH = '//button[@class="_3M-N-"]'

def get_cookies(driver):
    pickle.dump(driver.get_cookies(), open('cookies.pkl', 'wb'))
    return pickle.load(open('cookies.pkl', 'rb'))

def set_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)

def option():
    opsi = webdriver.ChromeOptions()
    return opsi.add_argument('--disable-usb-devices')

def read():
    with open(file_nomor, mode="r") as file:
        return file.readlines()

def send(driver, phone_number, message):
    # membuka halaman dengan nomor tertentu
    driver.get(f'https://web.whatsapp.com/send?phone={phone_number}')
    time.sleep(5)
    # mencari message box dan mengirim pesan
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, MESSAGE_BOX_XPATH)))
    message_box = driver.find_element_by_xpath(MESSAGE_BOX_XPATH)
    message_box.send_keys(message)
    send_button = driver.find_element_by_xpath(SEND_BUTTON_XPATH)
    send_button.click()
    time.sleep(3)

def main():
    # membaca nomor
    phone_numbers = read()
    #pesan dari user
    message = input("Masukkan pesan: ")
    # menginisialisasi driver dan membuka whatsapp web
    driver = webdriver.Chrome(CHROMEDRIVER_PATH,options=option())
    driver.get('https://web.whatsapp.com/'),
    set_cookies(driver, get_cookies(driver))
    # menunggu hingga user login
    input("tekan enter setelah scan QR code ")
    # mengirim pesan ke setiap nomor
    for phone_number in phone_numbers:
        send(driver, phone_number, message)
    driver.quit()

if __name__ == '__main__':
    main()