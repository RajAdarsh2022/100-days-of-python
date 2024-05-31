from turtle import Turtle
FONT = ("Courier", 16, "normal")
DISPLAY_LOCATION = (-220, 250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1

        self.penup()
        self.hideturtle()
        self.goto(DISPLAY_LOCATION)
        self.displayLevel()
        

    def displayLevel(self):
        """Displays the level on the game window"""
        self.clear()
        self.write(f"Level: {self.current_level}", align= "center", font=FONT)
    
    def increaseLevel(self):
        """Increases the level upon reaching the finish line"""
        self.current_level += 1
        self.displayLevel() 
    
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over!" , align="center", font=FONT)


