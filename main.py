"""
This program is a work in progress intented to be a graphing calculator
that improves as I learn new math topics and implement them in code.
Currently it is facing the challenge of being slow to boot and very resource expensive because of the many openGL screens.
A major goal is to make the typing on the screen prettier especially by the raised to functions.
"""

"""
Current List of screens:
-Main window screen(0)
-Equation screen(1)
-Graph screen(2)
"""

import sys
from PyQt5.uic import loadUi
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtOpenGL import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from variables import *

from mainGlWidget import mainGlWidget
from eval import *
from evalFunctions import *
from baseFunctions import *
from alphaFunctions import *
from secondFunctions import *
from keyboardFunctions import *

from writeEquationGlWidget import writeEquationGlWidget
from eqBaseFunctions import *
from eqAlphaFunctions import *
from eqSecondFunctions import *
from eqKeyboardFunctions import *

from displayEquationGlWidget import displayEquationGlWidget


class MainWindowUI(QMainWindow): 
    
    """
    Creates the main window(referneced as ui).
    Creates multiple openGL screens that are used in a stacked widget to switch between different pages of function
    (such as the main page, the equation writing page, and graphing page).
    A timer is created that handles calling the update screen functions in the openGL screens.
    A resize function is needed to control the height of the status bar.
    A key press event function is used to connect key strokes to their approiate functions given the conditions of the screen.
    """

    def __init__(self):
        super(MainWindowUI, self).__init__()

        loadUi("calculator.ui", self)

        # opengl widget
        self.mainopenglwidget = mainGlWidget()
        self.stackedWidget.insertWidget(0, self.mainopenglwidget)
        self.eqopenglwidget = writeEquationGlWidget()
        self.stackedWidget.insertWidget(1, self.eqopenglwidget)
        self.disopenglwidget = displayEquationGlWidget()
        self.stackedWidget.insertWidget(2, self.disopenglwidget)
        self.stackedWidget.setCurrentIndex(0)

        # Main window timer
        mainTimer = QtCore.QTimer(self)
        mainTimer.setInterval(20)
        mainTimer.timeout.connect(self.mainopenglwidget.updateGL)
        mainTimer.timeout.connect(self.eqopenglwidget.updateGL)
        mainTimer.timeout.connect(self.disopenglwidget.updateGL)
        mainTimer.timeout.connect(checkScreenUpdate)
        mainTimer.start()

        # Cursor blink timer
        Ctimer = QtCore.QTimer(self)
        Ctimer.setInterval(500)
        Ctimer.timeout.connect(cursor)
        Ctimer.start()
        
        self.resizeEvent = self.onResize
    

    def onResize(self, event):

        """
        Resizes the status bar and updates the the max number of lines before the screen starts wrapping
        """

        global statusBarTranslation
        resizedHeight = self.height()
        windowHeightChange = 870 - resizedHeight
        statusBarTranslation[0] = -1.0 - (windowHeightChange * .00595)
        # Get rightStatusBarText length
        self.mainopenglwidget.rightStatusBarLength()
        maxLines[0] = (self.mainopenglwidget.height() / 50)


    def keyPressEvent(self, event):

        """
        Connects the appropriate functions to the appropriate places when certain key/combinations of keys
        are pressed given the current screen conditions.
        """

        if inHistory[0] == "False" and ui.stackedWidget.currentIndex() == 0:          
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
            elif event.modifiers() & Qt.AltModifier:
                if event.key() == Qt.Key_Y:
                    equationFunction()
                elif event.key() == Qt.Key_Backspace:
                    quitFunction()
                elif event.key() == Qt.Key_Delete:
                    quitFunction()
                elif event.key() == Qt.Key_G:
                    graphFunction()
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
                    leftBracketFunction()
                elif event.key() == Qt.Key_BracketRight:
                    rightBracketFunction()
                elif event.key() == Qt.Key_Comma:
                    commaFunction()
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
        elif inHistory[0] == "True" and ui.stackedWidget.currentIndex() == 0:
            if event.modifiers() & Qt.ControlModifier:
                if event.key() == Qt.Key_C:
                    functionTypeControlC()
                elif event.key() == Qt.Key_Backspace:
                    clearFunction()
                    functions()
                elif event.key() == Qt.Key_Delete:
                    clearFunction()
                    functions()
            elif event.modifiers() & Qt.ShiftModifier:
                pass
            elif event.modifiers() & Qt.AltModifier:
                if event.key() == Qt.Key_Y:
                    equationFunction()
                elif event.key() == Qt.Key_Backspace:
                    quitFunction()
                elif event.key() == Qt.Key_Delete:
                    quitFunction()
                elif event.key() == Qt.Key_G:
                    graphFunction()
            else:
                if event.key() == Qt.Key_Up:
                    upArrowFunction()
                elif event.key() == Qt.Key_Down:
                    downArrowFunction()
                elif event.key() == Qt.Key_Return:
                    inHistoryEvalFunction()
        elif ui.stackedWidget.currentIndex() == 1:
            if event.modifiers() & Qt.ControlModifier:
                if event.key() == Qt.Key_C:
                    eqFunctionTypeControlC()
                elif event.key() == Qt.Key_V:
                    eqFunctionTypeControlV()
                elif event.key() == Qt.Key_Z:
                    eqFunctionTypeControlZ()
                elif event.key() == Qt.Key_Backspace:
                    eqClearFunction()
                elif event.key() == Qt.Key_Delete:
                    eqClearFunction()
            elif event.modifiers() & Qt.ShiftModifier:
                if event.key() == Qt.Key_Plus:
                    eqAdditionFunction()
                elif event.key() == Qt.Key_ParenRight:
                    eqRightParenthesesFunction()
                elif event.key() == Qt.Key_BraceLeft:
                    eqLeftCurlyBracketFunction()
                elif event.key() == Qt.Key_BraceRight:
                    eqRightCurlyBracketFunction()
                elif event.key() == Qt.Key_Exclam:
                    eqFunctionTypeExclamation()
                elif event.key() == Qt.Key_Underscore:
                    eqFunctionUnderscore()
                elif event.key() == Qt.Key_Colon:
                    eqFunctionColon()
                elif event.key() == Qt.Key_Question:
                    eqFunctionQuestionMark()
                elif event.key() == Qt.Key_QuoteDbl:
                    eqFunctionDoubleQuotationMark()
                elif event.key() == Qt.Key_At:
                    eqFunctionTypeAt()
                elif event.key() == Qt.Key_NumberSign:
                    eqFunctionTypeNumberSign()
                elif event.key() == Qt.Key_Dollar:
                    eqFunctionTypeDollarSign()
                elif event.key() == Qt.Key_Percent:
                    eqFunctionTypePercent()
                elif event.key() == Qt.Key_AsciiCircum:
                    eqPowerFunction()
                elif event.key() == Qt.Key_Ampersand:
                    eqFunctionTypeAmpersand()
                elif event.key() == Qt.Key_Asterisk:
                    eqMultiplicationFunction()
                elif event.key() == Qt.Key_ParenLeft:
                    eqLeftParenthesesFunction()
                elif event.key() == Qt.Key_A:
                    eqFunctionA()
                elif event.key() == Qt.Key_B:
                    eqFunctionB()
                elif event.key() == Qt.Key_C:
                    eqFunctionC()
                elif event.key() == Qt.Key_D:
                    eqFunctionD()
                elif event.key() == Qt.Key_E:
                    eqFunctionE()
                elif event.key() == Qt.Key_F:
                    eqFunctionF()
                elif event.key() == Qt.Key_G:
                    eqFunctionG()
                elif event.key() == Qt.Key_H:
                    eqFunctionH()
                elif event.key() == Qt.Key_I:
                    eqFunctionI()
                elif event.key() == Qt.Key_J:
                    eqFunctionJ()
                elif event.key() == Qt.Key_K:
                    eqFunctionK()
                elif event.key() == Qt.Key_L:
                    eqFunctionL()
                elif event.key() == Qt.Key_M:
                    eqFunctionM()
                elif event.key() == Qt.Key_N:
                    eqFunctionN()
                elif event.key() == Qt.Key_O:
                    eqFunctionO()
                elif event.key() == Qt.Key_P:
                    eqFunctionP()
                elif event.key() == Qt.Key_Q:
                    eqFunctionQ()
                elif event.key() == Qt.Key_R:
                    eqFunctionR()
                elif event.key() == Qt.Key_S:
                    eqFunctionS()
                elif event.key() == Qt.Key_T:
                    eqFunctionT()
                elif event.key() == Qt.Key_U:
                    eqFunctionU()
                elif event.key() == Qt.Key_V:
                    eqFunctionV()
                elif event.key() == Qt.Key_W:
                    eqFunctionW()
                elif event.key() == Qt.Key_X:
                    eqFunctionX() 
                elif event.key() == Qt.Key_Y:
                    eqFunctionY()
                elif event.key() == Qt.Key_Z:
                    eqFunctionZ()
            elif event.modifiers() & Qt.AltModifier:
                if event.key() == Qt.Key_Y:
                    equationFunction()
                elif event.key() == Qt.Key_Backspace:
                    quitFunction()
                elif event.key() == Qt.Key_Delete:
                    quitFunction()
                elif event.key() == Qt.Key_G:
                    graphFunction()
            else:
                if event.key() == Qt.Key_Return:
                    eqEvaluate()
                elif event.key() == Qt.Key_Backspace:
                    eqFunctionTypeBackspace()
                elif event.key() == Qt.Key_Delete:
                    eqFunctionTypeDelete()
                elif event.key() == Qt.Key_Minus:
                    eqNegativeFunction()
                elif event.key() == Qt.Key_Slash:
                    eqDivisionFunction()
                elif event.key() == Qt.Key_Period:
                    eqDecimalFunction()
                elif event.key() == Qt.Key_BracketLeft:
                    eqLeftBracketFunction()
                elif event.key() == Qt.Key_BracketRight:
                    eqRightBracketFunction()
                elif event.key() == Qt.Key_Comma:
                    eqCommaFunction()
                elif event.key() == Qt.Key_0:
                    eqFunction0()
                elif event.key() == Qt.Key_1:
                    eqFunction1()
                elif event.key() == Qt.Key_2:
                    eqFunction2()
                elif event.key() == Qt.Key_3:
                    eqFunction3()
                elif event.key() == Qt.Key_4:
                    eqFunction4()
                elif event.key() == Qt.Key_5:
                    eqFunction5()
                elif event.key() == Qt.Key_6:
                    eqFunction6()
                elif event.key() == Qt.Key_7:
                    eqFunction7()
                elif event.key() == Qt.Key_8:
                    eqFunction8()
                elif event.key() == Qt.Key_9:
                    eqFunction9()
                elif event.key() == Qt.Key_A:
                    eqFunctionTypea()
                elif event.key() == Qt.Key_B:
                    eqFunctionTypeb()
                elif event.key() == Qt.Key_C:
                    eqFunctionTypec()
                elif event.key() == Qt.Key_D:
                    eqFunctionTyped()
                elif event.key() == Qt.Key_E:
                    eqFunctionTypee()
                elif event.key() == Qt.Key_F:
                    eqFunctionTypef()
                elif event.key() == Qt.Key_G:
                    eqFunctionTypeg()
                elif event.key() == Qt.Key_H:
                    eqFunctionTypeh()
                elif event.key() == Qt.Key_I:
                    eqFunctionTypei()
                elif event.key() == Qt.Key_J:
                    eqFunctionTypej()
                elif event.key() == Qt.Key_K:
                    eqFunctionTypek()
                elif event.key() == Qt.Key_L:
                    eqFunctionTypel()
                elif event.key() == Qt.Key_M:
                    eqFunctionTypem()
                elif event.key() == Qt.Key_N:
                    eqFunctionTypen()
                elif event.key() == Qt.Key_O:
                    eqFunctionTypeo()
                elif event.key() == Qt.Key_P:
                    eqFunctionTypep()
                elif event.key() == Qt.Key_Q:
                    eqFunctionTypeq()
                elif event.key() == Qt.Key_R:
                    eqFunctionTyper()
                elif event.key() == Qt.Key_S:
                    eqFunctionTypes()
                elif event.key() == Qt.Key_T:
                    eqFunctionTypet()
                elif event.key() == Qt.Key_U:
                    eqFunctionTypeu()
                elif event.key() == Qt.Key_V:
                    eqFunctionTypev()
                elif event.key() == Qt.Key_W:
                    eqFunctionTypew()
                elif event.key() == Qt.Key_X:
                    eqFunctionTypex() 
                elif event.key() == Qt.Key_Y:
                    eqFunctionTypey()
                elif event.key() == Qt.Key_Z:
                    eqFunctionTypez()
                elif event.key() == Qt.Key_Left:
                    eqLeftArrowFunction()
                elif event.key() == Qt.Key_Right:
                    eqRightArrowFunction()
                elif event.key() == Qt.Key_Up:
                    eqUpArrowFunction()
                elif event.key() == Qt.Key_Down:
                    eqDownArrowFunction()
        elif ui.stackedWidget.currentIndex() == 2:
            if event.modifiers() & Qt.ControlModifier:
                pass
            elif event.modifiers() & Qt.ShiftModifier:
                pass
            elif event.modifiers() & Qt.AltModifier:
                if event.key() == Qt.Key_Y:
                    equationFunction()
                elif event.key() == Qt.Key_Backspace:
                    quitFunction()
                elif event.key() == Qt.Key_Delete:
                    quitFunction()
                elif event.key() == Qt.Key_G:
                    graphFunction()
            else:
                pass

        # Handles when the working line goes off screen
        offScreen()


