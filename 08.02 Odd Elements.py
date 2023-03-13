input_string = input("Enter a string of integers separated by spaces: ")
int_list = []
num_str = ""
for char in input_string:
    if char != " ":
        num_str += char
    else:
        int_list.append(int(num_str))
        num_str = ""
if num_str:
    int_list.append(int(num_str))
for i in range(len(int_list)):
    if int_list[i] % 2 != 0:
        print(int_list[i])