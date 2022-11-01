import random

# Rock Paper Scissor Game
def gameWin(comp , player):
    #If two values are equal, declare a tie!
    if comp == player:
        return None

    # Check for all possibilities when computer chose Rock 
    elif comp == 'R':
        if player == 'P':
            return True
        elif player == 'S':
            return False
    
    # Check for all possibilities when computer chose Paper
    elif comp == 'P':
        if player == 'R':
            return False
        elif player == 'S':
            return True

    # Check for all possibilities when computer chose Scissor
    elif comp == 'S':
        if player == 'R':
            return True
        elif player == 'P':
            return False

print("Computer Turn: Rock(R), Paper(P) or Scissor(S)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'R'
elif randNo == 2:
    comp = 'P'
elif randNo == 3:
    comp = 'S' 

player = input("Player's Turn: Rock(R), Paper(P) or Scissor(S)?")
a = gameWin(comp , player)

print(f"Computer chose {comp}")
print(f"Player chose {player}")

if a == None:
    print("The game is tie!")
elif a:
    print("You Win")
else:
    print("You loose")