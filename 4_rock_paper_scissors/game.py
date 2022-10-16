import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
computer_choice = random.randint(0, 2)


def winner(computer, player):

    if player == 0 and computer == 2:
        return "You win!"
    elif computer == 0 and player == 2:
        return "Computer wins."
    elif computer > player:
        return "Computer wins."
    elif player > computer:
        return "You win."
    elif computer == player:
        return "Draw."


player_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors.\n"))


if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. Get outta here.")
    exit()

print("You chose:")
print(images[player_choice])

print("The computer chose:")
print(images[computer_choice])

print(winner(computer_choice, player_choice))