def quitFunction():

    """
    Returns to the main screen and updates the appropriate variables to restore the exact conditions that the main screen was left in
    """

    secondResets()
    if ui.stackedWidget.currentIndex() != 0:
        ui.stackedWidget.setCurrentIndex(0)

        functions()

        if needSave[0] == "False":
            needSave[0] = "True"
            lines.clear()
            for i in save[0]:
                lines.append(i)
            workingLinePos[0] = save[1]
            numLines[0] = save[2]
        else:
            lines.clear()
            for i in mainPageSave[0]:
                lines.append(i)
            workingLinePos[0] = mainPageSave[1]
            numLines[0] = mainPageSave[2]
        workingLineShifter[0] = 0
        cursorInlinePosition[0] = -1
        cursorPos[0] = 0
        for i in expressionList:
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]
            cursorInlinePosition[0] = cursorInlinePosition[0] + 1


def equationFunction():

    """
    Switches to the equations page and updates the appropriate variables to restore the exact conditions that the equations screen was left in.
    """

    if ui.stackedWidget.currentIndex() != 1:
        ui.stackedWidget.setCurrentIndex(1)

        functions()

        mainPageSave[0] = lines[:]
        mainPageSave[1] = workingLinePos[0]
        mainPageSave[2] = numLines[0]

        workingLinePos[0] = 52
        workingLineShifter[0] = 34
        cursorInlinePosition[0] = -1
        cursorPos[0] = 14
        for i in equations[str(activeFunction[0])][0]:
            cursorPos[0] = cursorPos[0] + cursorPosDict[i]
        firstHistoryUpdate[0] = "True"
        inHistory[0] = "False"
        selectionBarPos[0] = 0


