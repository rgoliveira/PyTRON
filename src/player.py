from OpenGL.GL import *
from objloader import *
from filenames import *
from directions import *

def drawTrail(x1, y1, x2, y2, width = 5., height = 3., color = (1., 0., 0., 0.8), playerTrail = False):
    glColor4f(color[0], color[1], color[2], color[3])
    glPushMatrix()
    
    distanceFromPlayer = 5.1
    
    if (x1 == x2): # vertical
        x1 -= width/2
        x2 += width/2
        if (y1 < y2):
            y1 -= width/2 # south to north
            if (playerTrail):
                y2 = max(y2-distanceFromPlayer, y1)
        else:
            y1 += width/2 # north to south
            if (playerTrail):
                y2 = min(y2+distanceFromPlayer, y1)

    elif (y1 == y2): # horizontal
        y1 -= width/2
        y2 += width/2
        if (x1 < x2): 
            x1 -= width/2 # west to east
            if (playerTrail):
                x2 = max(x2-distanceFromPlayer, x1)
        else:
            x1 += width/2 # east to west
            if (playerTrail):
                x2 = min(x2+distanceFromPlayer, x1)

    glBegin(GL_QUADS);
    glVertex3f(x1, y1, height);
    glVertex3f(x1, y2, height);
    glVertex3f(x1, y2, 0.);
    glVertex3f(x1, y1, 0.);
    glEnd();

    glBegin(GL_QUADS);
    glVertex3f(x1, y1, 0.1);
    glVertex3f(x2, y1, 0.1);
    glVertex3f(x2, y1, height);
    glVertex3f(x1, y1, height);
    glEnd();
    
    glBegin(GL_QUADS);
    glVertex3f(x1, y1, height);
    glVertex3f(x2, y1, height);
    glVertex3f(x2, y2, height);
    glVertex3f(x1, y2, height);
    glEnd();
    
    glPopMatrix()

class Player:
    def __init__(self, x, y):
        self.model = OBJ(Filenames.models.player, swapyz=True)
        self.x = x
        self.y = y
        self.z = 0.
        self.direction = Direction()
        self.trailPoints = []
        self.saveTrailPoint()
        self.killed = False
        #self.trailMatrix = {}
        
    def saveTrailPoint(self):
        self.trailPoints.append((self.x, self.y))
    
    def steerRight(self):
        self.direction.steerRight()
        self.saveTrailPoint()
        
    def steerLeft(self):
        self.direction.steerLeft()
        self.saveTrailPoint()
        
    def step(self, trailMatrix, enabled = True):
        if(not trailMatrix.has_key(self.x)):
           trailMatrix[self.x] = [self.y]
        else:
           trailMatrix[self.x].append(self.y)
        if((self.x > 200 or self.x < 0) or (self.y > 200 or self.y < 0)):
            self.killed = True
        else:			
            if (not enabled):
              return
            increment = 0.5
            if (self.direction.current() == NORTH):
                 self.y += increment
            elif (self.direction.current() == SOUTH):
                 self.y -= increment
            elif (self.direction.current() == EAST):
                 self.x += increment
            elif (self.direction.current() == WEST):
                 self.x -= increment

            if(trailMatrix.has_key(self.x)):
               if(self.y in trailMatrix[self.x]):
                 self.killed = True	
				 
    def robotStep(self, trailMatrix, player, enabled = True):
        if(not trailMatrix.has_key(self.x)):
           trailMatrix[self.x] = [self.y]
        else:
           trailMatrix[self.x].append(self.y)
        if((self.x > 200 or self.x < 0) or (self.y > 200 or self.y < 0)):
            self.killed = True
        else:			
            if (not enabled):
              return
            increment = 0.5
            if(player.x <= self.x) and (player.y < self.y):
              if(self.direction.current() == NORTH):
                  self.steerLeft()
				  
            if (self.direction.current() == NORTH):
                 self.y += increment
            elif (self.direction.current() == SOUTH):
                 self.y -= increment
            elif (self.direction.current() == EAST):
                 self.x += increment
            elif (self.direction.current() == WEST):
                 self.x -= increment

            if(trailMatrix.has_key(self.x)):
               if(self.y in trailMatrix[self.x]):
                 self.killed = True	
   
    def removeTrail(self, trailMatrix):
       i = 0
       while(i <= len(self.trailPoints) - 2):
            if(self.trailPoints[i][0] == self.trailPoints[i+1][0]):
              y_min = min(self.trailPoints[i][1], self.trailPoints[i+1][1])
              while(y_min <= max(self.trailPoints[i][1], self.trailPoints[i+1][1])):
                if(y_min in trailMatrix[self.trailPoints[i][0]]):
                     trailMatrix[self.trailPoints[i][0]].remove(y_min)
                y_min += 0.5
            else:
              x_min = min(self.trailPoints[i][0], self.trailPoints[i+1][0])
              while(x_min <= max(self.trailPoints[i][1], self.trailPoints[i+1][1])):
                 if(self.trailPoints[i][1] in trailMatrix[x_min]):
                    trailMatrix[x_min].remove(self.trailPoints[i][1])
              x_min += 0.5
            i += 1	   
       
    def reset(self, x, y, trailMatrix):
        self.x = x
        self.y = y
        self.z = 0.
        self.direction = Direction()
        self.trailPoints = []
        self.saveTrailPoint()	
        self.killed = False
        trailMatrix = {}
		

    def was_killed(self):
        return 	self.killed

    def draw(self):
        glPushMatrix()
        glRotate(90, 1, 0, 0)

        glPushMatrix()
        glTranslate(self.x, self.y, 0)
        glRotate(-90 * self.direction.current(), 0, 0, 1)
        glScalef(3, 3, 3)
        glCallList(self.model.gl_list)
        glPopMatrix()

        trailWidth = 2
        i = 0
        while (i <= len(self.trailPoints) - 2):
            x1 = self.trailPoints[i][0]
            y1 = self.trailPoints[i][1]
            x2 = self.trailPoints[i+1][0]
            y2 = self.trailPoints[i+1][1]
            drawTrail(x1, y1, x2, y2, width = trailWidth)
            i += 1
        i = len(self.trailPoints) - 1
        x1 = self.trailPoints[i][0]
        y1 = self.trailPoints[i][1]
        x2 = self.x
        y2 = self.y
        drawTrail(x1, y1, x2, y2, width = trailWidth, playerTrail = True)
        
        glPopMatrix()