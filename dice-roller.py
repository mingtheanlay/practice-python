# import random dependency to random the number
import random
print('Welcome to Dice Rolling Simulator')
# get user to command to start the program
start = input("Press S to start: ")
# while loop
while True:
    #if user press s or S the program will start
    if start in ['s','S']:
        # random the number from 1 to 6
        index = random.randint(1,6)
        # output the result
        print("The result is ",index)
        # output the instruction for user
        print("Press anything to exit")
        print("Press A to play again")
        # get user choice
        choice = input("Waiting for input: ")
        # if user press a or A the program will restart to the while loop
        if choice in ['a','A']:
            continue
        # but if the user press any key beside a or A it will quit the program
        else:
            print('Bye World')
            break