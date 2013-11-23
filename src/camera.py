from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from directions import *

CM_Ortho        = 1
CM_Perspective  = 2

class Camera:
    def __init__(self, viewport = (800, 600)):
        self.mode = CM_Ortho
        self.x = 0
        self.y = 0
        self.z = 5
        self.viewport = viewport
        self.direction = Direction()
        self.player = None
    
    def bindToPlayer(self, player):
        self.player = player
        self.direction = player.direction
    
    def unbindFromPlayer(self):
        self.player = None
        self.direction = Direction()
    
    def changeMode(self):
        self.mode = (self.mode % 2) + 1

    def set(self):
        if (self.player != None):
            # self.direction doesn't to be set everytime, since it's a reference
            # to self.player.direction. That's not the case for self.x and 
            # self.y, since they're integers.
            self.x = self.player.x
            self.y = self.player.y

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if (self.mode == CM_Ortho):
            glOrtho(-10, 810, -10, 610, -5, 100)
            glRotate(0, 0, 0, 1)
        elif (self.mode == CM_Perspective):
            gluPerspective(120.0, self.viewport[0]/float(self.viewport[1]), 1, 100.0)
            glRotate(-70, 1, 0, 0) # set camera from behind
            distanceFromPlayer = 3
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
            
            #glTranslate(tx/20., ty/20., - zpos)
            glTranslate(-self.x + adjustmentX, -self.y + adjustmentY, - self.z)
            #glRotate(ry, 1, 0, 0)
        #glRotate(rx, 0, 0, 1)
        
        glEnable(GL_DEPTH_TEST)
        