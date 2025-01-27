class Circle(object):
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    def add(self, other_circle):
        return self.radius + other_circle.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return("The circle radius is: " + str(self.radius))

c1 = Circle(50)
c2 = Circle(30)
print(c1)
print(c2)
print(c1 == c2)
print(c1 > c2)
