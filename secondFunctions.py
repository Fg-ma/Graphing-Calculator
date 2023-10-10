from variables import *
from main import *
import re


def secondResets():
    subcommands.clear()
    rightStatusBarText.clear()
    cursorObj.clear()
    cursorObj.append("—")
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
    cursorPos[0] = cursorPos[0] + cursorPosDict["arcsin("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "arcsin("
        workingLine[cursorInlinePosition[0]] = "arcsin("
    except:
        expressionList.append("arcsin(")
        workingLine.append("arcsin(")


def arccosFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["arccos("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "arccos("
        workingLine[cursorInlinePosition[0]] = "arccos("
    except:
        expressionList.append("arccos(")
        workingLine.append("arccos(")


def arctanFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["arctan("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "arctan("
        workingLine[cursorInlinePosition[0]] = "arctan("
    except:
        expressionList.append("arctan(")
        workingLine.append("arctan(")


def piFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["π"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "π"
        workingLine[cursorInlinePosition[0]] = "π"
    except:
        expressionList.append("π")
        workingLine.append("π")


def squareRootFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["√("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "√("
        workingLine[cursorInlinePosition[0]] = "√("
    except:
        expressionList.append("√(")
        workingLine.append("√(")


def scientificNotationFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["e"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "e"
        workingLine[cursorInlinePosition[0]] = "e"
    except:
        expressionList.append("e")
        workingLine.append("e")


def tentotheFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["10**"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "10**"
        workingLine[cursorInlinePosition[0]] = "10**"
    except:
        expressionList.append("10**")
        workingLine.append("10**")