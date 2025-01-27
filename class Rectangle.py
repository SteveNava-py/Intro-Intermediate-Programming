class Rectangle(object):
    # class constructor
    def __init__(self, length, width):
        self._length = length  # length member variable
        self._width = width  # width member variable

    # getters
    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    # setters
    @length.setter
    def length(self, length):
        if length < 0:
            print("WARNING: Negative values not allowed!")
        else:
            self._length = length

    @width.setter
    def width(self, width):
        if width < 0:
            print("Warning: Someone is changing the width!")
        else:
            self._width = width

    def calculatearea(self):
        return self.length * self.width

    def calculateperimeter(self):
        return (2 * self.length) + (2 * self.width)

    # Main


r1 = Rectangle(10, 5)
r2 = Rectangle(20, 40)
print("The area of rectangle 1 is " + str(r1.calculatearea()))
print("The perimeter of rectangle 1 is " + str(r1.calculateperimeter()))

print(r1)
print(r1.length)
print(r1.width)

r1.length = 100
print(r1.length)
