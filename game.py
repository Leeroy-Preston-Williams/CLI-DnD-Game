from character import Character
import random
import os
import sys

class Game:
	
	commands = ("attack", "approach", "back", "forward", "left", "right", "guard", "eat", "runaway", "speak", "trade", "levelUp", "viewLevel", "trade", "light", "pickup")
	monster_finishers = {"Orc": "smash with giant axe", "Wolf": "eat you", "GiantSpider": "lay it's eggs in you", "Bandit": "knock you with a club over the head"}
	
	def __init__(self):
		self.play = ""
		self.story = """
						==History==
			Once upon a time, in a far away land filled with magic and all sorts of creatures,
			humanity lived in harmony with all the creatures.
			That is until the evil dragon Do'Mamu came and claimed the lands, as his own.
			The creatures of the land tried to battle the evil dragon, 
			and his minions, but the war went on for decades,
			until the creatures of the land admitted defeat, and eventually gave in to the rule of Do'Mamu.
			
			Time has passed on, and legend fortells of a hero that shall emerge from the lands,
			 to vanquish the ruthless dragon and free the people of this land.
			
						That hero is You.. 	
			"""
			
		self.decision = None
		self.dice = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
		random.shuffle(self.dice)
		self.option = ""
	
	def title_screen(self):
		# Display banner
		
		print("-*-" * 19)
		print("+\t\t\t\t\t\t\t+")
		print("+\t	 RPG World Text Game v0.1         \t+")
		print("+\t\t\t\t\t\t\t+")
		print("+\t                - begin-                    \t+")
		print("+\t                - help-                      \t+")
		print("+\t                - quit-                      \t+")
		print("-*-" * 19)


												
	#def display_screen(self):
#		
#		self.title_screen()
#		self.play = input("=> ")
#		while self.play.lower() not in ["begin", "help", "quit"]:
#			os.system("clear")
#			self.title_screen()
#			self.play = input("=> ")
#		if self.play.lower() == "begin":
#			self.begin_game()
#		elif self.play.lower() == "help":
#			print("Use commands, by adding a '$' before each command word.")
#			print("For example to attack you would type: $attack.")
#			print("Whenever in the game, and you fee you have forgotten the commands, type '$help' and it will display\n permitted values.\n")
#			sys.exit()
#		elif self.play.lower() == "quit":
#			os.system("clear")
#			sys.exit()											

	def roll_dice(self):
		# manipulate the entered commands	
		
		self.decision = input("=> ")
		if self.decision[0] == "$":
			for item in range(len(Game.commands)):
				if self.decision[1:] == "viewLevel":
					gamer = Character()
					gamer.view_character_level()
				elif self.decision[1:] == Game.commands[item]:
					print(f"{self.decision[1:]} has {self.dice[0]} hit points")

			
				
	def begin_game(self):
		# Start playing the game
			
		self.title_screen()
		self.play = input("=> ")
		while self.play.lower() not in ["begin", "help", "quit"]:
			os.system("clear")
			self.title_screen()
			self.play = input("=> ")
			
		if self.play.lower() == "begin".lower():
			player = Character()
			player.character_creation()
			print("\n")
			# display help
			self.help_menu()
			self.play_game()
			
			
		elif self.play.lower() == "help".lower():
			print("Use commands, by adding a '$' before each command word.")
			print("For example to attack you would type: $attack.")
			print("Whenever in the game, and you feel that you have forgotten the commands.\nType: '$help' and it will display permitted values.")
			input("")
			os.system("clear")
			sys.exit()
		elif self.play.lower() == "quit".lower():
			os.system("clear")
			sys.exit()											
		# Create a character instance	
		
		
		
		
		# Access game
		gameworld = GameWorld()
		gameworld.openning()


	
	def play_game(self):
		# Show game introduction story
		print(self.story)

	
	
	def help_menu(self):
		# Show the user the 'help' commands

		print("Do you wish for help?")
		self.roll_dice()
		if self.decision == "yes":
			for i in range(len(Game.commands)):
				print(f"${Game.commands[i]}")		
				
		input(" ")
		os.system("clear")
		
		
