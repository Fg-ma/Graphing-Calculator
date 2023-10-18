from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtGui import QFont
from PyQt5.QtOpenGL import *
from variables import *
import numpy as np
import math


class displayEquationGlWidget(QGLWidget):
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

        # Draws status bar
        self.drawStatusBar()


    # More parameters on intialization
    def initializeGL(self):
        glClearColor(0.945, 0.945, 0.945, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                    
        gluPerspective(45.0,1.33,0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW)
        gluOrtho2D(-2.0,2.0,-2.0,2.0)


    def plotfunc():
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0,0.0,0.0) 
        glPointSize(1.0)

        for a in np.arange(1.0,3.0,0.1):
            for t in np.arange(-200.0,200.0,0.005):
                x = math.sin(0.99*t) - 0.7*math.cos(3.01*t)
                y = math.cos(1.01*t) + 0.1*math.sin(15.03*t)

                glBegin(GL_POINTS)
                glVertex2f(x,y)
                glEnd()
                glFlush()


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

        # Font style
        self.setFont(QFont("Cambria Math", 14))

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
