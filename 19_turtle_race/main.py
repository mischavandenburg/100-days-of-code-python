from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-250, y=y_positions[i])
    turtles.append(t)

running = False
if user_bet:
    running = True

while running:
    for turtle in turtles:
        if turtle.xcor() > 230:
            running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You guessed correctly, the {winning_color} finished first.")
            else:
                print(f"You lost, the {winning_color} finished first.")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
