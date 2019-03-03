import random

def findDesc(x, cardDescriptions):
    for description in cardDescriptions:
        if description["cardNo"] == x:
            print(description["cardDesc"])
            break

def description_of_user_hand_cards(userHand):
    cardDescriptions = load_cards()
    for x in userHand:
        findDesc(x, cardDescriptions)


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
    return [
        {"cardNo" :16, "cardDesc" : "this is card 16"},
        {"cardNo" :1, "cardDesc" : "this is card 1"},
        {"cardNo" :2, "cardDesc" : "this is card 2"},
        {"cardNo" :3, "cardDesc" : "this is card 3"},
        {"cardNo" :4, "cardDesc" : "this is card 4"},
        {"cardNo" :5, "cardDesc" : "this is card 5"},
        {"cardNo" :6, "cardDesc" : "this is card 6"},
        {"cardNo" :7, "cardDesc" : "this is card 7"},
        {"cardNo" :8, "cardDesc" : "this is card 8"},
        {"cardNo" :9, "cardDesc" : "this is card 9"},
        {"cardNo" :10, "cardDesc" : "this is card 10"},
        {"cardNo" :11, "cardDesc" : "this is card 11"},
        {"cardNo" :12, "cardDesc" : "this is card 12"},
        {"cardNo" :13, "cardDesc" : "this is card 13"},
        {"cardNo" :14, "cardDesc" : "this is card 14"},
        {"cardNo" :15, "cardDesc" : "this is card 15"}
]


def make_deck():
    cardNumbers = get_numbers_of_cards() # returns a list of playable cards
    return cardNumbers

def main():


    gameDeck = make_deck()
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