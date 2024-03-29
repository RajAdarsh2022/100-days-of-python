import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")


starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for seg in starting_pos:
    t = turtle.Turtle("square")
    t.color("white")
    t.penup()
    t.goto(seg)
    segments.append(t)

screen.update()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg_index in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_index - 1].xcor()
        new_y = segments[seg_index - 1].ycor()
        segments[seg_index].goto(new_x, new_y)
    segments[0].setheading(0)  # Change direction to face upwards
    segments[0].forward(20)  # Move the head forward

screen.exitonclick()

