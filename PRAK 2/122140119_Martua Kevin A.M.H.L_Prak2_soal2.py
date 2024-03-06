class DecoratorExample:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Sebelum pemanggilan fungsi")
        result = self.func(*args, **kwargs)
        print("Setelah pemanggilan fungsi")
        return result

@DecoratorExample
def belanja( barang1,barang2):
    print("Sedang mentotalkan")
    return barang1 + barang2 
    
barang1 = 142000 
barang2 = 2500000

print("Jumlah total : " , belanja(barang1, barang2 ) )

class DecoratorExample :
    def __init__(self, namabarang,hargabarang):
        self.nama = namabarang
        self.harga = hargabarang
    
    def panggil_namabarang(self):
        print(f"Nama barang : {self.nama}" )

    def panggil_hargabarang(self):
        print(f"Harga barang : {self.harga} " )

belanja1 = DecoratorExample("Rolex" , 2500000)
belanja2 = DecoratorExample("Digitec" , 142000)

belanja1.panggil_namabarang()
belanja1.panggil_hargabarang()

belanja2.panggil_namabarang()
belanja2.panggil_hargabarang()

class DecoratorExample:
    def __init__(self, namabarang, hargabarang):
        self.nama = namabarang
        self.harga = hargabarang

    def __del__(self) :
        print(f"Barang :{self.nama} dihapus ")
        print(f"Harga barang :{self.harga} dihapus ")

belanja1 = DecoratorExample("Rolex" , 2500000)
        