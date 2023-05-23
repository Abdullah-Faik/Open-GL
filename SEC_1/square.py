from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
	glClearColor(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3d(1, .5, .5, 1)
	glBegin(GL_QUADS)
	glVertex2d(0, 0)
	glVertex2d(0, .5)
	glVertex2d(.5, .5)
	glVertex2d(.5, 0)
	glEnd()
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
