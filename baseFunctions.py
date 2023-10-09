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
    cursorPos[0] = cursorPos[0] + cursorPosDict["0"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "0"
        workingLine[cursorInlinePosition[0]] = "0"
    except:
        expressionList.append("0")
        workingLine.append("0")


def function1():
    cursorPos[0] = cursorPos[0] + cursorPosDict["1"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "1"
        workingLine[cursorInlinePosition[0]] = "1"
    except:
        expressionList.append("1")
        workingLine.append("1")


def function2():
    cursorPos[0] = cursorPos[0] + cursorPosDict["2"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "2"
        workingLine[cursorInlinePosition[0]] = "2"
    except:
        expressionList.append("2")
        workingLine.append("2")


def function3():
    cursorPos[0] = cursorPos[0] + cursorPosDict["3"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "3"
        workingLine[cursorInlinePosition[0]] = "3"
    except:
        expressionList.append("3")
        workingLine.append("3")


def function4():
    cursorPos[0] = cursorPos[0] + cursorPosDict["4"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "4"
        workingLine[cursorInlinePosition[0]] = "4"
    except:
        expressionList.append("4")
        workingLine.append("4")


def function5():
    cursorPos[0] = cursorPos[0] + cursorPosDict["5"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "5"
        workingLine[cursorInlinePosition[0]] = "5"
    except:
        expressionList.append("5")
        workingLine.append("5")


def function6():
    cursorPos[0] = cursorPos[0] + cursorPosDict["6"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "6"
        workingLine[cursorInlinePosition[0]] = "6"
    except:
        expressionList.append("6")
        workingLine.append("6")


def function7():
    cursorPos[0] = cursorPos[0] + cursorPosDict["7"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "7"
        workingLine[cursorInlinePosition[0]] = "7"
    except:
        expressionList.append("7")
        workingLine.append("7")


def function8():
    cursorPos[0] = cursorPos[0] + cursorPosDict["8"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "8"
        workingLine[cursorInlinePosition[0]] = "8"
    except:
        expressionList.append("8")
        workingLine.append("8")


def function9():
    cursorPos[0] = cursorPos[0] + cursorPosDict["9"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "9"
        workingLine[cursorInlinePosition[0]] = "9"
    except:
        expressionList.append("9")
        workingLine.append("9")


def additionFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" + "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" + ")
            workingLine.append(" + ")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" + "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append(" + ")
            workingLine.append(" + ")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" + "]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " + "
            workingLine[cursorInlinePosition[0]] = " + "
        except:
            expressionList.append(" + ")
            workingLine.append(" + ")


def subtractionFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" - "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" - ")
            workingLine.append(" - ")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" - "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("-")
            workingLine.append("-")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" - "]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " - "
            workingLine[cursorInlinePosition[0]] = " - "
        except:
            expressionList.append(" - ")
            workingLine.append(" - ")


def multiplicationFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" * "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" * ")
            workingLine.append(" * ")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" * "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append(" * ")
            workingLine.append(" * ")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" * "]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " * "
            workingLine[cursorInlinePosition[0]] = " * "
        except:
            expressionList.append(" * ")
            workingLine.append(" * ")


def divisionFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" / "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" / ")
            workingLine.append(" / ")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" / "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append(" / ")
            workingLine.append(" / ")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" / "]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " / "
            workingLine[cursorInlinePosition[0]] = " / "
        except:
            expressionList.append(" / ")
            workingLine.append(" / ")


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
    cursorInlinePosition[0] = -1
    cursor()


def commaFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict[", "]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = ", "
        workingLine[cursorInlinePosition[0]] = ", "
    except:
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
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" ** 2"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" ** 2")
            workingLine.append(" ** 2")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" ** 2"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append(" ** 2")
            workingLine.append(" ** 2")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" ** 2"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " ** 2"
            workingLine[cursorInlinePosition[0]] = " ** 2"
        except:
            expressionList.append(" ** 2")
            workingLine.append(" ** 2")


def rightParenthesesFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict[")"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = ")"
        workingLine[cursorInlinePosition[0]] = ")"
    except:
        expressionList.append(")")
        workingLine.append(")")


def leftParenthesesFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "("
        workingLine[cursorInlinePosition[0]] = "("
    except:
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
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" ** -1"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" ** -1")
            workingLine.append(" ** -1")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" ** -1"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append(" ** -1")
            workingLine.append(" ** -1")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" ** -1"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " ** -1"
            workingLine[cursorInlinePosition[0]] = " ** -1"
        except:
            expressionList.append(" ** -1")
            workingLine.append(" ** -1")


def powerFunction():
    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            expressionList.append(str(answer))
            workingLine.append(str(answer))
            cursorPos[0] = cursorPos[0] + (cursorPosDict["general"] * len(str(answer))) + cursorPosDict[" ** "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 2
            expressionList.append(" ** ")
            workingLine.append(" ** ")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict[" ** "]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append(" ** ")
            workingLine.append(" ** ")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict[" ** "]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = " ** "
            workingLine[cursorInlinePosition[0]] = " ** "
        except:
            expressionList.append(" ** ")
            workingLine.append(" ** ")


def decimalFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["."]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "."
        workingLine[cursorInlinePosition[0]] = "."
    except:
        expressionList.append(".")
        workingLine.append(".")


def logFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["log("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "log("
        workingLine[cursorInlinePosition[0]] = "log("
    except:
        expressionList.append("log(")
        workingLine.append("log(")


def lnFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["ln("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "ln("
        workingLine[cursorInlinePosition[0]] = "ln("
    except:
        expressionList.append("ln(")
        workingLine.append("ln(")


def sinFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["sin("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "sin("
        workingLine[cursorInlinePosition[0]] = "sin("
    except:
        expressionList.append("sin(")
        workingLine.append("sin(")


def cosFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["cos("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "cos("
        workingLine[cursorInlinePosition[0]] = "cos("
    except:
        expressionList.append("cos(")
        workingLine.append("cos(")


def tanFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["tan("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "tan("
        workingLine[cursorInlinePosition[0]] = "tan("
    except:
        expressionList.append("tan(")
        workingLine.append("tan(")


def negativeFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "-"
        workingLine[cursorInlinePosition[0]] = "-"
    except:
        expressionList.append("-")
        workingLine.append("-")


def variableFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["x"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "x"
        workingLine[cursorInlinePosition[0]] = "x"
    except:
        expressionList.append("x")
        workingLine.append("x")


def leftArrowFunction():
    if cursorInlinePosition[0] < 0:
        cursorPos[0] = 0
    else:
        cursorPos[0] = cursorPos[0] - cursorPosDict[workingLine[cursorInlinePosition[0]]]
        cursorInlinePosition[0] = cursorInlinePosition[0] - 1


def rightArrowFunction():
    if cursorInlinePosition[0] < len(expressionList) - 1:
        cursorPos[0] = cursorPos[0] + cursorPosDict[workingLine[cursorInlinePosition[0]]]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1