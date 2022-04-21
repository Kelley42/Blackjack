import random
import os
from art import logo

# Set up with 2 cards each
def deal(): 
    """Deals a card and returns it"""
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return random.choice(cards)

def hit_stay(player_cards, player_blackjack): 
    """Deals cards to player, returns player_sum"""
    # Sum up cards
    player_sum = sum_cards(player_cards)
    # If player has Blackjack
    if player_sum == 21 and len(player_cards) == 2:
        player_blackjack = True
        return player_sum
    else:
        while player_sum < 21:
            while True:
                hit_stay_input = input("\nType 'y' to get another card or type 'n' to pass: ")
                if hit_stay_input == 'y':
                    # Deal another card
                    player_cards.append(deal()) 
                    # Sum up cards
                    player_sum = sum_cards(player_cards)
                    print(f"\nYour cards: {player_cards}")
                    if player_sum > 21:
                        print(f"\nYou went over 21! You lose.")
                        play_again()
                elif hit_stay_input == 'n':
                    print(f"\nYour final hand: {player_cards}")
                    return player_sum
                else:
                    print("Incorrect answer - please try again.")
        return player_sum
    

def sum_cards(hand): 
    """Takes hand and returns sum_num"""
    sum_num = 0
    # Get values of cards and add to sum
    for i in hand:
        if i == "A":
            sum_num += 11
        elif i == "J" or i == "Q" or i == "K":
            sum_num += 10
        else:
            sum_num += int(i)
    # If sum over 21, change A = 1 if Ace present
    if sum_num > 21:
        if "A" in hand:
            sum_num = 0
            # Value is 1 instead
            for i in hand:
                if i == "A":
                    sum_num += 1
                elif i == "J" or i == "Q" or i == "K":
                    sum_num += 10
                else:
                    sum_num += int(i)
    return sum_num


def hit_comp(computer_cards): 
    """Deals cards to computer, returns computer_sum"""
    # Sum up cards
    computer_sum = sum_cards(computer_cards)
    # If computer has Blackjack
    if computer_sum == 21 and len(computer_cards) == 2:
        computer_blackjack = True
        print(f"\nComputer's final hand: {computer_cards}")
        return computer_sum
    # If computer is at or over 17
    if computer_sum >= 17:
        print(f"\nComputer's final hand: {computer_cards}")
        return computer_sum
    # If computer is under 17
    while computer_sum < 17:
        # Deal another card
        computer_cards.append(deal()) 
        # Sum up cards
        computer_sum = sum_cards(computer_cards)
        if computer_sum > 21:
            print(f"\nComputer's final hand: {computer_cards}")
            print(f"\nThe computer went over 21 - you win!")
            play_again()
        if computer_sum >= 17:
            print(f"\nComputer's final hand: {computer_cards}")
            return computer_sum
    return computer_sum
     

def play_game():
    """Runs game"""
    print(logo)
    game = True
    player_blackjack = False
    computer_blackjack = False
    while game:
        player_cards = []
        computer_cards = []
        # Deal 2 cards each to player and computer
        for x in range(2):
            player_cards.append(deal()) 
            computer_cards.append(deal()) 
        # Show both player cards and first computer card
        print(f"\nYour cards: {player_cards}")
        print(f"\nComputer's first card: {next(iter(computer_cards))}")
        # Hit or stay
        final_player_sum = hit_stay(player_cards, player_blackjack)
        # Computer's turn
        final_computer_sum = hit_comp(computer_cards) 
        determine_winner(player_blackjack, computer_blackjack, final_player_sum, final_computer_sum)


def determine_winner(player_blackjack, computer_blackjack, final_player_sum, final_computer_sum):
    """Takes sums and determines winner"""
    if player_blackjack and computer_blackjack:
        print(f"\nTie! You and the computer both had Blackjacks!")
        play_again()
    elif player_blackjack and not computer_blackjack:
        print(f"\nYou got a Blackjack - you win!")
        play_again()
    elif computer_blackjack and not player_blackjack:
        print(f"\nThe computer had a Blackjack - you lose.")
        play_again()
    elif final_player_sum > final_computer_sum:
        print(f"\nYou win!")
        play_again()
    elif final_computer_sum > final_player_sum:
        print(f"\nYou lose.")
        play_again()
    else:
        print(f"\nTie!")
        play_again()


def play_again():
    """Takes input on play again and returns answer"""
    while True:
        play_again_input = input("\nDo you want to play again? 'y' or 'n': ").lower()
        if play_again_input == 'n':
            game = False
            exit()
        elif play_again_input == 'y':
            os.system('clear')
            play_game()
        else:
            print("Incorrect answer - please try again.")


play_game()