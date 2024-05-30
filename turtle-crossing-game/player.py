from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def moveUp(self):
        """Makes the turtle go upwards"""
        curr_x = self.xcor()
        curr_y = self.ycor()
        self.goto(curr_x , curr_y + MOVE_DISTANCE)

    def reset(self):
        """Brings the turtle to the starting position"""
        self.goto(STARTING_POSITION)
