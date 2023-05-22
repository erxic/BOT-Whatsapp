import pywhatkit as pwk
import os
import pyautogui
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.parse
from tkinter import Tk, filedialog, messagebox, Button, Label, Text, PhotoImage, END


def read_file(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        return file.read()


def read_numbers(file_name):
    numbers = read_file(file_name).rstrip()
    return numbers.splitlines()


def read_message(file_name):
    return read_file(file_name)


def wait_for_whatsapp_web(phone_in_url, message_in_url):
    while True:
        try:
            encoded_message = urllib.parse.quote(message_in_url)
            address = f"https://web.whatsapp.com/send?phone={phone_in_url}&text={encoded_message}"
            req = Request(address)
            html = urlopen(req).read()
            data = BeautifulSoup(html, 'html.parser')
            table = data.find_all("div", {"class": "_2xy_p _3XKXx"})
            if not table in data:
                time.sleep(1)
                break
        except Exception as e:
            print(f"Error: {e}")
            continue


def send_message(numbers, message):
    if not numbers:
        return False
    num_in = numbers[0] 
    mess_in = message
    wait_for_whatsapp_web(num_in, mess_in)
    time.sleep(2)
    for number in numbers:
        try:
            pwk.sendwhatmsg_instantly(number, message, tab_close=True)
            pyautogui.press("enter")
        except Exception as e:
            print(f"Error: {e}")
    return True


def send_and_info():
    numbers_file = numbers_text.get("1.0", END).rstrip()
    message_file = message_text.get("1.0", END).rstrip()
    if not numbers_file:
        print("Error: File nomor tidak dipilih.")
        return
    if not message_file:
        print("Error: File pesan tidak dipilih.")
        return
    numbers = read_numbers(numbers_file)
    if not numbers:
        print("Error: Tidak ada nomor yang ditemukan dalam file.")
        return
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
                break
        else:
            messagebox.showinfo("Informasi", "Pesan dibatalkan.")
            break


def choose_file(file_text):
    file_path = filedialog.askopenfilename(title="Pilih File", filetypes=[("Text Files", "*.txt")])
    file_text.delete("1.0", END)
    file_text.insert(END, file_path)


window = Tk()
window.title("Aplikasi Pengiriman Pesan WhatsApp")
window.geometry("650x300")
user_path = os.getcwd()
image_file_path = os.path.join(user_path, "img", "Black-Gradiant.png")
bg_image = PhotoImage(file=image_file_path)


bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

numbers_label = Label(window, text="File Nomor:", font=('Helvetica bold', 10))
numbers_label.pack()

numbers_text = Text(window, height=2.5)
numbers_text.pack()

numbers_button = Button(window, text="Pilih", command=lambda: choose_file(numbers_text))
numbers_button.pack()

message_label = Label(window, text="File Pesan:", font=('Helvetica bold', 10))
message_label.pack()

message_text = Text(window, height=2.5)
message_text.pack()

message_button = Button(window, text="Pilih", command=lambda: choose_file(message_text))
message_button.pack()

send_button = Button(window, activeforeground="green", text="Kirim Pesan", command=send_and_info)
send_button.pack()

window.mainloop()

        