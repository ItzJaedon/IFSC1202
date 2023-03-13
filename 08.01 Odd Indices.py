inputstr = input("Enter Values Separated by Spaces: ")
inputlist = inputstr.split()
numberlist = []
for i in range(len(inputlist)):
    numberlist.append(int(inputlist[i]))
for i in range(1, len(numberlist), 2):
    print(numberlist[i])