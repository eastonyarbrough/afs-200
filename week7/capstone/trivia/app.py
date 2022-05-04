from flask import Flask, request, render_template
import triviagame

app = Flask(__name__)

myGame = triviagame.TriviaGame()
myGame.getMultipleChoice(15, 1, 'medium')

@app.route("/", methods=['GET'])
def home():
    return render_template('questions.html', questions=myGame.getAllQuestions())

@app.route("/score", methods=['POST'])
def score():
    user_answer = request.form.get('1')
    return render_template('answers.html', answers=myGame.getAllQuestions(), userAnswer=user_answer)