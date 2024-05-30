import time
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, BALL_SPEED_FACTOR


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = WINDOW_WIDTH , height = WINDOW_HEIGHT)
screen.title("Pong game")
screen.tracer(0)
screen.listen()




left_paddle = Paddle("Left")
right_paddle = Paddle("Right")
ball = Ball()
score_board = Scoreboard()

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
    # Case1 : collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounceX()
        score_board.rightPoint()
    
    # Case1 : collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounceX()
        score_board.leftPoint()

    #Checking for the collision between floors, wall and ball
    if ball.ycor() < -(WINDOW_HEIGHT / 2 - 20) or ball.ycor() > (WINDOW_HEIGHT / 2 - 20):
        ball.bounceY()

    if(ball.xcor() >= WINDOW_WIDTH / 2 or ball.xcor() <= - WINDOW_WIDTH/2):
        is_game_on = False

print("Game-over!")
screen.exitonclick()
