class Card:
    def __init__(self, face, suit, value):
        self.face = face
        self.suit = suit
        self.name = self.face + ' of ' + self.suit
        self.value = value

    def idCard(self):
        print(self.name)

deck = []
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
for suit in suits:
    for face in range (13):
        if face == 0:
            deck.append('Ace of ' + suit)
        elif face < 10:
            deck.append(f'{face + 1} of {suit}')
        elif face == 10:
            deck.append(f'Jack of {suit}')
        elif face == 11:
            deck.append(f'Queen of {suit}')
        elif face == 12:
            deck.append(f'King of {suit}')

#print(deck)
c1 = Card('Ace', 'Diamonds', 1)
c1.idCard()
