"Berisi Class kontak untuk menjalankan project program kontak"

import dokumen


class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()


    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            print("LIST KONTAK ANDA : ")
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("Kontak Masih Kosong!")
            return 1

    def menambah_kontak(self):
        # menambahkan kontak baru
        nama = input("Masukkan Nama Kontak yang baru: ")
        HP = input("Masukkan Nomor HP yang baru: ")
        email = input("Masukkan Email yang baru: ")
        kontak_baru = f"{nama} ({HP}, {email})" + "\n"
        self.kontak.append(kontak_baru)
        print("\nKontak Baru Berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukkan Nomor Kontak yang ingin dihapus: "))
                del self.kontak[i_hapus - 1]
                print("\nKontak Berhasil dihapus!")
            except:
                print("Input yang anda masukkan salah!")


    def keluar_kontak(self):
        dokumen.menyimpan_kontak(isi=self.kontak)