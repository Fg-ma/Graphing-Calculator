from variables import *


def secondResets():
    subcommands.clear()
    rightStatusBarText.clear()
    cursorObj.clear()
    cursorObj.append("—")
    cursor()


def eqArcsinFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["sin⁻¹("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "sin⁻¹("
    except:
        equations[str(activeFunction[0])][1].append("sin⁻¹(")


def eqArccosFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["cos⁻¹("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "cos⁻¹("
    except:
        equations[str(activeFunction[0])][1].append("cos⁻¹(")


def eqArctanFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["tan⁻¹("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "tan⁻¹("
    except:
        equations[str(activeFunction[0])][1].append("tan⁻¹(")


def eqPiFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["π"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "π"
    except:
        equations[str(activeFunction[0])][1].append("π")


def eqSquareRootFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["√("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "√("
    except:
        equations[str(activeFunction[0])][1].append("√(")

    
def eqExponentialFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["exp("]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "exp("
    except:
        equations[str(activeFunction[0])][1].append("exp(")


def eqScientificNotationFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["e"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "e"
    except:
        equations[str(activeFunction[0])][1].append("e")


def eqTentotheFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["10**"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "10**"
    except:
        equations[str(activeFunction[0])][1].append("10**")


def eqLeftCurlyBracketFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["{"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "{"
    except:
        equations[str(activeFunction[0])][1].append("{")


def eqRightCurlyBracketFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["}"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "}"
    except:
        equations[str(activeFunction[0])][1].append("}")

    
def eqLeftBracketFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["["]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "["
    except:
        equations[str(activeFunction[0])][1].append("[")


def eqRightBracketFunction():
    secondResets()
    cursorPos[0] = cursorPos[0] + cursorPosDict["]"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        equations[str(activeFunction[0])][1][cursorInlinePosition[0]] = "]"
    except:
        equations[str(activeFunction[0])][1].append("]")