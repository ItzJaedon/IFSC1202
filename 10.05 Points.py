from math import sqrt, atan, pi

# Step 1 - Define the class object "Point"
class Point:
    # Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
        # Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
        
    # Step 4 - Define the methods for the object
    # ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

# Distance function
def Distance(PointA, PointB):
    distance = sqrt((PointB.x - PointA.x) ** 2 + (PointB.y - PointA.y) ** 2)
    return distance

# MidPoint function
def MidPoint(PointA, PointB):
    midpoint_x = (PointB.x + PointA.x) / 2
    midpoint_y = (PointB.y + PointA.y) / 2
    midpoint = Point(midpoint_x, midpoint_y)
    return midpoint

# XAngle function
def XAngle(PointA, PointB):
    slope = (PointB.y - PointA.y) / (PointB.x - PointA.x)
    xangle = atan(slope) * 180 / pi
    return xangle
print("{:<18} {:<18} {:<12} {:<18} {:<8}".format("Point A", "Point B", "Distance", "Midpoint", "XAngle"))
with open("10.05 Points.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        # Create two Point objects
        PointA = Point(float(data[0]), float(data[1]))
        PointB = Point(float(data[2]), float(data[3]))
print("-" * 78)
print("{:<18} {:<18} {:<12.2f} {:<18} {:<8.2f}".format(PointA.ToString(), PointB.ToString(), distance, midpoint.ToString(), xangle))