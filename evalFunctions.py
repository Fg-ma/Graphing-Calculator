from evalVars import *
from variables import *


def simplifyExpression(expression):
    global firstTrigger
    global occ
    global regex
    global remainingTriggers
    # Closes open parenthesis
    fetchParenthesisLists(expression)
    while not len(leftParenthesis) == len(rightParenthesis):
        expression = expression + ")"
        fetchParenthesisLists(expression)

    # Searches for key words
    regex = r"(log\(|ln\(|\(|\))"
    occ = re.finditer(regex, expression)

    remainingTriggers = []

    for trig in occ:
        remainingTriggers.append(trig.group())

    # While there are still key words it keeps checking through them for thr inner most and solving its way out
    while remainingTriggers:
        try:
            subexpression = expression[firstTriggerPos[1]:firstTriggerEndingPos[0]]
            subocc = re.finditer(regex, subexpression)
        except:
            pass

        if firstSimpIter[0] == "True":
            firstSimpIter[0] = "False"
            rootExpressionSearch(expression)
        else:
            rootExpressionSearch(subexpression)

        subexpression = expression[firstTriggerPos[1]:firstTriggerEndingPos[0]]
        subocc = re.finditer(regex, subexpression)

        remainingTriggers = []
        for trigger in subocc:
            remainingTriggers.append(trigger.group())
        
        if not remainingTriggers:
            simpleAns = eval(subexpression)
            if firstTrigger[1] == "log(":
                simplified = evalLog(simpleAns)

            expression = expression[:firstTriggerPos[0]] + str(simplified) + expression[firstTriggerEndingPos[0]+1:]

            subocc = re.finditer(regex, expression)
            for trigger in subocc:
                remainingTriggers.append(trigger.group())
    return expression
    

def rootExpressionSearch(expression):
    firstTrigger[0] = "True"
    openpars = 0
    search = re.finditer(regex, expression)
    for trigger in search:
        if trigger.group() == ")":
            openpars = openpars - 1
        elif trigger.group() == "(":
            openpars = openpars + 1
        else:
            if firstTrigger[0] == "True":
                firstTrigger[0] = "False"
                firstTrigger.append(trigger.group())
                firstTriggerPos.append(trigger.span()[0])
                firstTriggerPos.append(trigger.span()[1])
            openpars = openpars + 1

        if openpars == 0:
            firstTriggerEndingPos.append(trigger.span()[0])
            return



def closeParentheses(expression):
    fetchParenthesisLists(expression)
    while not len(leftParenthesis) == len(rightParenthesis):
        if len(leftParenthesis) < len(rightParenthesis):
            expression = "(" + expression
        elif len(leftParenthesis) > len(rightParenthesis):
            expression = expression + ")"
        fetchParenthesisLists(expression)
    return expression


def evalSin(expression):
    pass


def evalCos(expression):
    pass


def evalTan(expression):
    pass


def evalInverseSin(expression):
    pass


def evalInverseCos(expression):
    pass


def evalInverseTan(expression):
    pass


import re
import math

def evalLog(simpleAns):
    return math.log(simpleAns, 10)
    


def evalLn(expression):
    pass


def evalE(expression):
    pass








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