from variables import *
from main import *
import re


def secondResets():
    subcommands.clear()
    rightStatusBarText.clear()
    cursorObj.clear()
    cursorObj.append("|")
    cursor()


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

    # Searches for key words
    occ = re.finditer(regex, problem)

    remainingTriggers = []

    for trig in occ:
        remainingTriggers.append(trig.group())

    if remainingTriggers:
        isFourFunction[0] = "False"


    expressionList.append(problem)
    workingLine.append(problem)


def arcsinFunction():
    secondResets()
    expressionList.append("arcsin(")
    workingLine.append("arcsin(")


def arccosFunction():
    secondResets()
    expressionList.append("arccos(")
    workingLine.append("arccos(")


def arctanFunction():
    secondResets()
    expressionList.append("arctan(")
    workingLine.append("arctan(")


def piFunction():
    secondResets()
    expressionList.append("π")
    workingLine.append("π")


def squareRootFunction():
    secondResets()
    expressionList.append("√(")
    workingLine.append("√(")


def scientificNotationFunction():
    secondResets()
    expressionList.append("e")
    workingLine.append("e")


def tentotheFunction():
    secondResets()
    expressionList.append("10 ** ")
    workingLine.append("10 ** ")