class GameWorld:
	creatures = {
		"Orc": {
			"HP": 100,
			"ST": 8,
			"MG": 2,
			"Level": 1,
			"WeaponStrength": 3
		},
		"GiantSpider": {
			"HP": 100,
			"ST": 6,
			"MG": 1,
			"Level": 1,
			"WeaponStrength": 2
		},
		"Bear": {
			"HP": 100,
			"ST": 8,
			"MG": 1,
			"Level": 1,
			"WeaponStrength": 5
		},
		"Wolf": {
			"HP": 100,
			"ST": 5,
			"MG": 1,
			"Level": 1,
			"WeaponStrength": 3
		},
		"Bandit": {
			"HP": 100,
			"ST": 6,
			"MG": 0,
			"Level": 1,
			"WeaponStrength": 2
		}
	}
	def __init__(self):
		self.decision = None
		self.creature_types = []

	def creature_list(self):
		
		for creature in GameWorld.creatures.keys():
			self.creature_types.append(creature)
		random.shuffle(self.creature_types)

				
	def openning(self):
		
		gamer = Game()
		self.creature_list()
		self.enemy_hp = 10
		self.my_hp = 10
		self.valid_options = ["light", "forward", "look", "attack"]
		
		print("\nYou awaken in a dark cave, with little memory of what has happened.")
		print("Only the slight taste of metal lingers around your mouth, and the chocking taste of dust.")
		print("You slowly open your eyes, to see you are in a dark space, with little light.\n")
		print("What do you do?")
		
		
		self.decision = input("=> ")
		if self.decision[0] == "$":
			if self.decision[1:] == self.valid_options[0]:
				print(f"You decided to light up a piece paper you had in you pockets, to light up your path.")
				print("Good idea...or was it?")
				print("\nYou keep walking, further down what seems to a cave,\nminerals reflect the light of your flame, to give of a shimmer as you pass by them.")
				print("......1 minute later.....")
				print(f"With your flame about to die out, you hear a snarl, coming from what seems to be close by..\n cautiously, you lower your source of light and see a {self.creature_types[0]}")
				print("\nWhat do you do?")
				self.decision = input("=> ")					
				while self.enemy_hp >= 1 and self.my_hp >= 2:
					if self.decision[1:] == self.valid_options[3]:
						print("Your quickly dart to the side of the creature and with a swift move...")
						print("cut one of it's legs with your dagger.")
						print(f"Your attack deals: 2 HIT POINTS on the {self.creature_types[0]}.")
						self.enemy_hp -= 2
						input(" ")
						os.system("clear")
						print(f"{self.creature_types[0]} has {self.enemy_hp} hp left")
						print(f"The {self.creature_types[0]} screeches, jumps onto the wall and begins attacking you from above.")
						print(f"You sustain: 1 DAMAGE POINT from the {self.creature_types[0]}.")
						self.my_hp -= 1
						print(f"You have {self.my_hp} hp left")
						input(" ")
						os.system("clear")
						if self.enemy_hp == 2:
							print(f"The {self.creature_types[0]} slowly yields and backs against the wall.")
							print(f"You have a choice, do you wish to tame {self.creature_types[0]} or do you want to destroy it?")
							self.decision = input("=> ")
							if self.decision[1:] == "tame":
								print(f"The {self.creature_types[0]} acknowledges your abilities and wishes to follow you.")
								self.enemy_hp = 10
								break
							elif self.decision[1:] == "destroy":
								print(f"You deal the final blow on the {self.creature_types[0]} thus ending it's life.")
								print("The battle was taxing, you lean against the wall to catch your breath and tend to your wounds.")
								print("You reach into you coat, and pull out what seems like an elixer.")
								print("You drink the elixer and your wounds heal instantly.")
								print("It is in that moment that you feel a gentle breeze coming from infront of you....")
								self.my_hp == 10
								print("-END OF MAP-")
					else:
						print(f"You decided to: {self.decision[1:]}, however the {self.creature_types[0]} struck you with a freeze potion,\n then came up to {gamer.monster_finishers[self.creature_types[0]]} .")
						print("Looks like you won't make it out of this one")
						self.my_hp = 0
				if self.my_hp <= 1:
					print("Looks like you didn't make it...")
					print("You can retry")
				
				
			elif self.decision[1:] == self.valid_options[1]:
				print("\nYou slowly try to move forward in the dark, feeling against the walls for a path.")
				print("You continue walking in the darkness, until your fingers touch something that seems cold and spikey...")
				print("Before you have a moment to react, you see 8 sets of gleaming eyes in the darkness, and feel your body trapped in it's clutches...")
				print("You have been caught by a Giant Spider, it traps you in it's web, and drags you to it's nest, where it lays eggs onto you soon to hatch and devour you.")
				print("Game Over!")
				sys.exit()
				
			elif self.decision[1:] == self.valid_options[2]:
				print("You try to look around, the lighting is terrible...however, you do see something shimmer in the far end of the darkness.")
		else:
			print("Invalid move!")
						



play = Game()
play.begin_game()


