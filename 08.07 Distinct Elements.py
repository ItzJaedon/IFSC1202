input_string = input("Enter Values Separated by Spaces: ")
input_list = input_string.split()
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])
prev_elem = None
distinct_count = 0
for i in range(len(input_list)):
    if input_list[i] != prev_elem:
        distinct_count += 1
        prev_elem = input_list[i]
print("Number of Distinct Elements:", distinct_count)