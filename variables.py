isFourFunction = ["True"]
onlyParentheses = ["True"]

firstTrigger = ["True", ""]
openpars = 0
firstSimpIter = ["True"]
firstTriggerPos = []
firstTriggerEndingPos = []
firstTriggerPosShifter = 0
domainError = ["False"]

# Key word search
regex = r"(\(|\)|log\(|ln\(|sin\(|cos\(|tan\(|arcsin\(|arccos\(|arctan\(|√\()"

# History variables
answerHistory = {}
problemHistory = {}
answerHistoryCount = [0]

# Storage variables
expressionList = []
leftParentheses = []
rightParentheses = []

# Count variables
position = 0
entryCount = []

# Conditionals
screenUpdate = []
shouldLinesMove = []
global subcommands
subcommands = []
resetEntry = []

# OpenGL
global lines
global workingLine
workingLine = []
numLines = [0]
lines = []
dots = "..................................................................................."
workingLinePos = [44]
sizeOfShift = 42

# Status bar variables
global rightStatusBarText
statusBarTranslation = -1.0
leftStatusBarText = ["Place Holder"]
rightStatusBarText = []
rightStatusBarPosition = 0

# Cursor variables
cursorObj = ["—"]
cursorHolder = ["—"]
cursorPosDict = {"general": 11, "1": 11, "2": 11,
                 "3": 11, "4": 11, "5": 11,
                 "6": 11, "7": 11, "8": 11,
                 "9": 11, "0": 11, "+": 14, 
                 "-": 6, "*": 8, "/": 9,
                 ", ": 8, "**2": 27, "(": 8, 
                 ")": 8, "**-1": 33, "**": 16, 
                 ".": 4, "log(": 32, "ln(": 24, 
                 "sin(": 32, "cos(": 34, "tan(": 34, 
                 "-": 8, "A": 12, "B": 12, 
                 "C": 11, "D": 13, "E": 11, 
                 "F": 10, "G": 12, "H": 13, 
                 "I": 6, "J": 6, "K": 12,
                 "L": 10, "M": 16, "N": 13,
                 "O": 12, "P": 11, "Q": 12,
                 "R": 12, "S": 9, "T": 11,
                 "U": 12, "V": 11, "W": 18,
                 "X": 11, "Y": 11, "Z": 11,
                 "a": 9, "b": 10, "c": 8,
                 "d": 11, "e": 9, "f": 6,
                 "g": 9, "h": 10, "i": 5,
                 "j": 5, "k": 10, "l": 5,
                 "m": 16, "n": 11, "o": 10,
                 "p": 11, "q": 10, "r": 8,
                 "s": 8, "t": 6, "u": 11,
                 "v": 10, "w": 15, "y": 10,
                 "x": 9, "z": 9, "!": 5,
                 "@": 17, "#": 12, "$": 10,
                 "%": 17, "&": 13, " ": 4,
                 "arcsin(": 57, "arccos(": 59, "arctan(": 59,
                 "π": 11, "√(": 20, "10**": 38}

cursorPos = [0]
cursorInlinePosition = [-1]
cursorUpperShift1 = [11]


# Joins the list into a displayable value
def getRightStatusBarText():
    return "".join(rightStatusBarText)


# Handles blinking cursor object
def cursor():
    global cursorObj
    if cursorHolder[0] == "":
        cursorHolder.clear()
        cursorHolder.append(cursorObj[0])
    else: 
        cursorHolder.clear()
        cursorHolder.append("")
