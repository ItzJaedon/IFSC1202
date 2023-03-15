input_string = input("Enter Values Separated by Spaces: ")
input_list = [int(x) for x in input_string.split()]
for i in range(0, len(input_list) - 1, 2):
    input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
print("Swapped Values: ", end="")
for i in range(len(input_list)):
    print(input_list[i], end=" ")
print()