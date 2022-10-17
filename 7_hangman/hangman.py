import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
lives = 6
# generate list of underscores
display = ["_" for i in chosen_word]
status = True
history = []

print(logo)
while status is True:
    print(stages[lives])
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: \n").lower()

    if guess in history:
        print("You already tried this letter.")

    history.append(guess)

    if guess not in chosen_word:
        if lives == 0:
            print("Game Over")
            print(f"The word was: {chosen_word}")
            status = False
            break
        lives -= 1
        print(f"You guessed {guess}, which is not in the word. You lose a life.")

    # check if the letter is in the word
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    if "_" not in display:
        print(f"{' '.join(display)}")
        status = False
        print("You Win")
