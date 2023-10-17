my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = [x for x in my_list if my_list.count(x) == 1]
print(unique_list)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)
