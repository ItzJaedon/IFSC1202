string = input("Enter a string: ")
first_h_index = string.find('h')
last_h_index = string.rfind('h')
if first_h_index != -1 and last_h_index != -1 and first_h_index != last_h_index:
    reversed_part = string[first_h_index+1:last_h_index][::-1]
    result = string[:first_h_index+1] + reversed_part + string[last_h_index:]
    print(result)
else:
    print("Error: Input string does not meet the requirements.")