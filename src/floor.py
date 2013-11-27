from OpenGL.GL import *
from objloader import *
from filenames import *

class Floor:
    def __init__(self, size, tileSize, y = 0):
        self.size = size
        self.tileSize = tileSize
        self.width = self.depth = size * tileSize
        self.y = 0
        self.texture = load2DTexture(Filenames.textures.floor_tile)
        
    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glPushMatrix()
        glBegin(GL_QUADS)
        glTexCoord2d(0.0, 0.0)
        glNormal3f(0., 1., 0.)
        glVertex3f(0, self.y, 0)
        
        glTexCoord2f(1.0*self.size, 0.0)
        glNormal3f(0.0,1.0,0.0)
        glVertex3f(self.size*self.tileSize, self.y, 0)
        
        glTexCoord2f(1.0*self.size, 1.0*self.size)
        glNormal3f(0.0,1.0,0.0)
        glVertex3f(self.size*self.tileSize, self.y, self.size*self.tileSize)
        
        glTexCoord2f(0.0, 1.0*self.size)
        glNormal3f(0.0,1.0,0.0)
        glVertex3f(0, self.y, self.size*self.tileSize)
        glEnd()
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)
