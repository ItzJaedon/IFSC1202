input_str = input("Enter Values Separated by Spaces: ")
input_list = input_str.split()
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])
unique_list = []
for i in range(len(input_list)):
    count = 0
    for j in range(len(input_list)):
        if i != j and input_list[i] == input_list[j]:
            count += 1
    if count == 0:
        unique_list.append(input_list[i])
for i in range(len(input_list)):
    if input_list[i] in unique_list:
        print(input_list[i], end = ' ')