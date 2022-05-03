import random

class TriviaQuestion():
    def __init__(self, question, category, difficulty, correct_answer, incorrect_answers, id):
        self.question = question
        self.category = category
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.incorrect_answers = []
        self.id = id

    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def getDifficulty(self):
        return self.difficulty

    def getCorrectAnswer(self):
        return self.correct_answer

    def getIncorrectAnswers(self):
        return self.incorrect_answers

    def getShuffledAnswers(self):
        shuffledAnswers = []

        for answer in self.incorrect_answers:
            shuffledAnswers.append(answer)
        
        shuffledAnswers.append(self.correct_answer)

        return random.shuffle(shuffledAnswers)