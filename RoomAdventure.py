###########################################################################################
# Name: Steven Navarrette
# Date: 3/24/2024
# Description: This game takes place in a mysterious and eery temple at the end of the universe
# The player is being hunted by the temple's keeper and must collect certain items to defeat the keeper and escape
# There is an Easter egg in the game where you access a certain room & grab a certain item that unlocks a secret ending
# Enhancements: Include three more rooms, more objects, sound, images, a secret ending, and storytelling
# Note: I had significant help from Jonathan in his office hours
# He suggested I use the template on blackboard and the code for the functions in the pdf file in Blackboard
###########################################################################################

import pygame
from tkinter import *

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
		s = ("Welcome to the end of the universe. \n"
			 "You are in Entropy's Temple. \n"
			 "You are not supposed to be here, \n"
			 "YOU MUST ESCAPE. \n"
			 "The guardian of this temple, \n"
			 "THE ROLL, \n"
			 "is after you! \n"
			 "To escape, collect Sirius' Key, \n"
			 "the Book of Forbidden Knowledge, \n"
			 "Pharaoh's Eye, and Shogun's Blade. \n"
			 "Then meet me at beginning's end. \n"
			 "DO NOT ENTER UNLESS YOU COLLECT THE ITEMS. \n\n")

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
		global currentRoom
		r1 = Room("Sirius Throne Room", "throne.gif")
		r2 = Room("Oblivion's Library", "fireplace.gif")
		r3 = Room("Hall of Leaders", "statue.gif")
		r4 = Room("All Seeing Eye's Dome", "eye.gif")
		r5 = Room("Shogunate's Temple", "shrine.gif")
		r6 = Room("Forbidden Gallery", "cape.gif")
		r7 = Room("Beginning's End", "ending.gif")

		r1.addExit("east", r2)
		r1.addExit("south", r3)
		r1.addExit("west", r5)
		r1.addGrabbable("key")
		r1.addItem("Throne", "There is a throne that is extremely bright I can only see white... ")
		r1.addItem("Cosmic Key", "There is a key over there on that chair  ")

		r2.addExit("west", r1)
		r2.addExit("south", r4)
		r2.addItem("White Rug", "Long rug across the floor made of... yeti skin? ")
		r2.addItem("Fireplace", "It is extremely hot in here, the fireplace is blue ")

		r3.addExit("north", r1)
		r3.addExit("east", r4)
		r3.addGrabbable("book")
		r3.addItem("Statue", "Its a statue... wait what's that book he's holding, looks like the book of Enoch ")

		r4.addExit("north", r2)
		r4.addExit("west", r3)
		r4.addGrabbable("eye")
		r4.addItem("Cosmic eyeball", "Its ahem... all-seeing")

		r5.addExit("west", r2)
		r5.addExit("south", r6)
		r5.addGrabbable("blade")
		r5.addItem("Katana", "They say this shrine holds the blade that cuts the fabric of reality... ")
		r5.addItem("Gateway", "Hopefully this gate does not take me anywhere else... ")

		r6.addExit("north", r5)
		r6.addExit("west", r7)
		r6.addGrabbable("cape")
		r6.addItem("Sphere of Doom", "This room has lots of mysterious artifacts in here including that floating sphere")
		r6.addItem("Cloak of Ascension", "This cloak was worn by the leaders of this society, they say it reveals THE END")

		# set room 1 as the current room at the beginning of the game
		Game.currentRoom = r1

		# initialize the players inventory
		Game.inventory = []

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
			Game.img = PhotoImage(file='rolled.gif')

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

		if (Game.currentRoom is None):
			Game.img = PhotoImage(file="rolled.gif")

			# if dead, let the player know
			Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
		else:

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

		# play basic sound
		self.play_sound("")

	# processes the player's input
	def process(self, event):

		# grab the player's input from the input at the bottom of
		# the GUI
		action = Game.player_input.get()

		# set the user's input to lowercase to make it easier to
		# compare the verb and noun to known values
		action = action.lower()

		# set a default response
		response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

		# exit the game if the player wants to leave (supports quit,
		# exit, and bye)
		if action == "quit" or action == "exit" or action == "bye" or action == "sionara!":
			exit(0)

		# if the player is dead if it goes/went south from room 4
		if (Game.currentRoom == None):
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
				response = "*Never Gonna Give You Up Plays*"

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

	def play_sound(sound_file):
		pygame.init()
		pygame.mixer.init()
		sound = pygame.mixer.Sound(sound_file)
		sound.play()

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
