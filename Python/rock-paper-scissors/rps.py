import random

name = input("Enter your name: ").upper()
print("="*75+"\n")
print(f"WELCOME {name} TO ROCK PAPER SCISSOR GAME!!!\n")
print("Winning Rules of the Rock Paper Scissor game as follows: \n"
    +"Rock(🪨) vs Paper(📃) -> Paper(📃) wins \n"
    +"Rock(🪨) vs Scissor(✂️) -> Rock(🪨) wins \n"
    +"Paper(📃) vs Scissor(✂️) -> Scissor(✂️) wins \n")
print("The first one to win 3 rounds is the final winner.")
print("SO LET THE GAME BEGINS!!!") 
print("="*75+"\n")

def getUser():
    hand = input("Enter - R(for rock) | P(for paper) | S(for scissor): ").upper()
    while not (hand == "R" or hand == "P" or hand == "S"):
        hand = input("Enter - R(for rock) | P(for paper) | S(for scissor): ").upper()
    return hand

def getPc():
    list = ['Rock','Paper','Scissor']
    return random.choice(list)

def winner(user, pc):
    if user == "R" and pc == "Rock":
        return "DRAW"
    elif user == "R" and pc == "Paper":
        return "PC"
    elif user == "R" and pc == "Scissor":
        return f"{name}"
    elif user == "P" and pc == "Paper":
        return "DRAW"
    elif user == "P" and pc == "Rock":
        return f"{name}"
    elif user == "P" and pc == "Scissor":
        return "PC"
    elif user == "S" and pc == "Scissor":
        return "DRAW"
    elif user == "S" and pc == "Paper":
        return f"{name}"
    elif user == "S" and pc == "Rock":
        return "PC"
    else:
        return "DRAW"

user_score = 0
pc_score = 0

while True:
    user = getUser()
    pc = getPc()
    print(f"PC choose {pc}.")
    win = winner(user, pc)
    if win == name or win == "PC":
        print(f"WINNER OF THIS ROUND : {win}")
    else:
        print(win)
    if win == name:
        user_score += 1
        if user_score == 3:
            break
    elif win == "PC":
        pc_score += 1
        if pc_score == 3:
            break

if user_score > pc_score:
    print(f"CONGRATULATIONS YOU ARE THE WINNER!!!!")
else:
    print("SORRY YOU LOST PLEASE TRY AGAIN!!!")
