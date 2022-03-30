#Prompt the user to input a number
userNum = int(input('Please input your number: '))

#Multiply this number by 3
timesThree = int(userNum * 3)
timesThreeDisp = print(f'{userNum:,} multiplied by 3 is {timesThree:,}')

#Add 6 to the number
addSix = int(timesThree + 6)
addSixDisp = print(f'{timesThree:,} plus 6 is {addSix:,}')

#Divide the new number by 3
divThree = int(addSix / 3)
divThreeDisp = print(f'{addSix:,} divided by 3 is {divThree:,}')

#Subtract the number from step 1 from step 4
subFinal = int(divThree - userNum)
subFinalDisp = print(f'{divThree:,} minus your original number of {userNum:,} is {subFinal:,}')