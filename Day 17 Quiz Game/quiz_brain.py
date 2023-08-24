class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False
            print("You've completed the quiz.")
            print(f"Your final score is: {self.score}/12.")


    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)? ").lower()
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You've got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number+1}.\n")