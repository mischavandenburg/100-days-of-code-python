import random

number = random.randint(1, 100)
attempts = 10

print("Welcome to the Number Guessing game.")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5

running = True
print(number)
while running:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1

    if guess > number:
        print("Too high.")
    if guess < number:
        print("Too low.")
    if guess == number:
        print("Correct! You win.")
        running = False

    if attempts < 1:
        print("You ran out of attempts, game over.")
        running = False
