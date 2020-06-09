class Bunga: 
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
    
    def hasil(self):
        return(f"Nama bunganya adalah {self.nama}, harganya sebesar {self.harga}, kelopaknya berjumlah {self.jumlah}")

bungas = []

bungas.append(Bunga('mawar', 14, 2))
bungas.append(Bunga('anggrek', 1, 3))
bungas.append(Bunga('tulip', 5, 6))

for obj in bungas: 
    print(obj.hasil())

