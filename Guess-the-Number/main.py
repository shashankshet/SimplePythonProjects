import numbers
from random import choice
from art import logo
import random
import os
from turtle import clear

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def play_game():
    print(logo)
    print("Welcome to Number guessing game!")
    print("I'm thinking of number between 1 and 100.")

    number = random.randint(1,100)

    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if choice == "easy":
        lives = 10
    elif choice == "hard":
        lives = 5

    game_is_still_on = True
    while game_is_still_on:
        while lives > 0 and game_is_still_on== True:
            print(f"You have {lives} remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print("You win!")
                game_is_still_on = False
                lives -= 1
            elif guess > number:
                print("Too High")
                lives -= 1
            elif guess < number:
                print("Too Low")
                lives -= 1
        game_is_still_on =False

while input("Do you want to play a Number guessing game? type 'y' if yes: ").lower() == "y":
    clearConsole()
    play_game()