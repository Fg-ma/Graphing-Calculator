from variables import *
from PyQt5.QtWidgets import QMainWindow


def secondFunction():
    global rightStatusBarText
    global cursorObj
    try:
        if subcommands[0] == "2nd":
            subcommands.clear()
            rightStatusBarText.clear()
            cursorObj.clear()
            cursorObj.append("|")
        else:
            subcommands.clear()
            rightStatusBarText.clear()
            subcommands.append("2nd")
            rightStatusBarText.append("2")
            rightStatusBarText.append("n")
            rightStatusBarText.append("d")
            cursorObj.clear()
            cursorObj.append("^")
    except:
        subcommands.clear()
        rightStatusBarText.clear()
        subcommands.append("2nd")
        rightStatusBarText.append("2")
        rightStatusBarText.append("n")
        rightStatusBarText.append("d")
        cursorObj.clear()
        cursorObj.append("^")
    cursor()


def alphaFunction():
    global rightStatusBarText
    global cursorObj
    try:
        if subcommands[0] == "alpha":
            subcommands.clear()
            rightStatusBarText.clear()
            cursorObj.clear()
            cursorObj.append("|")
        else:
            subcommands.clear()
            rightStatusBarText.clear()
            subcommands.append("alpha")
            rightStatusBarText.append("A")
            rightStatusBarText.append("l")
            rightStatusBarText.append("p")
            rightStatusBarText.append("h")
            rightStatusBarText.append("a")
            cursorObj.clear()
            cursorObj.append("α")
    except:
        subcommands.clear()
        rightStatusBarText.clear()
        subcommands.append("alpha")
        rightStatusBarText.append("A")
        rightStatusBarText.append("l")
        rightStatusBarText.append("p")
        rightStatusBarText.append("h")
        rightStatusBarText.append("a")
        cursorObj.clear()
        cursorObj.append("α")
    cursor()


def function0():
    try:
        expressionList[cursorInlinePosition[0]] = "0"
        workingLine[cursorInlinePosition[0]] = "0"
    except:
        expressionList.append("0")
        workingLine.append("0")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function1():
    try:
        expressionList[cursorInlinePosition[0]] = "1"
        workingLine[cursorInlinePosition[0]] = "1"
    except:
        expressionList.append("1")
        workingLine.append("1")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function2():
    try:
        expressionList[cursorInlinePosition[0]] = "2"
        workingLine[cursorInlinePosition[0]] = "2"
    except:
        expressionList.append("2")
        workingLine.append("2")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function3():
    try:
        expressionList[cursorInlinePosition[0]] = "3"
        workingLine[cursorInlinePosition[0]] = "3"
    except:
        expressionList.append("3")
        workingLine.append("3")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function4():
    try:
        expressionList[cursorInlinePosition[0]] = "4"
        workingLine[cursorInlinePosition[0]] = "4"
    except:
        expressionList.append("4")
        workingLine.append("4")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function5():
    try:
        expressionList[cursorInlinePosition[0]] = "5"
        workingLine[cursorInlinePosition[0]] = "5"
    except:
        expressionList.append("5")
        workingLine.append("5")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function6():
    try:
        expressionList[cursorInlinePosition[0]] = "6"
        workingLine[cursorInlinePosition[0]] = "6"
    except:
        expressionList.append("6")
        workingLine.append("6")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function7():
    try:
        expressionList[cursorInlinePosition[0]] = "7"
        workingLine[cursorInlinePosition[0]] = "7"
    except:
        expressionList.append("7")
        workingLine.append("7")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function8():
    try:
        expressionList[cursorInlinePosition[0]] = "8"
        workingLine[cursorInlinePosition[0]] = "8"
    except:
        expressionList.append("8")
        workingLine.append("8")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def function9():
    try:
        expressionList[cursorInlinePosition[0]] = "9"
        workingLine[cursorInlinePosition[0]] = "9"
    except:
        expressionList.append("9")
        workingLine.append("9")
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def additionFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" + ")
            workingLine.append(" + ")
            cursorPos[0] = cursorPos[0] + (cursorShift[0] * len(str(answer))) + cursorAdditionShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
        except:
            expressionList.append(" + ")
            workingLine.append(" + ")
            cursorPos[0] = cursorPos[0] + cursorAdditionShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    else:
        try:
            expressionList[cursorInlinePosition[0]] = " + "
            workingLine[cursorInlinePosition[0]] = " + "
        except:
            expressionList.append(" + ")
            workingLine.append(" + ")
        cursorPos[0] = cursorPos[0] + cursorAdditionShift[0]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def subtractionFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" - ")
            workingLine.append(" - ")
            cursorPos[0] = cursorPos[0] + (cursorShift[0] * len(str(answer))) + cursorSubtractionShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
        except:
            expressionList.append("-")
            workingLine.append("-")
            cursorPos[0] = cursorPos[0] + cursorSubtractionShift[0] - 8
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    else:
        try:
            expressionList[cursorInlinePosition[0]] = " - "
            workingLine[cursorInlinePosition[0]] = " - "
        except:
            expressionList.append(" - ")
            workingLine.append(" - ")
        cursorPos[0] = cursorPos[0] + cursorSubtractionShift[0]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def multiplicationFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" * ")
            workingLine.append(" * ")
            cursorPos[0] = cursorPos[0] + (cursorShift[0] * len(str(answer))) + cursorMultiplicationShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
        except:
            expressionList.append(" * ")
            workingLine.append(" * ")
            cursorPos[0] = cursorPos[0] + cursorMultiplicationShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    else:
        try:
            expressionList[cursorInlinePosition[0]] = " * "
            workingLine[cursorInlinePosition[0]] = " * "
        except:
            expressionList.append(" * ")
            workingLine.append(" * ")
        cursorPos[0] = cursorPos[0] + cursorMultiplicationShift[0]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def divisionFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" / ")
            workingLine.append(" / ")
            cursorPos[0] = cursorPos[0] + (cursorShift[0] * len(str(answer))) + cursorDivisonShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
        except:
            expressionList.append(" / ")
            workingLine.append(" / ")
            cursorPos[0] = cursorPos[0] + cursorDivisonShift[0]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    else:
        try:
            expressionList[cursorInlinePosition[0]] = " / "
            workingLine[cursorInlinePosition[0]] = " / "
        except:
            expressionList.append(" / ")
            workingLine.append(" / ")
        cursorPos[0] = cursorPos[0] + cursorDivisonShift[0]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def clearFunction():
    if workingLine == []:
        lines.clear()
        workingLinePos[0] = 44
        numLines[0] = 0
    expressionList.clear()
    workingLine.clear()
    subcommands.clear()
    rightStatusBarText.clear()
    cursorObj.clear()
    cursorObj.append("—")
    cursorPos[0] = 0
    cursor()


