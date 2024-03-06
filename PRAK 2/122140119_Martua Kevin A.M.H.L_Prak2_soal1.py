class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_angkatan(self):
        return self.angkatan

    def set_angkatan(self, angkatan):
        self.angkatan = angkatan

    def get_isMahasiswa(self):
        return self.isMahasiswa

    def set_isMahasiswa(self, isMahasiswa):
        self.isMahasiswa = isMahasiswa

    def method1(self):
        return f"{self.__nama} memiliki NIM {self.__nim}"

    def method2(self):
        return f"{self.__nama} adalah mahasiswa angkatan {self.angkatan}"

    def method3(self, status):
        if status:
            return f"{self.__nama} adalah mahasiswa"
        else:
            return f"{self.__nama} bukan mahasiswa"


# Object pertama dengan parameter isMahasiswa
mahasiswa1 = Mahasiswa("123456", "John Doe", 2020, True)
print(mahasiswa1.method1())  
print(mahasiswa1.method2()) 
print(mahasiswa1.method3(True))  
print(mahasiswa1.method3(False))  

# Object kedua tanpa parameter isMahasiswa
mahasiswa2 = Mahasiswa("654321", "Jane Doe", 2021)
print(mahasiswa2.method1())  
print(mahasiswa2.method2())  
print(mahasiswa2.method3(True))  
print(mahasiswa2.method3(False)) 