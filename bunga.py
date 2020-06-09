class Bunga: 
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
    
    def hasil(self):
        print(f"Nama bunganya adalah {self.nama}, harganya sebesar {self.harga}, kelopaknya berjumlah {self.jumlah}")
    
bunga1 = Bunga("mawar", 14, 2)
bunga1.hasil()
bunga2 = Bunga("anggrek", 1, 3)
bunga2.hasil()
bunga3 = Bunga("tulip", 5, 6)
bunga3.hasil()

# Bikin metode baru, pake for loop - panggil method yang direturn