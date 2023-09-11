class Deck:
    def __init__(self) -> None:

        suits = ['S', 'H', 'C', 'D']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.deck_contents = []

        for i in suits:
            for j in values:
                self.deck_contents += [(j, i)]
        
        self.num_of_cards = len(self.deck_contents)

    def __repr__(self) -> str:
        return "Deck has " + str(self.num_of_cards) + " cards left"

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
            print(card)

# --- MUST BE INITIALIZED TO RUN --- #
# ---       DO NOT REMOVE        --- #
d1 = Deck()

p1 = Player()

print(d1)
p1.show_hand()
print(d1)