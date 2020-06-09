class Siswa: #Nama class huruf pertama kapital
    def __init__(self, name, age, alamat): #dunder(double underscore) - function init (akan berjalan setiap kelas dibuat)
        self.name = name
        self.age = age
        self.alamat = alamat    
        
    def perkenalan(self): 
        print(self.name,self.age,self.alamat)

siswa1 = Siswa("Kenny", 16, "surga")
siswa1.perkenalan()
  