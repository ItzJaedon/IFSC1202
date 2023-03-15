input_string = input("Enter a string of integers separated by spaces: ")
input_list = input_string.split()
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])
count = 0
for i in range(1, len(input_list)-1):
    if input_list[i] > input_list[i-1] and input_list[i] > input_list[i+1]:
        count += 1
print("Example Output: ")
print(count)