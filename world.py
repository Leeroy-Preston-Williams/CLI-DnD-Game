import random
from game import Game

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
	
	def cave(self):
		print("You have entered a cave.")
		for creature in GameWorld.creatures.keys():
			self.creature_types.append(creature)
			
		random.shuffle(self.creature_types)		
		print(f"You come across a {self.creature_types[0]}, standing between you and the path.\n What do you do?")
		
		gameplay = Game()
		gameplay.roll_dice()

		