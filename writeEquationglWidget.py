from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtGui import QFont
from PyQt5.QtOpenGL import *
from baseFunctions import *
from eval import *
from evalFunctions import *
from alphaFunctions import *
from secondFunctions import *
from variables import *
from keyBoardFunctions import *
import math


class writeEquationglWidget(QGLWidget):
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
        for equation in list(equations.keys()):
            self.renderText(8, equationsPos[0], equations[equation][0] + "=" + equations[equation][1])
            equationsPos[0] = equationsPos[0] + 32
        equationsPos[0] = 52


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
        glTranslatef(-5.0, statusBarTranslation[0], -5.1)
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
