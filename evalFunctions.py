from variables import *
import re
import math


def simplifyExpression(expression):

    """
    Searches for triggers(sin,cos, tan, exp, ...) in the inputted expression,
    then sends them to be evaluated and tranformed into simple numbers working from the inside out. 
    """

    global firstTrigger
    global occ
    global regex
    global remainingTriggers
    global firstTriggerPosShifter
    # Closes open Parentheses
    fetchParenthesesLists(expression)
    while not len(leftParentheses) == len(rightParentheses):
        expression = expression + ")"
        fetchParenthesesLists(expression)

    # Searches for key words
    occ = re.finditer(regex, expression)

    remainingTriggers = []

    for trig in occ:
        remainingTriggers.append(trig.group())

        # Gets rid of and Ans keywords
        if trig.group() == "Ans":
            remainingTriggers.pop()
            simplified = evalAns()
            expression = expression[:trig.span()[0]] + str(simplified) + expression[trig.span()[1]:]


    # While there are still trigger words it keeps checking through them for thr inner most and solving its way out
    while remainingTriggers and domainError[0] == "False":
        # Handles the first iteration where there is no subexpression yet, then sends the subexpression through every other time
        if firstSimpIter[0] == "True":
            firstSimpIter[0] = "False"
            expressionSearch(expression)
        else:
            expressionSearch(subexpression)

        # Gets the subexpression using the position of the triggers in subexpression
        subexpression = expression[firstTriggerPos[1]+firstTriggerPosShifter:firstTriggerPos[1]+firstTriggerPosShifter+abs(firstTriggerEndingPos[0]-firstTriggerPos[1])]

        # An object(suboccurance) that contains all the information about the triggers
        subocc = re.finditer(regex, subexpression)

        # Creates a list of remaining triggers
        remainingTriggers.clear()
        for trigger in subocc:
            remainingTriggers.append(trigger.group())

        # If there aren't anymore trigger then it simplifies whatever is the resulting simple subexpression then
        # solves for whatever kind of trigger it is. Finally it splices the answer back into the expression
        if not remainingTriggers:
            # Evaluates the simple subexpression
            simpleAns = eval(subexpression)
            
            #Specific trigger functions
            if firstTrigger[1] == "(":
                simplified = eval(str(simpleAns))
            elif firstTrigger[1] == "log(":
                simplified = evalLog(simpleAns)
            elif firstTrigger[1] == "ln(":
                simplified = evalLn(simpleAns)
            elif firstTrigger[1] == "sin(":
                simplified = evalSin(simpleAns)
            elif firstTrigger[1] == "cos(":
                simplified = evalCos(simpleAns)
            elif firstTrigger[1] == "tan(":
                simplified = evalTan(simpleAns)
            elif firstTrigger[1] == "arcsin(" or firstTrigger[1] == "sin⁻¹(":
                simplified = evalArcSin(simpleAns)
            elif firstTrigger[1] == "arccos(" or firstTrigger[1] == "cos⁻¹(":
                simplified = evalArcCos(simpleAns)
            elif firstTrigger[1] == "arctan(" or firstTrigger[1] == "tan⁻¹(":
                simplified = evalArcTan(simpleAns)
            elif firstTrigger[1] == "√(" or firstTrigger[1] == "sqrt(":
                simplified = evalSquareRoot(simpleAns)
            elif firstTrigger[1] == "exp(":
                simplified = evalExponential(simpleAns)

            # Splicing into the string
            expression = expression[:firstTriggerPos[0]+firstTriggerPosShifter] + str(simplified) + expression[firstTriggerPos[0]+firstTriggerPosShifter+abs(firstTriggerEndingPos[0]-firstTriggerPos[0])+1:]
            # Gets the object to be check for anymore triggers
            subocc = re.finditer(regex, expression)

            # Checks for remaining triggers in the expression
            remainingTriggers.clear()
            for trigger in subocc:
                remainingTriggers.append(trigger.group())

            # Clean up
            firstSimpIter[0] = "True"
            firstTriggerPosShifter = 0
        else:
            # Adds to the shifter(used to locate the trigger in the original string)
            firstTriggerPosShifter += firstTriggerPos[1]

    # Clean up            
    firstTriggerPosShifter = 0
    onlyParentheses[0] = "True"
    return expression
    

