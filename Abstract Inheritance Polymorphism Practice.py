class Shape(object):
    def __init__(self, name):
        self.name = name

    def area(self):
        print('no')

    def draw(self):
        print('nada')

    def __str__(self):
        return "This is a shape object"


class Rectangle(Shape):
    def __init__(self, name, l, w):
        Shape.__init__(self, name)
        # or super().__init__(name)
        self.length = l
        self.width = w

    def area(self):
        a = self.length * self.width
        print('The area of the rectangle is: ' + str(a))

    def draw(self):
        for i in range(self.length):
            for j in range(self.width):
                print('*', end='')
            print()

    def __str__(self):
        return "This is a rectangle object with length = " + str(self.length) + " and a width = " + str(self.width)

class Triangle(Shape):
    def __init__(self, name, height, base):
        super().__init__(name)
        self.height = height
        self.base = base

    def __str__(self):
        return "This is a triangle with a base = " + str(self.base) + " and a height = " + str(self.height)

    def area(self):
        a = 0.5*self.base*self.height
        print('The area of this triangle: ' + str(a))

    def draw(self):
        for i in range(1, self.height):
            print('*'*i)
            print()


# Main


s = Shape('My shape')
r = Rectangle('My rectangle', 10, 20)
print(s)
print(r)
s.area()
s.draw()
r.area()
r.draw()
t = Triangle("My triangle", 10, 20)
print(t)
t.area()
t.draw()