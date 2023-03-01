with open('06.04 EmptyLinesInput.txt') as fin, open('06.04 EmptyLinesOutput.txt', 'w') as fout:
    num_read = 0
    num_written = 0
    for line in fin:
        num_read += 1
        if line.strip():
            fout.write(line)
            num_written += 1
    print(f"{num_read} records read")
    print(f"{num_written} records written")
