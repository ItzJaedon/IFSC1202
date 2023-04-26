import math
class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isoceles"
        else:
            return "Scalene"
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
    def angles(self):
        angle1 = math.degrees(math.acos((self.s2 ** 2 + self.s3 ** 2 - self.s1 ** 2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1 ** 2 + self.s3 ** 2 - self.s2 ** 2) / (2 * self.s1 * self.s3)))
        angle3 = math.degrees(math.acos((self.s1 ** 2 + self.s2 ** 2 - self.s3 ** 2) / (2 * self.s1 * self.s2)))
        return [angle1, angle2, angle3]
TriangleList = []
with open('Exam Three Triangles.txt') as file:
    for line in file:
        s1, s2, s3 = map(float, line.strip().split(','))
        TriangleList.append(Triangle(s1, s2, s3))
print("{:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}{:>10}".format(
    "Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))
for triangle in TriangleList:
    print("{:>10} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f}".format(
        triangle.type(), triangle.s1, triangle.s2, triangle.s3, triangle.perimeter(), triangle.area(), *triangle.angles()))