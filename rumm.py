import random

class Deck:
    def __init__(self) -> None:
        self.contents = []
        self.build()
        self.num_of_cards = len(self.contents)
        

    def __repr__(self) -> str:
        return "Deck has " + str(self.num_of_cards) + " cards left"
    
    def printDeck(self) -> None:
        for card in self.contents:
            print( card )

    def shuffleDeck(self) -> None:
        random.shuffle(self.contents)
    
    def build(self) -> None:
        card_order = {
            a: [] for a in range(52)
        }

        suit_order = ["Spade", "Heart", "Club", "Diamond"]
        value_order = [i for i in range(1, 13)]

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

        def helper_value(c):
            value = c[1:]
            return(int(value))
        
        def helper_suit(c):
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
        print(self.contents)
        self.contents.sort(key=helper_value)
        self.contents.sort(key=helper_suit)
        print(self.contents)


        


class Player:

    def __init__(self):
        self.id = id(self)
        self.hand = []

        for c in range(7):
            self.hand += d1.deck_contents.pop()
        
    
    def draw(self):
        self.hand += d1.deck_contents.pop()

    def show_hand(self):
        for card in self.hand:
            print( card )

# --- MUST BE INITIALIZED TO RUN --- #
# ---       DO NOT REMOVE        --- #

d1 = Deck()

# --        DO NOT REMOVE        --- #
# --- MUST BE INITIALIZED TO RUN --- # 

print( d1 )

d1.shuffleDeck()
d1.sortDeck()