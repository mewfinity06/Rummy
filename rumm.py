class Deck:
    def __init__(self) -> None:
        self.num_of_cards = 52;

    def __repr__(self) -> str:
        return "Deck has " + str(self.num_of_cards) + " cards left"

class Player:

    def __init__(self):
        self.id = 1

p1 = Player()
p2 = Player()

print(p1.id)
print(p2.id)
