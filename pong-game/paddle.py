from turtle import Turtle
from constants import STARTING_POSITION_LEFT, STARTING_POSITION_RIGHT, PADDLE_MOVING_DISTANCE




class Paddle(Turtle):

    def __init__(self, direction):
        super().__init__()
        if direction == "Left":
            #Move the paddle to the left side of the window
            self.createPaddle(STARTING_POSITION_LEFT)
        else:
            #Move the paddle to the right side of the window
            self.createPaddle(STARTING_POSITION_RIGHT)

    def createPaddle(self, starting_postion):
        """Creates the paddle according to the side mentioned"""
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.goto(starting_postion)
    
    def moveUp(self):
        """For moving the paddle upwards"""
        self.forward(PADDLE_MOVING_DISTANCE)


    def moveDown(self):
        """For moving the paddle downwards"""
        self.backward(PADDLE_MOVING_DISTANCE)


    