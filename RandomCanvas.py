from tkinter import *
from random import randint

WIDTH = 400
HEIGHT = 400
POINT_COLORS = ["red", "green", "blue", "orange"]
POINT_RADIUS = 1
NUM_POINTS = 2500

class Points(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        #Fill = BOTH expanding the canvas vertically and horizontally
        #Expand = 1 to fill out any extra spaces
        self.pack(fill=BOTH, expand = 1)

    def plotPoints(self, n):
        for i in range(0,n):
            x = randint(0, WIDTH -1)
            y = randint(0, HEIGHT-1)
            self.plot(x,y)

    def plot(self, x, y):
        i = randint(0, len(POINT_COLORS)-1)
        color = POINT_COLORS[i]
        self.create_oval(x, y, x+POINT_RADIUS*2, y+POINT_RADIUS*2, fill=color)

###Main#############
window = Tk()
window.geometry("{}x{}".format(WIDTH,HEIGHT))
p = Points(window)
p.plotPoints(NUM_POINTS)
window.mainloop()


