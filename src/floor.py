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
        for i in range(self.size):
            for j in range(self.size):
                glBegin(GL_QUADS)
                glTexCoord2f(0.0, 0.0);
                glNormal3f(0.0,1.0,0.0)
                glVertex3f(i*self.size, self.y, j*self.size)
                
                glTexCoord2f(1.0, 0.0)
                glNormal3f(0.0,1.0,0.0)
                glVertex3f(i*self.size + self.size, self.y, j*self.size)

                glTexCoord2f(1.0, 1.0)
                glNormal3f(0.0,1.0,0.0)
                glVertex3f(i*self.size + self.size, self.y, j*self.size + self.size)

                glTexCoord2f(0.0, 1.0)
                glNormal3f(0.0,1.0,0.0)
                glVertex3f(i*self.size, self.y, j*self.size + self.size)
                glEnd()
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)
