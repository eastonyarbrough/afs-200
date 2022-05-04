import requests
import triviaquestion

class TriviaGame():
    def __init__(self):
        self.all_questions = []

    def getAllQuestions(self):
        return self.all_questions

    def getMultipleChoice(self, category_id, num_questions, difficulty):
        URL = f'https://opentdb.com/api.php?amount={num_questions}&category={category_id}&difficulty={difficulty}&type=multiple'

        try:
            response = requests.get(URL, timeout=5)
            response.raise_for_status()
            response_JSON = response.json()
            returned_questions = response_JSON
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

        count = 0

        for questions in returned_questions['results']:
            newQuestion = questions['question']
            newCategory = questions['category']
            newDifficulty = questions['difficulty']
            newCorrect_answer = questions['correct_answer']
            newIncorrect_answers = questions['incorrect_answers']

            count = count + 1

            newTriviaQuestion = triviaquestion.TriviaQuestion(newQuestion, newCategory, newDifficulty, newCorrect_answer, newIncorrect_answers, count)
            self.all_questions.append(newTriviaQuestion)

myGame = TriviaGame()
myGame.getMultipleChoice(15, 10, 'medium')
myGameQuestions = myGame.getAllQuestions()

for question in myGameQuestions:
    print(question.question)
