def luas_persegi(panjang,lebar): 
    return panjang * lebar

def volume_balok(luas,tinggi): 
    print (luas * tinggi)

panjang = int(input("Masukkan panjang : "))
lebar = int(input("Masukkan lebar : "))
luas = luas_persegi(panjang,lebar)
luas_persegi(panjang, lebar)
tinggi = int(input ("Masukkan tinggi : "))
volume_balok(luas,tinggi)
