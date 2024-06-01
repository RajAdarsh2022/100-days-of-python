import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.display_score()

    def get_high_score(self):
        """Recieves the highscore from the file"""
        with open("highscore.txt") as f_pointer:
            high_score = f_pointer.read()
            self.high_score = high_score       

    def set_high_score(self):
        """Saves the new highscore created to the file"""
        with open("highscore.txt", mode="w") as f_pointer:
            f_pointer.write(self.high_score)
    
    def display_score(self):
        """Displays the score of the game"""
        self.clear()
        self.write(f"Score: {self.score} Highscore : {self.high_score}", move=False, align='center', font=('Arial', 12, 'normal'))
        
    
    def game_over(self):
        """Displays the message indicating that the game has ended and checks if the new highScore is created or not"""
        if(self.score > int(self.high_score)):
            self.high_score = str(self.score)
            self.set_high_score()
        self.goto(0,0)
        self.write(f"GAME OVER!", move=False, align='center', font=('Arial', 24, 'normal'))
        
        