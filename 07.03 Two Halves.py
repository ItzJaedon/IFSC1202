prompt_string = input("Enter A String: ")
length = len(prompt_string)
midpoint = length // 2
first_half, second_half = prompt_string[:midpoint], prompt_string[midpoint:]
new_string = second_half + first_half
print(new_string)