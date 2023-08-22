from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import os
font = GLUT_BITMAP_9_BY_15
exit_requested = False
scores_updated = False
player1score = 0
player2score = 0


matrix = [[0 for _ in range(3)] for _ in range(3)]
playerturn = 1
result = 0
gameover = False




#### Midpointlineaalgo{}{}{}

def find_zone(dx, dy):
    if dx >= 0:
        if dy >= 0:
            return 1 if abs(dx) <= abs(dy) else 0
        else:
            return 6 if abs(dx) <= abs(dy) else 7
    else:
        if dy >= 0:
            return 2 if abs(dx) <= abs(dy) else 3
        else:
            return 5 if abs(dx) <= abs(dy) else 4


def convert_to_zone0(z, x, y):
    return {
        0: (x, y),
        1: (y, x),
        2: (y, -x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (-y, x),
        7: (x, -y),
    }.get(z)


def convert_original(z, x, y):
    return {
        0: (x, y),
        1: (y, x),
        2: (-y, x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (y, -x),
        7: (x, -y)
    }.get(z)


def midpointline(x1, y1, x2, y2, z):
    #glColor3f(random.random(), random.random(), random.random())
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_points(px, py)
        x += 1
        if d < 0:
            d += e
        else:
            y += 1
            d += ne


def draw_lines(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    px1, py1 = convert_to_zone0(zone, x1, y1)
    px2, py2 = convert_to_zone0(zone, x2, y2)

    midpointline(px1, py1, px2, py2, zone)



## Midpoint circle algo {}{}{}

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
    glColor3f(random.random(),random.random(),random.random()) ##BBEF

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


def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

#$
def initgame(): #prpfrnwrnd
    global playerturn, matrix
    playerturn = 1
    matrix = [[0 for _ in range(3)] for _ in range(3)]


def KeyPress(key, x, y):
    global gameover, exit_requested , scores_updated
    if key == b'y':
        if gameover:
            gameover = False
            initgame()
            exit_requested = False  # Reset exit_requested when starting a new game
            scores_updated = False
    elif key == b'n':
        if gameover:
            if not exit_requested:
                os._exit(0)  # Terminate the program without raising an exception
    elif key == b'\x1b':#ESCKEY
        os._exit(0)

def click(button, state, x, y):
    global playerturn, matrix
    if not gameover and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        i = (y - 50) // 100
        j = x // 100
        if playerturn == 1:
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                playerturn = 2
        else:
            if matrix[i][j] == 0:
                matrix[i][j] = 2
                playerturn = 1


def drawString(s, x, y):
    glRasterPos2f(x, y)
    for char in s:
        glutBitmapCharacter(font, char)


def drawlines():

    glColor3f(0, 0, 0)
    draw_lines(100, 50, 100, 340)

    draw_lines(200, 50, 200, 340)

    draw_lines(0,150,300,150)

    draw_lines(0,250,300,250)

def drawxo():
    circle_radius = 25  #
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 1:
                glColor3f(0.5, 0.0, 0.5)  # prpl
                x_center = 50 + j * 100
                y_center = 100 + i * 100
                x1 = x_center - circle_radius
                y1 = y_center - circle_radius
                x2 = x_center + circle_radius
                y2 = y_center + circle_radius
                draw_lines(x1, y1, x2, y2)  # /
                draw_lines(x1, y2, x2, y1)  # \
                glColor3f(0, 0, 0)  # Reset color to black

            elif matrix[i][j] == 2:
                # Draw O symbol using the MidpointCircle algorithm
                x_center = 50 + j * 100
                y_center = 100 + i * 100
                MidpointCircle(circle_radius, x_center, y_center)

def checkifwin():
    global player1score, player2score, scores_updated

    for i in range(3): #RW
        if matrix[i][0] != 0 and matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] == 1 and not scores_updated:  # p1 win
                player1score += 1
                scores_updated = True
            elif matrix[i][0] == 2 and not scores_updated:  # p2 win
                player2score += 1
                scores_updated = True
            return True
    for i in range(3): #CLM
        if matrix[0][i] != 0 and matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == 1 and not scores_updated:  # p1 win
                player1score += 1
                scores_updated = True
            elif matrix[0][i] == 2 and not scores_updated:  # p2 win
                player2score += 1
                scores_updated = True
            return True
    if matrix[0][0] != 0 and matrix[0][0] == matrix[1][1] == matrix[2][2]: #TL BR
        if matrix[0][0] == 1 and not scores_updated:  # p1 win
            player1score += 1
            scores_updated = True
        elif matrix[0][0] == 2 and not scores_updated:  # p2 win
            player2score += 1
            scores_updated = True
        return True
    if matrix[2][0] != 0 and matrix[2][0] == matrix[1][1] == matrix[0][2]: #TR BL
        if matrix[2][0] == 1 and not scores_updated:  # p1 win
            player1score += 1
            scores_updated = True
        elif matrix[2][0] == 2 and not scores_updated:  # p2 win
            player2score += 1
            scores_updated = True
        return True
    return False

def checkifdraw():
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return False
    return True

def display():
    global playerturn, result, gameover
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.85, 0.85, 0.85, 1.0)  # Light gray background
    glColor3f(0, 0, 0)
    if playerturn == 1:
        glColor3f(0.5, 0.0, 0.5)
        drawString(b"Player1's turn", 100, 30)
    else:
        glColor3f(random.random(), random.random(), random.random())
        drawString(b"Player2's turn", 100, 30)

    drawlines()
    drawxo()

    if checkifwin():
        if playerturn == 1:
            gameover = True
            result = 2
        else:
            gameover = True
            result = 1
    elif checkifdraw():
        gameover = True
        result = 0

    if gameover:

        glColor3f(0.5, 0.0, 0.5)
        drawString(b"Player 1 Score: " + str(player1score).encode(), 40, 240)
        glColor3f(random.random(), random.random(), random.random())
        drawString(b"Player 2 Score: " + str(player2score).encode(), 40, 265)

        glColor3f(1.0, 0.0, 0.0)
        drawString(b"Game Over!!!", 100, 160)
        if result == 0:
            glColor3f(1,0,1)
            drawString(b"It's a draw", 100, 185)
        if result == 1:
            glColor3f(0.5, 0.0, 0.5)
            drawString(b"Player1 wins", 95, 185)
        if result == 2:
            glColor3f(random.random(),random.random(),random.random())
            drawString(b"Player2 wins", 95, 185)
        glColor3f(0,0,0)
        drawString(b"Do you want to continue (y/n)", 40, 210)

    glutSwapBuffers()


def reshape(x, y):
    glViewport(0, 0, x, y)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, x, y, 0, 0, 1)
    glMatrixMode(GL_MODELVIEW)

##CALL EVERYTHING <3
initgame()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowPosition(100, 100)
glutInitWindowSize(300, 350)
glutCreateWindow(b"Tic Tac Toe")
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(KeyPress)
glutMouseFunc(click)
glutIdleFunc(display)
glutMainLoop()


