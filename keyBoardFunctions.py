from variables import * 
import pyperclip


def functionTypea():
    expressionList.append("a")
    workingLine.append("a")


def functionTypeb():
    expressionList.append("b")
    workingLine.append("b")


def functionTypec():
    expressionList.append("c")
    workingLine.append("c")


def functionTyped():
    expressionList.append("d")
    workingLine.append("d")


def functionTypee():
    expressionList.append("e")
    workingLine.append("e")


def functionTypef():
    expressionList.append("f")
    workingLine.append("f")


def functionTypeg():
    expressionList.append("g")
    workingLine.append("g")


def functionTypeh():
    expressionList.append("h")
    workingLine.append("h")


def functionTypei():
    expressionList.append("i")
    workingLine.append("i")


def functionTypej():
    expressionList.append("j")
    workingLine.append("j")


def functionTypek():
    expressionList.append("k")
    workingLine.append("k")


def functionTypel():
    expressionList.append("l")
    workingLine.append("l")


def functionTypem():
    expressionList.append("m")
    workingLine.append("m")


def functionTypen():
    expressionList.append("n")
    workingLine.append("n")


def functionTypeo():
    expressionList.append("o")
    workingLine.append("o")


def functionTypep():
    expressionList.append("p")
    workingLine.append("p")


def functionTypeq():
    expressionList.append("q")
    workingLine.append("q")


def functionTyper():
    expressionList.append("r")
    workingLine.append("r")


def functionTypes():
    expressionList.append("s")
    workingLine.append("s")


def functionTypet():
    expressionList.append("t")
    workingLine.append("t")


def functionTypeu():
    expressionList.append("u")
    workingLine.append("u")


def functionTypev():
    expressionList.append("v")
    workingLine.append("v")


def functionTypew():
    expressionList.append("w")
    workingLine.append("w")


def functionTypex():
    expressionList.append("x")
    workingLine.append("x")


def functionTypey():
    expressionList.append("y")
    workingLine.append("y")


def functionTypez():
    expressionList.append("z")
    workingLine.append("z")


def functionTypeA():
    expressionList.append("A")
    workingLine.append("A")


def functionTypeB():
    expressionList.append("B")
    workingLine.append("B")


def functionTypeC():
    expressionList.append("C")
    workingLine.append("C")


def functionTypeD():
    expressionList.append("D")
    workingLine.append("D")


def functionTypeE():
    expressionList.append("E")
    workingLine.append("E")


def functionTypeF():
    expressionList.append("F")
    workingLine.append("F")


def functionTypeG():
    expressionList.append("G")
    workingLine.append("G")


def functionTypeH():
    expressionList.append("H")
    workingLine.append("H")


def functionTypeI():
    expressionList.append("I")
    workingLine.append("I")


def functionTypeJ():
    expressionList.append("J")
    workingLine.append("J")


def functionTypeK():
    expressionList.append("K")
    workingLine.append("K")


def functionTypeL():
    expressionList.append("L")
    workingLine.append("L")


def functionTypeM():
    expressionList.append("M")
    workingLine.append("M")


def functionTypeN():
    expressionList.append("N")
    workingLine.append("N")


def functionTypeO():
    expressionList.append("O")
    workingLine.append("O")


def functionTypeP():
    expressionList.append("P")
    workingLine.append("P")


def functionTypeQ():
    expressionList.append("Q")
    workingLine.append("Q")


def functionTypeR():
    expressionList.append("R")
    workingLine.append("R")


def functionTypeS():
    expressionList.append("S")
    workingLine.append("S")


def functionTypeT():
    expressionList.append("T")
    workingLine.append("T")


def functionTypeU():
    expressionList.append("U")
    workingLine.append("U")


def functionTypeV():
    expressionList.append("V")
    workingLine.append("V")


def functionTypeW():
    expressionList.append("W")
    workingLine.append("W")


def functionTypeX():
    expressionList.append("X")
    workingLine.append("X")


def functionTypeY():
    expressionList.append("Y")
    workingLine.append("Y")


def functionTypeZ():
    expressionList.append("Z")
    workingLine.append("Z")


def functionTypeExclamation():
    expressionList.append("!")
    workingLine.append("!")


def functionTypeAt():
    expressionList.append("@")
    workingLine.append("@")


def functionTypeNumberSign():
    expressionList.append("#")
    workingLine.append("#")


def functionTypeDollarSign():
    expressionList.append("$")
    workingLine.append("$")


def functionTypePercent():
    expressionList.append("%")
    workingLine.append("%")


def functionTypeAmpersand():
    expressionList.append("&")
    workingLine.append("&")


def functionTypeAsterisk():
    expressionList.append("*")
    workingLine.append("*")


def functionTypeBackspace():
    try:
        expressionList.pop()
        workingLine.pop()
    except:
        pass


def functionTypeControlC():
    if workingLine == []:
        try:
            copy = list(answerHistory.items())[-1][1]
            pyperclip.copy(copy)
        except:
            pass
    else:
        copy = "".join(workingLine)
        pyperclip.copy(copy)


def functionTypeControlV():
    paste = pyperclip.paste()
    workingLine.append(paste)
    expressionList.append(paste)
    

def functionTypeControlZ():
    if workingLine == []:
        try:
            if answerHistory:
                answerHistory.popitem()
                lines.pop()
                newOldLine = problemHistory.popitem()
                expressionList.append(newOldLine[1])
                workingLine.append(newOldLine[1])
                workingLinePos[0] = workingLinePos[0] - sizeOfShift
                answerHistoryCount[0] = answerHistoryCount[0] - 1
                numLines[0] = numLines[0] - 1
        except:
            pass
    else:
        workingLine.pop()
        expressionList.pop()