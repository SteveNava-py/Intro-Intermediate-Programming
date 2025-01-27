# Name: Steven Navarrette
# Date: 04/19/2024
# Description: A GUI code that runs a multiplayer dice game.
# The game takes user input for the amount of games the user wants to play and how many rolls in each
# It displays the results for each game and the overall statistics when the game is finished

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from random import randint


def play_game():

    # Get the number of games and rolls per game from the entry widgets
    num_games = int(games_entry.get())
    num_rolls = int(rolls_entry.get())

    # Initialize variables to keep track of wins for each group
    group1_wins = 0
    group2_wins = 0
    tie_count = 0

    # Clear previous stats
    stats_text_widget.delete('1.0', END)

    # Loop through each game
    for game in range(1, num_games + 1):
        group1_points = 0
        group2_points = 0

        # Loop through each roll in the game
        for roll in range(num_rolls):

            # Simulate dice rolls
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)
            stats_text_widget.insert(END, f"\nRolling the dice...\n")
            stats_text_widget.insert(END, f"Dice 1: {dice1}\n")
            stats_text_widget.insert(END, f"Dice 2: {dice2}\n\n")

            # Determine points for each group based on the dice rolls
            if dice1 > dice2:
                group1_points += 1
            elif dice1 < dice2:
                group2_points += 1

        # Determine the winner of the game
        if group1_points > group2_points:
            group1_wins += 1
            stats_text_widget.insert(END,
                                     f"Game {game}: Group 1 wins ({group1_points} points vs {group2_points} points)\n")
        elif group1_points < group2_points:
            group2_wins += 1
            stats_text_widget.insert(END,
                                     f"Game {game}: Group 2 wins ({group2_points} points vs {group1_points} points)\n")
        else:

            # In case of tie, randomly choose a winner
            tie_count += 1
            winner = randint(1, 2)
            if winner == 1:
                group1_wins += 1
                stats_text_widget.insert(END,
                                         f"Game {game}: Tie - Group 1 wins ({group1_points} points vs {group2_points} points)\n")
            else:
                group2_wins += 1
                stats_text_widget.insert(END,
                                         f"Game {game}: Tie - Group 2 wins ({group2_points} points vs {group1_points} points)\n")

    # Display summary statistics
    total_games = num_games
    group1_percentage = (group1_wins / total_games) * 100 if total_games > 0 else 0
    group2_percentage = (group2_wins / total_games) * 100 if total_games > 0 else 0
    tie_percentage = (tie_count / total_games) * 100 if total_games > 0 else 0

    stats_text_widget.insert(END, f"\nSummary:\n")
    stats_text_widget.insert(END, f"Group 1 wins: {group1_wins} ({group1_percentage:.2f}%)\n")
    stats_text_widget.insert(END, f"Group 2 wins: {group2_wins} ({group2_percentage:.2f}%)\n")
    stats_text_widget.insert(END, f"Ties: {tie_count} ({tie_percentage:.2f}%)\n")


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
simulate_button = Button(frame, text="Play", command=play_game)
simulate_button.grid(row=2, column=0, columnspan=2, pady=(5, 10))

# Text widget with scrollbar for stats
stats_text_widget = ScrolledText(window, height=25, width=70)
stats_text_widget.pack()

window.mainloop()
