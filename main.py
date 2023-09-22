import sys
from PyQt5.uic import loadUi
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtOpenGL import *
from PyQt5 import QtCore, QtWidgets, QtOpenGL
from baseFunctions import *
from eval import *
from evalFunctions import *
from alphaFunctions import *
from secondFunctions import *
from vars import *
import math


# Program mainwindow
class MainWindowUI(QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()

        loadUi("calculator.ui", self)

        # opengl widget
        self.openglwidget = glWidget()
        self.openGLScreenLayout.addWidget(self.openglwidget)

        # Main window timer
        timer = QtCore.QTimer(self)
        timer.setInterval(20)
        timer.timeout.connect(self.openglwidget.updateGL)
        timer.timeout.connect(checkScreenUpdate)
        timer.start()

        # Cursor blink timer
        Ctimer = QtCore.QTimer(self)
        Ctimer.setInterval(500)
        Ctimer.timeout.connect(cursor)
        Ctimer.start()
        
        self.resizeEvent = self.onResize

    def onResize(self, event):
        resizedHeight = self.height()
        windowHeightChange = 870 - resizedHeight
        global statusBarTranslation
        statusBarTranslation = -1.0 - (windowHeightChange * .0069)
        # Get rightStatusBarText length
        self.openglwidget.rightStatusBarLength()

    
def functions():
    # baseFunctions, secondFunctions, and alphaFunctions
    if subcommands == []:
        reconnectReset(ui.Number0.clicked, function0)
        reconnectReset(ui.Number1.clicked, function1)
        reconnectReset(ui.Number2.clicked, function2)
        reconnectReset(ui.Number3.clicked, function3)
        reconnectReset(ui.Number4.clicked, function4)
        reconnectReset(ui.Number5.clicked, function5)
        reconnectReset(ui.Number6.clicked, function6)
        reconnectReset(ui.Number7.clicked, function7)
        reconnectReset(ui.Number8.clicked, function8)
        reconnectReset(ui.Number9.clicked, function9)
        reconnectReset(ui.additionButton.clicked, additionFunction)
        reconnectReset(ui.subtractionButton.clicked, subtractionFunction)
        reconnectReset(ui.multiplicationButton.clicked, multiplicationFunction)
        reconnectReset(ui.divisionButton.clicked, divisionFunction)
        reconnectReset(ui.enterButton.clicked, evaluate)
        reconnectReset(ui.rightParenthesisButton.clicked, rightParenthesisFunction)
        reconnectReset(ui.leftParenthesisButton.clicked, leftParenthesisFunction)
        reconnectReset(ui.commaButton.clicked, commaFunction)
        reconnectReset(ui.squareButton.clicked, squareFunction)
        reconnectReset(ui.logButton.clicked, logFunction)
        reconnectReset(ui.lnButton.clicked, lnFunction)
        reconnectReset(ui.powerButton.clicked, powerFunction)
        reconnectReset(ui.tanButton.clicked, tanFunction)
        reconnectReset(ui.cosButton.clicked, cosFunction)
        reconnectReset(ui.sinButton.clicked, sinFunction)
        reconnectReset(ui.inverseButton.clicked, inverseFunction)
        reconnectReset(ui.clearButton.clicked, clearFunction)
        reconnectReset(ui.secondButton.clicked, secondFunction)
        reconnectReset(ui.alphaButton.clicked, alphaFunction)
        reconnectReset(ui.decimalButton.clicked, decimalFunction)
        reconnectReset(ui.negativeButton.clicked, negativeFunction)
    elif subcommands == ["2nd"]:
        reconnectReset(ui.negativeButton.clicked, ansFunction)
        reconnectReset(ui.enterButton.clicked, entryFunction)
        reconnectReset(ui.sinButton.clicked, arcsinFunction)
        reconnectReset(ui.cosButton.clicked, arccosFunction)
        reconnectReset(ui.tanButton.clicked, arctanFunction)
        reconnectReset(ui.powerButton.clicked, piFunction)
    elif subcommands == ["alpha"]:
        reconnectReset(ui.mathButton.clicked, functionA)
        reconnectReset(ui.appsButton.clicked, functionB)
        reconnectReset(ui.programButton.clicked, functionC)
        reconnectReset(ui.inverseButton.clicked, functionD)
        reconnectReset(ui.sinButton.clicked, functionE)
        reconnectReset(ui.cosButton.clicked, functionF)
        reconnectReset(ui.tanButton.clicked, functionG)
        reconnectReset(ui.powerButton.clicked, functionH)
        reconnectReset(ui.squareButton.clicked, functionI)
        reconnectReset(ui.commaButton.clicked, functionJ)
        reconnectReset(ui.leftParenthesisButton.clicked, functionK)
        reconnectReset(ui.rightParenthesisButton.clicked, functionL)
        reconnectReset(ui.divisionButton.clicked, functionM)
        reconnectReset(ui.logButton.clicked, functionN)
        reconnectReset(ui.Number7.clicked, functionO)
        reconnectReset(ui.Number8.clicked, functionP)
        reconnectReset(ui.Number9.clicked, functionQ)
        reconnectReset(ui.multiplicationButton.clicked, functionR)
        reconnectReset(ui.lnButton.clicked, functionS)
        reconnectReset(ui.Number4.clicked, functionT)
        reconnectReset(ui.Number5.clicked, functionU)
        reconnectReset(ui.Number6.clicked, functionV)
        reconnectReset(ui.subtractionButton.clicked, functionW)
        reconnectReset(ui.Number1.clicked, functionY)
        reconnectReset(ui.stoButton.clicked, functionX)
        reconnectReset(ui.Number2.clicked, functionZ)


# Swaps function reference for buttons and connects a reference to resetFunction
def reconnectReset(signal, newhandler=None, oldhandler=None):        
    try:
        if oldhandler is not None:
            while True:
                signal.disconnect(oldhandler)
        else:
            signal.disconnect()
    except TypeError:
        pass
    if newhandler is not None:
        signal.connect(newhandler)
        signal.connect(restFunction)


# Swaps function reference for buttons
def reconnect(signal, newhandler=None, oldhandler=None):        
    try:
        if oldhandler is not None:
            while True:
                signal.disconnect(oldhandler)
        else:
            signal.disconnect()
    except TypeError:
        pass
    if newhandler is not None:
        signal.connect(newhandler)


# Updates what functions are called when swapping from base functions to alpha to 2nd
def restFunction():
    functions()

        
class glWidget(QGLWidget):
    # Intial parameters
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(352, 250)

        # Intialize status bar variables
        global leftStatusBarText
        global rightStatusBarText
        leftStatusBarText = "".join(leftStatusBarText)
        rightStatusBarText = getRightStatusBarText()


    # Continuously redraws screen
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.draw_ui()

        # Updates dot line length when the screen changes sizes
        self.dotLenght()

        # Draws status bar
        self.drawStatusBar()


    # More parameters on intialization
    def initializeGL(self):
        glClearColor(0.945, 0.945, 0.945, 0.0)
        glClearDepth(1.0)              
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                    
        gluPerspective(45.0,1.33,0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW)


    # Handles what is drawn
    def draw_ui(self):
        global workingLine
        glUseProgram(0)

        # Font color
        glColor3f(0.2, 0.2, 0.2)

        # Font style
        self.setFont(QFont("Cambria Math", 14))

        # Compile lines into strings
        inputLine = "".join(workingLine)
        try:
            inputLine += cursorHolder[0]
        except:
            pass

        # Draws working line
        self.renderText(8, workingLinePos[0], inputLine)

        # Handles lines display answer history by referencing where the workingLine is
        for line in lines:
            lastProblemHistoryKey = list(problemHistory) [-1]
            problemNumber = list(problemHistory) [int(lastProblemHistoryKey) - line]
            problem = problemHistory[problemNumber]
            self.renderText(8, workingLinePos[0]-(line*42), problem)

            lastAnswerHistoryKey = list(answerHistory) [-1]
            answerNumber = list(answerHistory) [int(lastAnswerHistoryKey) - line]
            answer = answerHistory[answerNumber]
            rightAnsPosition = self.rightAnsLength(answer)
            self.renderText(rightAnsPosition, 20+(workingLinePos[0]-(line*42)), answer)

            self.renderText(0, 26+(workingLinePos[0]-((len(lines)-line+1)*42)), dots)


    # Handles calculating length of the dotted lines seperating answers
    def dotLenght(self):
        global dots
        screenWidth = self.width()
        numDots = math.ceil(screenWidth / 4)
        dots = ""
        for dot in range(numDots):
            dots += "."


    # Handles changing the position of the workingLine when there is a change
    def changingWorkingLines(self):
        global workingLinePos
        global maxWorkingLinePos
        maxWorkingLinePos = self.height() - 12
        if lines == []:
            workingLinePos[0] = 22
        else:
            if shouldLinesMove != []:
                workingLinePos[0] = workingLinePos[0] + sizeOfShift
        if workingLinePos[0] > (maxWorkingLinePos):
             workingLinePos[0] = maxWorkingLinePos

        shouldLinesMove.clear()


    # Get rightStatusBarText length
    def rightStatusBarLength(self):
        global rightStatusBarPosition
        movebyFactor = len(rightStatusBarText) * 7
        rightStatusBarPosition = self.width() - 20 - movebyFactor
    

    # Draws status bar
    def drawStatusBar(self):
        global leftStatusBarText
        global rightStatusBarText

        # Handles status bar
        glTranslatef(-5.0, statusBarTranslation, -5.5)
        glColor3f(0.2, 0.2, 0.2)
        glPolygonMode(GL_FRONT, GL_FILL)
        glRectf(1.0, 0.4, self.width(), 1.0)
        glFlush()

        # Handles status bar text
        glColor3f(0.945, 0.945, 0.945)
        self.rightStatusBarLength()
        leftStatusBarText = "".join(leftStatusBarText)
        rightStatusBarText = getRightStatusBarText()
        self.renderText(8, 18, leftStatusBarText)
        self.renderText(rightStatusBarPosition, 18, rightStatusBarText)


    # Gets rightAnsLength length
    def rightAnsLength(self, answer):
        movebyFactor = len(answer) * 11
        for symbol in answer:
            if symbol == "-":
                movebyFactor = movebyFactor - 5
        rightAnsPosition = self.width() - 10 - movebyFactor
        return rightAnsPosition


# Updates values on OpenGl screen
def checkScreenUpdate():
    if screenUpdate != []:
        screenUpdate.clear()
        ui.openglwidget.changingWorkingLines()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindowUI()
    functions()
    ui.show()
    app.exec_()