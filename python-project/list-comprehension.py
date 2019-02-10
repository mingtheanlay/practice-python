first_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# if first_list can devide with 2 and have o as remain it it will add to evenlist
even_list = [el for el in first_list if el % 2 == 0]
print(even_list)
