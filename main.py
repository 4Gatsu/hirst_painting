# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.hideturtle()

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
tim.penup()
tim.goto(-225, -225)
tim.pendown()
# obraz ma miec rozmiar 10x10 wypelnionych kropek


def tim_reset_line():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    
    return


for move in range(10):
    for line in range(10):
        tim.color(random.choice(color_list))
        tim.pendown()
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim_reset_line()

screen = t.Screen()
screen.exitonclick()
