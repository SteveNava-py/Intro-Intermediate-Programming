###########################################################################################
# Name: Steven Navarrette
# Date:02/22/2024
# Description: calculator code with some added buttons using OOP programming and GUI programming
###########################################################################################
from tkinter import *
from tkinter import PhotoImage


# the main GUI
class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()

    #     for row in range(6):
    #
    #         Grid.rowconfigure(self, row, weight=1)
    # # there are 4 columns (0 through 3)
    #     for col in range(4):
    #         Grid.columnconfigure(self, col, weight=1)

    # sets up the GUI
    # I came to Jonathan's TA office hrs and he helped me make some modifications to this setup

    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", \
                             height=2, width=15)
        self.display.grid(row=0, column=0, columnspan=4, sticky=E + W + N + S)
        # the first row
        #(
        img = PhotoImage(file="images-gif/lpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("("))
        button.image = img
        button.grid(row=1, column=0, sticky=N + S + E + W)
        #)
        img = PhotoImage(file="images-gif/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("#"))
        button.image = img
        button.grid(row=1, column=1, sticky=N + S + E + W)
        #AC(clear)
        img = PhotoImage(file="images-gif/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N + S + E + W)
        #Power (**)
        img = PhotoImage(file="images-gif/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("**"))
        button.image = img
        button.grid(row=1, column=3, sticky=N + S + E + W)
	# the second row
	# 7
        img = PhotoImage(file="images-gif/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N + S + E + W)
	# 8
        img = PhotoImage(file="images-gif/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N + S + E + W)
	# 9
        img = PhotoImage(file="images-gif/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N + S + E + W)
	# /
        img = PhotoImage(file="images-gif/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N + S + E + W)
	# the third row
	# 4
        img = PhotoImage(file="images-gif/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N + S + E + W)
	# 5
        img = PhotoImage(file="images-gif/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N + S + E + W)
	# 6
        img = PhotoImage(file="images-gif/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N + S + E + W)
	# *
        img = PhotoImage(file="images-gif/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N + S + E + W)
	# the fourth row
	# 1
        img = PhotoImage(file="images-gif/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness = 0, activebackground = "white", command=lambda:self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N + S + E + W)
	# 2
        img = PhotoImage(file="images-gif/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N + S + E + W)
	# 3
        img = PhotoImage(file="images-gif/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N + S + E + W)
	# -
        img = PhotoImage(file="images-gif/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N + S + E + W)
	# the fifth row
	# 0
        img = PhotoImage(file="images-gif/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N + S + E + W)
	# .
        img = PhotoImage(file="images-gif/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N + S + E + W)
	# =
        img = PhotoImage(file="images-gif/eql.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("="))
        button.image = img
        button.grid(row=5, column=2, sticky=N + S + E + W)
	# +
        img = PhotoImage(file="images-gif/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N + S + E + W)

    # added buttons
    # n!
        img = PhotoImage(
            file="images-gif/fact.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
            highlightthickness=0, activebackground="white", command=lambda:self.process("n!"))
        button.image = img
        button.grid(row=5, column=4, sticky=N + S + E + W)
    # <-
        img = PhotoImage(
            file="images-gif/bak.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
            highlightthickness=0, activebackground="white", command=lambda:self.process("<-"))
        button.image = img
        button.grid(row=1, column=4, sticky=N + S + E + W)
    # M+
        img = PhotoImage(file="images-gif/Mplus.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
            highlightthickness=0, activebackground="white", command=lambda:self.process("M+"))
        button.image = img
        button.grid(row=2, column=4, sticky=N + S + E + W)
    # MR
        img = PhotoImage(file="images-gif/MR.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
            highlightthickness=0, activebackground="white", command=lambda:self.process("MR"))
        button.image = img
        button.grid(row=3, column=4, sticky=N + S + E + W)
    # MC
        img = PhotoImage(file="images-gif/MC.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
            highlightthickness=0, activebackground="white", command=lambda:self.process("MC"))
        button.image = img
        button.grid(row=4, column=4, sticky=N + S + E + W)


        self.pack(fill=BOTH, expand=1)

    #processes button presses
    #I showed up to Jonathan's office hours and he provided me with hints and pointers to make this function
    def process(self, button):
        if button == "AC":
            self.display["text"] = ""
        elif button == "=":
            expr = self.display["text"]
            try:
                result = eval(expr)
                if len(str(result)) <= 14:
                    self.display["text"] = str(result)[:11] + "..."
                else:
                    self.display["text"] = str(result)
            except:
                self.display["text"] = "ERROR"
        elif button == "<-":
            num = self.display["text"]
            self.display["text"] = str(num)[:-1]
        elif button == "n!":
            num = int(self.display["text"])
            fact = 1
            for num in range(2, num + 1):
                fact *= num
            self.display["text"] = fact
        elif button == "M+":
            self.num = self.display["text"]
        elif button == "MR":
            self.display["text"] += self.num
        elif button == "MC":
            self.num = ""
        else:
            self.display["text"] += button


##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()

