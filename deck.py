import random

class Card:
	def __init__(self, val, name, order, suit):
		self.val=val
		self.suit=suit
		self.order=order
		self.name=name
		if name == "King" or name == "Queen" or name == "Jack":
			self.val=10
	
	def show(self):
		print("{} of {}.".format(self.name, self.suit))



		
class Deck:
	def __init__(self, shuffleTrue):
		self.cards=[]
		self.build()
		if shuffleTrue:
			self.shuffle()
	
	def build(self):
		for s in ["Hearts", "Diamonds", "Spades", "Clubs"]:
			for v, n in enumerate(["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]):
				self.cards.append(Card(v+1, n, v+1, s))
	
	def show(self):
		for c in self.cards:
			c.show()
	
	def shuffle(self):
		for _ in range(3):
			for i in range (len(self.cards)-1, 0, -1):
				r = random.randint(0, i)
				self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
	
	def draw(self):
		return self.cards.pop()