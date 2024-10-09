"PROGRAM MANAJEMEN KONTAK"
from turtledemo.penrose import start
import kontak

def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()



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
            kontak_keluarga.melihat_kontak()

        elif pilihan == '2':
            kontak_keluarga.menambah_kontak()

        elif pilihan == '3':
            kontak_keluarga.menghapus_kontak()

        elif pilihan == '4':
            # Keluar dari program
            kontak_keluarga.keluar_kontak()
            print("Terimakasih Sudah Menggunakan Program ini ya Guys :)")
            break
        else:
            print("\nPERHATIAN! Harap Masukkan pilihan angka yang benar!")

if __name__ == "__main__":
    main()