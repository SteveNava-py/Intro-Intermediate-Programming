import tkinter as tk
import json


class Profile:
    def __init__(self, name, height, age, sex, mode, username, password, current_weight=None, goal_weight=None, activity=None, food_plan=None, current_strength=None, bench=None, squat=None, deadlift=None, total=None):
        self.name = name
        self.height = height
        self.age = age
        self.sex = sex
        self.mode = mode
        self.username = username
        self.password = password
        self.current_weight = current_weight
        self.goal_weight = goal_weight
        self.activity = activity
        self.food_plan = food_plan
        self.current_strength = current_strength
        self.bench = bench
        self.squat = squat
        self.deadlift = deadlift
        self.total = total

    # Stores profile data as dictionary and returns
    def to_dict(self):
        return {
            'name': self.name,
            'height': self.height,
            'age': self.age,
            'sex': self.sex,
            'mode': self.mode,
            'username': self.username,
            'password': self.password,
            'current_weight': self.current_weight,
            'goal_weight': self.goal_weight,
            'activity': self.activity,
            'food_plan': self.food_plan,
            'current_strength': self.current_strength,
            'bench': self.bench,
            'squat': self.squat,
            'deadlift': self.deadlift,
            'total': self.total
        }

    # Converts dictionary back to profile class object
    @staticmethod
    def from_dict(data):
        return Profile(**data)


# Stores class instance profile data to JSON format in  new file
def save_profile(profile):
    with open("profiles.json", "a") as file:
        profile_data = {
            "name": profile.name,
            "height": profile.height,
            "age": profile.age,
            "sex": profile.sex,
            "mode": profile.mode,
            "username": profile.username,
            "password": profile.password
        }
        file.write(json.dumps(profile_data) + "\n")


# Reads profile from JSON file and converts back to profile object
# Works with from_dict staticmethod
def load_profiles():
    profiles = []
    with open("profiles.json", "r") as file:
        for line in file:
            profile_data = json.loads(line)
            profile = Profile(**profile_data)
            profiles.append(profile)
    return profiles


def create_profile():
    name = name_entry.get()
    height = int(height_entry.get())
    age = int(age_entry.get())
    sex = sex_entry.get()
    mode = mode_var.get()
    username = username_entry.get()
    password = password_entry.get()

    person = Profile(name, height, age, sex, mode, username, password)
    save_profile(person)
    refresh_profiles_list()


def refresh_profiles_list():
    profiles_list.delete(0, tk.END)
    for profile in profiles:
        profiles_list.insert(tk.END, profile.name)

def on_profile_select(event):
    index = profiles_list.curselection()[0]
    profile = profiles[index]
    # Display profile details in additional labels or widgets


# Modify this for GUI
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    for profile in profiles:
        if profile.username == entered_username and profile.password == entered_password:
            print("Login successful!")
            # add the rest of what we want to do here
            return

    print("Login failed. Invalid username or password.")
    # add the rest of what we want to do here
    pass


# Main application window
root = tk.Tk()
root.title("Welcome to WorkOut Buddy!")

# Labels and widgets
tk.Label(root, text="First Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Height (in inches):").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Label(root, text="Age:").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
sex_entry = tk.Entry(root)
sex_entry.grid(row=3, column=1)

mode_var = tk.IntVar()
tk.Label(root, text="Choose a Mode").grid(row=4, column=0)
tk.Radiobutton(root, text="Lose Fat", variable=mode_var, value=1).grid(row=4, column=1)
tk.Radiobutton(root, text="Gain Strength", variable=mode_var, value=2).grid(row=4, column=2)

tk.Label(root, text="Username:").grid(row=5, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=5, column=1)

tk.Label(root, text="Password:").grid(row=6, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=6, column=1)

# Buttons
create_button = tk.Button(root, text="Create Profile", command=create_profile)
create_button.grid(row=7, column=0)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=7, column=1)

# Display profiles
profiles_list = tk.Listbox(root)
profiles_list.grid(row=8, columnspan=2, padx=10, pady=10, sticky="nsew")
profiles_list.bind("<<ListboxSelect>>", on_profile_select)

# Load profiles
profiles = load_profiles()
refresh_profiles_list()

root.mainloop()
