# BOT-Whatsapp
Author: Tron

Bot ini sangat cocok untuk pebisnis online karena mempunyai fitur untuk mengirim pesan/promosi ke client hanya dalam satu perintah untuk 2 atau bahkan sampai 100 nomor 
sekaligus tanpa perlu menyimpan nomor tersebut, tetapi memiliki delay beberapa detik selama mengirim pesan untuk menghindari pemblokiran oleh pihak whatsapp. 

## Set-Up

**Pastikan sudah menginstall Python di komputer anda**

Jalankan perintah seperti dibawah ini pada terminal komputer anda:

`git clone https://github.com/Tron403/BOT-Whatsapp.git`

atau jika tidak mempunyai git bisa mendownload langsung dalam format zip.

Masuk kedalam direktori BOT-Whatsapp dan terdapat 3 file didalamnya:
  - bot.py
  - nomor.txt
  - pesan.txt

Ubah isi file _nomor.txt_ dengan nomor tujuan anda, Perhatikan format nya dan pastikan mempunyai code country.

Ubah isi file _pesan.txt_ dengan pesan yang anda sampaikan atau produk yang ingin anda promosikan.    
***INGAT UNTUK SELALU MENGUBAH FILE TERSEBUT JIKA INGIN MENGGANTI NOMOR TUJUAN ATAUPUN PESAN***

## Cara Pakai
**PASTIKAN SUDAH LOGIN PADA WHATSAPP WEB ANDA**

Jika isi dari file _nomor.txt_ dan _pesan.txt_ sudah sesuai dengan yang anda inginkan, sekarang jalankan programnya diterminal dengan perintah dibawah ini (pastikan direktorinya berada pada Bot_Whatsapp):

`python bot.py`

- pilih file _Nomor_ terlebih dahulu (***INI WAJIB FILE NOMOR***)
- Kemudian baru pilih file _pesan_ 

Pesan akan terkirim secara otomatis lewat Whatsapp web

