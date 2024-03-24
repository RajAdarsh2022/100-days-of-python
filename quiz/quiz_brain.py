class QuizBrain():
    def __init__(self, question_set):
        self.question_set = question_set
        self.current_question_index = 0
        self.score = 0

    
    def ask_current_question(self):
        current_question = self.question_set[self.current_question_index]
        self.current_question_index += 1
        question_text = current_question.text
        question_answer = current_question.answer
        user_res = input(f"Q. {self.current_question_index}: {question_text}? (True/False) : ")
        return [user_res , question_answer]
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")


    
    def play_quiz(self):
        for _ in range(len(self.question_set)):
            response = self.ask_current_question()
            self.check_answer(response[0], response[1])
            print(f"Your current score is {self.score}/{self.current_question_index}")
        print("You have completed the quiz!")
        print(f"Your final score is {self.score}/{self.current_question_index}")
