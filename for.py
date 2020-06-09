real_user = "harris"
real_pass = "1234"

tries = int(input("Berapa kali coba"))

for tries in range(tries, 0, -1):
    print(f"Anda memiliki {tries} coba")
    user_guess = input("Apa username : ")
    pass_guess = input("Apa pass : ")

    if user_guess == real_user and pass_guess == real_pass:
        print("Login berhasil")
        break
    else : print("login gagal")


    










        

