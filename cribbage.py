import deck
import player
import points
import random
import os

calum = player.Player("Calum")
opp = player.Player("Opponent")
crib = player.Player("Crib")
compCrib = False

#Select 1 or 2 at random to decide who gets the first crib
cribSelect = random.randint(1,2)


#Start the game running until a score of 131 is reached
while max([calum.score, opp.score]) < 131:
	gameDeck = deck.Deck()
	gameDeck.shuffle()
	os.system('cls' if os.name == 'nt' else 'clear')
	
	if cribSelect % 2 == 0:
		compCrib = False
		print("It is {}'s crib this round.".format(calum.name))
	else:
		compCrib = True
		print("It is {}'s crib this round.".format(opp.name))
	
	#Draw the player's hands
	for _ in range(6):
		calum.draw(gameDeck)
		opp.draw(gameDeck)
	
	#Show the human player their hand, and ask them to discard 2 cards to the crib
	calum.showHand()
	crib.hand.append(calum.hand.pop(int(input())))
	calum.showHand()
	crib.hand.append(calum.hand.pop(int(input())))
	
	#Discard two random cards from the computer's hand to the crib
	crib.hand.append(opp.hand.pop(random.randint(0, 5)))
	crib.hand.append(opp.hand.pop(random.randint(0, 4)))
	
	
	starter = gameDeck.draw()
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\nThe starter is: ")
	starter.show()
	print("\n{}'s hand is: ".format(calum.name))
	calum.showHand()
	print("\n{}'s hand is: ".format(opp.name))
	opp.showHand()
	print("\nThe crib has: ")
	crib.showHand()
	calum.addScore(calum.hand, starter)
	opp.addScore(opp.hand, starter)
	if compCrib:
		opp.addScore(crib.hand, starter)
	else:
		calum.addScore(crib.hand, starter)
	print("\nTotal scores are {} for {}, and {} for {}.".format(calum.name, calum.score, opp.name, opp.score))
	input()
	calum.clearHand()
	opp.clearHand()
	crib.clearHand()
	cribSelect += 1