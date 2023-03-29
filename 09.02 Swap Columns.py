def print_list(a):
    for row in a:
        print(" ".join(str(elem) for elem in row))
def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]
with open("09.02 NumbersList.txt") as f:
    a = [list(map(int, line.split())) for line in f]
print("Original list:")
print_list(a)
i = int(input("Enter first column number to swap: "))
j = int(input("Enter second column number to swap: "))
swap_columns(a, i, j)
print("List with swapped columns:")
print_list(a)
