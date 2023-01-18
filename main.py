from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_no = 4
question_bank = []
for questions in question_data:
    new_q = Question(questions["text"], questions["answer"])
    question_bank.append(new_q)
    # question_text = questions["text"]
    # question_answer = questions["answer"]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. \nYour final score was: {quiz.score}/{quiz.question_number}")
