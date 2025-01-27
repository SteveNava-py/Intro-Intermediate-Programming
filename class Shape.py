class Shape(object):
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        self._color = c


class Rectangle(Shape):
    def __init__(self, c, l, w):
        Shape.__init__(self, c)
        self.length = l
        self.width = w

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, l):
        self._length = l

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    def getarea(self):
        return self.length * self.width

    def __str__(self):
        return "This is a rectangle of color: " + self.color + "Area: " + str(self.getarea())
