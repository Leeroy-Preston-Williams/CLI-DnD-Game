"""
@ Author: Leeroy P. Williams
@ Date: 15.05.2023
@ Desc: Dungeons and Dragons like game, that works via CLI. The user will select a character from the species.

"""
import os

class Character:
	
	species = {
		"Troll": {
			"HP": 10,
			"ST": 8,
			"MG": 2,
			"Level": 1,
			"Inventory":
			{
					"Weapon1": "Axe",
					"Weapon2": "Giant Hammer",
					"HP-Potion": 1
			}
		},
		"Elf": {
			"HP": 10,
			"ST": 6,
			"MG": 7,
			"Level": 1,
			"Inventory": 
			{
				"Weapon1": "Bow",
				"Weapon2": "Sacred Dagger",
				"HP-Potion": 1
			}
		},
		"Human": {
			"HP": 10,
			"ST": 5,
			"MG": 1,
			"Level": 1,
			"Inventory":
			{
				"Weapon1": "Sword",
				"Weapon2": "Sheild",
				"HP-Potion": 1
			}
		},
		"Goblin": {
			"HP": 10,
			"ST": 4,
			"MG": 5,
			"Level": 1,
			"Inventory":
			{
				"Weapon1": "Daggers",
				"Weapon2": "Bomb",
				"HP-Potion": 1
			}
		},
		"Sorcerer": {
			"HP": 10,
			"ST": 4,
			"MG": 10,
			"Level": 1,
			"Inventory":
			{
				"Weapon1": "Staff",
				"Weapon2": "Talisman",
				"HP-Potion": 1
			}
		}
	}
	
	def __init__(self):
		self.name = None
		self.char_choice = None
		self.viewAttr = None
	
				
	def character_creation(self):
		
		print("\nWelcome brave traveller, do you wish to view the species attributes?")
		self.viewAttr = input("=> ")
		print("\n")
		
		if self.viewAttr == "yes".lower():
			for k, v in Character.species.items():
				print(f"\n{k}:")
				for attributes1, attributes2 in v.items():
					print(f"{attributes1}: {attributes2}")
		
		input("Hit ENTER!")
		os.system("clear")
		print("Please select a speicies: [Troll, Elf, Human, Goblin, Sorcerer]")
		self.char_choice = input("=> ")
		print("Please enter a valid name")
		self.name = input("=> ")
		
		# Check that the user entered a valid species
		for characters in Character.species:
			if self.char_choice in characters:
				continue
		
		os.system("clear")
		print("CHARACTER CREATED!.\n")
		print(f"Welcome:\nName: {self.name}\nSpecies:{self.char_choice}")
		
		
	
	def view_character_level(self):
		
		for k, v in Character.species[self.char_choice].items():
			if k == "Level":
			   	print(f"{k}")
								
