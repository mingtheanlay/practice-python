# get user to input the number
user_input = int(input("Input a number: "))

def result(user_input):
    """
        get the user input and compare it to find odd and even
        argument:
                : user_input : the input of user
    """
    # if the the number can divide with 2 and doesn't have remainder it is even
    if (user_input % 2 == 0):
        print(str(user_input) + " is even")
    # but if the the number cannot divide with 2 and have remainder it is odd
    else:
        print(str(user_input) + " is odd")

# call out the function for comparison to get result
result(user_input)