"PROGRAM MANAJEMEN KONTAK"
from turtledemo.penrose import start

kontak1 = {'nama' : 'Andi', 'HP' : '08121212', 'email' : 'andi@gmail.com'}
kontak2 = {'nama' : 'Anis', 'HP' : '08313131', 'email' : 'anis@gmail.com'}
kontak = [kontak1, kontak2]

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
        # melihat semua kontak
        if kontak:
            print("LIST KONTAK ANDA : ")
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak Masih Kosong!")

    elif pilihan == '2':
        # menambahkan kontak baru
        nama = input("Masukkan Nama Kontak yang baru: ")
        HP = input("Masukkan Nomor HP yang baru: ")
        email = input("Masukkan Email yang baru: ")
        kontak_baru = {'nama':nama, 'HP': HP, 'email':email}
        kontak.append(kontak_baru)
        print("\nKontak Baru Berhasil ditambahkan!")

    elif pilihan == '3':
        # Menghapus kontak
        if kontak:
            print("LIST KONTAK ANDA : ")
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak Masih Kosong!")
            continue

        i_hapus = int(input("Masukkan Nomor Kontak yang ingin dihapus: "))
        del kontak[i_hapus-1]
        print("\nKontak Berhasil dihapus!")

    elif pilihan == '4':
        # Keluar dari program
        break
    else:
        print("\nPERHATIAN! Harap Masukkan pilihan angka yang benar!")
