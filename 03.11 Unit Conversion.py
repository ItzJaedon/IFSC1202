from_value = float(input("Enter From Value: "))
from_unit = input("Enter From Unit (in, ft, yd, mi): ")

if from_unit not in ["in", "ft", "yd", "mi"]:
    print("FromUnit is not valid")
    exit()

to_unit = input("Enter To Unit (in, ft, yd, mi): ")

if to_unit not in ["in", "ft", "yd", "mi"]:
    print("ToUnit is not valid")
    exit()

multiplier = 1.0
if from_unit == "ft" and to_unit == "yd":
    multiplier = 0.3333333333
elif from_unit == "in" and to_unit == "ft":
    multiplier = 0.0833333333
elif from_unit == "in" and to_unit == "yd":
    multiplier = 0.0277777778
elif from_unit == "in" and to_unit == "mi":
    multiplier = 0.0000157828
elif from_unit == "ft" and to_unit == "in":
    multiplier = 12.0
elif from_unit == "ft" and to_unit == "mi":
    multiplier = 0.000189394
elif from_unit == "ft" and to_unit == "mi":
    multiplier = 0.000189394
elif from_unit == "yd" and to_unit == "in":
    multiplier = 36.0
elif from_unit == "yd" and to_unit == "ft":
    multiplier = 3.0
elif from_unit == "yd" and to_unit == "mi":
    multiplier = 0.000568182
elif from_unit == "mi" and to_unit == "in":
    multiplier = 63360.0
elif from_unit == "mi" and to_unit == "ft":
    multiplier = 5280.0
elif from_unit == "mi" and to_unit == "yd":
    multiplier = 1760.0

to_value = round(from_value * multiplier, 7)

print("%.7f %s = %.7f %s" % (from_value, from_unit, to_value, to_unit))