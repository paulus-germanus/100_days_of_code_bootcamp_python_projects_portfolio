import requests
import html
from question_model import Question
from quiz_brain import QuizBrain

response = requests.get(url="https://opentdb.com/api.php?amount=12&type=boolean")

question_bank = [Question(html.unescape(response.json()["results"][x]["question"]), response.json()["results"][x]["correct_answer"]) for x in range(len(response.json()["results"]))]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()