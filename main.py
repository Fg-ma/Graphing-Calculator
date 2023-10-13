import sys
from PyQt5.uic import loadUi
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtOpenGL import *
from PyQt5 import QtCore, QtWidgets, QtOpenGL
from PyQt5.QtCore import Qt
from baseFunctions import *
from eval import *
from evalFunctions import *
from alphaFunctions import *
from secondFunctions import *
from variables import *
from keyBoardFunctions import *
import math

# Program mainwindow
class MainWindowUI(QMainWindow): 
    def __init__(self):
        super(MainWindowUI, self).__init__()

        loadUi("calculator.ui", self)

        # opengl widget
        self.openglwidget = glWidget()
        self.stackedWidget.insertWidget(0, self.openglwidget)
        self.stackedWidget.setCurrentIndex(0)

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
    

    # Handles resize events
    def onResize(self, event):
        resizedHeight = self.height()
        windowHeightChange = 870 - resizedHeight
        global statusBarTranslation
        statusBarTranslation = -1.0 - (windowHeightChange * .00595)
        # Get rightStatusBarText length
        self.openglwidget.rightStatusBarLength()


    # Handles switching to equations page
    def equationFunction(self):
        self.stackedWidget.setCurrentIndex(1)


    # Handles quiting but and returning to main pageA
    def quitFunction(self):
        secondResets()
        self.stackedWidget.setCurrentIndex(0)   


    # Handles keyboard events
    def keyPressEvent(self, event):
        if inHistory[0] == "False":          
            if event.modifiers() & Qt.ControlModifier:
                if event.key() == Qt.Key_C:
                    functionTypeControlC()
                elif event.key() == Qt.Key_V:
                    functionTypeControlV()
                elif event.key() == Qt.Key_Z:
                    functionTypeControlZ()
                elif event.key() == Qt.Key_Backspace:
                    clearFunction()
                elif event.key() == Qt.Key_Delete:
                    clearFunction()
            elif event.modifiers() & Qt.ShiftModifier:
                if event.key() == Qt.Key_Plus:
                    additionFunction()
                elif event.key() == Qt.Key_ParenRight:
                    rightParenthesesFunction()
                elif event.key() == Qt.Key_BraceLeft:
                    leftCurlyBracketFunction()
                elif event.key() == Qt.Key_BraceRight:
                    rightCurlyBracketFunction()
                elif event.key() == Qt.Key_Exclam:
                    functionTypeExclamation()
                elif event.key() == Qt.Key_Underscore:
                    functionUnderscore()
                elif event.key() == Qt.Key_Colon:
                    functionColon()
                elif event.key() == Qt.Key_Question:
                    functionQuestionMark()
                elif event.key() == Qt.Key_QuoteDbl:
                    functionDoubleQuotationMark()
                elif event.key() == Qt.Key_At:
                    functionTypeAt()
                elif event.key() == Qt.Key_NumberSign:
                    functionTypeNumberSign()
                elif event.key() == Qt.Key_Dollar:
                    functionTypeDollarSign()
                elif event.key() == Qt.Key_Percent:
                    functionTypePercent()
                elif event.key() == Qt.Key_AsciiCircum:
                    powerFunction()
                elif event.key() == Qt.Key_Ampersand:
                    functionTypeAmpersand()
                elif event.key() == Qt.Key_Asterisk:
                    multiplicationFunction()
                elif event.key() == Qt.Key_ParenLeft:
                    leftParenthesesFunction()
                elif event.key() == Qt.Key_A:
                    functionA()
                elif event.key() == Qt.Key_B:
                    functionB()
                elif event.key() == Qt.Key_C:
                    functionC()
                elif event.key() == Qt.Key_D:
                    functionD()
                elif event.key() == Qt.Key_E:
                    functionE()
                elif event.key() == Qt.Key_F:
                    functionF()
                elif event.key() == Qt.Key_G:
                    functionG()
                elif event.key() == Qt.Key_H:
                    functionH()
                elif event.key() == Qt.Key_I:
                    functionI()
                elif event.key() == Qt.Key_J:
                    functionJ()
                elif event.key() == Qt.Key_K:
                    functionK()
                elif event.key() == Qt.Key_L:
                    functionL()
                elif event.key() == Qt.Key_M:
                    functionM()
                elif event.key() == Qt.Key_N:
                    functionN()
                elif event.key() == Qt.Key_O:
                    functionO()
                elif event.key() == Qt.Key_P:
                    functionP()
                elif event.key() == Qt.Key_Q:
                    functionQ()
                elif event.key() == Qt.Key_R:
                    functionR()
                elif event.key() == Qt.Key_S:
                    functionS()
                elif event.key() == Qt.Key_T:
                    functionT()
                elif event.key() == Qt.Key_U:
                    functionU()
                elif event.key() == Qt.Key_V:
                    functionV()
                elif event.key() == Qt.Key_W:
                    functionW()
                elif event.key() == Qt.Key_X:
                    functionX() 
                elif event.key() == Qt.Key_Y:
                    functionY()
                elif event.key() == Qt.Key_Z:
                    functionZ()
            else:
                if event.key() == Qt.Key_Return:
                    evaluate()
                elif event.key() == Qt.Key_Backspace:
                    functionTypeBackspace()
                elif event.key() == Qt.Key_Delete:
                    if workingLine == []:
                        clearFunction()
                    else:
                        functionTypeDelete()
                elif event.key() == Qt.Key_Minus:
                    negativeFunction()
                elif event.key() == Qt.Key_Slash:
                    divisionFunction()
                elif event.key() == Qt.Key_Period:
                    decimalFunction()
                elif event.key() == Qt.Key_BracketLeft:
                    functionTypeLeftBracket()
                elif event.key() == Qt.Key_BracketRight:
                    functionTypeRightBracket()
                elif event.key() == Qt.Key_0:
                    function0()
                elif event.key() == Qt.Key_1:
                    function1()
                elif event.key() == Qt.Key_2:
                    function2()
                elif event.key() == Qt.Key_3:
                    function3()
                elif event.key() == Qt.Key_4:
                    function4()
                elif event.key() == Qt.Key_5:
                    function5()
                elif event.key() == Qt.Key_6:
                    function6()
                elif event.key() == Qt.Key_7:
                    function7()
                elif event.key() == Qt.Key_8:
                    function8()
                elif event.key() == Qt.Key_9:
                    function9()
                elif event.key() == Qt.Key_A:
                    functionTypea()
                elif event.key() == Qt.Key_B:
                    functionTypeb()
                elif event.key() == Qt.Key_C:
                    functionTypec()
                elif event.key() == Qt.Key_D:
                    functionTyped()
                elif event.key() == Qt.Key_E:
                    functionTypee()
                elif event.key() == Qt.Key_F:
                    functionTypef()
                elif event.key() == Qt.Key_G:
                    functionTypeg()
                elif event.key() == Qt.Key_H:
                    functionTypeh()
                elif event.key() == Qt.Key_I:
                    functionTypei()
                elif event.key() == Qt.Key_J:
                    functionTypej()
                elif event.key() == Qt.Key_K:
                    functionTypek()
                elif event.key() == Qt.Key_L:
                    functionTypel()
                elif event.key() == Qt.Key_M:
                    functionTypem()
                elif event.key() == Qt.Key_N:
                    functionTypen()
                elif event.key() == Qt.Key_O:
                    functionTypeo()
                elif event.key() == Qt.Key_P:
                    functionTypep()
                elif event.key() == Qt.Key_Q:
                    functionTypeq()
                elif event.key() == Qt.Key_R:
                    functionTyper()
                elif event.key() == Qt.Key_S:
                    functionTypes()
                elif event.key() == Qt.Key_T:
                    functionTypet()
                elif event.key() == Qt.Key_U:
                    functionTypeu()
                elif event.key() == Qt.Key_V:
                    functionTypev()
                elif event.key() == Qt.Key_W:
                    functionTypew()
                elif event.key() == Qt.Key_X:
                    functionTypex() 
                elif event.key() == Qt.Key_Y:
                    functionTypey()
                elif event.key() == Qt.Key_Z:
                    functionTypez()
                elif event.key() == Qt.Key_Left:
                    leftArrowFunction()
                elif event.key() == Qt.Key_Right:
                    rightArrowFunction()
                elif event.key() == Qt.Key_Up:
                    upArrowFunction()
                elif event.key() == Qt.Key_Down:
                    downArrowFunction()
        elif inHistory[0] == "True":
            if event.modifiers() & Qt.ControlModifier:
                pass
            elif event.modifiers() & Qt.ShiftModifier:
                pass
            else:
                if event.key() == Qt.Key_Up:
                    upArrowFunction()
                elif event.key() == Qt.Key_Down:
                    downArrowFunction()
        # Handles when the working line goes off screen
        offScreen()


