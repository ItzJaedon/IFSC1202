input_string = input("Enter Values Separated by Spaces: ")
input_list = [int(x) for x in input_string.split()]
min_index = max_index = 0
for i in range(len(input_list)):
    if input_list[i] < input_list[min_index]:
        min_index = i
    if input_list[i] > input_list[max_index]:
        max_index = i
input_list[min_index], input_list[max_index] = input_list[max_index], input_list[min_index]
print("Swapped Minimum and Maximum: ", end="")
for i in range(len(input_list)):
    print(input_list[i], end=" ")
print()