import random

class Deck:
    def __init__(self) -> None:
        self.contents = []
        self.build()
        self.shuffleDeck()
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
    
    def sayName(self):
        print(self.name)
    
    def draw(self):
        self.hand.append(d1.contents.pop())

    def showHand(self):
        print("\n")
        for card in self.hand:
            if card[0] == "s":
                print("Spade", card[1:], end=", ")
            elif card[0] == "h":
                print("Heart", card[1:], end=", ")
            elif card[0] == "c":
                print("Club", card[1:], end=", ")
            elif card[0] == "d":
                print("Diamond", card[1:], end=", ")
        print("\n")

    def sortHand(self):

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
            
        self.hand.sort(key=helperValue)
        self.hand.sort(key=helperSuit)

class User(Player):
    def __init__(self, name = "1"):
        super().__init__(name)

class Bot(Player):
    def __init__(self):
        super().__init__("BOT")

# --- MUST BE INITIALIZED TO RUN --- #
# ---       DO NOT REMOVE        --- #

d1 = Deck()

# --        DO NOT REMOVE        --- #
# --- MUST BE INITIALIZED TO RUN --- # 

p1 = User("Ashton")

