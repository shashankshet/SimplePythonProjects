import random

#taking user input
user_choice = int(input("What do you choose? type 0 for Rock, 1 for paper and 2 for scissors"))

rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """
paper = """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """
scissor = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """

if(user_choice==0):
    # Rock
    print(rock)
elif(user_choice==1):
    # Paper
    print(paper)
elif(user_choice==2):
    # Scissors
    print(scissor)
else:
    print("Invalid Input, computer wins")


#taking computer input using randomization
computer_choice = random.randint(0,2)
print("Computer choose")
if(computer_choice==0):
    # Rock
    print(rock)
elif(computer_choice==1):
    # Paper
    print(paper)
elif(computer_choice==2):
    # Scissors
    print(scissor)


if(user_choice==0 and computer_choice==2):
    print("You win!!")
elif(user_choice==0 and computer_choice==1):
    print("You lost, Better luck next time")
elif(user_choice==0 and computer_choice==0):
    print("Game drawn")
if(user_choice==1 and computer_choice==0):
    print("You win!!")
elif(user_choice==1 and computer_choice==2):
    print("You lost, Better luck next time")
elif(user_choice==1 and computer_choice==1):
    print("Game drawn")
if(user_choice==2 and computer_choice==0):
    print("You lost, Better luck next time")
elif(user_choice==2 and computer_choice==1):
    print("You win!!")
elif(user_choice==2 and computer_choice==2):
    print("Game drawn")






