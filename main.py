# import colorgram

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.hideturtle()

# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
x_pos = -290
y_pos = 290

while y_pos >= -290:
    tim.teleport(x_pos, y_pos)
    tim.dot(20, random.choice(color_list))

    if x_pos >= 290:
        x_pos = -290
        y_pos -= 40
    else:
        x_pos += 40

screen = Screen()
screen.exitonclick()
