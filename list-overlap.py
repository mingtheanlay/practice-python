# Generate 2 list to compare
first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Initialize the third_list to add the common number
common_list = []


def comparison(first_list, second_list):
    """
        Comparing between the list
        Argument:
                : first_list : the list that want to compare
                : second_list : the list that going to compare with the first_list

    """

    for el in first_list:
        # Compare first_list with sconed_list
        if el in second_list:
            # if it the same it add to the third list
            common_list.append(el)


def removeDuplicates(listofElements):
    """
        To remove the duplicates value from list
        Argument:
                : listOfElements : the list that we want to filter out the duplicate data
    """
    # Initialize new list
    unique_list = []
    # Loop through the list that we want to see the value
    for el in listofElements:
        # If the element didn't have in unique_list it add
        # But if the same element is in there it doesn't add
        if el not in unique_list:
            # Add to the unique list
            unique_list.append(el)
            # Give back the result
    return unique_list


# Call the function comparison and add the list to function we want to compare
comparison(first_list, second_list)
# Print out the instruction and ,end=" " is not to start the new line
print("The common number is", end=" ")
# Call and Loop through the function and add the common_list to the function to get the result
for el in removeDuplicates(common_list):
    # Print out the element w/o starting the newline
    print(el, end=" ")
    # Start the new line
print("\n")
