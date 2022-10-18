from art import logo
import os

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    running = True

    while running:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the nexr number?: "))
        task = operations[operation_symbol]
        answer = task(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {num2}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            running = False
            os.system('clear')
            calculator()


calculator()
