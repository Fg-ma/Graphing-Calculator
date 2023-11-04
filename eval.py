from variables import *
from evalFunctions import *
from secondFunctions import entryFunction

def evaluate():

    """
    Gets expression from expression list,
    adds to the answer and problem history,
    closes any excess parentheses,
    simplies the expression to simple number(ex. sin(0)=>0),
    checks for any errors while simplifying(such as domain errors),
    solves simplified expression and returns a single numeric answer,
    expresses answers that are too long in scientific notation.
    """

    expression = "".join(expressionList)
    # Handles empty evaluate events
    if not expression:
        entryFunction()
        return

    # Set up variables
    global answerHistoryCount
    answerHistoryCount[0] = answerHistoryCount[0] + 1
    problemHistory[str(answerHistoryCount[0])] = str(expression)
    resetEntry.append("reset")

    # openGL screen variables
    global screenUpdate
    global lines
    global numLines
    screenUpdate.append("updated")
    numLines[0] = numLines[0] + 1
    lines.append(numLines[0])
    shouldLinesMove.append("move")
    cursorPos[0] = 0
    workingLineShifter[0] = 0
    cursorInlinePosition[0] = -1

    # Closes any open parentheses
    expression = closeParentheses(expression)

    # Gets simplified expression
    expression = simplifyExpression(expression)

    # Checks for domain errors
    if domainError[0] == "False":
        ans = solver(expression)
    else:
        ans = "Domain Error"
        domainError[0] = "False"

    if ans > 0:
        if ans > 999999:
            ans = f"{ans:.6e}"
        elif ans < 0.000001:
            ans = f"{ans:.6e}"
    elif ans < 0:
        if ans < -999999:
            ans = f"{ans:.5e}"
        elif ans > -0.000001:
            ans = f"{ans:.5e}"
    if len(str(ans)) > 12:
        ans = float(str(ans)[:12])

    # Records answer history
    answerHistory[str(answerHistoryCount[0])] = str(ans)
    
    # Regular cleanup
    expressionList.clear()
    workingLine.clear()
    expression = ""

    # Conditional cleanup
    isFourFunction[0] = "True"


def solver(expression):

    """
    Can only handle simple four function calculations and returns a single number. 
    """

    try:
        return eval(expression)
    except:
        return "Error"


def functionEvaluator(expression):
    
    """
    Closes parentheses then simplifies equation and finally returns a single answer if there are no errors.
    Only used to send a range of values into when getting points to plot functions on the equation page.
    """

    expression = closeParentheses(expression)

    expression = simplifyExpression(expression)

    if domainError[0] == "False":
        ans = solver(expression)
    else:
        ans = "Domain Error"
        domainError[0] = "False"

    return ans