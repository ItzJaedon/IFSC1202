def FahrToCel(F):
    return (F - 32) * 5 / 9
with open('06.03 FTemps.txt') as fin, open('06.03 CTemps.txt', 'w') as fout:
    for line in fin:
        F = float(line.strip())
        C = FahrToCel(F)
        fout.write(f"{C:5.1f}\n")
num_records = sum(1 for line in open('06.03 CTemps.txt'))
print(f" {num_records} records Written.")