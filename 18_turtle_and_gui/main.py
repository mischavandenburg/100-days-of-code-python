# draws a 10 x 10 grid of random colors from a list

import turtle as turtle_module
import random

color_list = [(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31)]

turtle_module.colormode(255)
t = turtle_module.Turtle()
t.penup()
t.hideturtle()

pos_y = 0

for y in range(1, 11):
    t.sety(pos_y)
    for i in range(1, 11):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    pos_y += 50
    t.setx(0)

screen = turtle_module.Screen()
screen.exitonclick()
