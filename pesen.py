banyak_makanan = ["es teh manis", "nasi pecel", "sambal bawang"]
print("Berikut makanan yang anda pesan : ")
for n in range(len(banyak_makanan)): 
    print (n+1, banyak_makanan[n])

while True: 
    nanya = input("Apa tambahan? (iya/tidak): ")
    if nanya == "iya":
        banyak_makanan.append(input("Nambah apa?: "))
    elif nanya == "tidak":
        print("Baik, berikut pesanan Anda : ")
        for n in range(len(banyak_makanan)): 
            print (n+1, banyak_makanan[n])
        break
