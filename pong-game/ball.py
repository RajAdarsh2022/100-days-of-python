from turtle import Turtle
import random
from constants import WINDOW_HEIGHT, WINDOW_WIDTH

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.createBall()
    
    def createBall(self):
        # self.ball = Turtle() 
        # THE ABOVE LINE TEACHES A VERY IMPORTANT THING
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.goto((0, -1 * random.randint(0, (WINDOW_HEIGHT / 2 - 50))))
        self.setheading(random.randint(0,60))
    
    def move(self):
        """Animation for moving the ball"""
        self.forward(5)
