import pywhatkit as pwk
import pyautogui
import time
from tkinter import Tk, filedialog, messagebox, Button, Label, Text, PhotoImage, END

# Fungsi membaca nomor dari file
def read_numbers(file_name):
    with open(file_name, mode="r") as file:
        return file.readlines()

# Fungsi membaca pesan dari file
def read_message(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        return file.read()

# Fungsi untuk menunggu hingga WhatsApp Web siap untuk interaksi
def wait_for_whatsapp_web():
    while True:
        try:
            pwk.search("https://web.whatsapp.com/send?phone=")
            time.sleep(1)
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

# Fungsi untuk mengirim pesan
def send_message(numbers, message):
    wait_for_whatsapp_web()
    time.sleep(5) # Menunggu tambahan waktu setelah WhatsApp Web siap
    for number in numbers:
        try:
            pwk.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True)
            pyautogui.press("enter")  # Menunggu waktu yang ditentukan oleh pengguna
        except Exception as e:
            print(f"Error: {e}")
            return False
    return True

# Fungsi untuk mengirim pesan dan menampilkan notifikasi
def send_and_notify():
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
    while not message:
        print("Error: Pesan tidak boleh kosong.")
        return

    # Tampilkan konfirmasi menggunakan MessageBox
    confirm = messagebox.askquestion("Konfirmasi", "Anda yakin ingin mengirim pesan?")
    if confirm == "yes":
        send_stat = send_message(numbers, message)
        if send_stat:
            messagebox.showinfo("Informasi", "Pesan berhasil terkirim.")
        else:
            messagebox.showerror("Error", "Pesan gagal terkirim.")
    else:
        messagebox.showinfo("Informasi", "Pesan dibatalkan.")

# Fungsi untuk memilih file nomor
def choose_numbers_file():
    file_path = filedialog.askopenfilename(title="Pilih File Nomor", filetypes=[("Text Files", "*.txt")])
    numbers_text.delete("1.0", END)
    numbers_text.insert(END, file_path)

# Fungsi untuk memilih file pesan
def choose_message_file():
    file_path = filedialog.askopenfilename(title="Pilih File Pesan", filetypes=[("Text Files", "*.txt")])
    message_text.delete("1.0", END)
    message_text.insert(END, file_path)

# Membuat GUI
window = Tk()
window.title("Aplikasi Pengiriman Pesan WhatsApp")
window.geometry("650x300")
bg_image = PhotoImage(file="E:\BOT\img\Black-Gradiant.png")

bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

numbers_label = Label(window, text="File Nomor:", font= ('Helvetica bold', 10),)
numbers_label.pack()

numbers_text = Text(window, height=2.5, cursor="pencil",)
numbers_text.pack()

numbers_button = Button(window, text="Pilih", cursor="hand1", command=choose_numbers_file)
numbers_button.pack()

message_label = Label(window, text="File Pesan:", font= ('Helvetica bold', 10))
message_label.pack()

message_text = Text(window, height=2.5, cursor="pencil")
message_text.pack()

message_button = Button(window, text="Pilih", command=choose_message_file, cursor="hand1")
message_button.pack()

send_button = Button(window, activeforeground="green", text="Kirim Pesan", command=send_and_notify, cursor="hand1")
send_button.pack()

window.mainloop()
