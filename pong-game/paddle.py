import turtle
from constants import STARTING_POSITIONS_LEFT, STARTING_POSITIONS_RIGHT




class Paddle(turtle.Turtle):

    def __init__(self, direction):
        super().__init__()
        self.segments = []
        self.segment_position = []

        if direction == "Left":
            #Move the paddle to the left side of the window
            self.createPaddle(STARTING_POSITIONS_LEFT)
        else:
            #Move the paddle to the right side of the window
            self.createPaddle(STARTING_POSITIONS_RIGHT)

    def createPaddle(self, starting_postions):
        """Creates the paddle"""
        for position in starting_postions:
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            self.segment_position.append(position)
    
    def moveUp(self):
        """For moving the paddle upwards"""
        print("Upwards!")

    def moveDown(self):
        """For moving the paddle downwards"""
        print("Downwards!")

    