from variables import *
import math


def secondFunction():

    """
    Switches the mode to the second mode by setting the subcommand to '2nd',
    also adds indicators(switching the cursor and appending a label to the right side of the status bar)
    """

    global rightStatusBarText
    global cursorObj
    try:
        if subcommands[0] == "2nd":
            subcommands.clear()
            rightStatusBarText.clear()
            cursorObj.clear()
            cursorObj.append("—")
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

    """
    Switches the mode to the alpha mode by setting the subcommand to 'alpha',
    also adds indicators(switching the cursor and appending a label to the right side of the status bar)
    """

    global rightStatusBarText
    global cursorObj
    try:
        if subcommands[0] == "alpha":
            subcommands.clear()
            rightStatusBarText.clear()
            cursorObj.clear()
            cursorObj.append("—")
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

    """
    Adds an addition sign to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending the addition sign.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["+"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("+")
            workingLine.append("+")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["+"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("+")
            workingLine.append("+")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["+"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "+"
            workingLine[cursorInlinePosition[0]] = "+"
        except:
            expressionList.append("+")
            workingLine.append("+")


def subtractionFunction():

    """
    Adds a subtraction sign to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending the subtraction sign.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("-")
            workingLine.append("-")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("-")
            workingLine.append("-")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "-"
            workingLine[cursorInlinePosition[0]] = "-"
        except:
            expressionList.append("-")
            workingLine.append("-")


