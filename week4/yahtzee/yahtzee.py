import random

class Die:
    def __init__(self, sides=6, currentFace=1):
        self.sides = sides
        self.currentFace = currentFace
    
    def roll(self):
        self.setCurrentFaceValue(random.randint(1, self.sides))

    def setCurrentFaceValue(self, roll):
        self.currentFace = roll

    def getCurrentFaceValue(self):
        return self.currentFace

    def showDieFace(self):
        print(f'({self.currentFace})', end=' ')

def rollForYahtzee():
    yahtzee = False

    for i in range(1, 6):
        globals()[f'die{i}'] = Die()
    
    for i in range(1, 6):
        globals()[f'die{i}'].roll()

    for i in range(1, 6):
        if globals()[f'die{1}'].getCurrentFaceValue() != globals()[f'die{i}'].getCurrentFaceValue():
            yahtzee = False
            break
        else:
            yahtzee = True

    if yahtzee == False:
        for i in range(1, 6):
            globals()[f'die{i}'].showDieFace()
        print()
        print('Sorry no Yahtzee yet...')
    else:
        for i in range(1, 6):
            globals()[f'die{i}'].showDieFace()
        print()
        print('YAHTZEE!')

rollForYahtzee()
