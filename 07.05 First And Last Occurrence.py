prompt_string=input("Enter a string: ")
if "f" in prompt_string:
    count = prompt_string.count("f")
    if count == 1:
        index = prompt_string.find("f")
        print(index)
    else:
        first_index = prompt_string.find("f")
        last_index = prompt_string.rfind("f")
        print(first_index, last_index)
else:
    print("0")