from variables import *


def ansFunction():
    secondResets()

    try:
        lastAnswerHistoryKey = list(answerHistory) [-1]
        answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
        answer = answerHistory[answerNumber]
        expressionList.append(str(answer))
        workingLine.append(str(answer))
    except:
        pass


def entryFunction():
    secondResets()

    if resetEntry != []:
        resetEntry.clear()
        entryCount.clear()
    
    entryCount.append("1")

    try:
        lastProblemHistoryKey = list(problemHistory) [-1]
        problemNumber = list(problemHistory) [int(lastProblemHistoryKey) - len(entryCount)]

        if int(problemNumber) < 1:
            problemNumber = "1"

        problem = problemHistory[problemNumber]
    except:
        problem = ""


    expressionList.clear()
    workingLine.clear()

    expressionList.append(problem)
    workingLine.append(problem)


def secondResets():
    subcommands.clear()
    rightStatusBarText.clear()
    cursorObj.clear()
    cursorObj.append("|")
    cursor()