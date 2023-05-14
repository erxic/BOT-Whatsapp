from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time

# Fungsi membaca nomor dari file
def read_numbers(file_name):
    with open(file_name, mode="r") as file:
        return file.readlines()

# Fungsi membaca pesan dari file
def read_message(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        return file.read()

# Fungsi untuk mengirim pesan
def send_message(numbers, message):
    driver = webdriver.Chrome()  # Ganti dengan driver yang sesuai, seperti Firefox atau Safari
    driver.get("https://web.whatsapp.com/")
    time.sleep(20)  # Tunggu pengguna untuk login ke WhatsApp Web

    for number in numbers:
        try:
            # Buka chat dengan nomor telepon
            chat_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
            chat_input.send_keys(number)
            time.sleep(2)
            chat_input.send_keys(Keys.ENTER)
            time.sleep(2)

            # Ketik pesan
            chat_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
            chat_input.send_keys(message)

            # Kirim pesan
            send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
            send_button.click()

            if not wait_for_message_sent(driver):
                print(f"Error: Pesan ke nomor {number} gagal terkirim")
                time.sleep(1)
                print(f"Mengirim ulang pesan ke nomor {number}")

                # Ketik pesan lagi
                chat_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
                chat_input.send_keys(message)

                # Kirim pesan lagi
                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click()
        except Exception as e:
            print(f"Error: {e}")
            driver.quit()
            return False

    driver.quit()
    return True

# Fungsi untuk menunggu pesan terkirim
def wait_for_message_sent(driver):
    timeout = 30  # Waktu maksimal menunggu dalam detik
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Implementasikan logika pengecekan pesan terkirim di sini
        # Misalnya, Anda dapat memeriksa apakah pesan sudah muncul dalam riwayat chat atau tampilan notifikasi pesan terkirim
        # Jika pesan terkirim, kembalikan True
        # Jika pesan belum terkirim, lanjutkan menunggu
        pass
    return False

def main():
    ## Memilih file nomor menggunakan GUI
    Tk().withdraw()
    numbers_file = askopenfilename(title="Pilih File Nomor", filetypes=[("Text Files", "*.txt")])
    if not numbers_file:
        print("File nomor tidak dipilih. Program berhenti.")
        return False

    numbers = read_numbers(numbers_file)

    ## Memilih file pesan menggunakan GUI
    Tk().withdraw()
    message_file = askopenfilename(title="Pilih File Pesan", filetypes=[("Text Files", "*.txt")])
    if not message_file:

        print("File pesan tidak dipilih. Program berhenti.")
        return False

    message = read_message(message_file)
    while not message:
        print("Pesan tidak boleh kosong!")
        message = read_message(message_file)
        Tk().withdraw()
        message_file = askopenfilename(title="Pilih File Pesan", filetypes=[("Text Files", "*.txt")])
        if not message_file:
            print("File pesan tidak dipilih. Program berhenti.")
            return False

    send_stat = send_message(numbers, message)
    if send_stat:
        print("Pesan berhasil terkirim")
    else:
        print("Pesan gagal terkirim")

if __name__ == '__main__':
    main()
