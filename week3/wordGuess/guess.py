myWord = 'BASEBALL'
guesses = []
wordBoard = ['_', '_', '_', '_', '_', '_', '_', '_']
incorrect = 0
continueGame = True

def showBoard():
    while continueGame:
        print(wordBoard)
        userGuess = input('Please guess a lowercase letter for the mystery word: ').upper()

        if len(userGuess) > 1 or userGuess.isdigit():
            print('Please enter a single letter.')
        else:
            checkGuess(userGuess)

def checkGuess(let):
    global incorrect
    if incorrect < 5:
        if let in myWord:
            if let in guesses:
                print(f'You have already found the {let}(s) in the word. Guess again.')
                print(f'Your guesses: {guesses}')
            else:
                addLetter(let)
                guesses.append(let)
                print('You guessed one of the letters!')
                winGame()
        else:
            if let in guesses:
                print(f'You have already tried that letter. Guess again.')
                print(f'Your guesses: {guesses}')
            else:
                incorrect = incorrect + 1
                print('That letter is not in the word.')
                print(f'You have {5 - incorrect} chances left!')
                guesses.append(let)
    else:
        global continueGame
        continueGame = False
        print('You guessed wrong too many times! You lose!')

def addLetter(let):
    for i in range(len(myWord)):
        if myWord[i] == let:
            wordBoard[i] = let

def winGame():
    if '_' not in wordBoard:
        global continueGame
        continueGame = False
        print(wordBoard)
        print(f'Congratulations! The word was "{myWord}"! You win!')
        

showBoard()