print("Generate random list...")
# Initialize a list with random number
list_number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list_number)
# to find the number that less than 5
# if element is less than 5 it add to list of variable number_less_than_five
number_less_than_five = [el for el in list_number if el < 5]
print("Number in the list less than 5")
# print out the number that less than 5 using loop bcuz of it is in list
for i in number_less_than_five:
    # print w/o start the newline
    print(i, end=" ")
print("\n")
