# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# nr_letters = 4
# nr_symbols = 3
# nr_numbers = 2

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Eazy is for PLEBS!

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
result = []


def get_values(amount, type):
    for i in range(1, amount + 1):
        if type == "letter":
            put = random.choice(letters)
            result.append(put)
        elif type == "symbol":
            put = random.choice(symbols)
            result.append(put)
        elif type == "number":
            put = random.choice(numbers)
            result.append(put)


get_values(nr_letters, "letter")
get_values(nr_symbols, "symbol")
get_values(nr_numbers, "number")

random.shuffle(result)
final = ''.join(result)
print(final)
