import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface(tk.Tk):

    def __init__(self, quiz_brain : QuizBrain):
        super().__init__()
        self.create_ui()
        self.quiz_brain = quiz_brain
        self.display_question()
        self.mainloop()

    def create_ui(self):
        self.title("My Quiz-App")
        self.geometry("600x600")
        self.config(bg= THEME_COLOR)

        self.score_label = tk.Label(self, text=f"Score: 0")


        self.question_canvas = tk.Canvas(self, height=400, width=500, background='white')
        self.question_canvas_text = self.question_canvas.create_text(250, 200, width= 450)


        self.response_label = tk.Label(self)
        self.true_button = tk.Button(self.response_label, text="True", command = self.true_response)
        self.false_button = tk.Button(self.response_label, text="False", command = self.false_response)

        self.response_label.rowconfigure(0, weight = 1)
        self.response_label.columnconfigure((0,1), weight= 1)
        self.true_button.grid(row= 0, column= 0)
        self.false_button.grid(row= 0, column=1)

        self.score_label.pack(side='top', padx= 5)
        self.question_canvas.pack(side='top', expand= True, padx=5)
        self.response_label.pack(side='top', expand= True, padx=5)
    
    def display_question(self):
        """Displays the question on the screen"""
        self.question_canvas.config(background='white')
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.ask_question()
            self.question_canvas.itemconfig(self.question_canvas_text, text= question_text)
        else:
            self.question_canvas.itemconfig(self.question_canvas_text, text= "Test over!")

    def display_response(self, response):
        """Changes the canvas color depending on whether the user-response was correct or wrong"""
        if response:
            self.question_canvas.config(background='green')
        else:
            self.question_canvas.config(background='red')
        self.display_score()
        self.after(1000, self.display_question)
        

    def true_response(self):
        """When true button is clciked"""
        self.display_response(self.quiz_brain.check_answer("True"))
    
    def false_response(self):
        """When false button is clicked"""
        self.display_response(self.quiz_brain.check_answer("False"))



    def display_score(self):
        """Displays the score on the scoreboard UI"""
        self.score_label.config(text= f"Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")