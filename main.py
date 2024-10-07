"PROGRAM MANAJEMEN KONTAK"
from turtledemo.penrose import start

class Kontak:
    def __init__(self):
        self.kontak = []


    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            print("LIST KONTAK ANDA : ")
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak Masih Kosong!")
            return 1

    def menambah_kontak(self):
        # menambahkan kontak baru
        nama = input("Masukkan Nama Kontak yang baru: ")
        HP = input("Masukkan Nomor HP yang baru: ")
        email = input("Masukkan Email yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("\nKontak Baru Berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:

            i_hapus = int(input("Masukkan Nomor Kontak yang ingin dihapus: "))
            del self.kontak[i_hapus - 1]
            print("\nKontak Berhasil dihapus!")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:

    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    #Variabel
    pilihan = input("Masukkan Pilihan Menu Kontak (1,2,3,4) : ")

    #logika if
    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        # Keluar dari program
        print("Terimakasih Sudah Menggunakan Program ini ya Guys :)")
        break
    else:
        print("\nPERHATIAN! Harap Masukkan pilihan angka yang benar!")
