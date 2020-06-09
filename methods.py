class Siswa: #Nama class huruf pertama kapital
    def __init__(self, name, age, alamat): #dunder(double underscore) - function init (akan berjalan setiap kelas dibuat)
        self.name = name
        self.age = age
        self.alamat = alamat    
        
    def perkenalan(self): 
        print(self.name,self.age,self.alamat)
    
    @classmethod
    def new_siswa(cls):
        name = input("Masukkan nama siswa : ")
        age = int(input("Masukkan umur siswa : "))
        alamat  = input("Masukkan alamat siswa : ")
        
        # siswa1 = Siswa(name, age, alamat) # Salah karena instance bakal sama terus

        return cls(name, age, alamat) #Ngebalikin data yang mau - bikin class baru - cls sama aja kayak Siswa

siswa1 = Siswa("Kenny", 16, "surga")
siswa1.perkenalan()

for x in range(3): 
    Siswa = Siswa.new_siswa() #Ngeadd 3 kali

for siswa in siswas: 
    print(siswa)