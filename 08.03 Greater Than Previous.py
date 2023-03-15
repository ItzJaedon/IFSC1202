input_string = input("Enter Values Seperated By Spaces: ")
input_list = []
current_num_str = ""
for char in input_string:
    if char == " ":
        current_num = int(current_num_str)
        input_list.append(current_num)
        current_num_str = ""
    else:
        current_num_str += char
input_list.append(int(current_num_str))
previous_num = input_list[0]
for i in range(1, len(input_list)):
    current_num = input_list[i]
    if current_num > previous_num:
        print(current_num)
    previous_num = current_num