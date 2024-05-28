import time
import turtle
from paddle import Paddle
from ball import Ball
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, BALL_SPEED_FACTOR


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = WINDOW_WIDTH , height = WINDOW_HEIGHT)
screen.title("Pong game")
screen.tracer(0)
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
ball = Ball()

#Adding event-listeners for paddle movement
screen.onkey(right_paddle.moveUp, "Up")
screen.onkey(right_paddle.moveDown, "Down")
screen.onkey(left_paddle.moveUp, "w")
screen.onkey(left_paddle.moveDown, "s")


is_game_on = True
while is_game_on:
    time.sleep(BALL_SPEED_FACTOR)
    ball.move()
    screen.update()


    #Checking for the collision between paddle and ball
    if abs(ball.xcor() - left_paddle.xcor()) < 5:
        pass
    if abs(ball.xcor() - right_paddle.xcor()) < 5:
        pass

    #Checking for the collision between horizontal floor and wall
    if ball.ycor() < -(WINDOW_HEIGHT / 2 + 10):
        #Do the bounce back logic
        pass

    if(ball.xcor() >= WINDOW_WIDTH / 2 or ball.xcor() <= - WINDOW_WIDTH/2):
        is_game_on = False

print("Game-over!")
screen.exitonclick()
