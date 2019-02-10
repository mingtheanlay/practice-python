import random

first_list = random.sample(range(0,30), 12)
second_list = random.sample(range(0,30),13)
list_overlap = [el for el in first_list if el in second_list]
unique_list = []

print('First List')
print(first_list)
print('Second List')
print(second_list)

# Filter the the dupliccate
for el in list_overlap:
    if el not in unique_list:
        unique_list.append(el)

if unique_list == []:
    print('No similarity')
else:
    print('Unique List')
    print(unique_list)