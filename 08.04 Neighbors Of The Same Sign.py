input_str = input("Enter Values Separated by Spaces: ")
input_list = []
current_num_str = ""
for i in range(len(input_str)):
    if input_str[i] == " ":
        input_list.append(int(current_num_str))
        current_num_str = ""
    else:
        current_num_str += input_str[i]
if current_num_str != "":
    input_list.append(int(current_num_str))
n = len(input_list)
results = []
for i in range(n - 1):
    if input_list[i] * input_list[i+1] > 0:
        results.append((input_list[i], input_list[i+1]))
if len(results) == 0:
    print("There are no adjacent elements with the same sign.")
else:
    for pair in results:
        print(pair[0], pair[1])