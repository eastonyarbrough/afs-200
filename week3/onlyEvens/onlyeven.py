#Prompt the user to enter a positive number. Verify that the input is an integer and it is positive.
def getNum():
    continueCheck = True

    while continueCheck:
        userNum = input('Please enter a positive number: ')

        if userNum.isdigit():
            countdownEvens(int(userNum)+1)
            continueCheck = False
        else:
            print('Invalid entry please try again.')

#Create a function that displays only even numbers between and including 0 up to and including (if valid) the number provided by the user.
def countdownEvens(num):
    for even in range(num):
        if even % 2 == 0:
            print(even)

getNum()