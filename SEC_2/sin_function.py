from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *

def draw():
	glLineWidth(3)
	glClearColor(.5,.5,1,1)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3d(1,1,1)
	glBegin(GL_LINES)
	glVertex2d(-1,0)
	glVertex2d(1,0)
	glVertex2d(0,1)
	glVertex2d(0,-1)
	glEnd()
	glColor3d(1,0.5,0.5)
	glBegin(GL_LINES)
	freq = 5
	for j in arange (-freq,freq,1):
		for i in arange(0,360,1):
			p = j / freq + i / (freq *360)
			q = .6 * cos( pi * i / 180)
			glVertex2d(p,q)
	glEnd()

	glFlush()

def main():
	glutInit()
	glutInitWindowSize(800,800)
	glutInitWindowPosition(220,112)
	glutInitDisplayMode(GLUT_SINGLE,GLUT_RGB)
	glutCreateWindow(b"human")
	glutDisplayFunc(draw)
	glutMainLoop()

if __name__ == "__main__":
	main()