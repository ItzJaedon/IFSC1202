m, n = map(int, input("Enter the number of rows and columns: ").split())
arr = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    arr[i] = list(map(int, input("Enter a line of data: ").split()))
print("Array:")
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
max_elem = arr[0][0]
max_i, max_j = 0, 0
for i in range(m):
    for j in range(n):
        if arr[i][j] > max_elem:
            max_elem = arr[i][j]
            max_i, max_j = i, j
print("The maximum value occured in row, column: " , max_i, max_j)
