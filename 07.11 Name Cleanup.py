def ProperCase(s):
    return s[0].upper() + s[1:].lower()
def RemoveNewLine(s):
    return s.replace("\n", "")
def Trim(s):
    return s.strip()
def FirstName(s):
    return ProperCase(s[:s.find(" ")])
def LastName(s):
    return ProperCase(s[s.rfind(" ")+1:])
def MiddleName(s):
    middle = s[s.find(" ")+1:s.rfind(" ")]
    if middle:
        middle = Trim(middle)
        middle = ProperCase(middle)
        if len(middle) == 1:
            middle += "."
    else:
        middle = ""
    return middle
print("{:<12} {:<12} {:<10}".format("First Name", "Middle Name", "Last Name"))
print("{:<12} {:<12} {:<10}".format("-----------", "-----------", "----------"))
with open("07.11 Names.txt", "r") as f:
    for line in f:
        line = Trim(line)
        line = RemoveNewLine(line)
        first = FirstName(line)
        middle = MiddleName(line)
        last = LastName(line)
        if middle:
            print("{:<12} {:<12} {:<10}".format(first, middle, last))
        else:
            print("{:<12} {:<12} {:<10}".format(first, "", last))