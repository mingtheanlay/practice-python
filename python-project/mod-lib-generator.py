# get the input from user
noun_1 = input("Noun : ")
noun_plural = input("Noun (Plural) : ")
noun_2 = input("Noun : ")
place = input("Place : ")
adjective = input("Adjective : ")
noun_3 = input("Noun : ")
# to get user to press s to start the mad-lib
go = input("Press S to go mad: ")

# loop the manu if it false it stop
while True:
    # if user press s the program start to combine the noun with given phrase
    if go == 's':
        first_line = 'Be kind to your '+noun_1+'-footed '+noun_plural
        second_line = 'For a duck may be somebody`s '+noun_2
        third_line = 'Be kind to your '+noun_plural+' in ' + place
        fourth_line = 'Where the weather is always '+adjective+'.'
        fifth_line = 'You may think that this is the '+noun_3+','
        sixth_line = 'Well it is.'
        # output the phrase and get it the the center of the star
        print(first_line.center(40, "*"))
        print(second_line.center(40, "*"))
        print(third_line.center(40, "*"))
        print(fourth_line.center(40, "*"))
        print(fifth_line.center(40, "*"))
        print(sixth_line.center(40, "*"))
        # print out the instruction for user to know
        print("Press A to generate again")
        print("Press anything to quit")
        # get the user instruction to start again or quit
        user_choice = input("Input your choice: ")
        # if user press a or A it will start the program ahain
        if user_choice in ['a', 'A']:
            # this will replace the old input
            noun_1 = input("Noun : ")
            noun_plural = input("Noun (Plural) : ")
            noun_2 = input("Noun : ")
            place = input("Place : ")
            adjective = input("Adjective : ")
            noun_3 = input("Noun : ")
            go = input("Press S to go mad: ")
            # continue here is to start while loop ahain
            continue
        # but if the user press the others letter the program will end
        else:
            print("Bye World, Try again next time.")
            # break here mean to break out the while loop and end the program
            break
    else:
        # but if the user press any key beside s the program will get the user to press the key again until the user press s
        print("Input Invalid.")
        go = input("Press S to go mad: ")
