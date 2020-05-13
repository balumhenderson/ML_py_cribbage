import deck
import player
import points
import random
import os

class Game():
	def __init__(self, player1, player2):
		self.player1 = player.Player(player1)
		self.player2 = player.Player(player2)
		self.crib = player.Player("Crib")
	
	
	#Define the main game function
	def play(self):
		#Select who will start with the crib
		cribSelect = random.randint(1,2)
		#Start the main game loop
		while max([self.player1.score, self.player2.score])<131:
			#Clear the terminal at the start of the game
			os.system('cls' if os.name == 'nt' else 'clear')
			playDeck = deck.Deck(True)
			
			if cribSelect % 2 == 0:
				player1Crib = True
				print("It is {}'s crib this round.".format(self.player1.name))
			else:
				player1Crib = False
				print("It is {}'s crib this round.".format(self.player2.name))
			
			#Deal the cards
			for _ in range(6):
				self.player1.draw(playDeck)
				self.player2.draw(playDeck)
			
			#Select which cards to send to the crib
			for _ in range(2):
				self.player1.showHand()
				self.crib.hand.append(self.player1.hand.pop(int(input("Which card would you like to put in the crib? "))))
				cribCard = random.randint(1, len(self.player2.hand)) - 1
				self.crib.hand.append(self.player2.hand.pop(cribCard))
				os.system('cls' if os.name == 'nt' else 'clear')
			
			#Draw and show the starter and update the scores
			starter = playDeck.draw()
			self.showAll(starter)
			self.scoreUpdate(starter, player1Crib)
			
			print("\nTotal scores are {} for {}, and {} for {}.".format(self.player1.name, self.player1.score, self.player2.name, self.player2.score))
			
			#Empty the player's hands and change the holder of the crib
			self.player1.clearHand()
			self.player2.clearHand()
			self.crib.clearHand()
			cribSelect += 1
			
			#Start the next round
			input("Press any key to start the next round.")
			
			
	def showAll(self, starter):
		print("The starter is: ")
		starter.show()
		print("\n{}'s hand is: ".format(self.player1.name))
		self.player1.showHand()
		print("\n{}'s hand is: ".format(self.player2.name))
		self.player2.showHand()
		print("\nThe crib has: ")
		self.crib.showHand()
		
	def scoreUpdate(self, starter, player1Crib):
		self.player1.addScore(self.player1.hand, starter)
		self.player2.addScore(self.player2.hand, starter)
		if player1Crib:
			self.player1.addScore(self.crib.hand, starter)
		else:
			self.player2.addScore(self.crib.hand, starter)