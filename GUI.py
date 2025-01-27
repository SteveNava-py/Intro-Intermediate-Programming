from tkinter import *

class GUITest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        #self.setupGUI()

    def setupGUI(self):
        l1 = Label(self.master, text="A label")
        l1.grid(row=0, column=0, sticky=W)

        l2 = Label(self.master, text="Another label")
        l2.grid(row=1, column=0, sticky=W)

        self.l3 = Label(self.master, text="A third label, centered")
        self.l3.grid(row=2, column=0, columnspan=2, sticky=E + W)

        self.e1 = Entry(self.master)
        self.e1.grid(row=0, column=1)

        self.e2 = Entry(self.master)
        self.e2.insert(END, "user input")
        self.e2.grid(row=1, column=1)

        self.check = IntVar()
        c1 = Checkbutton(self.master, text="Some Checkbutton option", variable = self.check)
        c1.grid(row=3, column=0, columnspan=2, sticky=W)

        b1 = Button(self.master, text="A button", command=self.quit)
        b1.grid(row=3, column=2)

        b2 = Button(self.master, text="Another button", command=self.onClick)
        b2.grid(row=3, column=3)

    def onClick(self):
        if self.check.get() == 1:
            print("The checkButton is checked")
        else:
            print("The checkbutton is unchecked")
        self.l3["text"] = "You clicked a button"
        self.e1.delete(0, END)
        self.e1.insert(0, "YOU HIT ME")


window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()

