# create a list
list_of_string =[]
# get user input
user_input = input('Input a String: ')
# get the length of user input
string_length = len(user_input)
# loop through user input and add it to the list of string
for i in user_input:
    list_of_string.append(i)
# if there are only a string it cant reverse
if string_length <= 1:
    print('Your Input cannot palindrome')
# but if the string is greater than 1
else:
    # it loop reversly through user input
    for i in reversed(list_of_string):
        # and it print out the result
        print(i,end="")
print("\n")
        