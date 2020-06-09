import random
import time

print("DICE ROLL SIMULATOR")
print("-------------------")

while True: 
    buang = input("Apakah anda ingin membuang dadu? (y/n)? ")
    if buang == "y":
        jumlah = int(input("Berapa dadu yang ingin anda buang? ")) 
        for x in range(1, jumlah+1): 
            dice = random.randint(1,6)
            time.sleep(1)
            print(f'Dadu {x} melempar {dice}')
            continue
    if buang == "n":        
        break        