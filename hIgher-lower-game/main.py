from itertools import count
from art import logo
from art import vs
from game_data import data
import random

def game(): 
    print(logo)

    count = 0
    game_is_on = True
    while game_is_on:
        
        A = random.choice(data)
        B = random.choice(data)
        print("Compare A: "+A['name']+", "+A['description']+", "+"from "+A['country'])
        print(vs)
        print("Compare B: "+B['name']+", "+B['description']+", "+"from "+B['country'])
        print("\n")

        choice = input("Who has more followers on instagram? Type 'A' or 'B': ")
        if(choice == "A"):
            if A["follower_count"] > B["follower_count"]:
                print("You are Correct!\n")
                count += 1
            else:
                print("you lost!")
                game_is_on = False
                print("your score is: "+str(count))
        elif(choice == "B"):
            if B["follower_count"] > A["follower_count"]:
                print("You are Correct!")
                count += 1
            else:
                print("you lost!")
                game_is_on = False
                print("your score is: "+str(count)+"\n")

if( input("Do you want to play a game of Higher and lower? If yes type 'y' else type 'n': ").lower()=="y"):
    game()