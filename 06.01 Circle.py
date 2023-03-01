import math
def diameter(radius):
    return 2 * radius
def circumference(radius):
    return 2 * math.pi * radius
def area(radius):
    return math.pi * radius ** 2
with open('06.01 Radius.txt') as f:
    radii = [float(line.strip()) for line in f]
print(f"{'Radius':>15} {'Diameter':>15} {'Circumference':>15} {'Area':>15}")
for radius in radii:
    d = diameter(radius)
    c = circumference(radius)
    a = area(radius)
    print(f"{radius:>15.5f} {d:>15.5f} {c:>15.5f} {a:>15.5f}")
