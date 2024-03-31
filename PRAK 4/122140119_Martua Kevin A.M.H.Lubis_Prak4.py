class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        return f"{self.__class__.__name__} {self.nama} bersuara: ???"

    def makan(self, eskulsen):
        return f"{self.__class__.__name__} {self.nama} sedang makan: {eskulsen}"

    def minum(self):
        return f"{self.__class__.__name__} {self.nama} sedang minum: air"

class Kucing(Hewan):
    def bersuara(self):
        return f"{self.__class__.__name__} {self.nama} bersuara: Meong!"

    def makan(self, eskulsen):
        return f"{self.__class__.__name__} {self.nama} sedang makan: {eskulsen}"

class Anjing(Hewan):
    def bersuara(self):
        return f"{self.__class__.__name__} {self.nama} bersuara: Guk Guk!"

    def makan(self, eskulsen):
        return f"{self.__class__.__name__} {self.nama} sedang makan: {eskulsen}"

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)
print(hewan2.nama) 
print(hewan1.bersuara()) 
print(hewan1.makan("tulang")) 
print(hewan2.bersuara()) 
print(hewan2.makan("tulang")) 