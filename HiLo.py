import random
import os
 
# Clears out the terminal
def clear_system():
    os.system("clear")
 
# Prints the scoreboard of game 
def print_scoreboard(score, chances):
    print("    ____________________")
    print("   |                    |")
    if score >= 10:
        print("   |     Score = {}     |".format(score))
    else:   
        print("    |     Score = {}      |".format(score))
    print("    |  Chances Left = {}  |".format(chances))  
    print("    |____________________|")
 
# Prints the cards 
def print_cards(prev_card, current_card): 
     
    print()
    print("\t ________________      ________________      ________________")
    print("\t|                |    |                |    |                |")
    if prev_card.value == '10' and current_card.value == '10':
        print("\t|  {}            |    |  {}            |    |                |".format(prev_card.value,current_card.value))
    elif prev_card.value == '10': 
        print("\t|  {}            |    |  {}             |    |                |".format(prev_card.value,current_card.value))   
    elif current_card.value == '10':
        print("\t|  {}             |    |  {}            |    |                |".format(prev_card.value,current_card.value))   
    else:
        print("\t|  {}             |    |  {}             |    |                |".format(prev_card.value,current_card.value))  
    print("\t|                |    |                |    |      * *       |")
    print("\t|                |    |                |    |    *     *     |")
    print("\t|                |    |                |    |   *       *    |")
    print("\t|                |    |                |    |   *       *    |")
    print("\t|       {}        |    |       {}        |    |          *     |".format(prev_card.suit, current_card.suit))
    print("\t|                |    |                |    |         *      |")
    print("\t|                |    |                |    |        *       |")
    print("\t|                |    |                |    |                |")
    print("\t|                |    |                |    |                |")
    if prev_card.value == '10' and current_card.value == '10':
        print("\t|            {}  |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))
    elif prev_card.value == '10': 
        print("\t|            {}  |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))   
    elif current_card.value == '10':
        print("\t|            {}   |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))   
    else:
        print("\t|            {}   |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))  
    print("\t|________________|    |________________|    |________________|")
    print()
 
 
# Display card classes
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
 
def hi_lo_game(deck):
 
    global cards_values
 
    # Generate the previous card
    prev_card = Card(" ", " ")
 
    # Generate the current card
    current_card = random.choice(deck)
 
    # The starting card cannot be lowest or highest
    while current_card.value == "A" or current_card.value == "K":
        current_card = random.choice(deck)
 
    # Remove the card from the deck 
    deck.remove(current_card)
 
    # Number of chances left
    chances = 3
 
    # The current
    score = 0
 
    # The GAME LOOP
    while chances:
 
        print_scoreboard(score, chances)
        print_cards(prev_card, current_card)
 
        print("   ------------------------------------")
        print(" Game Menu")
        print("   ------------------------------------")
        print()
        print("      Enter 1 to bet for a high card")
        print("     Enter 0 to bet for a low card")
        print()
         
        # See if the deck is finished
        if len(deck) == 0:
            clear_system()
            print_cards(prev_card, current_card)
            print("    You have reached the end of the deck!")
            print("    Congratulations!!!")
            print()
            print("    Your Final Score =", score)
            print("    Thank you for playing!!!")
            break
 
        # Try block for player input error
        try:
            choice = int(input(" Enter your choice = "))
        except ValueError:
            clear_system()
            print("Wrong Input!! Try Again.")
            continue   
 
        #  wrong choice
        if choice > 1 or choice < 0:
            clear_system()
            print("Wrong Input!! Try Again.")
            continue       
 
        # Change the current card 
        prev_card = current_card
 
        # Choose the current card
        current_card = random.choice(deck)
 
        # Remove the new card 
        deck.remove(current_card)
 
        # A high card
        if cards_values[current_card.value] > cards_values[prev_card.value]:
            result = 1
 
        # A low card    
        elif cards_values[current_card.value] < cards_values[prev_card.value]:
            result = 0
 
        # Same value card   
        else:
            result = -1    
 
        # A Tie Round
        if result == -1:
            clear_system()
            print(" You tied... Play Again")
 
        # Round won
        elif choice == result:
            clear_system()
            print(" Congrats, you won! Play Again")
            score = score + 1  
 
        # Round Lost    
        else:
            if chances == 1:
                clear_system()
                print("Game is Over")
                print_cards(prev_card, current_card)
                print("\  Your Final Score =", score)
                print(" Thanks for playing!!!")
                break  
            clear_system()
            print("\t\t\t YOU LOSE!! Play Again")
            chances = chances - 1
 
 
if __name__ == '__main__':
 
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The suit value 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # The card value
    cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
 
    # The deck of cards
    deck = []
 
    # Loop for every type of suit
    for suit in suits:
 
        # Loop for every type of card in a suit
        for card in cards:
 
            # Adding card to the deck
            deck.append(Card(suits_values[suit], card))
 
    hi_lo_game(deck)









    
