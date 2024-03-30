import turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
FORWARD_DISTANCE = 20


class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]
    
    def add_segment(self, position):
        """Adds a new segment to the snake's body"""
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def create_snake(self):
        """Creating the snake body / Initializing the snake body"""
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
        
    def extend(self):
        """Increases the snake length whenever snake consumes the food"""
        snake_tail_pos = self.snake_segments[-1].pos()
        self.add_segment(snake_tail_pos)


    def move_forward(self):
        """Creating the forward movement of the snake """
        for index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[index - 1].xcor()
            new_y = self.snake_segments[index - 1].ycor()
            self.snake_segments[index].goto(new_x, new_y)
    
        self.snake_head.forward(FORWARD_DISTANCE)
    
    def up(self):
        """Moves the snake's head towards north/upwards direction"""
        current_heading = self.snake_head.heading()
        if current_heading != 270:
            self.snake_head.setheading(90)
    
    def down(self):
        """Moves the snake's head towards south/downwards direction"""
        current_heading = self.snake_head.heading()
        if current_heading != 90:
            self.snake_head.setheading(270)     

    def left(self):
        """Moves the snake's head towards west/left direction"""
        current_heading = self.snake_head.heading()
        if current_heading != 0:
            self.snake_head.setheading(180) 

    def right(self):
        """Moves the snake's head towards east/right direction"""
        current_heading = self.snake_head.heading()
        if current_heading != 180:
            self.snake_head.setheading(0)           