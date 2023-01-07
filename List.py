numbers = [1, 3, 0, 4, 0, 5, 6, 0, 7]
new_list = [num for num in numbers if num != 0] + [num for num in numbers if num == 0]
print(new_list)
