with open("09.04 Conversion.txt", "r") as file:
    conversion_table = [line.split() for line in file.readlines()]
from_value = float(input("Enter From Value: "))
from_unit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
to_unit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
from_unit_row = -1
for i in range(1, len(conversion_table)):
    if conversion_table[i][0] == from_unit:
        from_unit_row = i
        break
if from_unit_row == -1:
    print("FromUnit is not valid")
    exit()
to_unit_col = -1
for i in range(1, len(conversion_table[0])):
    if conversion_table[0][i] == to_unit:
        to_unit_col = i
        break
if to_unit_col == -1:
    print("ToUnit is not valid")
    exit()
multiplier = float(conversion_table[from_unit_row][to_unit_col])
result = round(from_value * multiplier, 7)
print(from_value, from_unit, "=", result, to_unit)
