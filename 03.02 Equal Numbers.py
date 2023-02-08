a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if (a == b and a == c):
    print(3)
else: 
    if(a != b and a != c and b != c):
        print(0)
    else:
        print(2)
        