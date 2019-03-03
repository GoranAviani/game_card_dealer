import random


def description_of_user_hand_cards(userHand):
    pass


def draw_cards(gameDeck, userNoOfCards): #draw cards will draw as many cards aas userNoOfcards parameter holds.
    # it will return whats not drawn
    userHand = []
    for x in range(0, userNoOfCards):
        userHand.append(gameDeck.pop())
    return userHand, gameDeck


def no_of_drawn_cards():
    canDraw = [5,6,7]
    userAnswer = None
    firstTimeAsked = 0
    while userAnswer not in canDraw:
        if firstTimeAsked == 0:
            firstTimeAsked = 1
        else:
            print("\n")
            print("That is not 5,6 or 7. Try again")
            print("\n")


        userAnswer = input("How many cards do you want to draw: 5, 6 or 7?")
        userAnswer = int(userAnswer)

    return userAnswer

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


def load_cards():
    return [{1:"this is card 1"},
        {2:"this is card 2"},
        {3: "this is card 3"},
        {4: "this is card 4"},
        {5: "this is card 5"},
        {6: "this is card 6"},
        {7: "this is card 7"},
        {8: "this is card 8"},
        {9: "this is card 9"},
        {10: "this is card 10"},
        {11: "this is card 11"},
        {12: "this is card 12"},
        {13: "this is card 13"},
        {14: "this is card 14"},
        {15: "this is card 15"},
        {16: "this is card 16"}]

def make_deck():
    cardNumbers = get_numbers_of_cards() # returns a list of playable cards
    return cardNumbers

def main():


    gameDeck = make_deck()
    cardDescriptions = load_cards()
    gameDeck = shuffle_cards(gameDeck)
    print ("Shuffled deck is {}" .format(gameDeck))
    userNoOfCards = no_of_drawn_cards()
    print ("User has picked {} cards to draw" .format(userNoOfCards))
    userHand, gameDeck = draw_cards(gameDeck, userNoOfCards)
    print("After drawing cards user hand holds {}" .format(userHand))
    print("After drawing cards {} cards remain in deck " .format(gameDeck))

    description_of_user_hand_cards(userHand)



if __name__ == "__main__":
    main()


# This code must have solutions for this
# cards must be shuffled  before the beginning of the drawn
# there must be several banned cards that cannot be picked
# each card drawn must have a description
# after a card is drawn the same card must not be drawn again (ex is removed from the deck)
# limit a number of cards drawn (ex 6)
# number of drawn cards can me chosed from option menu (6 or 7 cards)