def graphFunction():

    """
    Switches to the graphing screen
    """

    if ui.stackedWidget.currentIndex() != 2:
        ui.stackedWidget.setCurrentIndex(2)


def functions():

    """
    Connects the appropriate function to the button presed under given conditions(such as screen state or inhistory state)
    """

    if inHistory[0] == "False" and ui.stackedWidget.currentIndex() == 0:
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
            reconnectReset(ui.equationButton.clicked, equationFunction)
            reconnectReset(ui.variableButton.clicked, variableFunction)
            reconnectReset(ui.leftArrowButton.clicked, leftArrowFunction)
            reconnectReset(ui.rightArrowButton.clicked, rightArrowFunction)
            reconnectReset(ui.upArrowButton.clicked, upArrowFunction)
            reconnectReset(ui.downArrowButton.clicked, downArrowFunction)
            reconnectReset(ui.graphButton.clicked, graphFunction)
        elif subcommands == ["2nd"]:
            reconnectReset(ui.negativeButton.clicked, ansFunction)
            reconnectReset(ui.enterButton.clicked, entryFunction)
            reconnectReset(ui.sinButton.clicked, arcsinFunction)
            reconnectReset(ui.cosButton.clicked, arccosFunction)
            reconnectReset(ui.tanButton.clicked, arctanFunction)
            reconnectReset(ui.lnButton.clicked, exponentialFunction)
            reconnectReset(ui.powerButton.clicked, piFunction)
            reconnectReset(ui.modeButton.clicked, quitFunction)
            reconnectReset(ui.squareButton.clicked, squareRootFunction)
            reconnectReset(ui.commaButton.clicked, scientificNotationFunction)
            reconnectReset(ui.logButton.clicked, tentotheFunction)
            reconnectReset(ui.leftParenthesesButton.clicked, leftCurlyBracketFunction)
            reconnectReset(ui.rightParenthesesButton.clicked, rightCurlyBracketFunction)
            reconnectReset(ui.multiplicationButton.clicked, leftBracketFunction)
            reconnectReset(ui.subtractionButton.clicked, rightBracketFunction)
        elif subcommands == ["alpha"]:
            reconnectReset(ui.enterButton.clicked)
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
    elif inHistory[0] == "True" and ui.stackedWidget.currentIndex() == 0:
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
        reconnectReset(ui.enterButton.clicked, inHistoryEvalFunction)
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
        reconnectReset(ui.clearButton.clicked, clearFunction)
        reconnectReset(ui.secondButton.clicked)
        reconnectReset(ui.alphaButton.clicked)
        reconnectReset(ui.decimalButton.clicked)
        reconnectReset(ui.negativeButton.clicked)
        reconnectReset(ui.equationButton.clicked, equationFunction)
        reconnectReset(ui.variableButton.clicked)
        reconnectReset(ui.leftArrowButton.clicked)
        reconnectReset(ui.rightArrowButton.clicked)
        reconnectReset(ui.graphButton.clicked, graphFunction)
    elif ui.stackedWidget.currentIndex() == 1:
        if subcommands == []:
            reconnectReset(ui.Number0.clicked, eqFunction0)
            reconnectReset(ui.Number1.clicked, eqFunction1)
            reconnectReset(ui.Number2.clicked, eqFunction2)
            reconnectReset(ui.Number3.clicked, eqFunction3)
            reconnectReset(ui.Number4.clicked, eqFunction4)
            reconnectReset(ui.Number5.clicked, eqFunction5)
            reconnectReset(ui.Number6.clicked, eqFunction6)
            reconnectReset(ui.Number7.clicked, eqFunction7)
            reconnectReset(ui.Number8.clicked, eqFunction8)
            reconnectReset(ui.Number9.clicked, eqFunction9)
            reconnectReset(ui.additionButton.clicked, eqAdditionFunction)
            reconnectReset(ui.subtractionButton.clicked, eqSubtractionFunction)
            reconnectReset(ui.multiplicationButton.clicked, eqMultiplicationFunction)
            reconnectReset(ui.divisionButton.clicked, eqDivisionFunction)
            reconnectReset(ui.enterButton.clicked, eqEvaluate)
            reconnectReset(ui.rightParenthesesButton.clicked, eqRightParenthesesFunction)
            reconnectReset(ui.leftParenthesesButton.clicked, eqLeftParenthesesFunction)
            reconnectReset(ui.commaButton.clicked, eqCommaFunction)
            reconnectReset(ui.squareButton.clicked, eqSquareFunction)
            reconnectReset(ui.logButton.clicked, eqLogFunction)
            reconnectReset(ui.lnButton.clicked, eqLnFunction)
            reconnectReset(ui.powerButton.clicked, eqPowerFunction)
            reconnectReset(ui.tanButton.clicked, eqTanFunction)
            reconnectReset(ui.cosButton.clicked, eqCosFunction)
            reconnectReset(ui.sinButton.clicked, eqSinFunction)
            reconnectReset(ui.inverseButton.clicked, eqInverseFunction)
            reconnectReset(ui.clearButton.clicked, eqClearFunction)
            reconnectReset(ui.secondButton.clicked, secondFunction)
            reconnectReset(ui.alphaButton.clicked, alphaFunction)
            reconnectReset(ui.decimalButton.clicked, eqDecimalFunction)
            reconnectReset(ui.negativeButton.clicked, eqNegativeFunction)
            reconnectReset(ui.equationButton.clicked, equationFunction)
            reconnectReset(ui.variableButton.clicked, eqVariableFunction)
            reconnectReset(ui.leftArrowButton.clicked, eqLeftArrowFunction)
            reconnectReset(ui.rightArrowButton.clicked, eqRightArrowFunction)
            reconnectReset(ui.upArrowButton.clicked, eqUpArrowFunction)
            reconnectReset(ui.downArrowButton.clicked, eqDownArrowFunction)
            reconnectReset(ui.graphButton.clicked, graphFunction)
        elif subcommands == ["2nd"]:
            reconnectReset(ui.negativeButton.clicked)
            reconnectReset(ui.enterButton.clicked)
            reconnectReset(ui.sinButton.clicked, eqArcsinFunction)
            reconnectReset(ui.cosButton.clicked, eqArccosFunction)
            reconnectReset(ui.tanButton.clicked, eqArctanFunction)
            reconnectReset(ui.lnButton.clicked, eqExponentialFunction)
            reconnectReset(ui.powerButton.clicked, eqPiFunction)
            reconnectReset(ui.modeButton.clicked, quitFunction)
            reconnectReset(ui.squareButton.clicked, eqSquareRootFunction)
            reconnectReset(ui.commaButton.clicked, eqScientificNotationFunction)
            reconnectReset(ui.logButton.clicked, eqTentotheFunction)
            reconnectReset(ui.leftParenthesesButton.clicked, eqLeftCurlyBracketFunction)
            reconnectReset(ui.rightParenthesesButton.clicked, eqRightCurlyBracketFunction)
            reconnectReset(ui.multiplicationButton.clicked, eqLeftBracketFunction)
            reconnectReset(ui.subtractionButton.clicked, eqRightBracketFunction)
        elif subcommands == ["alpha"]:
            reconnectReset(ui.enterButton.clicked)
            reconnectReset(ui.mathButton.clicked, eqFunctionA)
            reconnectReset(ui.appsButton.clicked, eqFunctionB)
            reconnectReset(ui.programButton.clicked, eqFunctionC)
            reconnectReset(ui.inverseButton.clicked, eqFunctionD)
            reconnectReset(ui.sinButton.clicked, eqFunctionE)
            reconnectReset(ui.cosButton.clicked, eqFunctionF)
            reconnectReset(ui.tanButton.clicked, eqFunctionG)
            reconnectReset(ui.powerButton.clicked, eqFunctionH)
            reconnectReset(ui.squareButton.clicked, eqFunctionI)
            reconnectReset(ui.commaButton.clicked, eqFunctionJ)
            reconnectReset(ui.leftParenthesesButton.clicked, eqFunctionK)
            reconnectReset(ui.rightParenthesesButton.clicked, eqFunctionL)
            reconnectReset(ui.divisionButton.clicked, eqFunctionM)
            reconnectReset(ui.logButton.clicked, eqFunctionN)
            reconnectReset(ui.Number7.clicked, eqFunctionO)
            reconnectReset(ui.Number8.clicked, eqFunctionP)
            reconnectReset(ui.Number9.clicked, eqFunctionQ)
            reconnectReset(ui.multiplicationButton.clicked, eqFunctionR)
            reconnectReset(ui.lnButton.clicked, eqFunctionS)
            reconnectReset(ui.Number4.clicked, eqFunctionT)
            reconnectReset(ui.Number5.clicked, eqFunctionU)
            reconnectReset(ui.Number6.clicked, eqFunctionV)
            reconnectReset(ui.subtractionButton.clicked, eqFunctionW)
            reconnectReset(ui.Number1.clicked, eqFunctionY)
            reconnectReset(ui.stoButton.clicked, eqFunctionX)
            reconnectReset(ui.Number2.clicked, eqFunctionZ)
            reconnectReset(ui.Number3.clicked, eqFunctionTheta)
            reconnectReset(ui.Number0.clicked, eqFunctionUnderscore)
            reconnectReset(ui.decimalButton.clicked, eqFunctionColon)
            reconnectReset(ui.negativeButton.clicked, eqFunctionQuestionMark)
            reconnectReset(ui.additionButton.clicked, eqFunctionDoubleQuotationMark)
    elif ui.stackedWidget.currentIndex() == 2:
        if subcommands == []:
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
            reconnectReset(ui.secondButton.clicked, secondFunction)
            reconnectReset(ui.alphaButton.clicked, alphaFunction)
            reconnectReset(ui.decimalButton.clicked)
            reconnectReset(ui.negativeButton.clicked)
            reconnectReset(ui.equationButton.clicked, equationFunction)
            reconnectReset(ui.variableButton.clicked)
            reconnectReset(ui.leftArrowButton.clicked)
            reconnectReset(ui.rightArrowButton.clicked)
            reconnectReset(ui.upArrowButton.clicked)
            reconnectReset(ui.downArrowButton.clicked)
            reconnectReset(ui.graphButton.clicked, graphFunction)
        elif subcommands == ["2nd"]:
            reconnectReset(ui.negativeButton.clicked)
            reconnectReset(ui.enterButton.clicked)
            reconnectReset(ui.sinButton.clicked)
            reconnectReset(ui.cosButton.clicked)
            reconnectReset(ui.tanButton.clicked)
            reconnectReset(ui.powerButton.clicked)
            reconnectReset(ui.modeButton.clicked, quitFunction)
            reconnectReset(ui.squareButton.clicked)
            reconnectReset(ui.commaButton.clicked)
            reconnectReset(ui.logButton.clicked)
            reconnectReset(ui.leftParenthesesButton.clicked)
            reconnectReset(ui.rightParenthesesButton.clicked)
            reconnectReset(ui.multiplicationButton.clicked)
            reconnectReset(ui.subtractionButton.clicked)
        elif subcommands == ["alpha"]:
            reconnectReset(ui.enterButton.clicked)
            reconnectReset(ui.mathButton.clicked)
            reconnectReset(ui.appsButton.clicked)
            reconnectReset(ui.programButton.clicked)
            reconnectReset(ui.inverseButton.clicked)
            reconnectReset(ui.sinButton.clicked)
            reconnectReset(ui.cosButton.clicked)
            reconnectReset(ui.tanButton.clicked)
            reconnectReset(ui.powerButton.clicked)
            reconnectReset(ui.squareButton.clicked)
            reconnectReset(ui.commaButton.clicked)
            reconnectReset(ui.leftParenthesesButton.clicked)
            reconnectReset(ui.rightParenthesesButton.clicked)
            reconnectReset(ui.divisionButton.clicked)
            reconnectReset(ui.logButton.clicked)
            reconnectReset(ui.Number7.clicked)
            reconnectReset(ui.Number8.clicked)
            reconnectReset(ui.Number9.clicked)
            reconnectReset(ui.multiplicationButton.clicked)
            reconnectReset(ui.lnButton.clicked)
            reconnectReset(ui.Number4.clicked)
            reconnectReset(ui.Number5.clicked)
            reconnectReset(ui.Number6.clicked)
            reconnectReset(ui.subtractionButton.clicked)
            reconnectReset(ui.Number1.clicked)
            reconnectReset(ui.stoButton.clicked)
            reconnectReset(ui.Number2.clicked)
            reconnectReset(ui.Number3.clicked)
            reconnectReset(ui.Number0.clicked)
            reconnectReset(ui.decimalButton.clicked)
            reconnectReset(ui.negativeButton.clicked)
            reconnectReset(ui.additionButton.clicked)

    # Handles when the working line goes off screen
    offScreen()


