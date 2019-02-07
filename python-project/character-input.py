# Import the denpendency datetime to know the the current date
import datetime
# now is equal the current timestamp, it doesn't show the exact date yet
now = datetime.datetime.now()
# Initialize the default data
name = 'default'
age = '0'

def user_input(name,age):
    """
        To get user input
        Argument:
                : name : get the default data and replace it with user input
                : age : get the default data and replace it with user input
    """
    name = input("Name: ")
    age = input("Age: ")
    # return back the replace result of name and age
    return name, age


def calculate_age(now, age):
    """
        Calculate the age of user to the year of birth and minus it with current time
        Argement:
                : now : current time
                : age : user age
    """
    # now.year use to know the current year
    # int(age) conver age to integer and we have the user year of birth
    year_of_birth = now.year - int(age)
    # to know the year of user will reach 100 year
    hundread_year = year_of_birth + 100
    # give back the result of year the user will reach a hundred year
    return hundread_year

# call the function user input and unpacking the user input to single variable
name, age = user_input(name,age)
# output the name and age of user
print("Username: ",name)
print("Age: ",age)
# call out the function to show the result
hundread_year = calculate_age(now,age)
print(name + " will be a 100 years old in " + str(hundread_year))