import random

discard_pile = []

class Deck:
	def __init__(self) -> None:
		self.contents = []
		self.build()
		self.shuffleDeck()
		discard_pile.append(self.contents.pop())
		self.num_of_cards = len(self.contents)
		

	def __repr__(self) -> str:
		return "Deck has " + str(self.num_of_cards) + " cards left"
	
	def printDeck(self) -> None:
		for card in self.contents:
			print( card )

	def shuffleDeck(self) -> None:
		for i in range(10):
			random.shuffle(self.contents)
	
	def build(self) -> None:
		card_order = {
			a: [] for a in range(52)
		}

		temp_deck = []

		# Add Spades to Contents
		for i in range(52):
			if i in range(0, 13):
				card_order[i] = ["Spade", i % 13, "s" + str(i % 13 + 1)]
			elif i in range(13, 26):
				card_order[i] = ["Heart", i % 13, "h" + str(i % 13 + 1)]
			elif i in range(26, 39):
				card_order[i] = ["Club", i % 13, "c" + str(i % 13 + 1)]
			elif i in range(39, 52):
				card_order[i] = ["Diamond", i % 13, "d" + str(i % 13 + 1)]
		
		for element in range(len(card_order)):
			temp_deck.append(card_order[element][2])
		
		self.contents = temp_deck
			
		
	def sortDeck(self):

		def helperValue(c):
			value = c[1:]
			return(int(value))
		
		def helperSuit(c):
			suit = c[0]
			if suit == "s":
				return 0
			elif suit == "h":
				return 1
			elif suit == "c":
				return 2
			elif suit == "d":
				return 3
			else:
				return 4
			
		self.contents.sort(key=helperValue)
		self.contents.sort(key=helperSuit)

class Player:

	def __init__(self, name):
		self.name = "User: " + name

		self.id = id(self)
		self.hand = []

		for c in range(7):
			self.hand.append(d1.contents.pop())

		self.hand_length = len(self.hand)

		self.sortHand()
	
	def __repr__(self):
		return self.name + " has " + str(len(self.hand)) + " cards left"
	
	def sayName(self):
		print( self.name )
	
	def draw(self):
		new_card = d1.contents.pop()
		if str(type(self)) == '<class \'__main__.User\'>':
			self.printCard(new_card)
		self.hand.append(new_card)
		self.sortHand()
		self.hand_length = len(self.hand)
	
	def printCard(self, card):
		if card[0] == "s":
			print( "Spade", card[1:] )
		elif card[0] == "h":
			print( "Heart", card[1:] )
		elif card[0] == "c":
			print( "Club", card[1:] )
		elif card[0] == "d":
			print( "Diamond", card[1:] )
		else:
			print( "Other" )

	def showHand(self):
		print( "\n=============================================================\n" )
		i = 1
		for card in self.hand:
			print( str(i), end=": " )
			if card[0] == "s":
				print( "Spade", card[1:], end=", " )
			elif card[0] == "h":
				print( "Heart", card[1:], end=", " )
			elif card[0] == "c":
				print( "Club", card[1:], end=", " )
			elif card[0] == "d":
				print( "Diamond", card[1:], end=", " )
			else:
				print( "Other" )
			
			if i % 5 == 0:
				print( "\n" )
			i += 1
		print( "\n\n=============================================================\n" )

	def sortHand(self):

		def helperValue(c):
			value = c[1:]
			return int(value)
		
		def helperSuit(c):
			suit = c[0]
			if suit == "s":
				return 0
			elif suit == "h":
				return 1
			elif suit == "c":
				return 2
			elif suit == "d":
				return 3
			else:
				return 4
			
		self.hand.sort(key=helperValue)
		self.hand.sort(key=helperSuit)


class User(Player):
	def __init__(self, name = "1"):
		super().__init__(name)
	
	def playCard(self):
			print( "\nTop Card: ", end="" )
			self.printCard(discard_pile[-1])
			self.showHand()
			card = input( "Please choose a card [1 - " + str(self.hand_length) + "]: " )

			card_index = int(card)

			for card in self.hand:
				if self.playableCard(card):
					pass
				print( "No playable card! Ending turn with drawing" )
				self.draw()
				return 0

			if card_index > self.hand_length or card_index <= 0:
				print( "Not a valid card, please choose one in range!" )
				return self.playCard()
			if not self.playableCard(self.hand[card_index-1]):
				print( "Not a playable card! Try again!" )
				return self.playCard()
			discard_pile.append(self.hand.pop(card_index-1))
			self.printCard(discard_pile[-1])
	
	def playableCard(self, card):

		if discard_pile == []:
			return True
		
		top_card = discard_pile[-1]

		if card[0] == top_card[0]:
			print( "Suit is the same!" )
			return True
		if card[1:] == top_card[1:]:
			print( "Value is the same!" )
			
		return False

class Bot(Player):
	def __init__(self, id):
		name = "BOT" + str(id)
		super().__init__(name)

# --- MUST BE INITIALIZED TO RUN --- #
# ---       DO NOT REMOVE        --- #

d1 = Deck()

# --        DO NOT REMOVE        --- #
# --- MUST BE INITIALIZED TO RUN --- # 

def start():
	game_on = True
	player_name = input("Name: ")
	p1 = User(player_name)

	num_of_bots = int(input("Number of bots [MAX 3]: "))
	bots = []

	for bot in range(num_of_bots):
		bots.append(Bot(bot))

	for bot in bots:
		print( bot )
	
	p1.draw()
	p1.showHand()
	p1.playCard()

	# while (game_on):
	# 	print ( \
	# 		"\tPLEASE SELECT ACTIONS:\n" + \
	# 		"1. DRAW\n" + \
	# 		"2. SHOW HAND\n" + \
	# 		"3. PLAY CARDS\n" + \
	# 		"q. QUIT\n" )
	# 	action = input( "Number of action: " ).lower()

	# 	if action == 'q' or action == 'quit':
	# 		game_on = False
	# 	elif action == '1':
	# 		p1.draw()
	# 	elif action == '2':
	# 		p1.showHand()
	# 	elif action == '3':
	# 		p1.playCard()

if __name__ == "__main__":
	start()