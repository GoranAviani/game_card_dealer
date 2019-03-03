

def get_numbers_of_cards():
    return [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16] # card no 14 is to strong to play with

def make_deck():
    cardNumbers = get_numbers_of_cards() # returns a list of playable cards
    return cardNumbers

def main():


    gameDeck = make_deck()
    print (gameDeck)

if __name__ == "__main__":
    main()