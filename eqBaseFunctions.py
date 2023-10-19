from variables import *


def eqEvaluate():
    print("evaluate")


def eqFunction0():
    cursorPos[0] = cursorPos[0] + cursorPosDict["0"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "0"
    except:
        equations[str(activeFunction[0])][1].append("0")


def eqFunction1():
    cursorPos[0] = cursorPos[0] + cursorPosDict["1"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "1"
    except:
        equations[str(activeFunction[0])][1].append("1")


def eqFunction2():
    cursorPos[0] = cursorPos[0] + cursorPosDict["2"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "2"
    except:
        equations[str(activeFunction[0])][1].append("2")


def eqFunction3():
    cursorPos[0] = cursorPos[0] + cursorPosDict["3"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "3"
    except:
        equations[str(activeFunction[0])][1].append("3")


def eqFunction4():
    cursorPos[0] = cursorPos[0] + cursorPosDict["4"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "4"
    except:
        equations[str(activeFunction[0])][1].append("4")


def eqFunction5():
    cursorPos[0] = cursorPos[0] + cursorPosDict["5"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "5"
    except:
        equations[str(activeFunction[0])][1].append("5")


def eqFunction6():
    cursorPos[0] = cursorPos[0] + cursorPosDict["6"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "6"
    except:
        equations[str(activeFunction[0])][1].append("6")


def eqFunction7():
    cursorPos[0] = cursorPos[0] + cursorPosDict["7"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "7"
    except:
        equations[str(activeFunction[0])][1].append("7")


def eqFunction8():
    cursorPos[0] = cursorPos[0] + cursorPosDict["8"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "8"
    except:
        equations[str(activeFunction[0])][1].append("8")


def eqFunction9():
    cursorPos[0] = cursorPos[0] + cursorPosDict["9"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "9"
    except:
        equations[str(activeFunction[0])][1].append("9")


def eqAdditionFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["+"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "+"
    except:
        equations[str(activeFunction[0])][1].append("+")


def eqSubtractionFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "-"
    except:
        equations[str(activeFunction[0])][1].append("-")


def eqMultiplicationFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["*"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "*"
    except:
        equations[str(activeFunction[0])][1].append("*")


def eqDivisionFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["/"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "/"
    except:
        equations[str(activeFunction[0])][1].append("/")


def eqCommaFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict[","]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = ","
    except:
        equations[str(activeFunction[0])][1].append(",")


def eqSquareFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["**2"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "**2"
    except:
        equations[str(activeFunction[0])][1].append("**2")


def eqRightParenthesesFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict[")"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = ")"
    except:
        equations[str(activeFunction[0])][1].append(")")


def eqLeftParenthesesFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "("
    except:
        equations[str(activeFunction[0])][1].append("(")


def eqInverseFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["**-1"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "**-1"
    except:
        equations[str(activeFunction[0])][1].append("**-1")


def eqPowerFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["**"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "**"
    except:
        equations[str(activeFunction[0])][1].append("**")


def eqDecimalFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["."]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "."
    except:
        equations[str(activeFunction[0])][1].append(".")


def eqLogFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["log("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "log("
    except:
        equations[str(activeFunction[0])][1].append("log(")


def eqLnFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["ln("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "ln("
    except:
        equations[str(activeFunction[0])][1].append("ln(")


def eqSinFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["sin("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "sin("
    except:
        equations[str(activeFunction[0])][1].append("sin(")


def eqCosFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["cos("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "cos("
    except:
        equations[str(activeFunction[0])][1].append("cos(")


def eqTanFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["tan("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "tan("
    except:
        equations[str(activeFunction[0])][1].append("tan(")


def eqNegativeFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "-"
    except:
        equations[str(activeFunction[0])][1].append("-")


def eqVariableFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["x"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "x"
    except:
        equations[str(activeFunction[0])][1].append("x")


def eqLeftArrowFunction():
    if cursorInlinePosition[0] >= 0:
        cursorPos[0] = cursorPos[0] - cursorPosDict[equations[str(activeFunction[0])][1][cursorInlinePosition[0]]]
        cursorInlinePosition[0] = cursorInlinePosition[0] - 1
    elif cursorInlinePosition[0] == -1:
        print("wokred")
        equationsPosHorizontalShift[str(activeFunction[0])] = 0
        cursorPos[0] = 14
        for i in equations[str(activeFunction[0])][0]:
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]

def eqRightArrowFunction():
    if cursorInlinePosition[0] < len(equations[str(activeFunction[0])][1]) - 1:
        cursorPos[0] = cursorPos[0] + cursorPosDict[equations[str(activeFunction[0])][1][cursorInlinePosition[0]]]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def eqUpArrowFunction():
    if activeFunction[0] > 1:
        activeFunction[0] = activeFunction[0] - 1
        cursorPos[0] = 14
        cursorInlinePosition[0] = -1
        for i in equations[str(activeFunction[0])][0]:
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]

        equationsPosHorizontalShift[str(activeFunction[0] + 1)] = 0
        screenUpdate.append("updated")

        cursor()


def eqDownArrowFunction():
    if activeFunction[0] < 20:
        activeFunction[0] = activeFunction[0] + 1
        cursorPos[0] = 14
        cursorInlinePosition[0] = -1
        for i in equations[str(activeFunction[0])][0]:
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]

        equationsPosHorizontalShift[str(activeFunction[0] - 1)] = 0
        screenUpdate.append("updated")

        cursor()


def eqClearFunction():
    equations[str(activeFunction[0])][1] = [""]
    subcommands.clear()
    rightStatusBarText.clear()
    cursorObj.clear()
    cursorObj.append("—")
    cursorPos[0] = 14
    for i in equations[str(activeFunction[0])][0]:
        cursorPos[0] = cursorPos[0] + cursorPosDict[i]
    cursorInlinePosition[0] = -1
    cursor()