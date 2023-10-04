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
regex = r"(\(|\)|log\(|ln\(|sin\(|cos\(|tan\(|arcsin\(|arccos\(|arctan\()"

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
cursorObj = ["|"]
cursorHolder = []


# Clear numLines
def clearNumLines():
    global numLines
    numLines = 0
    return None


# Joins the list into a displayable value
def getRightStatusBarText():
    return "".join(rightStatusBarText)


# Handles blinking cursor object
def cursor():
    global cursorObj
    if cursorHolder == []:
        cursorHolder.append(cursorObj[0])
    else: 
        cursorHolder.clear()
