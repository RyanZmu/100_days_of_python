class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def nextQuestion(self):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_input = input(f"Q.{self.question_number}: {current_question.text} True/False?")
            self.check_answer(correct_answer=current_question.answer,user_answer=user_input)
        return


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct!\nThe Answer Was: {correct_answer}\nScore: {self.score}/{self.question_number}\n")
        else:
            print(f"Sorry, that was incorrect!\nThe Answer Was: {correct_answer}\nScore: {self.score}/{self.question_number}\n")
        return user_answer