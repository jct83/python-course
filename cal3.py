calculator = {}

print("""
Calculator
----------------------
1 : Luas Tabung
2 : Volume Tabung
3 : Usage history
4 : Exit Program
""" )
option = int(input("Enter an option : "))

while option != 0: 
    if option == 1: 
        input_jari = int(input("Masukkan Jari-Jari Tabung: "))

        if item in shopping_basket:
            print("Item already in shopping basket")
            quan = int(input("Enter the quantity : "))
            shopping_basket[item] += quan

        else : 
            quan = int(input("Enter the quantity : "))
            shopping_basket[item] = quan
        
    elif option ==2: 
        item = input("Enter an item : ")
        del(shopping_basket[item])
        
    elif option ==3:
        for item in shopping_basket:
            print(item,":",shopping_basket[item])
            
    elif option !=0: 
        print("You didnt enter a valid number.")
        break 
    
    print("----------------------------------")
    option = int(input("Enter an option : "))

else: 
    print("Shopping basket program closed. ")