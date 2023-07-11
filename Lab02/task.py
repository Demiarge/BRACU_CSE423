from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

work_done = False
xen = None
xen1 = None
string_to_force_it_to_run_only_Onetime = 0
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

    if work_done:
        x1+=200
        x2+=200

    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    px1, py1 = convert_to_zone0(zone, x1, y1)
    px2, py2 = convert_to_zone0(zone, x2, y2)

    midpointline(px1, py1, px2, py2, zone)

def lets_draw_the_number(number):
    global work_done

    number_draw_functions = {
        0: [
            (100, 350, 200, 350),
            (100, 350, 100, 150),
            (100, 150, 200, 150),
            (200, 350, 200, 150)
        ],
        1: [
            (150, 350, 150, 150)
        ],
        2: [
            (100, 350, 200, 350),
            (200, 350, 200, 250),
            (100, 250, 200, 250),
            (100, 250, 100, 150),
            (100, 150, 200, 150)
        ],
        3: [
            (100, 350, 200, 350),
            (200, 350, 200, 250),
            (100, 250, 200, 250),
            (200, 250, 200, 150),
            (100, 150, 200, 150)
        ],
        4: [
            (100, 350, 100, 250),
            (100, 250, 200, 250),
            (200, 350, 200, 150)
        ],
        5: [
            (100, 350, 200, 350),
            (100, 350, 100, 250),
            (100, 250, 200, 250),
            (200, 250, 200, 150),
            (100, 150, 200, 150)
        ],
        6: [
            (100, 350, 200, 350),
            (100, 350, 100, 150),
            (100, 250, 200, 250),
            (200, 250, 200, 150),
            (100, 150, 200, 150)
        ],
        7: [
            (100, 350, 200, 350),
            (115, 275, 200, 275),
            (200, 350, 150, 150)
        ],
        8: [
            (100, 350, 200, 350),
            (100, 250, 200, 250),
            (100, 150, 200, 150),
            (100, 350, 100, 150),
            (200, 350, 200, 150)
        ],
        9: [
            (100, 350, 200, 350),
            (100, 250, 200, 250),
            (200, 350, 200, 150),
            (100, 350, 100, 250),
            (100, 150, 200, 150)
        ]
    }

    if number in number_draw_functions:
        for line in number_draw_functions[number]:
            draw_lines(*line)

    work_done = True

def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global xen, xen1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 1)

    if xen in range(10):
        lets_draw_the_number(xen)
    if xen1 in range(10):
        lets_draw_the_number(xen1)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
lets_take_input_here = input("Please type your 8 digit student ID: ")
while len(lets_take_input_here) != 8 or not lets_take_input_here.isdigit():
    print("Please provide a valid 8 digit student ID.")
    lets_take_input_here = input("Please type your 8 digit student ID: ")

xen = int(lets_take_input_here[-2])
xen1 = int(lets_take_input_here[-1])
window_title = f"Student ID: {lets_take_input_here} | Let's Draw: {xen}{xen1}"
wind = glutCreateWindow(window_title.encode())

glutDisplayFunc(showScreen)
glutMainLoop()

