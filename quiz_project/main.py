"""
Quiz Project!
Create a Quiz game asking the user random True or False questions
Use OOP only!
- Ask Question
- Track how many questions user has correct out of how many were asked
 - Stretch - Add percentage of correct answers
"""
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface

# Create question bank
question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# Start Quiz Brain to handle game logic
quiz = QuizBrain(question_list=question_bank)
quiz_ui = QuizInterface(quiz)

# Output final score
print(f"You have completed the quiz!\nFinal Score: {quiz.score} Correct out of {quiz.question_number} Total Questions")
