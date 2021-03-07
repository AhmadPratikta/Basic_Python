# Import library
import os
import smtplib

# File Handling, untuk membaca isi yang ada di file .txt

a = open('Isi_Pesan.txt', 'r')
b = open('Pengirim.txt', 'r')
c = open('Penerima.txt', 'r')


EMAIL_ADDRESS = os.environ.get(str(b.read()))
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 443) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    # Login akun
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Isi pesan
    subject = 'Ada sebuah pesan nan epic'
    body = str(a.read())

    msg = f'Subject: {subject}\n\n{body}'

    # Mengirim pesan
    smtp.sendmail(EMAIL_ADDRESS, str(c.read()), msg)