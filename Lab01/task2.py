from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_triangles(): #For roof will call later so that roof color will be more visible
    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.4, 0.8)
    glVertex2f(300, 500)
    glVertex2f(100, 400)
    glVertex2f(500, 400)
    glEnd()

def draw_lines():
    glLineWidth(5)
    glBegin(GL_LINES)

    glColor3f(0.6, 0.2, 0.4)

    glVertex2f(100, 100) #Left
    glVertex2f(100, 400)

    glVertex2f(100, 400) #UP
    glVertex2f(500, 400)

    glVertex2f(500, 400) #Right
    glVertex2f(500, 100)

    glVertex2f(500, 100) #Bottom
    glVertex2f(100, 100)

    # window left
    glColor3f(0.8, 0.5, 0.3)

    glVertex2f(150, 350)
    glVertex2f(250, 350)

    glVertex2f(250, 350)
    glVertex2f(250, 250)

    glVertex2f(250, 250)
    glVertex2f(150, 250)

    glVertex2f(150, 250)
    glVertex2f(150, 350)

    # window right
    glVertex2f(350, 250)
    glVertex2f(450, 250)

    glVertex2f(450, 250)
    glVertex2f(450, 350)

    glVertex2f(450, 350)
    glVertex2f(350, 350)

    glVertex2f(350, 350)
    glVertex2f(350, 250)


    #door
    glColor3f(0.2, 0.4, 0.8)

    glVertex2f(275,100)
    glVertex2f(325,100)

    glVertex2f(325, 100)
    glVertex2f(325,225)

    glVertex2f(325,225)
    glVertex2f(275,225)

    glVertex2f(275, 225)
    glVertex2f(275, 100)

    glEnd()

    #door dot
    glPointSize(8)
    glBegin(GL_POINTS)
    glColor3f(0.9, 0.3, 0.5)
    glVertex2f(320, 150)
    glEnd()

def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    #call the draw methods here
    draw_lines()
    draw_triangles()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2: My Unique House")
glutDisplayFunc(showScreen)

glutMainLoop()
