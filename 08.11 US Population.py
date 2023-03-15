def calculate_change(current, previous):
    if previous == 0:
        return "N/A"
    else:
        change = current - previous
        percent_change = (change / previous) * 100
        return change, percent_change
with open('08.11 USPopulation.txt', 'r') as file:
    data = [int(line.strip()) * 1000 for line in file]
print("{:<6} {:<15} {:<10} {}".format("Year", "Population", "Change", "Percent Change"))
average_change = 0
min_change = None
max_change = None
for i in range(len(data)):
    year = 1950 + i
    population = data[i]
    if i == 0:
        change = "N/A"
        percent_change = "N/A"
    else:
        change, percent_change = calculate_change(population, data[i-1])
    if i > 0:
        average_change += abs(change)
        if min_change is None or change < min_change[0]:
            min_change = (change, year)
        if max_change is None or change > max_change[0]:
            max_change = (change, year)
    print("{:<6} {:<15,} {:<10} {:.3}%".format(year, population, change, percent_change))
average_change /= len(data) - 1
print("\nAverage Change = {:.1f}".format(average_change))
print("Minimum Change = {} ({})".format(min_change[0], min_change[1]))
print("Maximum Change = {} ({})".format(max_change[0], max_change[1]))