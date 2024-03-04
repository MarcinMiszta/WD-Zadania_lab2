num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list2 = []
i = 0
while i < len(num_list):
    if num_list[i] % 2 == 0:
        num_list2.append(num_list[i])
    i += 1
print(num_list2)
