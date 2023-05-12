import pywhatkit as pwk
import pyautogui
from tkinter import Tk
from tkinter.filedialog import askopenfilename


#Fungsi membaca nomor dari file
def read_numbers(file_name):
    with open(file_name, mode="r") as file:
        return file.readlines()

#fungsi membaca pesan dari file
def read_message(file_name):
    with open(file_name, mode="r",encoding="utf-8") as file:
        return file.read()
    

#fungsi untuk mengirim pesan 
def send_message(numbers, message):
    for number in numbers:
        try:
            pwk.sendwhatmsg_instantly(number, message, tab_close=True)
            pyautogui.press("enter")
        except Exception as e:
            print(f"Error: {e}")
            return False
    return True

def main():
    ## Memilih file nomor menggunakan GUI
    Tk().withdraw()
    numbers_file = askopenfilename(title="Pilih File Nomor", filetypes=[("Text Files", "*.txt")])
    if not numbers_file:
        print("File nomor tidak dipilih. Program berhenti.")
        return

    numbers = read_numbers(numbers_file)
    
    ## Memilih file pesan menggunakan GUI
    Tk().withdraw()
    message_file = askopenfilename(title="Pilih File Pesan", filetypes=[("Text Files", "*.txt")])
    if not message_file:
        print("File pesan tidak dipilih. Program berhenti.")
        return

    message = read_message(message_file)
    while not message:
        print("Pesan tidak boleh kosong!")
        message = read_message(message_file)
    
    send_stat = send_message(numbers, message)
    if send_stat:
        print("Pesan berhasil terkirim")
    else:
        print("Pesan gagal terkirim")

if __name__ == '__main__':
    main()
