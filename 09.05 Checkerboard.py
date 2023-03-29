def create_checkerboard(n):
    checkerboard = []
    top_row = ["+"]
    top_row.extend(["-" for i in range(n)])
    top_row.append("+")
    checkerboard.append(top_row)
    for i in range(n):
        row = ["|"]
        row.extend([" " for j in range(n)])
        row.append("|")
        checkerboard.append(row)
    bottom_row = ["+"]
    bottom_row.extend(["-" for i in range(n)])
    bottom_row.append("+")
    checkerboard.append(bottom_row)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i + j) % 2 == 0:
                checkerboard[i][j] = "*"
    for row in checkerboard:
        print("".join(row))
n = int(input("Enter Size: "))
create_checkerboard(n)
