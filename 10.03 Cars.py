class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        self.speed = 0
    def accelerate(self, value):
        self.speed += value
    def brake(self, value):
        self.speed = max(0, self.speed - value)
car = Car("Jeep", 2014)
data = [(60, ), (-5, ), (-10, ), (3, )]
print("  change", "   speed")
for change in data:
    if change[0] > 0:
        car.accelerate(change[0])
    else:
        car.brake(abs(change[0]))
    print(f"{change[0]:>6} {car.speed:>6}")
