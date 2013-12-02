from OpenGL.GL import *
from objloader import *
from filenames import *
from directions import *

trailHeight = 5
trailWidth = 0.5

def drawBox(x1, y1, x2, y2):
    glBegin(GL_QUADS);
    glVertex3f(x1, y1, 0.1);
    glVertex3f(x2, y1, 0.1);
    glVertex3f(x2, y2, 0.1);
    glVertex3f(x1, y2, 0.1);
    glEnd();

    glBegin(GL_QUADS);
    glVertex3f(x1, y1, 0.1);
    glVertex3f(x1, y2, 0.1);
    glVertex3f(x1, y2, trailHeight);
    glVertex3f(x1, y1, trailHeight);
    glEnd();

    glBegin(GL_QUADS);
    glVertex3f(x1, y1, 0.1);
    glVertex3f(x2, y1, 0.1);
    glVertex3f(x2, y1, trailHeight);
    glVertex3f(x1, y1, trailHeight);
    glEnd();

    glBegin(GL_QUADS);
    glVertex3f(x1, y1, trailHeight);
    glVertex3f(x2, y1, trailHeight);
    glVertex3f(x2, y2, trailHeight);
    glVertex3f(x1, y1, trailHeight);
    glEnd();

class Player:
    def __init__(self):
        self.model = OBJ(Filenames.models.player, swapyz=True)
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = Direction()
        self.trailPoints = []
        self.saveTrailPoint()
        
    def saveTrailPoint(self):
        self.trailPoints.append((self.x, self.y))
    
    def steerRight(self):
        self.direction.steerRight()
        self.saveTrailPoint()
        
    def steerLeft(self):
        self.direction.steerLeft()
        self.saveTrailPoint()
        
    def step(self, enabled = True):
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
    
    def draw(self):
        glPushMatrix()
        glRotate(90, 1, 0, 0)

        glPushMatrix()
        glTranslate(self.x, self.y, 0)
        glRotate(-90 * self.direction.current(), 0, 0, 1)
        glScalef(3, 3, 3)
        glCallList(self.model.gl_list)
        glPopMatrix()

        glColor3f(1., 0., 0.)
        i = 0
        while (i <= len(self.trailPoints) - 2):
            x1 = self.trailPoints[i][0]
            y1 = self.trailPoints[i][1]
            x2 = self.trailPoints[i+1][0]
            y2 = self.trailPoints[i+1][1]
            if (x1 == x2): # vertical
                x1 -= trailWidth
                x2 += trailWidth
            if (y1 == y2): # horizontal
                y1 -= trailWidth
                y2 += trailWidth
            drawBox(x1, y1, x2, y2)
            i += 1
        i = len(self.trailPoints) - 1
        x1 = self.trailPoints[i][0]
        y1 = self.trailPoints[i][1]
        x2 = self.x
        y2 = self.y
        if (x1 == x2): # vertical
            x1 -= trailWidth
            x2 += trailWidth
        if (y1 == y2): # horizontal
            y1 -= trailWidth
            y2 += trailWidth
        # TODO: CLAMP TO MATCH LAST POINT
        if (self.direction.current() == NORTH):
            y2 -= 5
        elif (self.direction.current() == SOUTH):
            y2 += 5
        elif (self.direction.current() == WEST):
            x2 += 5
        elif (self.direction.current() == EAST):
            x2 -= 5
        drawBox(x1, y1, x2, y2)
        glPopMatrix()