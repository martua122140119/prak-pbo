def hitung_bilangan_ganjil(batas_bawah, batas_atas):
    # Mengecek apakah batas_bawah atau batas_atas di bawah nol
    if batas_bawah < 0 or batas_atas < 0:
        print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
        return

    jumlah_ganjil = 0
    for i in range(batas_bawah, batas_atas + 1):
        if i % 2 != 0:
            jumlah_ganjil += 1

    print("Jumlah bilangan ganjil antara", batas_bawah, "dan", batas_atas, "adalah:", jumlah_ganjil)

def main():
    batas_bawah = int(input("Masukkan batas bawah : "))
    batas_atas = int(input("Masukkan batas atas : "))

    hitung_bilangan_ganjil(batas_bawah, batas_atas)

if __name__ == "__main__":
    main()
