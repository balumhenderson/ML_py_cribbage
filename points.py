import itertools
import random

def countHand(hand, starter):
	score = 0
	hand.append(starter)
	
	#Score 2 points for a count to 15
	nums=[]
	for i in hand:
		nums.append(i.val)
	for i in range(len(hand)):
		for seq in itertools.combinations(nums, i):
			if sum(seq) == 15:
				#print("Sum 15:")
				#print(seq)
				score +=2
	
	#Score 2 points for doubles
	for i in range(0, len(hand)-1):
		for j in range(i+1, len(hand)):
			if hand[i].name == hand[j].name:
				#print("Doubles:")
				#hand[i].show(), hand[j].show()
				score += 2
	
	#Score points for runs (3 for 3 cards, 4 for 4 etc)
	straightScore = []
	for i in range(len(hand)-1):
		straight = [hand[i]]
		for j in range(i+1, len(hand)):
			for k in range(len(straight)):
				if hand[i].suit == hand[j].suit:
					if hand[j].order == straight[k].order + 1 or hand[j].order == straight[k].order -1:
						straight.append(hand[j])
		if len(straight) >= 3:
			#print(len(straight))
			#print(straightScore)
			straightScore.append(len(straight))
			#print(straightScore)
	
	
	if len(straightScore) > 0 and max(straightScore) >= 3:
		score += max(straightScore)
		#print("Straight:", max(straightScore))
	
	return(score)



def vals(cards):
	vals = []
	for i range(len(cards)):
		vals.append(cards[i].val)
	return vals

def count15(cards):
	tot = 0
	for i in range(1, len(cards)):
		tot += cards[i].val
	if tot == 15:
		return True

def count31(cards):
	tot = 0
	for i in range(1, len(cards)):
		tot += cards[i].val
	if tot == 31:
		return True


def compCount(player, comp):
	cards = []
	playerPoints, compPoints = 0, 0
	
	if sum(vals(cards)) + min(vals(comp.hand)) <= 31 and len(comp.hand) > 0:
		countCards.append(opp.hand.pop(random.randint(0, len(comp.hand)-1)))
		compPoints += 2 if count15(cards)
		compPoints += 2 if count31(cards)
		if len(cards) > 1:
			compPoints += 2 if cards[-1].val == cards[-2].val
		cards = [] if count31(cards)
		
		tot = 0
		for i in len(cards):
			tot += cards[i].val
			cards[i].show()
		print(tot)
		
	if 	sum(vals(cards)) + min(vals(player.hand)) <= 31 and len(player.hand) > 0:
		countCards.append(player.hand.pop(player.hand[input()]))
		playerPoints += 2 if count15(cards)
		playerPoints += 2 if count31(cards)
		if len(cards) > 1:
			playerPoints += 2 if cards[-1].val == cards[-2].val
		cards = [] if count31(cards)
		
		tot = 0
		for i in len(cards):
			tot += cards[i].val
			cards[i].show()
		print(tot)









