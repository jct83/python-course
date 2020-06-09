list = []

class Calculator:
    def __init__(self, jari, tinggi, tanya, hasil):
        self.jari = jari
        self.tinggi = tinggi
        self.tanya = tanya
        self.hasil = hasil
        list.append(self)

    def jadi(self):
        if self.tanya == 1 :
            self.tanya = "Luas permukaan tabung"
        if self.tanya == 2: 
            self.tanya = "Volume tabung"
        print(f"Jari-jari tabung {self.jari}, Tinggi tabung {self.tinggi}, {self.tanya} {self.hasil}")
    
    @classmethod
    def Nanya(cls):
        try : 
            jari = int(input("Masukkan Jari-Jari Tabung: "))
            tinggi = int(input("Masukkan Tinggi Tabung: "))
        except ValueError:
            print("Value Error")
        except: 
            print("Terdapat sebuah kesalahan")
        else: 
            print("1. Hitung luas permukaan tabung")
            print("2. Hitung volume tabung")
            tanya = int(input("Apa yang ingin dihitung? "))
            if tanya == 1 : 
                hasil = (2 * 3.14 * jari * jari) + (2 * 3.14 * jari * tinggi)
                print(f"Luas permukaan tabung : {int(hasil)}")
            elif tanya == 2 : 
                hasil = 3.14 * jari * jari * tinggi
                print(f"Volume tabung : {int(hasil)}")
            return cls(jari, tinggi , tanya, hasil)

print("--Calculator--")
x = input("Ingin menggunakan kalkulator? (y/n): ")

while x == "y":
    Calculator.Nanya()
    ulang = input("Anda ingin menggunakan kalkulator ini kembali? (y/n): ")
    if ulang == "n":
        print("--Usage History--")
        for y in list: 
            print(y.jadi())
