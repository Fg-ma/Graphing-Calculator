from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtGui import QFont
from PyQt5.QtOpenGL import *
from variables import *
import time

class writeEquationGlWidget(QGLWidget):

    """
    Creates the openGL widget in which the equations screen page is displayed,
    contains functions for updating the screen with the appropriate information given the appropriate inputs.
    """

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
        glUseProgram(0)

        # Font color
        glColor3f(0.2, 0.2, 0.2)

        # Draws cursor
        self.setFont(QFont("Cambria Math", 10))
        self.renderText(7 + cursorPos[0], (activeFunction[0] * 32) + 24 - equationsPosVerticalShift[0], cursorHolder[0])

        # Handles lines displaying the equations
        self.setFont(QFont("Cambria Math", 14))
        for equation in list(equations.keys()):
            print("=" + "".join(equations[equation][1]))
            equationsPos[0] = int(equation) * 32
            self.renderText(8 + equationsPosHorizontalShift[equation], equationsPos[0] + 18 - equationsPosVerticalShift[0], equations[equation][0] + "=" + "".join(equations[equation][1]))


    # Handles changing the position of the workingLine when there is a change
    def eqChangingWorkingLines(self):
        global workingLinePos
        global maxWorkingLinePos
        maxWorkingLinePos = self.height() - 12

        if (activeFunction[0] * 32) + 24 - equationsPosVerticalShift[0] >= maxWorkingLinePos:
            equationsPosVerticalShift[0] = equationsPosVerticalShift[0] + 32
        elif (activeFunction[0] * 32) + 24 - equationsPosVerticalShift[0] <= 24:
            equationsPosVerticalShift[0] = equationsPosVerticalShift[0] - 32

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
