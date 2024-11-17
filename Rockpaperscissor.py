import random
user = int(input("Enter your choice: Type 0 for Rock, 1 for paper, 2 for scissors ")) 
if user>= 3 or user<0:
    print("you entered invaild number, you lose")
else:
    computer = random.randint(0,2)
    print("computer choice:")
    print(computer)
    if computer == user:
        print("Its a draw.")
    elif computer ==0 and user==2 :
        print("you lose")
    elif user ==0 and computer ==2:
        print("you win")
    elif computer>user :
        print("you lose")
    elif user>computer:
        print("you win")
