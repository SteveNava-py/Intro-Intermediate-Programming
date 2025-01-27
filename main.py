from tkinter import *
from tkinter.scrolledtext import ScrolledText
from random import randint

# Initialize the main window
window = Tk()
window.title("Dice Roll Game")

# Create and pack the frame
frame = Frame(window)
frame.pack(padx=10, pady=10)

# Number of games
games_label = Label(frame, text="Number of games:")
games_label.grid(row=0, column=0, pady=(0, 5))
games_entry = Entry(frame)
games_entry.grid(row=0, column=1, pady=(0, 5))


# GUI setup for the dice roll game
rolls_label = Label(frame, text="Number of dice rolls per game:")
rolls_label.grid(row=1, column=0)
rolls_entry = Entry(frame)
rolls_entry.grid(row=1, column=1)

# Simulate button
simulate_button = Button(frame, text="Play") # modify and add the command
simulate_button.grid(row=2, column=0, columnspan=2, pady=(5, 10))

# Text widget with scrollbar for stats
stats_text_widget = ScrolledText(window, height=25, width=70)
stats_text_widget.pack()

window.mainloop()


