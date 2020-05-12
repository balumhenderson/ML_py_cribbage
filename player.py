import points
class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.score = 0
	
	def draw(self, deck):
		self.hand.append(deck.draw())
	
	def showHand(self):
		for i, c in enumerate(self.hand):
			print(i, "{} of {}.".format(c.name, c.suit))

	def addScore(self, hand, starter):
		self.score += points.countHand(hand, starter)
		
	def clearHand(self):
		self.hand = []