def multiplicationFunction():

    """
    Adds a multiplication sign to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending the multiplication sign.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["*"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("*")
            workingLine.append("*")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["*"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("*")
            workingLine.append("*")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["*"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "*"
            workingLine[cursorInlinePosition[0]] = "*"
        except:
            expressionList.append("*")
            workingLine.append("*")


def divisionFunction():

    """
    Adds an division sign to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending the division sign.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["/"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("/")
            workingLine.append("/")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["/"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("/")
            workingLine.append("/")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["/"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "/"
            workingLine[cursorInlinePosition[0]] = "/"
        except:
            expressionList.append("/")
            workingLine.append("/")


def clearFunction():

    """
    Celars the appropriate variables, specifcally the ones that are storing the lines displayed on screen,
    the histroy is not deleted and can be scrolled up to by using the arrows,
    if inhistory then the line that is hovered over in deleted.
    """

    if inHistory[0] == "False":
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
        workingLineShifter[0] = 0
        cursorInlinePosition[0] = -1
        cursor()
    else:
        linePos = math.ceil(selectionBarPos[0]/2)

        resetHistories()

        answerHistory.pop(str(len(answerHistory) - linePos + 1))
        problemHistory.pop(str(len(problemHistory) - linePos + 1))

        resetHistories()

        lines.clear()
        numLines[0] = numLines[0] - 1
        for i in range(numLines[0]):
            lines.append(i + 1)

        workingLinePos[0] = workingLinePos[0] - 42
        selectionBarPos[0] = selectionBarPos[0] - 2

        if selectionBarPos[0] <= 0:
            inHistory[0] = "False"
            selectionBarPos[0] = 0



def commaFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict[","]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = ","
        workingLine[cursorInlinePosition[0]] = ","
    except:
        expressionList.append(",")
        workingLine.append(",")


def squareFunction():

    """
    Adds '**2' to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending '**2'.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["**2"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("**2")
            workingLine.append("**2")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["**2"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("**2")
            workingLine.append("**2")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["**2"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "**2"
            workingLine[cursorInlinePosition[0]] = "**2"
        except:
            expressionList.append("**2")
            workingLine.append("**2")


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

    """
    Adds '**-1' to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending '**-1'.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["**-1"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("**-1")
            workingLine.append("**-1")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["**-1"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("**-1")
            workingLine.append("**-1")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["**-1"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "**-1"
            workingLine[cursorInlinePosition[0]] = "**-1"
        except:
            expressionList.append("**-1")
            workingLine.append("**-1")


def powerFunction():

    """
    Adds '**' to the working line and other appropriate variables,
    but also checks to see if it is the first symbol in the working line in which case it checks if there is a history,
    if there is a history it appends the previous answer before appending '**'.
    """

    if not expressionList:
        try:
            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
            answer = answerHistory[answerNumber]
            for i in [*str(answer)]:
                expressionList.append(i)
                workingLine.append(i)
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
                cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            cursorPos[0] = cursorPos[0] + cursorPosDict["**"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("**")
            workingLine.append("**")
        except:
            cursorPos[0] = cursorPos[0] + cursorPosDict["**"]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
            expressionList.append("**")
            workingLine.append("**")
    else:
        cursorPos[0] = cursorPos[0] + cursorPosDict["**"]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1
        try:
            expressionList[cursorInlinePosition[0]] = "**"
            workingLine[cursorInlinePosition[0]] = "**"
        except:
            expressionList.append("**")
            workingLine.append("**")


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

    """
    Differs from subtraction function because it doesn't check for previous answer history if it's the first value in the working line.
    """

    cursorPos[0] = cursorPos[0] + cursorPosDict["-"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "-"
        workingLine[cursorInlinePosition[0]] = "-"
    except:
        expressionList.append("-")
        workingLine.append("-")


def variableFunction():
    cursorPos[0] = cursorPos[0] + cursorPosDict["X"]
    cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    try:
        expressionList[cursorInlinePosition[0]] = "X"
        workingLine[cursorInlinePosition[0]] = "X"
    except:
        expressionList.append("X")
        workingLine.append("X")


def leftArrowFunction():

    """
    If the cursor is in the very first position nothing happens,
    but if it isn't in the first position the cursors moves left by a distance that is looked up in the cursorPosDict
    """

    if cursorInlinePosition[0] < 0:
        cursorPos[0] = 0
    else:
        cursorPos[0] = cursorPos[0] - cursorPosDict[workingLine[cursorInlinePosition[0]]]
        cursorInlinePosition[0] = cursorInlinePosition[0] - 1


def rightArrowFunction():

    """
    If the cursor is in the very last position nothing happens,
    but if it isn't in the last position the cursor moves right by a distance that is looked up in the cursorPosDict
    """

    if cursorInlinePosition[0] < len(expressionList) - 1:
        cursorPos[0] = cursorPos[0] + cursorPosDict[workingLine[cursorInlinePosition[0]]]
        cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def upArrowFunction():

    """
    Moves the selection bar up if there is a history value to move onto, if there is no history above then nothing happens,
    if there is no history above on the screen but there has been a previous history that was cleared it will still move up into history
    """

    if (numLines[0] * 2) > selectionBarPos[0]:
        inHistory[0] = "True"
        selectionBarTranslation[0] = -0.5
        for i in range(len(lines)):
            selectionBarTranslation[0] = selectionBarTranslation[0] + 0.5
        selectionBarPos[0] = selectionBarPos[0] + 1
        selectionBarTranslation[0] = selectionBarTranslation[0] - (selectionBarPos[0] * 0.25)
    elif (numLines[0] * 2) == selectionBarPos[0] and len(answerHistory) > numLines[0]:
        if needSave[0] == "True":
            needSave[0] = "False"
            save[0] = lines[:]
            save[1] = workingLinePos[0]
            save[2] = numLines[0]
        inHistory[0] = "True"
        selectionBarTranslation[0] = -0.5
        for i in range(len(lines)):
            selectionBarTranslation[0] = selectionBarTranslation[0] + 0.5
        selectionBarPos[0] = selectionBarPos[0] + 1
        selectionBarTranslation[0] = selectionBarTranslation[0] - (selectionBarPos[0] * 0.25)
        numLines[0] = numLines[0] + 1
        lines.append(numLines[0])
        shouldLinesMove.append("move")
        workingLinePos[0] = workingLinePos[0] + sizeOfShift


def downArrowFunction():

    """
    Moves the selection bar down if there is a history value to move onto, if there is no history below then nothing happens,
    if there is no history below on the screen but there is history below it will still move down into history
    """

    if selectionBarPos[0] != 0:
        inHistory[0] = "True"
        selectionBarTranslation[0] = -0.5
        for i in range(len(lines)):
            selectionBarTranslation[0] = selectionBarTranslation[0] + 0.5
        selectionBarPos[0] = selectionBarPos[0] - 1
        selectionBarTranslation[0] = selectionBarTranslation[0] - (selectionBarPos[0] * 0.25)

        # Handles exiting history mode
        if selectionBarPos[0] == 0:
            firstHistoryUpdate[0] = "True"
            inHistory[0] = "False"
            cursor()


def inHistoryEvalFunction():

    """
    When the eval function is called from in history it will append whatever value or equation that is currently selected 
    to the working line and exit from inhistory.
    """

    if (selectionBarPos[0] % 2) == 1:
        answerPos = -math.ceil(selectionBarPos[0]/2)
        answer = list(answerHistory.values())[answerPos]
        answer = [*str(answer)]
        for i in answer:
            expressionList.append(i)
            workingLine.append(i)
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    else:
        problemPos = -math.ceil(selectionBarPos[0]/2)
        problem = list(problemHistory.values())[problemPos]
        problem = [*str(problem)]
        for i in problem:
            expressionList.append(i)
            workingLine.append(i)
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1
    
    # Variable cleanup
    if needSave[0] == "False":
        needSave[0] = "True"
        lines.clear()
        for i in save[0]:
            lines.append(i)
        workingLinePos[0] = save[1]
        numLines[0] = save[2]
    firstHistoryUpdate[0] = "True"
    inHistory[0] = "False"
    selectionBarPos[0] = 0