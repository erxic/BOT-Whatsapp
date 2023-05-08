import pywhatkit as pwk
import pyautogui
import time 


def read(file_nomor):
    with open(file_nomor, mode="r") as file:
        return file.readlines()
    
def send(numbers, message):
    for number in numbers:
        try:
            pwk.sendwhatmsg_instantly(number, message, 0, True)
            time.sleep(3) 
            window_position = pyautogui.locateOnScreen('apple-touch-icon.png',)
            input_field_position = pyautogui.locateOnScreen('',)
            send_button_x = window_position.left + window_position.width - 50
            send_button_y = input_field_position.top + input_field_position.height + 10
            pyautogui.click(send_button_x, send_button_y)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return True

def main():
    file_numbers = "nomor.txt"
    numbers = read(file_numbers)
    message = input("Masukkan Pesan : ")
    send_stat = send(numbers, message)
    if send_stat:
        print("Pesan berhasil terkirim")
    else:
        print("Pesan gagal terkirim")
    

if __name__ == '__main__':
    main()
