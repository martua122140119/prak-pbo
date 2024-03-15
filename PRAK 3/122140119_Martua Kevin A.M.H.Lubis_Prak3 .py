class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    def lihat_barang():
        print("Jumlah barang:", Dagangan.jumlah_barang)
        print("List barang:")
        for barang in Dagangan.list_barang:
            print(barang[0], "seharga:", barang[2] , "Stok :" ,barang[1]  )

    lihat_barang = staticmethod(lihat_barang)

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for barang in Dagangan.list_barang:
            if barang[0] == self.__nama:
                Dagangan.list_barang.remove(barang)  

   
                



Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()

del Dagangan1

Dagangan.lihat_barang()
