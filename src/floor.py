from OpenGL.GL import *
from objloader import *
from filenames import *

class Floor:
    def __init__(self, size, tileSize, y = 0):
        self.size = size
        self.tileSize = tileSize
        self.width = self.depth = size * tileSize
        self.y = 0
        self.wallHeight = 15
        self.texture = load2DTexture(Filenames.textures.floor_tile)
        self.wallTexture = load2DTexture(Filenames.textures.wall_tile)
        self.skyTexture = load2DTexture(Filenames.textures.sky)
        
    def draw(self):
        glPushMatrix()
        
        ## floor
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
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
        glDisable(GL_TEXTURE_2D)
        
        ## sky
        """
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.skyTexture)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        """
        glColor3f(1., 0., 0.)
        
        glBegin(GL_QUADS)
        glTexCoord2d(0.0, 0.0)
        glNormal3f(0., -1., 0.)
        glVertex3f(0, self.wallHeight, 0)        
        
        glTexCoord2f(1.0*self.size, 0.0)
        glNormal3f(0.0,-1.0,0.0)
        glVertex3f(self.size*self.tileSize, self.wallHeight, 0)
        
        glTexCoord2f(1.0*self.size, 1.0*self.size)
        glNormal3f(0.0,-1.0,0.0)
        glVertex3f(self.size*self.tileSize, self.wallHeight, self.size*self.tileSize)
        
        glTexCoord2f(0.0, 1.0*self.size)
        glNormal3f(0.0,-1.0,0.0)
        glVertex3f(0, self.wallHeight, self.size*self.tileSize)
        glEnd()
        #glDisable(GL_TEXTURE_2D)
        
        ### walls
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.wallTexture)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
        ## west wall
        glBegin(GL_QUADS)
        glTexCoord2f(0., 0.)
        glNormal3f(0.5, 0., 0.5)
        glVertex3f(0, self.y, 0)
        
        glTexCoord2f(0., 1)
        glNormal3f(0.5, 0., 0.5)
        glVertex3f(0, -self.wallHeight, 0)
        
        glTexCoord2f(1, 1)
        glNormal3f(0.5, 0., -0.5)
        glVertex3f(0, -self.wallHeight, self.size*self.tileSize)
        
        glTexCoord2f(1, 0)
        glNormal3f(0.5, 0., -0.5)
        glVertex3f(0, 0, self.size*self.tileSize)
        glEnd()
        
        ## south wall
        glBegin(GL_QUADS)
        
        glTexCoord2f(1, 0.)
        glNormal3f(0.5, 0., 0.5)
        glVertex3f(0, self.y, 0)
        
        glTexCoord2f(0. ,0.)
        glNormal3f(-0.5, 0., 0.5)
        glVertex3f(self.size*self.tileSize, self.y, 0)
        
        glTexCoord2f(0., 1)
        glNormal3f(-0.5, 0., 0.5)
        glVertex3f(self.size*self.tileSize, -self.wallHeight, 0)
        
        glTexCoord2f(1, 1)
        glNormal3f(0.5, 0., 0.5)
        glVertex3f(0, -self.wallHeight, 0)
        glEnd()
        
        ## east wall
        glBegin(GL_QUADS)
        glTexCoord2f(1, 0)
        glNormal3f(-0.5, 0., 0.5)
        glVertex3f(self.size*self.tileSize, self.y, 0)
        
        glTexCoord2f(0., 0.)
        glNormal3f(-0.5, 0., -0.5)
        glVertex3f(self.size*self.tileSize, self.y, self.size*self.tileSize)
        
        glTexCoord2f(0., 1)
        glNormal3f(-0.5, 0., -0.5)
        glVertex3f(self.size*self.tileSize, -self.wallHeight, self.size*self.tileSize)
        
        glTexCoord2f(1, 1)
        glNormal3f(-0.5, 0., 0.5)
        glVertex3f(self.size*self.tileSize, -self.wallHeight, 0)
        glEnd()
        
        ## north wall
        glBegin(GL_QUADS)
        glTexCoord2f(0., 0.)
        glNormal3f(0.5, 0., -0.5)
        glVertex3f(0, self.y, self.size*self.tileSize)
        
        glTexCoord2f(1, 0)
        glNormal3f(-0.5, 0., -0.5)
        glVertex3f(self.size*self.tileSize, self.y, self.size*self.tileSize)
        
        glTexCoord2f(1, 1)
        glNormal3f(-0.5, 0., -0.5)
        glVertex3f(self.size*self.tileSize, -self.wallHeight, self.size*self.tileSize)
        
        glTexCoord2f(0., 1)
        glNormal3f(0.5, 0., -0.5)
        glVertex3f(0, -self.wallHeight, self.size*self.tileSize)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        
        glPopMatrix()
