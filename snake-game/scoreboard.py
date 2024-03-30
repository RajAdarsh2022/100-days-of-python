import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.display_score()

    
    def display_score(self):
        """Displays the score of the game"""
        self.clear()
        self.write(f"Scoreboard: {self.score}", move=False, align='center', font=('Arial', 12, 'normal'))
        self.hideturtle()
    
    def game_over(self):
        """Displays the message indicating that the game has ended"""
        self.goto(0,0)
        self.write(f"GAME OVER!", move=False, align='center', font=('Arial', 24, 'normal'))
        
        