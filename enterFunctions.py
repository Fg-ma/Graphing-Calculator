from variables import *
import re


# Main evaluation function
def evaluate():
    # Set up variables
    global expressionString
    global answerHistoryCount
    answerHistoryCount += 1
    expressionString = ''.join(expressionList)
    problemHistory[str(answerHistoryCount)] = str(expressionString)
    resetEntry.append("reset")

    # openGL screen variables
    global screenUpdate
    global lines
    global numLines
    screenUpdate.append("updated")
    numLines = numLinesPlusOne()
    lines.append(numLines)
    shouldLinesMove.append("move")

    # Gets parenthesis if there are any
    fetchParenthesisLists(expressionString)

    # Handles parenthesis
    if areThereParenthesis != []:
        while not leftParenthesis == [] or not rightParenthesis == []:
            # Handles open parenthesis
            expressionString = checkNotClosedParenthesis(expressionString)

            # Finds the correct inner most parenthesis to evalutae first
            leftInnerMostParenthesis = leftParenthesis[-1]
            totalParenthesis = leftParenthesis + rightParenthesis
            totalParenthesis.sort()
            indexLeftInnerMostParenthesis = totalParenthesis.index(leftInnerMostParenthesis)
            endIndex = totalParenthesis[(indexLeftInnerMostParenthesis + 1)]
            startSlice = int(leftInnerMostParenthesis)
            endSlice = endIndex + 1
            substring = expressionString[(startSlice+1):(endSlice-1)]
            if areThereLogs == []:
                subanswer = expressionsWithoutParenthesis(substring)
            elif areThereLogs != []:
                    logsolver(substring)
            else:
                subanswer = expressionsWithoutParenthesis(substring)
            expressionString = expressionString[:startSlice] + str(subanswer) + expressionString[endSlice:]
            # gets positions of parenthesis
            fetchParenthesisLists(expressionString)
        expressionString = expressionsWithoutParenthesis(expressionString)
        areThereLogs.clear()

    # Handles logs
    if areThereLogs != []:
        cleanedExpression = logsolver(expressionString)
        expressionString = expressionsWithoutParenthesis(cleanedExpression)

    # Handles all simple expressions
    if areThereParenthesis == [] and areThereLogs == []:
        expressionString = expressionsWithoutParenthesis(expressionString)

    answerHistory[str(answerHistoryCount)] = str(expressionString)

    # Cleanup
    expressionList.clear()
    expressionString = ""
    position = 0
    workingLine.clear()
    areThereParenthesis.clear()
    areThereLogs.clear()


# gets positions of parenthesis
def fetchParenthesisLists(expressionString):
    global position
    global leftParenthesis
    global rightParenthesis

    leftParenthesis.clear()
    rightParenthesis.clear()
    position = 0

    for character in expressionString:
        if character == "(":
            leftParenthesis.append(position)
        elif character == ")":
            rightParenthesis.append(position)

        position += 1

# Handles open parenthesis
def checkNotClosedParenthesis(expressionString):
    if leftParenthesis == [] and not rightParenthesis == []:
        expressionString = "(" + expressionString
        fetchParenthesisLists(expressionString)
    if not leftParenthesis == [] and rightParenthesis == []:
        expressionString = expressionString + ")"
        fetchParenthesisLists(expressionString)
    return expressionString


# Handles logs
def logsolver(evaluationString):
    fetchParenthesisLists(evaluationString)
    print(evaluationString)
    while evaluationString.find("log(") != None:
        pass
        



# Handles expressions without parenthesis
def expressionsWithoutParenthesis(evaluationString):
    global simpleExpression
    for character in evaluationString:
        if character in simpleExpressions:
            pass
        else:
            simpleExpression = False

    if simpleExpression == True:
        try:
            ans = eval(evaluationString)
        except:
            ans = "Error"
        return ans
    
    if simpleExpression == False:
        simpleExpression = True
        return None