def expressionSearch(expression):

    """
    Searched for triggers in an inputted expression then returns the first trigger it comes across.
    Returns the first trigger in the firstTrigger array which contains vital information like the position of the parenthesis that closes the function.
    """

    # Variable rest
    firstTrigger[0] = "True"
    firstTriggerPos.clear()
    firstTriggerEndingPos.clear()
    openpars = 0

    # Gets and object containing all of the triggers
    search = re.finditer(regex, expression)

    # Searches the triggers to find the outer most one
    for trigger in search:
        # If the tigger is ")" then subtracts one from an open Parentheses counter(openpars)
        # if the trigger is anything else it adds one to openpars
        # when openpars = 0 then the outermost function has been found
        if trigger.group() == ")":
            openpars = openpars - 1
        elif trigger.group() == "(" and firstTrigger[0] == "False":
            openpars = openpars + 1
        else:
            if firstTrigger[0] == "True":
                firstTrigger[0] = "False"
                firstTrigger[1] = trigger.group()
                firstTriggerPos.append(trigger.span()[0])
                firstTriggerPos.append(trigger.span()[1])
            openpars = openpars + 1

        if openpars == 0:
            firstTriggerEndingPos.append(trigger.span()[0])
            return
    return


def closeParentheses(expression):

    """
    Adds parentheses to the beginning or the end of an expression based on the inequality of parenthesis balance.
    """

    fetchParenthesesLists(expression)
    while not len(leftParentheses) == len(rightParentheses):
        if len(leftParentheses) < len(rightParentheses):
            expression = "(" + expression
        elif len(leftParentheses) > len(rightParentheses):
            expression = expression + ")"
        fetchParenthesesLists(expression)
    return expression


def fetchParenthesesLists(expression):

    """
    Gets the positions of all the parentheses in a given expression and stores them in two arrays.
    """

    global position
    global leftParentheses
    global rightParentheses

    leftParentheses.clear()
    rightParentheses.clear()
    position = 0

    for character in expression:
        if character == "(":
            leftParentheses.append(position)
        elif character == ")":
            rightParentheses.append(position)

        position += 1


def evalSin(simpleExpression):
    if inGraph[0] == "False":
        if modeStates["degradState"] == "deg":
            return math.sin(math.radians(simpleExpression))
        elif modeStates["degradState"] == "rad":
            return math.sin(simpleExpression)
    elif inGraph[0] == "True":
        return math.sin(simpleExpression)


def evalCos(simpleExpression):
    if inGraph[0] == "False":
        if modeStates["degradState"] == "deg":
            return math.cos(math.radians(simpleExpression))
        elif modeStates["degradState"] == "rad":
            return math.cos(simpleExpression)
    elif inGraph[0] == "True":
        return math.cos(simpleExpression)


def evalTan(simpleExpression):
    if inGraph[0] == "False":
        if modeStates["degradState"] == "deg":
            return math.tan(math.radians(simpleExpression))
        elif modeStates["degradState"] == "rad":
            return math.tan(simpleExpression)
    elif inGraph[0] == "True":
        return math.tan(simpleExpression)


def evalArcSin(simpleExpression):
    try:
        if inGraph[0] == "False":
            if modeStates["degradState"] == "deg":
                return math.asin(math.radians(simpleExpression))
            elif modeStates["degradState"] == "rad":
                return math.asin(simpleExpression)
        elif inGraph[0] == "True":
            return math.asin(simpleExpression)
    except:
        domainError[0] = "True"
        return "Domain Error"


def evalArcCos(simpleExpression):
    try:
        if inGraph[0] == "False":
            if modeStates["degradState"] == "deg":
                return math.acos(math.radians(simpleExpression))
            elif modeStates["degradState"] == "rad":
                return math.acos(simpleExpression)
        elif inGraph[0] == "True":
            return math.acos(simpleExpression)
    except:
        domainError[0] = "True"
        return "Domain Error"


def evalArcTan(simpleExpression):
    try:
        if inGraph[0] == "False":
            if modeStates["degradState"] == "deg":
                return math.atan(math.radians(simpleExpression))
            elif modeStates["degradState"] == "rad":
                return math.atan(simpleExpression)
        elif inGraph[0] == "True":
            return math.atan(simpleExpression)
    except:
        domainError[0] = "True"
        return "Domain Error"


def evalLog(simpleExpression):
    try:
        ans = math.log(simpleExpression, 10)
    except:
        domainError[0] = "True"
        ans = "Domain Error"
    return ans
    

def evalLn(simpleExpression):
    try:
        ans = math.log(simpleExpression)
    except:
        domainError[0] = "True"
        ans = "Domain Error"
    return ans


def evalSquareRoot(simpleExpression):
    try:
        ans = math.sqrt(simpleExpression)
    except:
        domainError[0] = "True"
        ans = "Domain Error"
    return ans


def evalExponential(simpleExpression):
    return math.exp(simpleExpression)


def evalAns():
    try:
        lastAnswerHistoryKey = list(answerHistory) [-1]
        answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - 1]
        ans = answerHistory[answerNumber]
    except:
        ans = "Error"
    return ans
