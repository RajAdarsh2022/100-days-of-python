import colorgram
import turtle
import random

colors = colorgram.extract('hirst-painting.jpeg', 30)
colors_rgb = []
for color in colors:
    rgb_object = color.rgb
    rgb_mix = (rgb_object.r, rgb_object.g, rgb_object.b)
    colors_rgb.append(rgb_mix)


# Removing the backgroud colors so as it doesn't help in contributing dots
color_list = colors_rgb[5:]

def replicate_hirst_painting(num_rows, num_columns, dot_size, distance):
    """Replicates the hirst painting"""
    timmy_turtle.hideturtle()
    for row in range(num_rows):
        for col in range(num_columns):
            dot_color = random.choice(color_list)
            # Convert RGB tuple to a color string
            color_string = '#' + ''.join(f'{c:02x}' for c in dot_color)
            timmy_turtle.dot(dot_size , color_string)
            timmy_turtle.penup()
            timmy_turtle.fd(distance)
        timmy_turtle.penup()
        timmy_turtle.goto(0, (row + 1)* distance)


timmy_turtle = turtle.Turtle()
timmy_turtle.shape("arrow")
replicate_hirst_painting(10, 10, 20, 50)


screen = turtle.Screen()
screen.exitonclick()
