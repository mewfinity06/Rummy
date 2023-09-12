import random

class Deck:
    def __init__(self) -> None:
        self.contents = {}
        self.num_of_cards = len(self.contents)
        

    def __repr__(self) -> str:
        return "Deck has " + str(self.num_of_cards) + " cards left"

    def shuffleDeck(self):
        random.shuffle(self.contents)
    
    def build(self):
        card_order = {
            a: [] for a in range(52)
        }

        # Add Spades to Contents
        for i in range(52):
            if i in range(0, 12):
                card_order[i] = ["Spade",]
            elif i in range(13, 25):
                card_order[i] = ["Heart",]
            elif i in range(26, 38):
                card_order[i] = ["Club",]
            elif i in range(39, 51):
                card_order[i] = ["Diamond",]
            
            
        
        self.contents = card_order



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

d1.build()


print(d1.contents)
