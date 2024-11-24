"""Previously in this chapter you saw the card_dealer.py program that simulates cards being
dealt from a deck. Enhance the program so it simulates a simplified version of the game of
Blackjack between two virtual players. The cards have the following values:
• Numeric cards are assigned the value they have printed on them. For example, the value
of the 2 of spades is 2, and the value of the 5 of diamonds is 5.
• Jacks, queens, and kings are valued at 10.
• Aces are valued at 1 or 11, depending on the player’s choice.
The program should deal cards to each player until one player’s hand is worth more than
21 points. When that happens, the other player is the winner. (It is possible that both
players’ hands will simultaneously exceed 21 points, in which case neither player wins.) The
program should repeat until all the cards have been dealt from the deck.
If a player is dealt an ace, the program should decide the value of the card according to the
following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed
21 points. In that case, the ace will be worth 1 point.""" # Similar to unbelivaboat
import random

strat = 0

def main():
    global strat
    strat = int(input('What strategy would you like the computer to use? (choose between 1 or any other integer): '))
    
    deck = create()
    random.shuffle(deck)  # Shuffle the deck

    again = 'y'
    while (again != 'n') and (len(deck) > 7):
        print("\nStarting a new round...\n")
        player1 = []
        player2 = []

        # Player 1's turn
        print("Player 1's turn:")
        player(deck, player1)
        value = calculate(player1)
        if value <= 21:
            print(f"Player 1's final hand value: {value}")
        else:
            print(f"Player 1 busted with a hand value of {value}")

        # Player 2's turn if Player 1 didn't bust
        if value <= 21:
            print("\nPlayer 2's turn (Computer):")
            computer(deck, player2, value)
            nilai = calculate(player2)
            if nilai <= 21:
                print(f"Player 2's final hand value: {nilai}")
            else:
                print(f"Player 2 busted with a hand value of {nilai}")

            # Determine the winner
            winner(value, nilai)
        else:
            print("Player 2 wins by default as Player 1 busted.")
        
        again = input('Do you want to play again? "n" for no. ')
        
    if len(deck) < 8:
        print("\nThe deck is low on cards. Please restart.")        

def create(): # changed to tuple for import random
    deck = [
        ('Ace of Spades', 1), ('2 of Spades', 2), ('3 of Spades', 3),
        ('4 of Spades', 4), ('5 of Spades', 5), ('6 of Spades', 6),
        ('7 of Spades', 7), ('8 of Spades', 8), ('9 of Spades', 9),
        ('10 of Spades', 10), ('Jack of Spades', 10),
        ('Queen of Spades', 10), ('King of Spades', 10),
        
        ('Ace of Hearts', 1), ('2 of Hearts', 2), ('3 of Hearts', 3),
        ('4 of Hearts', 4), ('5 of Hearts', 5), ('6 of Hearts', 6),
        ('7 of Hearts', 7), ('8 of Hearts', 8), ('9 of Hearts', 9),
        ('10 of Hearts', 10), ('Jack of Hearts', 10),
        ('Queen of Hearts', 10), ('King of Hearts', 10),
        
        ('Ace of Clubs', 1), ('2 of Clubs', 2), ('3 of Clubs', 3),
        ('4 of Clubs', 4), ('5 of Clubs', 5), ('6 of Clubs', 6),
        ('7 of Clubs', 7), ('8 of Clubs', 8), ('9 of Clubs', 9),
        ('10 of Clubs', 10), ('Jack of Clubs', 10),
        ('Queen of Clubs', 10), ('King of Clubs', 10),
        
        ('Ace of Diamonds', 1), ('2 of Diamonds', 2), ('3 of Diamonds', 3),
        ('4 of Diamonds', 4), ('5 of Diamonds', 5), ('6 of Diamonds', 6),
        ('7 of Diamonds', 7), ('8 of Diamonds', 8), ('9 of Diamonds', 9),
        ('10 of Diamonds', 10), ('Jack of Diamonds', 10),
        ('Queen of Diamonds', 10), ('King of Diamonds', 10)
    ]
    return deck

def draw(deck, hand): # Draw a single card from the deck and add it to the player's hand
    if deck:
        card = deck.pop()  # Draw a card from the deck
        hand.append(card)  # Add the card to the player's hand
        print(f"Drew: {card[0]}")
    else:
        print("No more cards in the deck.")

def calculate(hand): # Calculate the value of a given hand
    value = sum(v for _, v in hand)
    num_aces = sum(1 for card, _ in hand if 'Ace' in card)
    while value + 10 <= 21 and num_aces > 0:
        value += 10
        num_aces -= 1
    return value

def display(hand): # Display the cards in the hand
    for card, _ in hand:
        print(card)

def player(deck, hand): # Allows you to draw cards until they bust or decide to stop
    while True:
        draw(deck, hand)
        display(hand)
        value = calculate(hand)
        print('Value of this hand:', value)
        
        if value > 21:
            print("You bust!")
            break
        
        if value == 21:
            print("You have 21, which is a BlackJack! Stopping.")
            break

        # Ask if the player wants to draw another card
        response = input("Do you want to draw another card? (y/n): ").strip().lower()
        if response != 'y':
            print("You decide to stop drawing cards.")
            break

def computer(deck, hand, target): # 2 strategies to choose from
    if strat == 1:
        while True:
            draw(deck, hand)
            value = calculate(hand)
            
            if value > 21:
                print("Computer busts!")
                break
            
            if value >= 17:
                print("Computer stops drawing cards.")
                break
    else:   
        while True:
            draw(deck, hand)
            value = calculate(hand)

            if value > 21:
                print("Computer busts!")
                break

            if value < target and value < 21:
                print("Computer draws another card.")
            else:
                print("Computer stops drawing cards.")
                break    

def winner(value, nilai): # Determine the winner based on hand values
    if value > 21 and nilai > 21:
        print("Both players have busted. No winner.")
    elif value > 21:
        print("Player 1 busted. Computer wins!")
    elif nilai > 21:
        print("Computer busted. Player 1 wins!")
    elif value > nilai:
        print("Player 1 wins!")
    elif nilai > value:
        print("Computer wins!")
    else:
        print("It's a tie!")

main()