def display_kontak(list_kontak):
    for kontak in list_kontak:
        print("=========================================")
        print(f"Nama :  {kontak['nama']}")
        print(f"Nomor :  {kontak['nomor']}")

def kontak_baru():
    nama = input("Nama: ")
    nomor_telepon = input("No telepon: ")
    kontak = {
        'nama' : nama,
        'nomor' : nomor_telepon
    }
    return kontak

list_kontak = []
list_kontak.append({
    "nama" : "Farhan",
    "nomor" : "08768373651"
})
list_kontak.append({
    "nama" : "Joko",
    "nomor" : "08987654321"
})

perulangan = True

print("Selamat datang!")

while (perulangan):
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. keluar")

    pilih_menu = int(input("Pilih menu: "))

    if pilih_menu == 1:
        print("==Daftar kontak==")
        display_kontak(list_kontak)

    elif pilih_menu == 2:
        print("==Masukkan nama dan nomor telepon==")
        penambahan_kontak = kontak_baru()
        list_kontak.append(penambahan_kontak)
    elif pilih_menu == 3:
        break
    else:
        print("unidentified")

print("Shut down.....")