def functions():
    # baseFunctions, secondFunctions, and alphaFunctions
    if inHistory[0] == "False":
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
            reconnectReset(ui.rightParenthesesButton.clicked, rightParenthesesFunction)
            reconnectReset(ui.leftParenthesesButton.clicked, leftParenthesesFunction)
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
            reconnectReset(ui.equationButton.clicked, ui.equationFunction)
            reconnectReset(ui.variableButton.clicked, variableFunction)
            reconnectReset(ui.leftArrowButton.clicked, leftArrowFunction)
            reconnectReset(ui.rightArrowButton.clicked, rightArrowFunction)
            reconnectReset(ui.upArrowButton.clicked, upArrowFunction)
            reconnectReset(ui.downArrowButton.clicked, downArrowFunction)
        elif subcommands == ["2nd"]:
            reconnectReset(ui.negativeButton.clicked, ansFunction)
            reconnectReset(ui.enterButton.clicked, entryFunction)
            reconnectReset(ui.sinButton.clicked, arcsinFunction)
            reconnectReset(ui.cosButton.clicked, arccosFunction)
            reconnectReset(ui.tanButton.clicked, arctanFunction)
            reconnectReset(ui.powerButton.clicked, piFunction)
            reconnectReset(ui.modeButton.clicked, ui.quitFunction)
            reconnectReset(ui.squareButton.clicked, squareRootFunction)
            reconnectReset(ui.commaButton.clicked, scientificNotationFunction)
            reconnectReset(ui.logButton.clicked, tentotheFunction)
            reconnectReset(ui.leftParenthesesButton.clicked, leftCurlyBracketFunction)
            reconnectReset(ui.rightParenthesesButton.clicked, rightCurlyBracketFunction)
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
            reconnectReset(ui.leftParenthesesButton.clicked, functionK)
            reconnectReset(ui.rightParenthesesButton.clicked, functionL)
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
            reconnectReset(ui.Number3.clicked, functionTheta)
            reconnectReset(ui.Number0.clicked, functionUnderscore)
            reconnectReset(ui.decimalButton.clicked, functionColon)
            reconnectReset(ui.negativeButton.clicked, functionQuestionMark)
            reconnectReset(ui.additionButton.clicked, functionDoubleQuotationMark)
    if inHistory[0] == "True":
        reconnectReset(ui.Number0.clicked)
        reconnectReset(ui.Number1.clicked)
        reconnectReset(ui.Number2.clicked)
        reconnectReset(ui.Number3.clicked)
        reconnectReset(ui.Number4.clicked)
        reconnectReset(ui.Number5.clicked)
        reconnectReset(ui.Number6.clicked)
        reconnectReset(ui.Number7.clicked)
        reconnectReset(ui.Number8.clicked)
        reconnectReset(ui.Number9.clicked)
        reconnectReset(ui.additionButton.clicked)
        reconnectReset(ui.subtractionButton.clicked)
        reconnectReset(ui.multiplicationButton.clicked)
        reconnectReset(ui.divisionButton.clicked)
        reconnectReset(ui.enterButton.clicked)
        reconnectReset(ui.rightParenthesesButton.clicked)
        reconnectReset(ui.leftParenthesesButton.clicked)
        reconnectReset(ui.commaButton.clicked)
        reconnectReset(ui.squareButton.clicked)
        reconnectReset(ui.logButton.clicked)
        reconnectReset(ui.lnButton.clicked)
        reconnectReset(ui.powerButton.clicked)
        reconnectReset(ui.tanButton.clicked)
        reconnectReset(ui.cosButton.clicked)
        reconnectReset(ui.sinButton.clicked)
        reconnectReset(ui.inverseButton.clicked)
        reconnectReset(ui.clearButton.clicked)
        reconnectReset(ui.secondButton.clicked)
        reconnectReset(ui.alphaButton.clicked)
        reconnectReset(ui.decimalButton.clicked)
        reconnectReset(ui.negativeButton.clicked)
        reconnectReset(ui.equationButton.clicked)
        reconnectReset(ui.variableButton.clicked)
        reconnectReset(ui.leftArrowButton.clicked)
        reconnectReset(ui.rightArrowButton.clicked)

    # Handles when the working line goes off screen
    offScreen()


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


