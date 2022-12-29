import turtle
import pandas

# set up screen and turtle
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the data
data = pandas.read_csv("50_states.csv")
score = 0


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


running = True
while running:

    user_answer = screen.textinput(title=f"{score}/50 States Correct",
                                   prompt="What's another state's name?")

    key = user_answer.title()

    # if the user input exists in the series, create a new turtle
    # and update the score
    if data.state.isin([key]).any():
        row = data[data.state == key]
        create_turtle(row)
        score += 1

screen.exitonclick()
