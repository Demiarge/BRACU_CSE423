from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_lines():
    glLineWidth(4)
    glBegin(GL_LINES)

    # Line segments for each digit
    # 2
    glColor3f(0.529, 0.078, 0.839)
    glVertex2f(50, 500)
    glVertex2f(100, 500)

    glVertex2f(100, 500)
    glVertex2f(100, 450)

    glVertex2f(100, 450)
    glVertex2f(50, 450)

    glVertex2f(50, 450)
    glVertex2f(50, 400)

    glVertex2f(50, 400)
    glVertex2f(100, 400)



    # 0

    glColor3f(0.984, 0.647, 0.082)
    glVertex2f(150, 500)
    glVertex2f(150, 400)

    glVertex2f(150, 400)
    glVertex2f(200, 400)

    glVertex2f(200, 400)
    glVertex2f(200, 500)

    glVertex2f(200, 500)
    glVertex2f(150, 500)



    # 3
    glColor3f(0.596, 0.984, 0.082)
    glVertex2f(250, 500)
    glVertex2f(300, 500)

    glVertex2f(300, 500)
    glVertex2f(300, 450)

    glVertex2f(300, 450)
    glVertex2f(250, 450)

    glVertex2f(300, 450)
    glVertex2f(300, 400)

    glVertex2f(250, 400)
    glVertex2f(300, 400)


    # 0
    glColor3f(0.082, 0.878, 0.984)
    glVertex2f(400, 500)
    glVertex2f(400, 400)

    glVertex2f(400, 400)
    glVertex2f(350, 400)

    glVertex2f(350, 400)
    glVertex2f(350, 500)

    glVertex2f(350, 500)
    glVertex2f(400, 500)



    # 1
    glColor3f(0.984, 0.082, 0.082)
    glVertex2f(525,475)
    glVertex2f(550, 500)
    glVertex2f(550,500)
    glVertex2f(550,400)
    glVertex2f(525,400)
    glVertex2f(575,400)

    #0
    glColor3f(0.082, 0.749, 0.984)
    glVertex2f(600,400)
    glVertex2f(650,400)
    glVertex2f(650,400)
    glVertex2f(650,500)
    glVertex2f(650,500)
    glVertex2f(600,500)
    glVertex2f(600,500)
    glVertex2f(600,400)

    #7
    glColor3f(0.984, 0.082, 0.647)
    glVertex2f(700,500)
    glVertex2f(750,500)
    glVertex2f(750,500)
    glVertex2f(750,400)
    glVertex2f(730,450)
    glVertex2f(770,450)

    #4
    glColor3f(0.082, 0.984, 0.674)
    glVertex2f(800,500)
    glVertex2f(800,450)
    glVertex2f(800,450)
    glVertex2f(850,450)
    glVertex2f(850,500)
    glVertex2f(850,400)

    glEnd()


def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 900, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    #call the draw methods here
    draw_lines()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3: 20301074")
glutDisplayFunc(showScreen)

glutMainLoop()
