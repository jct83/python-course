import random

print("Computer vs Human")
print("Game Suit")
print("-------------------")

def shortcut():
    if pc_nebak == "Paper" and human_nebak == "Paper":
        print("Tie")
    elif pc_nebak == "Scissors" and human_nebak == "Scissors":  
        print("Tie")
    elif pc_nebak == "Rock" and human_nebak == "Rock":  
        print("Tie")
    elif pc_nebak == "Paper" and human_nebak == "Scissors":
        print("Human win")
    elif pc_nebak == "Scissors" and human_nebak == "Paper":
        print("PC win")
    elif pc_nebak == "Paper" and human_nebak == "Rock":
        print("PC win")
    elif pc_nebak == "Rock" and human_nebak == "Paper":
        print("human win")
    elif pc_nebak == "Scissors" and human_nebak == "Rock":
        print("human win")
    elif pc_nebak == "Rock" and human_nebak == "Scissors":
        print("PC win")

while True: 
    nanya = input("Mau main gak? (y/n)")
    if nanya == "y":
        human_nebak = input("Pilih antar Paper, Scissors, Rock : ")
        pc_nebak = random.randint(1,3)
        # Rock
        if pc_nebak==1:
            pc_nebak = "Rock"
            shortcut()

        # Paper
        elif pc_nebak==2:
            pc_nebak = "Paper"
            shortcut()

        # Scissors
        elif pc_nebak==3:
            pc_nebak = "Scissors"
            shortcut()
        continue
    else: 
        break
            