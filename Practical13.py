
import math

class TwoDPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


p1 = TwoDPoint(2, 3)
p2 = TwoDPoint(5, 7)

print("First point:", p1)
print("Second point:", p2)
print("Distance between points:", p1.distance(p2))