#Halo.py-program pertama
Nama = input("Nama:")
print(f"Halo,{Nama}!Selamat datang di program Python.")
print("Semoga sukses!")
umur = int(input("Masukkan umur Anda:"))  
print(f"Umur Anda {umur + 1} tahun.")

import datetime

def main():
    print("===Program Perhitungan Perkiraan Usia===")

    #Tantangan: menangani input jika bukan angka dengan try-except
    while True:
        try:
            tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
            tahun_sekarang = datetime.datetime.now().year

            if tahun_lahir > tahun_sekarang or tahun_lahir < 1900:
                print(f"Tahun lahir harus antara 1900 dan {tahun_sekarang}. Silakan coba lagi.\n")
                continue

            usia = tahun_sekarang - tahun_lahir
            print(f"\nPerkiraan usia Anda saat ini adalah {usia} tahun.")
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka (tahun) yang benar.\n")

if __name__ == "__main__":
    main()