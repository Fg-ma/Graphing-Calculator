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
        for i in [*str(answer)]:
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
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
    for i in [*str(problem)]:
        cursorPos[0] = cursorPos[0] + cursorPosDict[i]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def arcsinFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["sin⁻¹("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "sin⁻¹("
        workingLine[cursorInlinePosition[0]] = "sin⁻¹("
    except:
        expressionList.append("sin⁻¹(")
        workingLine.append("sin⁻¹(")


def arccosFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["cos⁻¹("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "cos⁻¹("
        workingLine[cursorInlinePosition[0]] = "cos⁻¹("
    except:
        expressionList.append("cos⁻¹(")
        workingLine.append("cos⁻¹(")


def arctanFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["tan⁻¹("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "tan⁻¹("
        workingLine[cursorInlinePosition[0]] = "tan⁻¹("
    except:
        expressionList.append("tan⁻¹(")
        workingLine.append("tan⁻¹(")


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


def leftCurlyBracketFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["{"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "{"
        workingLine[cursorInlinePosition[0]] = "{"
    except:
        expressionList.append("{")
        workingLine.append("{")


def rightCurlyBracketFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["}"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "}"
        workingLine[cursorInlinePosition[0]] = "}"
    except:
        expressionList.append("}")
        workingLine.append("}")

    
def functionTypeLeftBracket():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["["]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "["
        workingLine[cursorInlinePosition[0]] = "["
    except:
        expressionList.append("[")
        workingLine.append("[")


def functionTypeRightBracket():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["]"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "]"
        workingLine[cursorInlinePosition[0]] = "]"
    except:
        expressionList.append("]")
        workingLine.append("]")