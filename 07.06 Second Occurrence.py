string = input("Enter a string: ")
if "f" in string:
    second_f_index = string.find("f", string.find("f") + 1)
    if second_f_index == -1:
        print("One f")
    else:
        print(second_f_index)
else:
    print("Zero f")