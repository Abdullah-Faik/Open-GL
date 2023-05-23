from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


def circle(r, theta):
    glPushMatrix()
    glBegin(GL_LINE_STRIP)
    for i in range(-theta, theta, 1):
        glVertex2d(r * sin(i * pi / 180), r * cos(i * pi / 180))
    glEnd()
    glPopMatrix()


def draw():
    glLoadIdentity()
    glLineWidth(3)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3d(1, .5, .5, 1)
    circle(.9, 180)

    glTranslated(.4, .4, 0)
    circle(.15, 180)

    glLoadIdentity()
    glTranslated(-.4, .4, 0)
    circle(.15, 180)

    glLoadIdentity()
    glRotated(180, 0, 0, 1)
    circle(.5, 70)
    
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(112, 240)
    glutInitDisplayMode(GLUT_SINGLE, GLUT_RGBA)
    glutCreateWindow(b"hi there")
    glutDisplayFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()
