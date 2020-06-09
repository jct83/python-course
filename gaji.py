def gaji(jam, nominal):     
    if jam>40: 
        return nominal * jam + 500
        
    elif jam<40: 
        return nominal * jam

nama = input("Siapa nama Anda : ")
jam = int(input("Berapa jam anda kerja?: "))
nominal = int(input("Berapa jumlah gaji per jam?: "))

gaji = gaji(jam,nominal)

print("hey " + str(nama) + ", gaji anda " + str(gaji))

 












        

