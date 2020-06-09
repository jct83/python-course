list = []

class Calculator : 
    def __init__(self, jari, tinggi, volume, luas):
        self.jari = jari
        self.tinggi = tinggi
        self.volume = volume
        self.luas = luas
        list.append(self)
    
    def jadi(self):
        if self.tanya == 1: 
            self.tanya = "Luas permukaan tabung"
        if self.tanya == 2:
            self.tanya = "Luas volume tabung"
        print(f"Jari - jari tabung ", {self.jari}, "Tinggi tabung  ", {self.tinggi}, {self.tanya}  {self.hasil})

    @classmethod
    def Ask(cls):
        try : 
            jari = int(input("Masukkan jari-jari tabung : "))
            tinggi = int(input("Masukkan tinggi tabung : "))
        except ValueError:
            print("Value Error")
        except: 
            print("ada kesalahan")
        else :
            print("1. Hitung Luas Tabung")
            print("2. Hitung volume tabung:")
            tanya = int(input("Apa yang ingin dilakukan? "))
            if tanya == 1: 
                hasil = rumus
                print(f"Luas tabung : {self.hasil}")
            elif tanya == 2: 
                hasil = rumus
                print(f"Volume tabung : {self.hasil}")
            return cls(jari, tinggi, volume, luas)

print("-- Calculator --")
x = input("Anda ingin menggunakan? ")

if x == "y":
    Calculator.Ask()
    repeat = "Masih pengen lagi? "
    if repeat == "n":
        print("-- Usage History --")
        for y in list: 
            print(y.jadi())


        