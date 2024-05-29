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
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.goto((0, -1 * random.randint(0, (WINDOW_HEIGHT / 2 - 50))))
        self.setheading(random.randint(0,60))
    
    def move(self):
        """Animation for moving the ball"""
        self.forward(5)
    
    def reverse(self):
        """For reversing the direction of the ball"""
        current_heading = self.heading()
        self.setheading(current_heading + 180)

    def reflect(self):
        """Reflects the ball upon collision with the floor"""
        current_heading = self.heading()
        if current_heading > 270 and current_heading < 360:
            angle_to_be_rotated = 2 * (360 - current_heading)
            self.setheading(current_heading + angle_to_be_rotated)
        if current_heading > 180 and current_heading < 270:
            angle_to_be_rotated = 2 * (current_heading - 180)
            self.setheading(current_heading - angle_to_be_rotated)
