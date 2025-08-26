import random 

# 1 FOR SNAKE , -1 FOR WATER , 0 FOR GUN 
computer = -1
youstr = input("Enter your choice")
youdict = { "s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

you  = youdict[youstr]

print(f"You chose{reversedict[you]}\n computer chose {reversedict[computer]}")

if(computer == you):
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print(" you win")
    elif(computer == -1 and you == 0):
        print(" you lose")
    elif(computer == -1 and you == 1):
        print(" you lose")
    elif(computer == 1 and you == 0):
         print(" you win")
    elif(computer == 0 and you == -1):  
        print("You win")
    elif(computer == 0 and you == 1):  
        print("You Lose")
    else:
        print("something went wrong")
