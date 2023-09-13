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

        self.hand_length = len(self.hand)

        self.sortHand()
    
    def __repr__(self):
        return self.name + " has " + str(len(self.hand)) + " cards left"
    
    def sayName(self):
        print( self.name )
    
    def draw(self):
        new_card = d1.contents.pop()
        self.printCard(new_card)
        self.hand.append(new_card)
        self.sortHand()
        self.hand_length = len(self.hand)
    
    def printCard(self, card):
        if card[0] == "s":
            print( "Spade", card[1:] )
        elif card[1] == "h":
            print( "Heart", card[1:] )
        elif card[2] == "c":
            print( "Club", card[1:] )
        elif card[3] == "d":
            print( "Diamond", card[1:] )
        else:
            print( "Other" )

    def showHand(self):
        print( "\n" )
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
            i += 1
        print( "\n" )

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
    
    def playCard(self):
        
        self.showHand()
        card = input( "Please choose a card [1 - " + str(self.hand_length) + "]: " )

        try:
            card_index = int(card)
            if card_index > self.hand_length or card_index < 0:
                return self.playCard()
        except:
            print( 'PLEASE CHOOSE A CORRECT CARD' )
            return self.playCard()

class User(Player):
    def __init__(self, name = "1"):
        super().__init__(name)

class Bot(Player):
    def __init__(self, id):
        name = "BOT" + str(id)
        super().__init__(name)
    
    def __repr__(self):
        return self.name

# --- MUST BE INITIALIZED TO RUN --- #
# ---       DO NOT REMOVE        --- #

d1 = Deck()

# --        DO NOT REMOVE        --- #
# --- MUST BE INITIALIZED TO RUN --- # 

def start():
    game_on = True
    player_name = input("Name: ")
    p1 = Player(player_name)

    num_of_bots = int(input("Number of bots [MAX 3]: "))
    bots = []

    for bot in range(num_of_bots):
        bots.append(Bot(bot))

    for bot in bots:
        print( "BOT", bot )

    while (game_on):
        print ( \
            "\tPLEASE SELECT ACTIONS:\n" + \
            "1. DRAW\n" + \
            "2. SHOW HAND\n" + \
            "3. PLAY CARDS\n" + \
            "q. QUIT\n" )
        action = input( "Number of action: " ).lower()

        if action == 'q' or action == 'quit':
            game_on = False
        elif action == '1':
            p1.draw()
        elif action == '2':
            p1.showHand()
        elif action == '3':
            p1.playCard()

if __name__ == "__main__":
    start()