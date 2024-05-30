from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.writeScore()
    
    def writeScore(self):
        """Writes the score on the top of the window pane"""
        self.goto(-100 , 200)
        self.write(self.score_left, align="center", font= ("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font= ("Courier", 40, "normal"))

    def leftPoint(self):
        """Increases the score upon collision with left paddle"""
        self.score_left += 1
        self.clear()
        self.writeScore()

    def rightPoint(self):
        """Increases the score upon collision with right paddle"""
        self.score_right += 1
        self.clear()
        self.writeScore()



