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

print(deck)
