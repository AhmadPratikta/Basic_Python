print("===Selamat datang di Aplikasi menentukan luas jari-jari Lingkaran===")
print(" ")

jari_jari = int(input("Masukkan nilai jari-jari: "))
phi = 22 / 7

luas = phi * jari_jari
belakang = "cm adalah {:.2f}".format(luas)

print("Luas lingkaran dengan jari-jari", jari_jari, belakang, "cm\u00b2")