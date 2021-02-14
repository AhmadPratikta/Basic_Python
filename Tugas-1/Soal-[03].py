print("===Selamat datang di Aplikasi menentukan lulus ujian===")

teori = int(input("Masukkan nilai Ujian Teori: "))
praktek = int(input("Masukkan nilai Ujian Praktek: "))

if teori >= 70 and praktek >= 70:
    print("Selamat, anda lulus")
elif teori >= 70 and praktek < 70:
    print("Anda harus mengulangi ujian praktek")
elif teori < 70 and praktek >= 70:
    print("Anda harus mengulangi ujian teori")
else:
    print("Anda harus mengulangi ujian teori dan praktek")