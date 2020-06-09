list = []

class Bunga: 
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        list.append(self)
    def hasil(self):
        print("Nama bunganya adalah " ,self.nama, ", harganya sebesar " ,self.harga, ", kelopaknya berjumlah " ,self.jumlah, " rupiah.")

    @classmethod 
    def ask (cls):
        nama = input("Apa nama bunganya : ")
        harga = int(input("Berapa harga bunganya? "))
        jumlah = input("Berapa jumlah kelopaknya? ")

        return cls(nama, harga, jumlah)

x = "y"
while x == "y" :
    Bunga.ask() 
    repeat = input("Apakah Anda ingin mengisi bunga baru? (y/n)")
    if repeat == "n": 
        for x in list: 
            print(x.hasil())



