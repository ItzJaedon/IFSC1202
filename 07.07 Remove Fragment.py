string = input("Enter a string: ")
first_h = string.find('h')
last_h = string.rfind('h')
result = string[:first_h] + string[last_h+1:]
print(result)