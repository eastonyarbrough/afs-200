from flask import Flask, request, render_template
import triviagame

app = Flask(__name__)

myGame = triviagame.TriviaGame()
myGame.getMultipleChoice(15, 10, 'medium')

@app.route("/", methods=['GET'])
def home():
    return render_template('questions.html', questions=myGame.getAllQuestions())

@app.route("/score", methods=['POST'])
def score():
    correct = []
    incorrect = []
    for question in myGame.getAllQuestions():
        if (request.form.get(str(question.getID())) == question.getCorrectAnswer()):
            correct.append(question)
        else:
            incorrect.append(question)
    return render_template('answers.html', answers=myGame.getAllQuestions(), correctQuestions = correct, incorrectQuestions = incorrect)