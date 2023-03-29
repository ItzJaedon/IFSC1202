def print_list(a):
    for row in a:
        print(' '.join(str(x) for x in row))
def scale_list(a, s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= s
with open('09.03 NumbersList.txt', 'r') as f:
    a = [[int(x) for x in line.split()] for line in f]
print("Original List:")
print_list(a)
s = float(input("Enter scale value: "))
scale_list(a, s)
print("Scaled List:")
print_list(a)
