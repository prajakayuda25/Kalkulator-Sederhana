def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Perpangkatan (^)")
    print("0. Keluar")

    while True:
        pilihan = input("Masukkan pilihan (0-5): ")

        if pilihan == '0':
            print("Terima kasih telah menggunakan kalkulator ini!")
            break
        elif pilihan in ('1', '2', '3', '4', '5'):
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Masukan tidak valid. Mohon masukkan angka.")
                continue

            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"Hasil: {angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"Hasil: {angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"Hasil: {angka1} * {angka2} = {hasil}")
            elif pilihan == '4':
                if angka2 == 0:
                    print("Tidak bisa melakukan pembagian dengan nol.")
                else:
                    hasil = angka1 / angka2
                    print(f"Hasil: {angka1} / {angka2} = {hasil}")
            elif pilihan == '5':
                hasil = angka1 ** angka2
                print(f"Hasil: {angka1} ^ {angka2} = {hasil}")
        else:
            print("Pilihan tidak valid. Mohon masukkan pilihan antara 0 dan 5.")

kalkulator()