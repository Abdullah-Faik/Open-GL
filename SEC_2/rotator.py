from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math

i = 0


def draw():
    global i
    glClearColor(.5, .5, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3d(1, .5, .5, 1)
    glRotatef(i, 0, 0, 1)
    glBegin(GL_QUADS)
    glVertex2d(-.5, -.5)
    glVertex2d(0.5, -.5)
    glVertex2d(.5, .5)
    glVertex2d(-.5, .5)
    glEnd()
    glutSwapBuffers()
    i += 1


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
