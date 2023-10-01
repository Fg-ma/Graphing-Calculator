from variables import *
from evalFunctions import *

def evaluate():
    expression = "".join(expressionList)
    # Handles empty evaluate events
    if not expression:
        return

    # Set up variables
    global answerHistoryCount
    answerHistoryCount += 1
    problemHistory[str(answerHistoryCount)] = str(expression)
    resetEntry.append("reset")

    # openGL screen variables
    global screenUpdate
    global lines
    global numLines
    screenUpdate.append("updated")
    numLines = numLinesPlusOne()
    lines.append(numLines)
    shouldLinesMove.append("move")

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

    # Records answer history
    answerHistory[str(answerHistoryCount)] = str(ans)
    
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