from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Dummy data for flags and countries
flags = {
    "Germany": "germany.png",
    "France": "france.png",
    "Italy": "italy.png",
    # Add more flags and countries as needed
}

class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    country, flag = random.choice(list(flags.items()))
    options = list(flags.keys())
    random.shuffle(options)
    quiz_question = Quiz(f"What country does this flag belong to?", options, country)

    if request.method == 'POST':
        user_answer = request.form['answer']
        if quiz_question.check_answer(user_answer):
            return jsonify({"result": "correct"})
        else:
            return jsonify({"result": "incorrect"})

    return render_template('quiz.html', flag=flag, question=quiz_question.question, options=quiz_question.options)

if __name__ == '__main__':
    app.run(debug=True)
