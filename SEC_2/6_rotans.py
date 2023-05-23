from math import *
from numpy import *
from OpenGL.GL import *
from OpenGL.GLUT import *

i = 0


def draw():
    global i
    glLineWidth(3)
    glPointSize(9)
    glClearColor(.5, .5, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glRotate(i, 0, 0, 1)
    glTranslated(.25, 0, 0)
    glRotate(10*i, 0, 0, 1)

    glBegin(GL_LINES)
    glColor3d(1, .5, .5)
    glVertex2d(.25, 0)
    glVertex2d(-.25, 0)
    glEnd()

    glBegin(GL_POINTS)
    glColor3d(0, 0, 0)
    glVertex2d(0, 0)
    glEnd()

    glLoadIdentity()
    glBegin(GL_LINE_STRIP)
    glColor3d(1, 1, 1)
    for j in arange(0, 360, 1):
        glVertex2d(.25*cos(j*pi/180), .25*sin(j*pi/180))
    glEnd()
    glutSwapBuffers()
    i += .5


def main():

    glutInit()
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(220, 112)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutCreateWindow("self rotation")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()