def reconnectReset(signal, newhandler=None, oldhandler=None):    

    """
    Swaps the what function the inputed signal(button press) is connected to
    by disconnecting the signal then connecting it if a newhandler is inputted
    """

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
        signal.connect(functions)


def offScreen():

    """
    Differentiates between screens then handles the event where the text on the screen goes beyond the bounds of the screen,
    then shifts the position of the workingline and cursor accordingly in order to make the text fit on the screen bytext going off the left edge
    """

    if ui.stackedWidget.currentIndex() == 0:
        workingDistanceToEdge = ui.mainopenglwidget.width() - cursorPos[0]
        if workingDistanceToEdge < 24:
            workingLineShifter[0] = workingLineShifter[0] - (24 - workingDistanceToEdge)
            cursorPos[0] = cursorPos[0] - (24 - workingDistanceToEdge)
        if workingDistanceToEdge > ui.mainopenglwidget.width():
            workingLineShifter[0] = workingLineShifter[0] - (ui.mainopenglwidget.width() - workingDistanceToEdge)
            cursorPos[0] = cursorPos[0] - (ui.mainopenglwidget.width() - workingDistanceToEdge)
        workingLineLen = 0
        for i in workingLine:
            workingLineLen += cursorPosDict[i]
        if workingLineLen < ui.mainopenglwidget.width() - 24 and cursorInlinePosition[0] == len(workingLine) - 1:
            workingLineShifter[0] = 0
            cursorPos[0] = 0
            for i in workingLine:
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
    if ui.stackedWidget.currentIndex() == 1:
        workingDistanceToEdge = ui.eqopenglwidget.width() - cursorPos[0]
        if workingDistanceToEdge < 24:
            equationsPosHorizontalShift[str(activeFunction[0])] = equationsPosHorizontalShift[str(activeFunction[0])] - (24 - workingDistanceToEdge)
            cursorPos[0] = cursorPos[0] - (24 - workingDistanceToEdge)
        if workingDistanceToEdge > ui.eqopenglwidget.width():
            equationsPosHorizontalShift[str(activeFunction[0])] = equationsPosHorizontalShift[str(activeFunction[0])] - (ui.eqopenglwidget.width() - workingDistanceToEdge)
            cursorPos[0] = cursorPos[0] - (ui.eqopenglwidget.width() - workingDistanceToEdge)
        workingLineLen = 14
        for i in equations[str(activeFunction[0])][1]:
            workingLineLen += cursorPosDict[i]
        for i in equations[str(activeFunction[0])][0]:
            workingLineLen += cursorPosDict[i]
        if workingLineLen < ui.mainopenglwidget.width() - 24 and cursorInlinePosition[0] == len(equations[str(activeFunction[0])][1]) - 1:
            equationsPosHorizontalShift[str(activeFunction[0])] = 0
            cursorPos[0] = 14
            for i in equations[str(activeFunction[0])][1]:
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]
            for i in equations[str(activeFunction[0])][0]:
                cursorPos[0] = cursorPos[0] + cursorPosDict[i]


def checkScreenUpdate():

    """
    Updates screen when it is necessary to forcibly update it.
    """

    # Handles screen updates
    if screenUpdate != []:
        screenUpdate.clear()
        ui.mainopenglwidget.changingWorkingLines()
        ui.eqopenglwidget.eqChangingWorkingLines()
    
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