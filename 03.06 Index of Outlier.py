a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if (a == b and a != c):
    print(3)
else: 
    if(a == c and a != b ):
        print(2)
    else:
        print(1)