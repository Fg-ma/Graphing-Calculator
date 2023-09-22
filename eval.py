from vars import *
from evalFunctions import *

def evaluate():
    # Gets expression
    expression = ''.join(expressionList)

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

    # Check if the expression is a basic four function expression
    if trig[0] == "True" or logs[0] == "True":
        isFourFunction[0] = "False"
    
    # If expression is four function then runs standard eval()
    # If parentheses are involved it send to evalParentheses()
    # If no parentheses then goes to simplifyExpresion()
    if isFourFunction[0] == "True" and parentheses[0] == "False":
        ans = solver(expression)
    elif isFourFunction[0] == "True" and parentheses[0] == "True":
        # Closes parentheses first
        expression = closeParentheses(expression)
        ans = solver(expression)
    else:
        # Closes parentheses
        if parentheses[0] == "True":
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
    parentheses[0] = "False"
    trig[0] = "False"
    logs[0] = "False"


def solver(expression):
    try:
        ans = eval(expression)
    except:
        ans = "Error"
    return ans