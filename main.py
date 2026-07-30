'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1, 1, 0])
user_choice = input(
    "Enter your choice(s = Snake, w = Water, g = Gun): "
    ).lower()
userDict = {
            "s": 1, 
           "w": -1, 
           "g": 0
           }
reverseDict = {
                1: "Snake",
                -1: "water", 
                0: "Gun"
                }
if user_choice not in userDict:
    print("Invalid choice! Please enter only s, w, or g.")
    exit()
user = userDict[user_choice]
print(f"user choose: {reverseDict[user]}")
print(f"computer choose: {reverseDict[computer]}")
if(computer == user):
    print("It's a draw")
else:    
    if(computer == -1 and user == 1):
        print("user win!")
    elif(computer == -1 and user == 0):
        print("user lose!")
    elif(computer == 1 and user == -1):
        print("user lose!")
    elif(computer == 1 and user == 0):
        print("user win!")
    elif(computer == 0 and user == -1):
        print("user win!")
    elif(computer == 0 and user == 1):
        print("user lose!")
    else:
        print("something went wrong")    