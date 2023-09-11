class Deck:
    def __init__(self) -> None:
        self.num_of_cards = 52;

    def __repr__(self) -> str:
        return "Deck has " + str(self.num_of_cards) + " cards left"

class Player:

    def __init__(self):
        self.id = id(self)
        self.hand = []
        d1.num_of_cards -= 7

# --- MUST BE INITIALIZED TO RUN --- #
# ---       DO NOT REMOVE        --- #
d1 = Deck()

p1 = Player()

print(d1)