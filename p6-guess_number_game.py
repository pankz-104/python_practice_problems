#
#     Guess the number
# Genereate a random integer from a to b. You and your friend have ti guess a number between two
# numbers a and b. a and bare inputs taken from the user. Your friend is player 1 and plays first.
# He will have to keep choosing the number and your program must tekk whether the number is greeater
# thaen the actual number or less than the actual number . Log the trails it took your friend
# to arrive to number. Ypu play the same game then the person with minimum number of trail wins.
#
# Randomly generate a number and don't show that to the user (say 6)
#
# Input:
#     Enter value of a
#     Enter value of b
#
# Output :
#     player 1 please enter the number 4
#     5
#     wrong guess again
#     7
#     wrong guess a smaller number again
#     6
#     3 correct trial to gusess the number
#
#     Player 2
#
#     .
#     .
#     .
#     .
#     2 correct trials to guess the number
#


import random
a = int(input("Enter the min range value :: "))
b = int(input("Enter the max range value :: "))
answer = random.randint(a, b)

count_1 = 0
while(True):
    guess = int(input("Player_1 making a guess : "))
    count_1 += 1
    if guess == answer:
        print("Correct guess\n")
        print(f"Attempts made : {count_1}")
        break
    elif guess < answer:
        print("make a bigger guess ")
        print(f"Attempts made : {count_1}")
    elif guess > answer:
        print("Make a smaller guess ")
        print(f"Attempts made : {count_1}")
    else:
         print("Game Exited")

count_2 = 0
while(True):
    guess = int(input("Player_2 making a guess: "))
    count_2 += 1
    if guess == answer:
        print("Correct guess\n")
        print(f"Attempts made {count_2}")
        break
    elif guess < answer:
        print("make a bigger guess")
        print(f"Attempts made : {count_2}")
    elif guess > answer:
        print("make a smaller guess")
        print(f"Attempts made : {count_2}")
    else:
        print("Game exited")

print("winner of game: ")
if count_1 < count_2:
    print("Player_1")
elif count_2 < count_1
    print("Player_2")
else:
    print("Game draw")

