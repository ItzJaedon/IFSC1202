A = int(input("Enter A Number: "))
from math import floor
Ones = A % 10
A = floor(A / 10)
Tens = (A % 10)
A = floor(A / 10)
Hundred = floor(A % 10)
Thousand = (A // 10)
if Thousand == Ones and Tens == Hundred:
    print("YES")
else:
    print("NO")