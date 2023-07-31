from OpenGL.GL import *
from OpenGL.GLUT import *
import math
import random

def EightWaySymmetry(x, y, x0, y0):
    draw_points(x + x0, y + y0) #ZOne 1
    draw_points(y + x0, x + y0) #z2 ...
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)


def MidpointCircle(radius, x0, y0):

    #print(radius,x0,y0)

    glColor3f(random.random(),random.random(),random.random())

    d = 1 - radius
    x = 0
    y = radius

    EightWaySymmetry(x, y, x0, y0)

    while x < y:
        if d >= 0: # SouthEast
            d += 2 * x - 2 * y + 5
            x += 1
            y -= 1
        else: #East
            d += 2 * x + 3
            x += 1

        EightWaySymmetry(x, y, x0, y0)

def draw_circle(radius, x, y):
    MidpointCircle(radius, x, y)  # outer circle
    MidpointCircle(radius // 2, x + radius // 2, y)  # Left inner circle
    MidpointCircle(radius // 2, x - radius // 2, y)  # right inner circle
    MidpointCircle(radius // 2, x, y + radius // 2)  # upper inner circle
    MidpointCircle(radius // 2, x, y - radius // 2)  # Lower inner circle

    opposite = int(math.sin(math.radians(45)) * radius / 2)
    MidpointCircle(radius // 2, x + opposite, y + opposite)  # Right upper diagonal
    MidpointCircle(radius // 2, x + opposite, y - opposite)  # Right lower diagonal
    MidpointCircle(radius // 2, x - opposite, y + opposite)  # Left upper diagonal
    MidpointCircle(radius // 2, x - opposite, y - opposite)  # Left lower diagonal

def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    #glColor3f(random.random(), random.random(), random.random())
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

   # glColor3f(1.0, 1.0, 1.0)  # (Red, Green, Blue)

    draw_circle(400, 500, 500)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"LAB03_MidpointCircle")
glutDisplayFunc(showScreen)
glutMainLoop()
