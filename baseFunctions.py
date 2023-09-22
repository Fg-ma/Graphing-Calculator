from variables import *
from evalVars import *
from enterFunctions import *


def function0():
    expressionList.append("0")
    workingLine.append("0")


def function1():
    expressionList.append("1")
    workingLine.append("1")


def function2():
    expressionList.append("2")
    workingLine.append("2")


def function3():
    expressionList.append("3")
    workingLine.append("3")


def function4():
    expressionList.append("4")
    workingLine.append("4")


def function5():
    expressionList.append("5")
    workingLine.append("5")


def function6():
    expressionList.append("6")
    workingLine.append("6")


def function7():
    expressionList.append("7")
    workingLine.append("7")


def function8():
    expressionList.append("8")
    workingLine.append("8")


def function9():
    expressionList.append("9")
    workingLine.append("9")


def additionFunction():
    expressionList.append(" + ")
    workingLine.append("+")


def subtractionFunction():
    expressionList.append(" - ")
    workingLine.append("-")


def multiplicationFunction():
    expressionList.append(" * ")
    workingLine.append("*")


def divisionFunction():
    expressionList.append(" / ")
    workingLine.append("/")


def clearFunction():
    if workingLine == []:
        lines.clear()
        workingLinePos[0] = 44
        clearNumLines()
    expressionList.clear()
    workingLine.clear()


def commaFunction():
    expressionList.append(", ")
    workingLine.append(",")


def squareFunction():
    expressionList.append(" ** 2")


def rightParenthesisFunction():
    parentheses[0] = "True"
    expressionList.append(")")
    workingLine.append(")")


def leftParenthesisFunction():
    parentheses[0] = "True"
    expressionList.append("(")
    workingLine.append("(")


def inverseFunction():
    expressionList.append(" ** -1")
    workingLine.append(" ** -1")


def powerFunction():
    expressionList.append(" ** ")
    workingLine.append(" ** ")


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


def decimalFunction():
    expressionList.append(".")
    workingLine.append(".")


def logFunction():
    expressionList.append("log(")
    workingLine.append("log(")
    logs[0] = "True"
    log[0] = "True"


def lnFunction():
    expressionList.append("ln(")
    workingLine.append("ln(")