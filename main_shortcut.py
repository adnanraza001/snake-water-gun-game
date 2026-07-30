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
    "g": 0}
reverseDict = {
    1: "snake",
    -1: "water",
    0: "gun"
    }
if user_choice not in userDict:
    print("Invalid choice! Please enter only s, w, or g.")
    exit()
you = userDict[user_choice]
print(f"you choose {reverseDict[you]}")
print(f"computer choose {reverseDict[computer]}")
if(computer == you):
    print("It's draw")
else:    
    # if(computer == -1 and you == 1): # try to find pattern computer - you = -2
    #     print("You win!")
    # elif(computer == -1 and you == 0): # -1
    #     print("You lose")
    # elif(computer == 1 and you == -1): # 2
    #     print("You lose")
    # elif(computer == 1 and you == 0): # 1
    #     print("You win!")
    # elif(computer == 0 and you == -1): # 1
    #     print("You win!")
    # elif(computer == 0 and you == 1): # -1
    #     print("You lose!")
    # else:
    #     print("something went wrong")    
    '''
the below logic is based on pattern which is computer - you
we are lossing when computer-you = -1 or 2
so as per this logic we can write below code

    '''
    if ((computer-you) == -1 or (computer-you) == 2):
        print("You lose")
    else:
        print("You win")           