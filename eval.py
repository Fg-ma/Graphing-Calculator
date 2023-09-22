from evalVars import *
from variables import *
from evalFunctions import *

def evaluate():
    # Gets expression
    global expressionString
    expressionString = ''.join(expressionList)
    expression = expressionString

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
        print("simp no para")
        ans = solver(expression)
    elif isFourFunction[0] == "True" and parentheses[0] == "True":
        print("simp with para")
        # Closes parentheses first
        expression = closeParentheses(expression)
        ans = solver(expression)
    else:
        print("not simp with para")
        # Closes parentheses
        if parentheses[0] == "True":
            expression = closeParentheses(expression)

        expression = simplifyExpression(expression)
        ans = solver(expression)
          
    # Records answer history
    answerHistory[str(answerHistoryCount)] = str(ans)

    # Regular cleanup
    expressionList.clear()
    workingLine.clear()
    expressionString = ""
    expression = ""

    # Conditional cleanup
    isFourFunction[0] = "True"
    parentheses[0] = "False"
    trig[0] = "False"
    logs[0] = "False"
    sin[0] = "False"
    cos[0] = "False"
    tan[0] = "False"
    inverseSin[0] = "False"
    inverseCos[0] = "False"
    inverseTan[0] = "False"
    log[0] = "False"
    ln[0] = "False"
    e[0] = "False"


def solver(expression):
    try:
        ans = eval(expression)
    except:
        ans = "Error"
    return ans