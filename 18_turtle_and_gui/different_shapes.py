from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("green")

corners = 3

while corners < 10:
    for i in range(1, corners + 1):
        t.forward(100)
        t.right(360 / corners)
    corners += 1


screen = Screen()
screen.exitonclick()
