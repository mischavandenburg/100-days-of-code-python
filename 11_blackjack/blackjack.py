from art import logo
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal(party):
    party.append(random.choice(cards))


def count(card_list):
    if len(card_list) and sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has blackjack and wins"
    elif user_score == 0:
        return "You win with blackjack"
    elif computer_score > 21:
        return "Computer went over 21, you win!"
    elif user_score > 21:
        return "You went over 21, you lose."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."


def game():
    print(logo)
    print("Welcome to the game. Blackjack is indicated by 0")

    computer = []
    user = []
    game_over = False

    # set up the game by dealing 2 cards to each party
    for i in range(2):
        deal(user)
        deal(computer)

    # user's turn
    while game_over is False:
        user_score = count(user)
        computer_score = count(computer)
        print(f"Your Cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        # finish the game if user or computer has blackjack already
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                deal(user)
            else:
                game_over = True

    # computer's turn, not allowed to stop hitting if score is less than 17
    while computer_score != 0 and computer_score < 17:
        deal(computer)
        computer_score = count(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Would you like to play another game? 'y' or 'n': ") == "y":
    os.system('clear')
    game()
