with open('06.05 CompareFileA.txt') as fileA, open('06.05 CompareFileB.txt') as fileB:
    line_num = 0
    num_diff = 0
    for lineA, lineB in zip(fileA, fileB):
        line_num += 1
        if lineA != lineB:
            print(f"Difference at line {line_num}:")
            print(f"File A: {lineA.strip()}")
            print(f"File B: {lineB.strip()}")
            num_diff += 1
    print(f"{num_diff} differences")
