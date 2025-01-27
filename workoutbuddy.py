######################################################################
# Project Tite: Workout buddy
# Team Member Names: Zachary Ryan, Timothy Gilley, Steven Navarrette
# Creating a workout user interface that assists with weight loss while providing heart rate data and workouts
# This magnitude of GUI was a difficult task, it took many Youtube videos, Online tutorials, and Pyhton Websites
# Some code was pulled from previous modules on Blackboard
######################################################################

# Import needed libraries
# Found some libraries that we havent used on Python websites- These were a big help on improving our GUI
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import serial
import threading
import time

# Initialize serial port
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except serial.SerialException as e:
    messagebox.showerror("Serial Connection Error", f"Failed to connect on {SERIAL_PORT}: {e}")
    arduino = None


# Mixing OOP and GUI programming to set attributes of the class
class WorkoutBuddy:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Buddy")
        self.root.configure(bg='white')
        self.root.state('zoomed')
        self.selected_workouts = []
        self.workout_count = 0
        self.current_heart_rate = "Not Connected"
        self.load_user_data()
        self.create_home_screen()

    # Using json files to save and load profiles
    def load_user_data(self):
        self.user_data = {}
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                self.user_data = json.load(file)

    # Function to clear the widget
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Function that makes the home screen
    def create_home_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Workout Buddy", font=('Arial', 42, 'bold'), fg='white', bg='black').pack(pady=40)
        tk.Button(self.root, text="Login", font=('Arial', 25), bg='white', fg='black',
                  command=self.create_login_window).pack(pady=20)
        tk.Button(self.root, text="Create Profile", font=('Arial', 25), bg='white', fg='black',
                  command=self.create_profile_window).pack(pady=20)

    # Function that creates the login window
    def create_login_window(self):
        self.clear_screen()
        tk.Label(self.root, text="Username:", font=('Arial', 18), fg='white', bg='black').pack(pady=10)
        username_entry = tk.Entry(self.root, font=('Arial', 16), bg='white', fg='black')
        username_entry.pack(pady=10)
        tk.Label(self.root, text="Password:", font=('Arial', 18), fg='white', bg='black').pack(pady=10)
        password_entry = tk.Entry(self.root, font=('Arial', 16), show='*', bg='white', fg='black')
        password_entry.pack(pady=10)

        # Function implements the login process
        def attempt_login():
            username = username_entry.get()
            password = password_entry.get()
            user = self.user_data.get(username)
            if user and user.get('Password') == password:
                self.create_user_profile(username)
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password")
                self.create_home_screen()

        login_button = tk.Button(self.root, text="Login", font=('Arial', 20), bg='white', fg='black',
                                 command=attempt_login)
        login_button.pack(pady=20)
        self.create_back_button()

    # Functions that creates and saves profile through GUI buttons, user input, and conditionals
    def create_profile_window(self):
        self.clear_screen()
        fields = ['Name', 'Height (in inches)', 'Age', 'Gender', 'Username', 'Password', 'Weight (lbs)',
                  'Current Activity Level from 1-10']
        entries = {}
        for field in fields:
            tk.Label(self.root, text=field + ":", font=('Arial', 20), fg='black', bg='white').pack(pady=5)
            entry = tk.Entry(self.root, font=('Arial', 16), bg='white', fg='black')
            entry.pack(pady=5)
            entries[field] = entry

        # Deciphers if username is in Json file
        def save_profile():
            user_info = {field: entries[field].get() for field in fields}
            if user_info['Username'] in self.user_data:
                messagebox.showerror("Error", "Username already exists!")
                return
            self.user_data[user_info['Username']] = user_info
            with open('users.json', 'w') as file:
                json.dump(self.user_data, file)
            self.create_user_profile(user_info['Username'])

        save_button = tk.Button(self.root, text="Save Profile", font=('Arial', 20), bg='white', fg='black',
                                command=save_profile)
        save_button.pack(pady=20)
        self.create_back_button()

    # Creating of user profile
    def create_user_profile(self, username):
        self.clear_screen()
        user_data = self.user_data[username]
        tk.Label(self.root, text=f"{user_data['Name']}'s Profile", font=('Arial', 24, 'bold'), fg='black',
                 bg='white').pack(pady=20)
        tk.Label(self.root, text=f"Workouts completed: {self.workout_count}", font=('Arial', 16), fg='black',
                 bg='white').pack(pady=10)

        for key in ['Name', 'Height (in inches)', 'Age', 'Gender', 'Weight (lbs)', 'Current Activity Level from 1-10']:
            tk.Label(self.root, text=f"{key}: {user_data[key]}", font=('Arial', 16), fg='black', bg='white').pack(
                pady=5)

        tk.Button(self.root, text="Set Weight Loss Goal", font=('Arial', 16), bg='white', fg='black',
                  command=lambda: self.set_weight_loss_goal(username)).pack(pady=10)
        tk.Button(self.root, text="Get Caloric Intake Plan", font=('Arial', 16), bg='white', fg='black',
                  command=lambda: self.show_caloric_intake_plan(username)).pack(pady=10)
        tk.Button(self.root, text="Start Workout", font=('Arial', 16), bg='white', fg='black',
                  command=lambda: self.start_workout(username)).pack(pady=10)
        self.create_back_button()

    # Function that saves the user weight loss goal input
    def set_weight_loss_goal(self, username):
        weight_loss_goal = simpledialog.askfloat("Weight Loss Goal", "How many pounds do you want to lose per week?")
        if weight_loss_goal is not None:
            self.user_data[username]['weight_loss_goal'] = weight_loss_goal
            with open('users.json', 'w') as file:
                json.dump(self.user_data, file)
            self.create_user_profile(username)

    # Functions that calculate the users caloric needs based on user input
    def calculate_caloric_needs(self, username):
        user_data = self.user_data[username]
        return self.BMR_CALC(
            height=float(user_data['Height (in inches)']),
            age=int(user_data['Age']),
            sex=user_data['Gender'],
            activity_level=int(user_data['Current Activity Level from 1-10']),
            weight=float(user_data['Weight (lbs)'])
        )

    def BMR_CALC(self, height, age, sex, activity_level, weight):
        activity_deviation = activity_level - 5
        if sex.lower() == 'male':
            BMR = ((10 / 2.2) * weight) + (6.25 * 2.54 * height) - (5 * age) + 5
            BMR += (0.08 * activity_deviation * BMR)
        else:
            BMR = ((10 / 2.2) * weight) + (6.25 * 2.54 * height) - (5 * age) - 161
            BMR += (0.08 * activity_deviation * BMR)
        return BMR

    def show_caloric_intake_plan(self, username):
        BMR = self.calculate_caloric_needs(username)
        messagebox.showinfo("Caloric Intake Plan", f"Daily Caloric Intake: {BMR:.2f} calories to reach your goal.")

    # Functions that implement workout process
    def start_workout(self, username):
        self.clear_screen()
        self.workout_start_time = time.time()
        self.heart_rate_readings = []
        resources = {
            "Weights": ["Barbell Bench Press", "Dumbbell Bench Press", "Dumbbell Chest Fly"],
            "No Equipment Strength": ["Pushups", "Pull-ups", "Plank"],
            "Equipment Cardio": ["Treadmill", "Stair Master", "Elliptical"],
            "No Equipment Cardio": ["Jogging", "Speed Jumping", "Stretching"]
        }
        self.selected_workouts = []

        def add_workout(workout_name):
            self.selected_workouts.append(workout_name)

        for category, workouts in resources.items():
            tk.Label(self.root, text=category, font=('Arial', 20, 'bold'), fg='white', bg='black').pack(pady=10)
            for workout in workouts:
                btn = tk.Button(self.root, text=workout, font=('Arial', 16), bg='white', fg='black',
                                command=lambda w=workout: add_workout(w))
                btn.pack(pady=5)

        def finish_selection():
            if not self.selected_workouts:
                messagebox.showinfo("No Workouts Selected", "Please select at least one workout to start.")
                return
            self.create_workout_interface(username)

        finish_btn = tk.Button(self.root, text="Finish Selection and Start Workout", font=('Arial, 20'), bg='white',
                               fg='black', command=finish_selection)
        finish_btn.pack(pady=20)
        self.create_back_button()

    # Screen that displays workout information.
    # Implimenting the Arduino code into our Python and calling on the port ACM0

    def create_workout_interface(self, username):
        self.clear_screen()
        tk.Label(self.root, text="Your Workout Session", font=('Arial', 24, 'bold'), fg='white', bg='black').pack(
            pady=20)

        for workout in self.selected_workouts:
            tk.Label(self.root, text=workout, font=('Arial', 18), fg='black', bg='white').pack(pady=10)

        heart_rate_label = tk.Label(self.root, text=f"Your current heart rate is: {self.current_heart_rate}",
                                    font=('Arial', 16), fg='black', bg='white')
        heart_rate_label.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

        # Makes sure the value is valid
        def update_heart_rate():
            while True:
                if arduino.in_waiting > 0:
                    line = arduino.readline().decode('utf-8').strip()
                    if line.isdigit():  # Ensure it's a valid heart rate reading
                        self.current_heart_rate = line
                        self.heart_rate_readings.append(int(line))
                        heart_rate_label.config(text=f"Your current heart rate is: {self.current_heart_rate}")

        threading.Thread(target=update_heart_rate, daemon=True).start()

        def end_workout():
            workout_duration = time.time() - self.workout_start_time
            if self.heart_rate_readings:
                average_heart_rate = sum(self.heart_rate_readings) / len(self.heart_rate_readings)
            else:
                average_heart_rate = "No Data"
            calories_burned = self.calculate_calories_burned(username, workout_duration, average_heart_rate)
            self.create_workout_summary(username, average_heart_rate, calories_burned, workout_duration)

        end_workout_btn = tk.Button(self.root, text="End Workout", font=('Arial', 20), bg='black', fg='white',
                                    command=end_workout)
        end_workout_btn.pack(side=tk.LEFT, anchor='sw', padx=20, pady=20)

    # takes user's data and converts to cals
    def calculate_calories_burned(self, username, duration, heart_rate):
        user_data = self.user_data[username]
        age = int(user_data['Age'])
        weight = float(user_data['Weight (lbs)'])
        if user_data['Gender'].lower() == 'male':
            # formula using average BMR composition data
            calories = ((age * 0.2017) - (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * duration / 4.184
        else:
            calories = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * duration / 4.184
        return max(0, calories)

    # Displays all the data using formulas we came up with
    def create_workout_summary(self, username, heart_rate, calories, duration):
        self.clear_screen()
        tk.Label(self.root, text="Workout Summary", font=('Arial', 24, 'bold'), fg='white', bg='black').pack(pady=20)
        tk.Label(self.root, text=f"Average Heart Rate: {heart_rate} bpm", font=('Arial', 18), fg='black',
                 bg='white').pack(pady=10)
        tk.Label(self.root, text=f"Calories Burned: {calories:.2f} calories", font=('Arial', 18), fg='black',
                 bg='white').pack(pady=10)
        tk.Label(self.root, text=f"Workout Duration: {duration / 60:.2f} minutes", font=('Arial', 18), fg='black',
                 bg='white').pack(pady=10)
        tk.Button(self.root, text="Return to Profile", font=('Arial', 16), bg='white', fg='black',
                  command=lambda: self.create_user_profile(username)).pack(pady=20)

    def create_back_button(self):
        back_button = tk.Button(self.root, text="Back", font=('Arial', 16), bg='white', fg='black',
                                command=self.create_home_screen)
        back_button.pack(anchor='nw', padx=10, pady=10)


# Main window
root = tk.Tk()
app = WorkoutBuddy(root)
root.mainloop()

