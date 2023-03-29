with open('09.06 CityTemps.txt', 'r') as f:
    temps = []
    for line in f:
        line = line.strip()
        if not line:
            break
        parts = line.split()
        temps.append(parts)
for row in temps:
    total_temp = 0
    for temp in row[1:]:
        total_temp += float(temp)
    avg_temp = str(total_temp / (len(row) - 1))
    row.append(avg_temp)
print("City\tMo\tTu\tWe\tTh\tFr\tSa\tSu\tAverage")
for row in temps:
    print("\t".join(row))