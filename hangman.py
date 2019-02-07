# import random dependency
import random
# generate a word list
word_list = ['book', 'pen', 'cat']
# generate an empty list
display_dash = []
# the index in word list
random.shuffle(word_list)
# get the first index
answer = word_list[0]
# put the character of word to list
#[a,b,c]
display_dash.extend(answer)
# count the lenght of the word
string_len = len(answer)
# loop from the same amount of the lenght of word
for i in range(string_len):
    # replace the chracter in the list to dash
    display_dash[i] = "_"
    # print out the dashes of the word for user to guess
print(" ".join(display_dash))

# user have 7 chances to guess 
chance = 7
# the remain word that user need to guess
word_count =0

# loop the menu
# if the word_count is smaller than the lenght of answer it still loop
# if the word is equal, it will end the loop and go to else
while word_count < string_len:
    # get user to guess
    user_guess = input("Your Guess: ")
    a = 0
    # output the remain chance for user to guess
    print('Your chance: ', chance)
    # looping the same amount of the character lenght 
    for i in range(string_len):
        # compare the user input with every single word in the answer list 
        if user_guess == answer[i]:
            # if it is equal, it will replace the dash in dashes list
            display_dash[i] = user_guess
            print(" ".join(display_dash))
            # increase the word count to make the while end and to tell the user
            word_count += 1
            a = 1
    # if a = 1 or the program execute the compare loop, this comparison will not work
    if a == 0:
        # if the user fail to guess the program will reduce the chances
        chance = chance - 1
        # if chance equal 0, it will print lose comment and end the program
        if chance == 0:
            print("You lose")
            break
        else:
            # if there still the chance the while is restart
            continue
# if the word count is equal the lenght it will print the word us guessed
else:
    print("You guessed the word")
