from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from directions import *

CM_Ortho        = 1
CM_Perspective  = 2

class Camera:
    def __init__(self, viewport = (800, 600), gameArea = (800, 600)):
        self.mode = CM_Ortho
        self.x = 0
        self.y = 0
        self.z = 5
        self.viewport = viewport
        self.gameArea = gameArea
        self.direction = Direction()
        self.boundPlayer = None
    
    def bindToPlayer(self, player):
        self.boundPlayer = player
        self.direction = player.direction
    
    def unbindFromPlayer(self):
        self.boundPlayer = None
        self.direction = Direction()
    
    def changeMode(self):
        self.mode = (self.mode % 2) + 1

    def set(self):
        if (self.boundPlayer != None):
            # self.direction doesn't to be set everytime, since it's a reference
            # to self.boundPlayer.direction. That's not the case for self.x and 
            # self.y, since they're integers.
            self.x = self.boundPlayer.x
            self.y = self.boundPlayer.y

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if (self.mode == CM_Ortho):
            offset = 10
            glOrtho(-offset, self.gameArea[0] + offset, -offset, self.gameArea[1] + offset, -5, 10)
            glRotate(0, 0, 0, 1)
        elif (self.mode == CM_Perspective):
            gluPerspective(120.0, self.viewport[0]/float(self.viewport[1]), 1, max(self.viewport[0], self.viewport[1]))
            glRotate(-70, 1, 0, 0) # set camera from behind
            distanceFromPlayer = 5
            adjustmentX = 0
            adjustmentY = 0
            if (self.direction.current() == NORTH):
                adjustmentY = distanceFromPlayer
            elif (self.direction.current() == EAST):
                glRotate(90, 0, 0, 1)
                adjustmentX = distanceFromPlayer
            elif (self.direction.current() == SOUTH):
                glRotate(180, 0, 0, 1)
                adjustmentY = -distanceFromPlayer
            elif (self.direction.current() == WEST):
                glRotate(-90, 0, 0, 1)
                adjustmentX = -distanceFromPlayer
            glTranslate(-self.x + adjustmentX, -self.y + adjustmentY, - self.z)
