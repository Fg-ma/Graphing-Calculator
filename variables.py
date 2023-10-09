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
                 "9": 11, "0": 11, " + ": 22, 
                 " - ": 14, " * ": 16, " / ": 17,
                 ", ": 8, " ** 2": 35, "(": 8, 
                 ")": 8, " ** -1": 41, " ** ": 24, 
                 ".": 4, "log(": 32, "ln(": 24, 
                 "sin(": 32, "cos(": 34, "tan(": 34, 
                 "-": 8,
                 "A": 0, "B": 0, "C": 11,
                 "D": 0, "E":11, "F": 0,
                 "G": 0, "H": 0, "I": 0,
                 "I": 0, "J": 0, "K": 0,
                 "L": 0, "M": 0, "N": 0,
                 "O": 0, "P": 11, "Q": 0,
                 "R": 0, "S": 0, "T": 11,
                 "U": 0, "V": 11, "W": 0,
                 "X": 11, "Y": 0, "Z": 0,}
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
