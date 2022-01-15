import random
import hangman_words


choosen_word = random.choice(hangman_words.word_list)
from hangman_art import logo
print(logo)
print("Choosen word is: "+choosen_word)

lives = 6
end_of_game = False
ans = []
for i in range(len(choosen_word)):
    ans.append("_")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    
    if guess in ans:
        print("you have already guessed this letter "+guess)
 

    for i in range(len(choosen_word)):
        if guess == choosen_word[i]:
            ans[i] = guess
            print(ans)

    # if guess in ans:
    #     print("You have already guessed the letter "+guess+" try a diffrent letter")
    if guess not in choosen_word:
        lives -= 1
        print("The letter "+guess+" is not in the word, you lose a life")
        if lives == 0:
            end_of_game = True
            print("You lose.")
 

    if "_" not in ans:
        end_of_game = True
        print("You win!")
    from hangman_art import stages
    print(stages[lives])