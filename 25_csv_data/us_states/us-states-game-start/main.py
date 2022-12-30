import turtle
import pandas
from icecream import ic

# set up screen and turtle
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
score = 0
guessed_states = []


def create_turtle(state):
    """
    This function creates a new turtle that writes the state name
    at the x and y coordinate from the csv file
    """
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()

    state_name = state.state.item()
    x_cor = state.x.item()
    y_cor = state.y.item()

    text.setposition(x_cor, y_cor)
    text.write(state_name, move=False, align="left")


while len(guessed_states) < 50:

    user_answer = screen.textinput(title=f"{score}/50 States Correct",
                                   prompt="What's another state's name?").title()

    if user_answer == "Exit":
        break

    # if the user input exists in the series, create a new turtle
    # and update the score
    if user_answer in all_states:
        guessed_states.append(user_answer)
        ic(guessed_states)
        row = data[data.state == user_answer]
        create_turtle(row)
        score += 1
        if score == 50:
            running = False
            print("You win, Game Over")
            break

# write the states the user did not guess to a csv file
with open("states_to_learn.csv", "w") as f:
    for state in all_states:
        if state not in guessed_states:
            f.write(f"{state}\n")
