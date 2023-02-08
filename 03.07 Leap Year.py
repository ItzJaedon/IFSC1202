year = int(input("Enter a 4-digit year: "))
if year % 400 == 0:
    print("LEAP YEAR")
elif year % 100 == 0:
    print("COMMON YEAR")
elif year % 4 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")