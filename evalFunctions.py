from sysVars import *
import re
import math


# Simplifies complex expressions into expressions with numbers and basic functions
def simplifyExpression(expression):
    global firstTrigger
    global occ
    global regex
    global remainingTriggers
    global firstTriggerPosShifter
    # Closes open parenthesis
    fetchParenthesisLists(expression)
    while not len(leftParenthesis) == len(rightParenthesis):
        expression = expression + ")"
        fetchParenthesisLists(expression)

    # What triggers to search for
    regex = r"(\(|\)|log\(|ln\(|sin\(|cos\(|tan\(|arcsin\(|arccos\(|arctan\()"

    # Searches for key words
    occ = re.finditer(regex, expression)

    remainingTriggers = []

    for trig in occ:
        remainingTriggers.append(trig.group())

    # While there are still trigger words it keeps checking through them for thr inner most and solving its way out
    while remainingTriggers and domainError[0] == "False":
        # Handles the first iteration where there is no subexpression yet, then sends the subexpression through every other time
        if firstSimpIter[0] == "True":
            firstSimpIter[0] = "False"
            expressionSearch(expression)
        else:
            expressionSearch(subexpression)


        # Gets the subexpression useing the position of the triggers in 
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
            if firstTrigger[1] == "log(":
                simplified = evalLog(simpleAns)
            elif firstTrigger[1] == "ln(":
                simplified = evalLn(simpleAns)
            elif firstTrigger[1] == "sin(":
                simplified = evalSin(simpleAns)
            elif firstTrigger[1] == "cos(":
                simplified = evalCos(simpleAns)
            elif firstTrigger[1] == "tan(":
                simplified = evalTan(simpleAns)
            elif firstTrigger[1] == "arcsin(":
                simplified = evalArcSin(simpleAns)
            elif firstTrigger[1] == "arccos(":
                simplified = evalArcCos(simpleAns)
            elif firstTrigger[1] == "arctan(":
                simplified = evalArcTan(simpleAns)

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
    return expression
    

# Finds the outermost complex function and returns information about it
def expressionSearch(expression):
    # Variable rest
    firstTrigger[0] = "True"
    firstTriggerPos.clear()
    firstTriggerEndingPos.clear()
    openpars = 0

    # Gets and object containing all of the triggers
    search = re.finditer(regex, expression)

    # Searches the triggers to find the outer most one
    for trigger in search:
        # If the tigger is ")" then subtracts one from an open parenthesis counter(openpars)
        # if the trigger is anything else it adds one to openpars
        # when openpars = 0 then the outermost function has been found
        if trigger.group() == ")":
            openpars = openpars - 1
        elif trigger.group() == "(":
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


# Closes any open parenthesis so it doesn't break program
def closeParentheses(expression):
    fetchParenthesisLists(expression)
    while not len(leftParenthesis) == len(rightParenthesis):
        if len(leftParenthesis) < len(rightParenthesis):
            expression = "(" + expression
        elif len(leftParenthesis) > len(rightParenthesis):
            expression = expression + ")"
        fetchParenthesisLists(expression)
    return expression


# Gets a list of parenthesis to be used in checking that they are closed
def fetchParenthesisLists(expression):
    global position
    global leftParenthesis
    global rightParenthesis

    leftParenthesis.clear()
    rightParenthesis.clear()
    position = 0

    for character in expression:
        if character == "(":
            leftParenthesis.append(position)
        elif character == ")":
            rightParenthesis.append(position)

        position += 1


def evalSin(simpleExpression):
    return math.sin(simpleExpression)


def evalCos(simpleExpression):
    return math.cos(simpleExpression)


def evalTan(simpleExpression):
    return math.tan(simpleExpression) 


def evalArcSin(simpleExpression):
    try:
        ans = math.asin(simpleExpression)
    except:
        domainError[0] = "True"
        ans = "Domain Error"
    return ans 


def evalArcCos(simpleExpression):
    try:
        ans = math.acos(simpleExpression)
    except:
        domainError[0] = "True"
        ans = "Domain Error"
    return ans 


def evalArcTan(simpleExpression):
    try:
        ans = math.atan(simpleExpression)
    except:
        domainError[0] = "True"
        ans = "Domain Error"
    return ans


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


def evalE(simpleExpression):
    pass

