# suitcase = {"pants" : 5, "shoes" : 2}

# for item in suitcase:
#     print(item)

# for item in suitcase: 
#     print(item, ":", suitcase[item])

shopping_basket = {}

print("""
Shopping Basket Options 
----------------------
1 : Add item 
2 : Remove item
3 : View basket
4 : Exit Program
""" )
option = int(input("Enter an option : "))

while option != 0: 
    if option == 1: 
        item = input("Enter an item : ")

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




