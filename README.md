# BOT-Whatsapp

Bot ini sangat cocok untuk pebisnis online karena mempunyai fitur untuk mengirim pesan/promosi ke client hanya dalam satu perintah untuk 2 atau bahkan sampai 100 nomor 
sekaligus tanpa perlu menyimpan nomor tersebut, tetapi memiliki delay beberapa detik selama mengirim pesan untuk menghindari pemblokiran oleh pihak whatsapp. 

## Set-Up

Jalankan perintah seperti dibawah ini pada terminal komputer anda:

`git clone https://github.com/Tron403/BOT-Whatsapp.git`

atau jika tidak mempunyai git bisa mendownload langsung dalam format zip.


Masuk kedalam direktori BOT-Whatsapp dengan perintah berikut:

- Di Mac/linux `cd BOT-Whatsapp`
- Di Windows `cd .\BOT-Whatsapp\`

Terdapat 3 File yang harus diperhatikan:
  - bot.py
  - nomor.txt
  - pesan.txt

Ubah isi file _nomor.txt_ dengan nomor tujuan anda, Perhatikan format nya dan pastikan mempunyai code country.

Ubah isi file _pesan.txt_ dengan pesan yang anda sampaikan atau produk yang ingin anda promosikan.    
***INGAT UNTUK SELALU MENGUBAH FILE TERSEBUT JIKA INGIN MENGGANTI NOMOR TUJUAN ATAUPUN PESAN***

## Cara Pakai
**PASTIKAN SUDAH LOGIN PADA WHATSAPP WEB ANDA**

**Lewat Terminal**
Jika isi dari file _nomor.txt_ dan _pesan.txt_ sudah sesuai dengan yang anda inginkan, sekarang jalankan programnya diterminal dengan perintah dibawah ini (pastikan direktorinya berada pada Bot_Whatsapp):

- Di Mac/linux  `python bot.py`
- Di Windows  `python.exe .\bot.py`

- pilih file _Nomor.txt_ terlebih dahulu (***INI WAJIB FILE NOMOR***)
- Kemudian baru pilih file _pesan.txt_ 

**Lewat file .EXE**

Jika ingin membuka program lewat file .exe pergi ke folder _bot-exe_, lalu cari file bernama _bot.exe_ cukup double klick pada file tersebut maka program akan dijalankan, atau jika tidak ingin ribet masuk ke dalam folder tersebut maka cari file bernama _bot.exe.lnk_/file shortcut dari bot.exe, lalu copy kan file tersebut ke desktop jadi program bisa langsung dijalankan lewat desktop
