# import denpendency random
import random
print("Welcome to Guess the Number Challenge")
# random from 1 to 10
number = int(random.randint(1,10))
# loop the menu
while True:
    # get user to input the number that they want to guess
    user_guess =int(input("Input the number that you want to guess: "))
    # if the guess number is lower than the random number it will output lower
    if user_guess < number:
        print ('The number is too low')
    # if the guess number is greater than the random number it will output higher
    elif user_guess > number:
        print ('The number is too high')
    # if the guess number is equal to the random number it will output correct and the random number
    elif user_guess == number:
        print('You are correct, the number is', number)
        # output the instruction for user
        print("Press A to play agian")
        print("Press anything to exit")
         # get user choice
        user_choice = input("Input your choice: ")
         # if user press the program will restart to the while loop
        if user_choice == 'a':
            number = int(random.randint(1,10))
            print("-"*40)
            continue
        # but if the user press any key beside a it will quit the program
        else:
            print("Thank you for gussing")
            break
