import random


def shuffle_cards(gameDeck): #this def is needed because there might be more shufflinf down the line
    print(gameDeck)
    randomDeck = []
    for x in range(0,len(gameDeck)):
        pickedNumber = random.choice(gameDeck)
        gameDeck.remove(pickedNumber)
        randomDeck.append(pickedNumber)
    return randomDeck

def get_numbers_of_cards():
    return [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16] # card no 14 is to strong to play with

def make_deck():
    cardNumbers = get_numbers_of_cards() # returns a list of playable cards
    return cardNumbers

def main():


    gameDeck = make_deck()
    gameDeck = shuffle_cards(gameDeck)
    print (gameDeck)

if __name__ == "__main__":
    main()


# This code must have solutions for this
# cards must be shuffled  before the beginning of the drawn
# there must be several banned cards that cannot be picked
# each card drawn must have a description
# after a card is drawn the same card must not be drawn again (ex is removed from the deck)
# limit a number of cards drawn (ex 6)
# number of drawn cards can me chosed from option menu (6 or 7 cards)