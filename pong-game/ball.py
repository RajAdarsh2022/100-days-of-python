from turtle import Turtle
import random
from constants import WINDOW_HEIGHT, WINDOW_WIDTH

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    
    def move(self):
        """Animation for moving the ball"""
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounceY(self):
        """Reflects the ball upon collision with the floor or wall"""
        self.y_move *= -1
    
    def bounceX(self):
        """Reflects the ball upon collision with the paddle"""
        self.x_move *= -1
