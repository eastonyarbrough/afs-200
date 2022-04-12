import random
rolledDie = []

class Die:
    def __init__(self, sides, currentFace):
        self.sides = sides
        self.currentFace = currentFace
    
    def roll(self):
        self.getCurrentFaceValue(random.randint(1, self.sides))

    def getCurrentFaceValue(self, roll):
        self.currentFace = roll

    def showDieFace(self):
        return self.currentFace

def rollForYahtzee():
    ctrlList = [1, 2, 3, 4, 5]
    yahtzee = False

    for i in ctrlList:
        globals()[f'die{i}'] = Die(6, 1)
    
    for i in ctrlList:
        globals()[f'die{i}'].roll()
        rolledDie.append(globals()[f'die{i}'].showDieFace())

    for rolls in rolledDie:
        if rolledDie[0] != rolls:
            yahtzee = False
            break
        else:
            yahtzee = True

    if yahtzee == False:
        for num in rolledDie:
            print(f'({num})', end=' ')
        print()
        print('Sorry no Yahtzee yet...')
    else:
        for num in rolledDie:
            print(f'({num})', end=' ')
        print()
        print('YAHTZEE!')

rollForYahtzee()
