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
    MidpointCircle(radius, x, y)
    MidpointCircle(radius // 2, x + radius // 2, y)  #R
    MidpointCircle(radius // 2, x - radius // 2, y)  #L
    MidpointCircle(radius // 2, x, y + radius // 2)  #U
    MidpointCircle(radius // 2, x, y - radius // 2)  #B

    diagonal = int(math.sin(math.radians(45)) * radius / 2)

    MidpointCircle(radius // 2, x + diagonal, y + diagonal) #LU
    MidpointCircle(radius // 2, x + diagonal, y - diagonal) #LB
    MidpointCircle(radius // 2, x - diagonal, y + diagonal) #RU
    MidpointCircle(radius // 2, x - diagonal, y - diagonal) #RB
def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
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
    draw_circle(350, 600, 600)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1200, 1200)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 03 Midpoint Circle Drawing Algorithm")
glutDisplayFunc(showScreen)
glutMainLoop()

#bvh

print(math.sin(math.radians(45)))