def offScreen():
    workingDistanceToEdge = ui.openglwidget.width() - cursorPos[0]
    if workingDistanceToEdge < 24:
        workingLineShifter[0] = workingLineShifter[0] - (24 - workingDistanceToEdge)
        cursorPos[0] = cursorPos[0] - (24 - workingDistanceToEdge)
    if workingDistanceToEdge > ui.openglwidget.width():
        workingLineShifter[0] = workingLineShifter[0] - (ui.openglwidget.width() - workingDistanceToEdge)
        cursorPos[0] = cursorPos[0] - (ui.openglwidget.width() - workingDistanceToEdge)

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

        # Draws status bar
        if inHistory[0] == "True":
            self.drawSelectionBar()
            drawSelectionBarRest()


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

        # Draws cursor
        self.setFont(QFont("Cambria Math", 10))
        self.renderText(7 + cursorPos[0], workingLinePos[0] + 6, cursorHolder[0])

        # Font style
        self.setFont(QFont("Cambria Math", 14))

        # Compile lines into strings
        inputLine = "".join(workingLine)

        # Draws working line
        self.renderText(8 + workingLineShifter[0], workingLinePos[0], inputLine)

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
        movebyFactor[0] = 0
        for i in [*str(rightStatusBarText)]:
            movebyFactor[0] = movebyFactor[0] + cursorPosDict[i]
        rightStatusBarPosition = self.width() - 10 - movebyFactor[0]
    

    # Draws status bar
    def drawStatusBar(self):
        global leftStatusBarText
        global rightStatusBarText

        # Handles status bar
        glTranslatef(-5.0, statusBarTranslation, -5.1)
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


    def drawSelectionBar(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glTranslatef(-5.0, statusBarTranslation - selectionBarTranslation[0], -5.1)
        glColor4f(0.0, 0.3215686274, 0.8, 0.7)
        glPolygonMode(GL_FRONT, GL_FILL)
        glRectf(0.06, 0.3, self.width(), 0.06)
        glFlush()


    # Gets rightAnsLength length
    def rightAnsLength(self, answer):
        movebyFactor[0] = 0
        for i in [*str(answer)]:
            movebyFactor[0] = movebyFactor[0] + cursorPosDict[i]
        rightAnsPosition = self.width() - 10 - movebyFactor[0]
        return rightAnsPosition


# Updates values on OpenGl screen
def checkScreenUpdate():
    if screenUpdate != []:
        screenUpdate.clear()
        ui.openglwidget.changingWorkingLines()
    # Resets button functions
    if inHistory[0] == "True" and firstHistoryUpdate[0] == "True":
        firstHistoryUpdate[0] = "False"
        functions()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindowUI()
    functions()
    ui.show()
    app.exec_()