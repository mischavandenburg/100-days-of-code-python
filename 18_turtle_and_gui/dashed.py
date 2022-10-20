from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("green")

for i in range(15):
    t.down()
    t.forward(10)
    t.up()
    t.forward(10)


screen = Screen()
screen.exitonclick()
