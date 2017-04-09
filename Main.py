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
        if (k < 0.582):
            arr[i] = generateNumberForCard(arr)
        else:
            arr[i] = 0

    return arr


def init():
    bochenki = [0] * 90
    player = generateCard()
    computer = generateCard()
    k = 0;
    for i in range(len(bochenki)):
        bochenki[i] = i + 1


def printStep(arr1, arr2, currentBoch, ostBoch):
    print("Текущий боченок: %s" % str(currentBoch))
    print("Боченков осталось: %s" % str(ostBoch))

    print("=================================")
    print("==========Ваша карточка==========")
    for i in range(3):
        outputString = ""
        for j in range(9):
            if (arr1[i * 9 + j] == 0):
                outputString += "   "
            elif (arr1[i * 9 + j] == -1):
                outputString += " --"
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
            elif (arr2[i * 9 + j] == -1):
                outputString += " --"
            else:
                number = arr2[i * 9 + j]
                outputString += "%3d" % number
        print(outputString)

    print("=================================")


def isOver(arr1, arr2):
    player_win = True
    computer_win = True

    for i in range(len(arr1)):
        if (arr1[i] >= 1):
            player_win = False
            break

    for i in range(len(arr2)):
        if (arr2[i] >= 1):
            computer_win = False
            break

    if (player_win):
        return 1
    elif (computer_win):
        return 2
    else:
        return 0


def exist(arr, number):
    for i in range(len(arr)):
        if (arr[i] == number):
            return True
    return False


def checkplayerstep(answer, exist, number):
    if ((answer == "y" or answer == "н") and exist):
        index = player.index(number)
        player[index] = -1
        return True
    if ((answer == "n" or answer == "т") and (not exist)):
        return True
    return False


def makecomputerstep(exist, number, arr):
    if (exist):
        arr[arr.index(number)] = -1


def step(a):
    while True:
        flag = True
        numb = random.randint(1, len(bochenki) - 1)
        if (bochenki[numb] == True): #Если боченок до этого не использовался
            bochenki[numb] = False #Ставим его использованным
            flag = False
            printStep(player, computer, numb, 90 - a)
            makecomputerstep(exist(computer, numb), numb, computer)
            # makecomputerstep(exist(player, numb), numb, player) #Debug
            # return True # Debug
            while True:
                answer = str(input("Хотите ли вы зачеркнуть данный боченок на вашей карточке?[y/n]: "))
                if ((answer == "y") or (answer == "н") or (answer == "т") or (answer == "n")):
                    break

            if (checkplayerstep(answer, exist(player, numb), numb)):
                return True
            else:
                return False

        if not flag:
            break



bochenki = [0] * 91
player = generateCard()
computer = generateCard()
k = 0;
for i in range(len(bochenki)):
    bochenki[i] = True
bochenki[0] = False
stepNumber = 1
who_win = 0

while (stepNumber <= 90):
    try:
        os.system('clear')
    except:
        os.system('cls')

    if not(step(stepNumber)):
        print("Вы ошиблись! Игра окончена! Компьютер победил");
        break

    over = isOver(player, computer)
    if (over == 1):
        printStep(player, computer, "--", "--")
        print("Поздравляю! Вы победили!")
        break
    elif (over == 2):
        printStep(player, computer, "--", "--")
        print("К сожалению, компьютер оказался сильнее")
        break

    stepNumber += 1