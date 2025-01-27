###########################################################################################
# Name: Steven Navarrette
# Date: 3/24/2024
# Description: This game takes place in a mysterious and eery temple at the end of the universe
# The player is being hunted by the temple's keeper and must escape by avoiding him
# There is an Easter egg in the game where you collect all the items and unlock a secret ending...
# Enhancements: Include three more rooms, more objects, sound, images, a secret ending, and storytelling
# Note: I had significant help from Jonathan in his office hours
# He suggested I use the template on blackboard and the code for the functions in the pdf file in Blackboard
###########################################################################################
from tkinter import *
import pygame

pygame.mixer.init()
background = pygame.mixer.Sound("RoomAdventureOST/rooms.mp3")
death = pygame.mixer.Sound("RoomAdventureOST/death.mp3")
ending = pygame.mixer.Sound("RoomAdventureOST/ending.mp3")
secret_ending = pygame.mixer.Sound("RoomAdventureOST/secretending.mp3")


# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):

	# the constructor
	def __init__(self, name, image):

		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):

		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):

		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):

		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):

		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		s = ("Welcome to the end. \n"
			 "You are in Entropy's Temple. \n"
			 "YOU MUST ESCAPE. \n"
			 "The guardian of this temple, \n"
			 "THE ROLL, \n"
			 "Is after you! \n"
			 "To escape, make your way to Forbidden Gallery \n"
			 "Then go 'weast' \n"
			 "But if you want to know your destiny... \n"
			 "Collect ALL items \n"
			 "NOW RUN! \n\n\n\n")

		# first, the room name
		s += "You are in: {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the grabbables in the room
		s += "You can carry: "
		for grab in self.grabbables:
			s += grab + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s


# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):

	# the constructor
	def __init__(self, parent):

		# call the constructor in the superclass
		Frame.__init__(self, parent)

	# creates the rooms
	def createRooms(self):
		global finalroom
		r1 = Room("Sirius' Throne Room", "throne.gif")
		r2 = Room("Oblivion's Library", "fireplace.gif")
		r3 = Room("Hall of Leaders", "statue.gif")
		r4 = Room("Dome of All Seeing Eye", "eye.gif")
		r5 = Room("Shogunate's Temple", "shrine.gif")
		r6 = Room("Forbidden Gallery", "cape.gif")
		r7 = Room("Beginning's End", "ending.gif")

		r1.addExit("north", r2)
		r1.addExit("east", None)
		r1.addExit("south", None)
		r1.addExit("west", None)
		r1.addGrabbable("key")
		r1.addItem("throne", "The throne is extremely bright \n"
							 "I can only see white... ")
		r1.addItem("keys", "There are lots of keys on the throne  ")

		r2.addExit("north", None)
		r2.addExit("east", r4)
		r2.addExit("south", r1)
		r2.addExit("west", r3)
		r2.addItem("rug", "Long rug across the floor \n"
						  "Made of... yeti skin? ")
		r2.addItem("fireplace", "It is extremely hot in here \n"
								"The fire is blue ?! ")

		r3.addExit("north", r5)
		r3.addExit("east", r2)
		r3.addExit("south", None)
		r3.addExit("west", r4)
		r3.addGrabbable("book")
		r3.addItem("statue", "Its a statue...  \n"
							 "Wait what's that book he's holding \n"
							 "Looks like the book of Enoch ")

		r4.addExit("north", r6)
		r4.addExit("east", r3)
		r4.addExit("south", None)
		r4.addExit("west", r2)
		r4.addGrabbable("eye")
		r4.addItem("eyeball", "It looks... all-seeing")

		r5.addExit("north", None)
		r5.addExit("east", r6)
		r5.addExit("south", r3)
		r5.addExit("west", None)
		r5.addGrabbable("blade")
		r5.addItem("katana", "There is a katana in the temple \n"
							 "It can cut the fabric of... \n"
							 "REALITY")
		r5.addItem("door", "Where does this door lead ?")

		r6.addExit("north", None)
		r6.addExit("east", None)
		r6.addExit("south", None)
		r6.addExit("west", None)
		r6.addExit("weast", r7)
		r6.addGrabbable("cape")
		r6.addItem("sphere", "Why is that sphere floating ?")
		r6.addItem("cloak", "That cloak is levitating \n"
							"Trying to reach me hmm...")

		r7.addExit("north", None)
		r7.addExit("east", None)
		r7.addExit("south", None)
		r7.addExit("west", None)

		# set room 1 as the current room at the beginning of the game
		Game.currentRoom = r1
		# initialize the players inventory
		Game.inventory = []
		# set the final room to be room 7 to code the secret ending
		finalroom = r7

	# sets up the GUI
	def setupGUI(self):

		# organize the gui
		self.pack(fill=BOTH, expand=1)

		# sets player input up, widget, and background to white
		# binds return key, pushes it to bottom, fills horizontally, and gives focus
		Game.player_input = Entry(self, bg="white")
		Game.player_input.bind("<Return>", self.process)
		Game.player_input.pack(side=BOTTOM, fill=X)
		Game.player_input.focus()

		# sets image to the left, widget, and does not let image control widget size
		img = None
		Game.image = Label(self, width=int(WIDTH / 2), image=img)
		Game.image.image = img
		Game.image.pack(side=LEFT, fill=Y)
		Game.image.pack_propagate(False)

		# sets up text to right, adds another widget,  disables it by default, and doesn't let control widget size
		text_frame = Frame(self, width=WIDTH / 2)

		Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
		Game.text.pack(fill=Y, expand=1)
		text_frame.pack(side=RIGHT, fill=Y)
		text_frame.pack_propagate(False)

	# sets the current room image
	def setRoomImage(self):
		if (Game.currentRoom == None):
			# if dead, set the death image
			death.play()
			Game.img = PhotoImage(file='rolled.gif')

		elif Game.currentRoom is finalroom:
			# check if the user collected the items then set the room image for the ending
			if 'cape' and 'blade' and 'eye' and 'book' and 'key' in Game.inventory:
				background.stop()
				secret_ending.play()
				Game.img = PhotoImage(file="secretending.gif")
				Game.text.insert(END, "You collected all the items \n"
									  "Now face your destiny... \n"
									  "You have become THE ROLL \n"
									  "'Enter quit'")
			else:
				# otherwise play the usual ending
				background.stop()
				ending.play()
				Game.img = PhotoImage(file="ending.gif")
				Game.text.insert(END, "Congratulations! \n"
									  "You have escaped \n"
									  "You are home now \n"
									  "Don't do drugs kids \n"
									  "'Enter quit' ")

		else:
			# otherwise grab the image for the current room
			# display the image on the left of the GUI
			Game.img = PhotoImage(file=Game.currentRoom.image)

		Game.image.config(image=Game.img)
		Game.image.image = Game.img

	# sets the status displayed on the right of the GUI
	def setStatus(self, status):

		# enable the text widget, clear it, set it, and disabled it
		Game.text.config(state=NORMAL)
		Game.text.delete("1.0", END)

		if Game.currentRoom is None:
			background.stop()
			death.play()
			Game.img = PhotoImage(file="rolled.gif")

			# if dead, let the player know
			Game.text.insert(END, "The Roll has caught you \n"
								  "You are dead. \n"
								  "The only thing you can do now is quit.\n")

		elif Game.currentRoom is finalroom:
			# check if the user collected all items and set the secret ending status
			if 'cape' and 'blade' and 'eye' and 'book' and 'key' in Game.inventory:
				background.stop()
				secret_ending.play()
				Game.img = PhotoImage(file="secretending.gif")
				Game.text.insert(END, "You collected all the items \n"
									  "Now face your destiny... \n"
									  "You have become THE ROLL \n"
									  "'Enter quit'")
			else:
				# otherwise display the regular ending status
				background.stop()
				ending.play()
				Game.img = PhotoImage(file="ending.gif")
				Game.text.insert(END, "Congratulations! \n"
									  "You have escaped \n"
									  "You are home now \n"
									  "Don't do drugs kids \n"
									  "'Enter quit' ")

		else:
			background.play()
			# otherwise, display the appropriate status
			possible_actions = ("Hints:\nYou Can Type:\n'go' direction \n- direction = south, north, east, west \n"
								"'look' item \n- item = check \"You see\" \n'take' grabbable \n"
								"- grabbable = see \"You can carry\"")

			Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status + "\n\n\n" + possible_actions)

		Game.text.config(state=DISABLED)

	# plays the game
	def play(self):

		# add the rooms to the game
		self.createRooms()

		# configure the GUI
		self.setupGUI()

		# set the current room
		self.setRoomImage()

		# set the current status
		self.setStatus(" ")

	# processes the player's input
	def process(self, event):

		# grab the player's input from the input at the bottom of
		# the GUI
		action = Game.player_input.get()

		# set the user's input to lowercase to make it easier to
		# compare the verb and noun to known values
		action = action.lower()

		# set a default response
		response = ("I don't understand. \n"
					"Try verb noun. \n"
					"Valid verbs are \n"
					"go, look, and take")

		# exit the game if the player wants to leave (supports quit,
		# exit, and bye)
		if action == "quit" or action == "exit" or action == "bye" or action == "sionara!":
			exit(0)

		# if the player is dead if it goes/went south from room 4
		if Game.currentRoom == None:
			# clear the player's input
			Game.player_input.delete(0, END)
			return

		# split the user input into words (words are separated by
		# spaces) and store the words in a list
		words = action.split()

		# the game only understands two word inputs
		if len(words) == 2:
			# isolate the verb and noun
			verb = words[0]
			noun = words[1]

			# the verb is: go
			if verb == "go":

				# set a default response
				response = "*Never Gonna Give You Up*"

			# check for valid exits in the current room
				if noun in Game.currentRoom.exits:

					# if one is found, change the current room to
					# the one that is associated with the
					# specified exit
					Game.currentRoom = \
						Game.currentRoom.exits[noun]

					# set the response (success)
					response = "Room changed."

			# the verb is: look
			elif verb == "look":

				# set a default response
				response = "I don't see that item."

			# check for valid items in the current room
				if noun in Game.currentRoom.items:

					# if one is found, set the response to the
					# item's description
					response = Game.currentRoom.items[noun]

			# the verb is: take
			elif verb == "take":

				# set a default response
				response = "I don't see that item."

				# check for valid grabbable items in the current
				# room
				for grabbable in Game.currentRoom.grabbables:

					# a valid grabbable item is found
					if noun == grabbable:

						# add the grabbable item to the player's
						# inventory
						Game.inventory.append(grabbable)

						# remove the grabbable item from the
						# room
						Game.currentRoom.delGrabbable(grabbable)

						# set the response (success)
						response = "Item grabbed."

						# no need to check any more grabbable
						# items

						break
				# display the response on the right of the GUI
				# display the room's image on the left of the GUI
				# clear the player's input
			self.setStatus(response)
			self.setRoomImage()
			Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
