import random
import os
from game_data import data
from art import logo, vs

score = 0


def get_winner(dictionary_a, dictionary_b):
    """
    Returns the winner and the winner's data
    """
    if dictionary_a['follower_count'] > dictionary_b['follower_count']:
        return ["a", dictionary_a]
    elif dictionary_b['follower_count'] > dictionary_a['follower_count']:
        return ["b", dictionary_b]


def game(person_a, person_b, score):
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']} from {person_b['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    winner = get_winner(person_a, person_b)

    # if guess is correct, start a new round by calling the function again
    if choice == winner[0]:
        os.system("clear")
        score += 1
        game(winner[1], random.choice(data), score)

    # if the guess is wrong, end the game
    os.system("clear")
    print(logo)
    print("You lose.")
    print(f"Your final score: {score}")


game(random.choice(data), random.choice(data), score)
