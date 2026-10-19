
import math

class TwoDPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


class ThreeDPoint(TwoDPoint):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 +
                         (self.y - p.y)**2 +
                         (self.z - p.z)**2)


p1 = ThreeDPoint(2, 3, 4)
p2 = ThreeDPoint(5, 7, 8)

print("First point:", p1)
print("Second point:", p2)
print("Distance between points:", p1.distance(p2))
