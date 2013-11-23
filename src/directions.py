NORTH   = 0
EAST    = 1
SOUTH   = 2
WEST    = 3

class Direction:
    def __init__(self):
        self.currentDirection = NORTH
    
    def current(self):
        return self.currentDirection
    
    def steerRight(self):
        self.currentDirection = (self.currentDirection + 1) % 4
        #print "direction={0}".format(self.currentDirection)
        
    def steerLeft(self):
        self.currentDirection = (self.currentDirection + 3) % 4
        #print "direction={0}".format(self.currentDirection)