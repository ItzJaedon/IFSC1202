import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y   
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
def Distance(pointA, pointB):
    distance = math.sqrt((pointB.x - pointA.x)**2 + (pointB.y - pointA.y)**2)
    return distance
def MidPoint(pointA, pointB):
    x = (pointB.x + pointA.x) / 2
    y = (pointB.y + pointA.y) / 2
    return Point(x, y)
def XAngle(pointA, pointB):
    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)
    angle = math.atan(slope) * 180 / math.pi
    return angle
with open("10.05 Points.txt", "r") as f:
    for line in f:
        data = line.split(",")
        pointA = Point(float(data[0].replace(",", ".")), float(data[1].replace(",", ".")))
        pointB = Point(float(data[2].replace(",", ".")), float(data[3].replace(",", ".")))          
        distance = Distance(pointA, pointB)
        midpoint = MidPoint(pointA, pointB)
        xangle = XAngle(pointA, pointB)
        print("{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}".format(pointA.ToString(), pointB.ToString(), round(distance, 7), midpoint.ToString(), round(xangle, 7)))