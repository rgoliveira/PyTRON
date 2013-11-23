from OpenGL.GL import *
from objloader import *
from filenames import *
from directions import *

class Player:
    def __init__(self):
        self.model = OBJ(Filenames.models.player, swapyz=True)
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = Direction()
        
    def steerRight(self):
        self.direction.steerRight()
        
    def steerLeft(self):
        self.direction.steerLeft()
        
    def step(self):
        increment = 0.5
        if (self.direction.current() == NORTH):
            self.y += increment
        elif (self.direction.current() == SOUTH):
            self.y -= increment
        elif (self.direction.current() == EAST):
            self.x += increment
        elif (self.direction.current() == WEST):
            self.x -= increment
    
    def draw(self):
        glPushMatrix()
        glRotate(90, 1, 0, 0)
        glTranslate(self.x, self.y, 0)
        glRotate(-90 * self.direction.current(), 0, 0, 1)
        glCallList(self.model.gl_list)
        glPopMatrix()

