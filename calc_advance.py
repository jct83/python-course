while True : 

    try:
        num1 = float(input("Ketiklah angka pertama : "))
        op = int(input("Pilihlah operator yang akan digunakan : \n 1. Penjumlahan \n 2. Pengurangan \n 3. Pembagian \n 4. Perkalian \n 5. Exit"))
        num2 = float(input("Ketiklah angka kedua : "))
    
        if op==1:
            print(num1+num2)
        elif op==2:
            print(num1-num2)
        elif op==3:
            print(num1/num2)
        elif op==4:
            print(num1*num2)
        elif op==5: 
            break
    except ValueError:
        print("Value Error")
    except: 
        print("Terdapat sebuah kesalahan")













        

