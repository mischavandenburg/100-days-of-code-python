from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
should_run = True

def caesar(message, number, action):
    result = ""
    for letter in message:
        if letter in alphabet:
            alphabet_location = alphabet.index(letter)
            if action == "encode":
                result += alphabet[alphabet_location + number]
            if action == "decode":
                result += alphabet[alphabet_location - number]
        else:
            result += letter
    print(f"The {action}ed text is {result}")


while should_run is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    keep_going = input("Do you want to do another word? Type yes or no.\n")
    if keep_going == "no":
        should_run = False
        print("Goodbye.")
