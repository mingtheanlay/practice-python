# get the quotient from user to analyze and put it to integer
user_input = int(input("Input number to fine divisors: "))
# create a empty list
number = []
# loop from 1 to 10 to find the diversion
for x in range(1,11):
# if the number can devide with the number from 1 to 10 and equal 0
    if user_input % x == 0:
        # it will transfer vaule of x to the empty list (number)
        number.append(x)
# output the result by looping to list number
print("Divisor of "+str(user_input)+" is ",end=" ")
for el in number:
    print(el,end=" ")

print("\n")