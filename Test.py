import random
import os

def generateNumberForCard(arr):
    while True:
        k = random.randint(1, 90)
        flag = True
        for i in range(len(arr)):
            if (arr[i] == k):
                flag = False;
        if flag:
            break
    return k


def generateCard():
    arr = [0] * 27
    for i in range(len(arr)):
        k = random.random()
        if (k < 0.59):
            arr[i] = generateNumberForCard(arr)
        else:
            arr[i] = 0

    return arr


def init(player, computer):
    bochenki = [0] * 90
    player = generateCard()
    computer = generateCard()
    k = 0;
    for i in range(len(bochenki)):
        bochenki[i] = i + 1


def printStep(arr1, arr2, currentBoch, ostBoch):
    print("Текущий боченок %d" % currentBoch)
    print("Боченков осталось %d" % ostBoch)

    print("=================================")
    print("==========Ваша карточка==========")
    for i in range(3):
        outputString = ""
        for j in range(9):
            if (arr1[i * 9 + j] == 0):
                outputString += "   "
            else:
                number = arr1[i * 9 + j]
                outputString += "%3d" % number
        print(outputString)

    print("=================================")
    print("=======Карточка компьютера=======")
    for i in range(3):
        outputString = ""
        for j in range(9):
            if (arr2[i * 9 + j] == 0):
                outputString += "   "
            else:
                number = arr2[i * 9 + j]
                outputString += "%3d" % number
        print(outputString)

    print("=================================")

def isOver(arr1, arr2):
    for i in range(len(arr1)):
        if not(arr1[i] == 0):
            return 1

    for i in range(len(arr2)):
        if not(arr2[i] == 0):
            return 2

    return 0

def step(a):
    while True:
        flag = True
        numb = random.randint(1, len(bochenki) - 1)
        if (bochenki[numb] == True):
            bochenki[numb] = False
            flag = False
            printStep(player, computer, numb, 90 - a)
        if not flag:
            break

bochenki = [0] * 92
player = generateCard()
computer = generateCard()
k = 0;
for i in range(len(bochenki)):
    bochenki[i] = True
bochenki[0] = False
stepNumber = 0

while (stepNumber <= 90):
    # try:
    #     os.system('clear')
    # except:
    #     os.system('cls')
    step(stepNumber)
    stepNumber += 1

print(len(bochenki))