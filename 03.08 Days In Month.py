month = int(input("Enter Month: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month in [4, 6, 9, 11]:
    print(30)
elif month == 2:
    print(28)
else:
     print("Invalid month")