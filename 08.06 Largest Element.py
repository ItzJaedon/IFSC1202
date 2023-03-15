input_string = input("Enter Values Separated by Spaces: ")
input_list = input_string.split()
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])
max_value = input_list[0]
max_index = 0
for i in range(len(input_list)):
    if input_list[i] > max_value:
        max_value = input_list[i]
        max_index = i
print("Largest Value: ", max_value)
print("Index Of Largest Value: ", max_index)