from variables import *
from evalFunctions import *

def evaluate():
    expression = "".join(expressionList)
    # Handles empty evaluate events
    if not expression:
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
    cursorInlinePosition[0] = 0

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

    sciDist = 9

    if ans > 0:
        print("worked")
        if ans > 999999999:
            ans = f"{ans:.9e}"
        elif ans < 0.00000001:
            ans = f"{ans:.9e}"
    elif ans < 0:
        if ans < -999999999:
            ans = f"{ans:.9e}"
        elif ans > -0.00000001:
            ans = f"{ans:.9e}"

    # Records answer history
    answerHistory[str(answerHistoryCount[0])] = str(ans)
    
    # Regular cleanup
    expressionList.clear()
    workingLine.clear()
    expression = ""

    # Conditional cleanup
    isFourFunction[0] = "True"

def solver(expression):
    try:
        ans = eval(expression)
    except:
        ans = "Error"
    return ans