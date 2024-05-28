import turtle
from paddle import Paddle
from constants import WINDOW_HEIGHT, WINDOW_WIDTH


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = WINDOW_WIDTH , height = WINDOW_HEIGHT)
screen.title("Pong game")
screen.listen()


# print(screen.window_height())
# print(screen.window_width())


#Drawing the midline separating the two windows
def divideScreen():
    midline = turtle.Turtle()
    midline.color("white")
    midline.speed("fastest")
    midline.hideturtle()
    midline.penup()
    midline.goto((0 , -1 * (WINDOW_HEIGHT / 2)))
    midline.setheading(90)
    while midline.ycor() < WINDOW_HEIGHT / 2 :
        if(midline.isdown()):
            midline.penup()
        else:
            midline.pendown()
        midline.forward(10)

divideScreen()


left_paddle = Paddle("Left")
right_paddle = Paddle("Right")

#Adding event-listeners for paddle movement
screen.onkey(right_paddle.moveUp, "Up")
screen.onkey(right_paddle.moveDown, "Down")
screen.onkey(left_paddle.moveUp, "w")
screen.onkey(left_paddle.moveDown, "s")

screen.exitonclick()
