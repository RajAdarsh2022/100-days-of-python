from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for _ in question_data:
    q_text = _["question"]
    q_answer = _["correct_answer"]
    question_bank.append(Question(q_text , q_answer))

# print(len(question_bank))
# print(question_bank)
quiz = QuizBrain(question_bank)
quiz.play_quiz()