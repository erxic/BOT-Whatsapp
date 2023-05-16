import pywhatkit as pwk
import pyautogui
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib, urllib.parse
from tkinter import Tk, filedialog, messagebox, Button, Label, Text, PhotoImage, END


def read_numbers(file_name):
    with open(file_name, mode="r") as file:
        return file.read().splitlines()

def read_message(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        return file.read()

# Fungsi mengambil nomor pertama untuk pengecekan 
def get_first_number(numbers_file):
    numbers = read_numbers(numbers_file)
    if not numbers:
        print("Error: File nomor kosong!")
        return None
    return numbers[0]

# Fungsi mengambil pesan untuk pengecekan 
def get_message(message_file):
    message = read_message(message_file)
    if not message:
        print("Error: File Pesan kosong!")
        return None
    return message


# Fungsi untuk mengecek apakah whatsapp web sudah siap untuk berinteraksi secara penuh
def wait_for_whatsapp_web(phone_in_url, message_in_url):
    while True:
        try:
            encoded_message = urllib.parse.quote(message_in_url)
            address = f"https://web.whatsapp.com/send?phone={phone_in_url}&text={encoded_message}" 
            req = Request(address)
            html = urlopen(req).read() # Untuk mendapatkan html
            data = BeautifulSoup(html, 'html.parser') # Melakukan parsing pada html
            table = data.find_all("div", {"class": "_2xy_p _3XKXx"})[0] # Mencari elemen tertentu 
            if not table:
                time.sleep(1)
                break
        except Exception as e:
            print(f"Error: {e}")
            continue


def send_message(numbers, message):
    phone_in_url = get_first_number(numbers)
    message_in_url = get_message(message)
    if not message_in_url:
        return False
    wait_for_whatsapp_web(phone_in_url, message_in_url)
    time.sleep(3)
    for number in numbers:
        try:
            pwk.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True)
            pyautogui.press("enter") 
        except Exception as e:
            print(f"Error: {e}")
            return False
    return True

# Send pada GUI dan Info
def send_and_info():
    numbers_file = numbers_text.get("1.0", END).strip()
    message_file = message_text.get("1.0", END).strip()
    if not numbers_file:
        print("Error: File nomor tidak dipilih.")
        return
    if not message_file:
        print("Error: File pesan tidak dipilih.")
        return
    numbers = read_numbers(numbers_file)
    message = read_message(message_file)
    send_stat = False
    while not send_stat:
        if not message:
            print("Error: Pesan tidak boleh kosong.")
            break
        confirm = messagebox.askquestion("Konfirmasi", "Anda yakin ingin mengirim pesan?")
        if confirm == "yes":
            send_stat = send_message(numbers, message)
            if send_stat:
                print("Informasi", "Pesan berhasil terkirim.")
            else:
                messagebox.showerror("Error", "Pesan gagal terkirim.")
        else:
            messagebox.showinfo("Informasi", "Pesan dibatalkan.")

def choose_numbers_file():
    file_path = filedialog.askopenfilename(title="Pilih File Nomor", filetypes=[("Text Files", "*.txt")])
    numbers_text.delete("1.0", END)
    numbers_text.insert(END, file_path)


def choose_message_file():
    file_path = filedialog.askopenfilename(title="Pilih File Pesan", filetypes=[("Text Files", "*.txt")])
    message_text.delete("1.0", END)
    message_text.insert(END, file_path)

# GUI
window = Tk()
window.title("Aplikasi Pengiriman Pesan WhatsApp")
window.geometry("650x300")
bg_image = PhotoImage(file="E:\BOT\img\Black-Gradiant.png")

bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

numbers_label = Label(window, text="File Nomor:", font= ('Helvetica bold', 10))
numbers_label.pack()

numbers_text = Text(window, height=2.5)
numbers_text.pack()

numbers_button = Button(window, text="Pilih", command=choose_numbers_file)
numbers_button.pack()

message_label = Label(window, text="File Pesan:", font= ('Helvetica bold', 10))
message_label.pack()

message_text = Text(window, height=2.5)
message_text.pack()

message_button = Button(window, text="Pilih", command=choose_message_file)
message_button.pack()

send_button = Button(window, activeforeground="green", text="Kirim Pesan", command=send_and_info)
send_button.pack()

window.mainloop()
