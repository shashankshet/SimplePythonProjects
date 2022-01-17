############### Blackjack Project #####################
import random
import os
from turtle import clear
from art import logo
from art import logo1
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =  random.choice(cards)
    return card


def calculate_score(cards):
    if(sum(cards)==21 and len(cards)==2):
        return 0
    if 11 in cards and sum(cards)>=21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has BlackJack!!"
    elif user_score == 0:
        return "You win with a BlackJacl!!"
    elif user_score>21:
        return "You went over, you lose"
    elif computer_score >21:
        return "Opponent went over, you win!"
    elif user_score>computer_score:
        return "you win!"
    else:
        return "you lose"

def play_game():
    print(logo)
    print(logo1)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score==0 or computer_score == 0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal = input("type 'y' to get another cards, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over=True


    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, and final score is: {user_score}")
    print(f"Your opponent's final hand is {computer_cards}, and final score is: {computer_score}")
    print(compare(user_score,computer_score))


while input("Enter 'y' to play a game of BlackJack:  ").lower() == "y":
    clearConsole()
    play_game()