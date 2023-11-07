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
regex = r"(\(|\)|log\(|ln\(|sin\(|cos\(|tan\(|arcsin\(|arccos\(|arctan\(|√\(|sin⁻¹\(|cos⁻¹\(|tan⁻¹\(|Ans|sqrt\(|exp\()"

# History variables
answerHistory = {}
problemHistory = {}
answerHistoryCount = [0]
needSave = ["True"]
save = ["lines", "workingLinePos", "numLines"]

# Storage variables
expressionList = []
leftParentheses = []
rightParentheses = []
mainPageSave = ["lines", "workingLineShifter", "numLines", "workingLine"]

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
movebyFactor = [0]

# Status bar variables
global rightStatusBarText
statusBarTranslation = [-1.0]
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
                 ",": 4, "**2": 27, "(": 8, 
                 ")": 8, "**-1": 33, "**": 16, 
                 ".": 4, "log(": 32, "ln(": 24, 
                 "sin(": 32, "cos(": 34, "tan(": 34,
                 "A": 12, "B": 12, "C": 11, 
                 "D": 13, "E": 11, "F": 10, 
                 "G": 12, "H": 13,  "I": 6, 
                 "J": 6, "K": 12, "L": 10, 
                 "M": 16, "N": 13, "O": 12, 
                 "P": 11, "Q": 12, "R": 12, 
                 "S": 9, "T": 11, "U": 12, 
                 "V": 11, "W": 18, "X": 11, 
                 "Y": 11, "Z": 11, "a": 9, 
                 "b": 10, "c": 8, "d": 11, 
                 "e": 9, "f": 6, "g": 9, 
                 "h": 10, "i": 5, "j": 5, 
                 "k": 10, "l": 5, "m": 16, 
                 "n": 11, "o": 10, "p": 11, 
                 "q": 10, "r": 8, "s": 8, 
                 "t": 6, "u": 11, "v": 10, 
                 "w": 15, "y": 10, "x": 9, 
                 "z": 9, "!": 5, "@": 17, 
                 "#": 12, "$": 10, "%": 17, 
                 "&": 13, " ": 4, "arcsin(": 57, 
                 "arccos(": 59, "arctan(": 59, "sin⁻¹(": 48,
                 "cos⁻¹(": 50, "tan⁻¹(": 50, "π": 11, 
                 "√(": 20, "10**": 38, "⁻": 8,
                 "¹": 8, "{": 7, "}": 7,
                 "[":7 , "]": 7, "θ": 10,
                 "_": 7, ":": 5, "?": 8,
                 "\"": 7, "—": 7, "": 0,
                 "₁": 8, "₂": 8, "₃": 8,
                 "₄": 8, "₅": 8, "₆": 8,
                 "₇": 8, "₈": 8, "₉": 8,
                 "₀": 8, "=": 14, "Ans": 31,
                 "exp(": 37}
cursorPos = [0]
cursorInlinePosition = [-1]
workingLineShifter = [0]
selectionBarTranslation = [-0.5]
selectionBarPos = [0]
maxLines = [5]
inHistory = ["False"]
firstHistoryUpdate = ["True"]

# Equation Page Variables
inGraph = ["False"]
equations = {"1": ["Y₁", [""]], "2": ["Y₂", [""]], "3": ["Y₃", [""]],
             "4": ["Y₄", [""]], "5": ["Y₅", [""]], "6": ["Y₆", [""]],
             "7": ["Y₇", [""]], "8": ["Y₈", [""]], "9": ["Y₉", [""]],
             "10": ["Y₁₀", [""]], "11": ["Y₁₁", [""]], "12": ["Y₁₂", [""]],
             "13": ["Y₁₃", [""]], "14": ["Y₁₄", [""]], "15": ["Y₁₅", [""]],
             "16": ["Y₁₆", [""]], "17": ["Y₁₇", [""]], "18": ["Y₁₈", [""]],
             "19": ["Y₁₉", [""]], "20": ["Y₂₀", [""]]}
equationsPos = [0]
activeFunction = [1]
equationsPosVerticalShift = [0]
equationsPosHorizontalShift = {"1": 0, "2": 0, "3": 0,
                               "4": 0, "5": 0, "6": 0,
                               "7": 0, "8": 0, "9": 0,
                               "10": 0, "11": 0, "12": 0,
                               "13": 0, "14": 0, "15": 0,
                               "16": 0, "17": 0, "18": 0,
                               "19": 0, "20": 0}


# Display Equations Variables
xpts = []
ypts = []
colorLookUp = {"1": "orange", "2": "royalblue", "3": "red", "4": "purple", "5": "pink", 
               "6": "crimson", "7": "dimgray", "8": "darkslategray", "9": "turquoise", "10": "lawngreen",
               "11": "indianred", "12": "gold", "13": "seagreen", "14": "deeppink", "15": "darkseagreen",
               "16": "lightpink", "17": "steelblue", "18": "darkviolet", "19": "dodgerblue", "20": "tomato",}


# Dialog Variables
windowDialogStatus = ["Hidden"]
modeDialogStatus = ["Hidden"]


# Window Dialog Varibles
lowerXLimit = [-10]
upperXLimit = [10]
xScale = [1]
lowerYLimit = [-10]
upperYLimit = [10]
yScale = [1]


# Mode Dialog Variables
modeStates = {
    "degradState": "rad"
}


# Joins the list into a displayable value
def getRightStatusBarText():
    return "".join(rightStatusBarText)


# Handles blinking cursor object
def cursor():
    if inHistory[0] == "False":
        if cursorHolder[0] == "":
            cursorHolder.clear()
            cursorHolder.append(cursorObj[0])
        else: 
            cursorHolder.clear()
            cursorHolder.append("")
    else:
        cursorHolder.clear()
        cursorHolder.append("")


# Resets selection bat
def drawSelectionBarRest():
    selectionBarTranslation[0] = -0.5
    for i in range(len(lines)):
        selectionBarTranslation[0] = selectionBarTranslation[0] + 0.5
    selectionBarTranslation[0] = selectionBarTranslation[0] - (selectionBarPos[0] * 0.25)


# Resets answer and problem histories
def resetHistories():
    answers = list(answerHistory.values())
    problems = list(problemHistory.values())

    answerHistory.clear()
    problemHistory.clear()
    
    for i in range(len(answers)):
        answerHistory[str(i + 1)] = answers[i]
        problemHistory[str(i + 1)] = problems[i]