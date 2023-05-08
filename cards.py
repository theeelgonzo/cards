class Card:
    def __init__(self, face, suit, value):
        self.face = face
        self.suit = suit
        self.name = str(self.face) + ' of ' + self.suit
        self.value = value

    def idCard(self):
        print(self.name)

deck = []
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
for suit in suits:
    for face in range (13):
        
        if face == 0:
            card = Card('Ace', suit, 1)
            deck.append(card)
        elif face < 10:
            card = Card(face + 1, suit, face + 1)
            deck.append(card)
        elif face == 10:
            card = Card('Jack', suit, 11)
            deck.append(card)
        elif face == 11:
            card = Card('Queen', suit, 12)
            deck.append(card)
        elif face == 12:
            card = Card('King', suit, 13)
            deck.append(card)

def shuffle():
    shuffledDeck = []
    pass


for card in deck:
    card.idCard()
