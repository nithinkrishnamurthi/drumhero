from flask import Flask, render_template
from .agent import get_question
import random


app = Flask(__name__)

@app.route("/")
def main():
    question_data = get_question(100)
    questions = [question_data['correct']] + question_data['incorrect']
    random.shuffle(questions)
    question_data['shuffled_questions'] = questions
    return render_template('base_template.html', question_data=question_data)