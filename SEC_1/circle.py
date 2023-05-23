from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


def draw():
    glLineWidth(3)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(1, .5, .5, 1)
    glBegin(GL_LINE_LOOP)
    for i in range(0, 360, 1):
        x = .5 * sin(i * pi / 180)
        y = .5 * cos(i * pi / 180)
        glVertex2d(x, y)
    glEnd()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(112, 240)
    glutInitDisplayMode(GLUT_DOUBLE, GLUT_RGBA)
    glutCreateWindow(b"hi there")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()