def commaFunction():
    expressionList.append(", ")
    workingLine.append(", ")


def squareFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" ** 2 ")
            workingLine.append(" ** 2 ")
        except:
            expressionList.append(" ** 2 ")
            workingLine.append(" ** 2 ")
    else:
        expressionList.append(" ** 2 ")
        workingLine.append(" ** 2 ")


def rightParenthesesFunction():
    expressionList.append(")")
    workingLine.append(")")


def leftParenthesesFunction():
    expressionList.append("(")
    workingLine.append("(")


def inverseFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" ** -1 ")
            workingLine.append(" ** -1 ")
        except:
            expressionList.append(" ** -1 ")
            workingLine.append(" ** -1 ")
    else:
        expressionList.append(" ** -1 ")
        workingLine.append(" ** -1 ")


def powerFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            expressionList.append(" ** ")
            workingLine.append(" ** ")
        except:
            expressionList.append(" ** ")
            workingLine.append(" ** ")
    else:
        expressionList.append(" ** ")
        workingLine.append(" ** ")


def decimalFunction():
    expressionList.append(".")
    workingLine.append(".")


def logFunction():
    expressionList.append("log(")
    workingLine.append("log(")


def lnFunction():
    expressionList.append("ln(")
    workingLine.append("ln(")


def sinFunction():
    expressionList.append("sin(")
    workingLine.append("sin(")


def cosFunction():
    expressionList.append("cos(")
    workingLine.append("cos(")


def tanFunction():
    expressionList.append("tan(")
    workingLine.append("tan(")


def negativeFunction():
    expressionList.append("-")
    workingLine.append("-")


def variableFunction():
    expressionList.append("x")
    workingLine.append("x")


def leftArrowFunction():
    cursorPos[0] = cursorPos[0] - cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] - 1

def rightArrowFunction():
    cursorPos[0] = cursorPos[0] + cursorShift[0]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1