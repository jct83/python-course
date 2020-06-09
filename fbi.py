import time
print("-------------------------------------------") 
print ("FBI WATCH LIST")
print("-------------------------------------------")
password = input("Enter password : ")
if password != "caylan":
    print("Password Salah")
elif password == "caylan": 
    # Loading 
    for a in range(1,4): # Loading cycle 3 kali 
        for b in range(0,4,1): # Titiknya 
            time.sleep(1)
            print(f'Data loading{"." *b}')
    #load = ["Loading", "Loading", "Loading"]
    #itik = [".", "..", "..."]
    #for x in load:
     #   for y in titik: 
      #      print(x,y)
       #     time.sleep(1)
    print("-------------------------------------------")
    print("Data loaded")
    print("-------------------------------------------")
    cry = {'name': 'Crystal', 'law': 'Terrorism'}
    j = {'name': 'John', 'law': 'Fraud'}
    s = {'name' : 'Sergio', 'law' : 'Rape and Murder'}
    print("First Person : " + cry['name'])
    print("Charged with : " + cry['law'])
    print("-------------------------------------------")
    print("Second person: " + j['name'])
    print("Charged with : " + j['law'])
    print("-------------------------------------------")
    print("Third person : " + s['name'])
    print("Charged with : " + s['law'])
    print("-------------------------------------------")






