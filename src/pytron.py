import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from player import *
from floor import *
from directions import *
from camera import *

def setup():
    pygame.init()
    viewport = (1024,768)
    pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    glLightfv(GL_LIGHT0, GL_POSITION,   (viewport[0]/2, 0, viewport[1]/2, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT,    (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,    (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    global clock
    clock   = pygame.time.Clock()
    
    global player
    player  = Player(0., 0.)
    
    global enemy
    enemy = Player(200., 0.)

    global trailMatrix
    trailMatrix	= {}
    
    global floor
    floor   = Floor(size=20, tileSize=10)
    
    global camera
    camera  = Camera(viewport, (floor.size*floor.tileSize, floor.size*floor.tileSize))
    camera.bindToPlayer(player)
    
    global playerEnabled
    playerEnabled = True

def drawAxis():
    glPushMatrix()
    glLoadIdentity()
    glTranslate(-1, -1, -1)
    
    glLineWidth(2)
    
    glColor3f(1,0,0)
    
    glBegin(GL_LINES)
    glVertex3f(0,0,0)
    glVertex3f(5,0,0)
    glEnd()
    
    glColor3f(0,1,0)
    glBegin(GL_LINES)
    glVertex3f(0,0,0)
    glVertex3f(0,5,0)
    glEnd()
    
    glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex3f(0,0,0)
    glVertex3f(0,0,5)
    glEnd()
    glPopMatrix()

def render():
    # camera operations
    camera.set()
    
    # setup ModelView
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawAxis()
    glLoadIdentity()
    glRotate(270, 1, 0, 0) # ajusta eixos
    
    # render game objects
    floor.draw()
    player.draw()
    if(not enemy.was_killed()):
       enemy.draw()
    
    # update screen
    pygame.display.flip()

def handleInputEvent(e):
    if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            sys.exit()
    elif e.type == KEYDOWN:
        ### camera
        # change mode
        if e.key == K_c:
            camera.changeMode()
        
        ### player
        elif e.key == K_d:
            if (camera.mode == CM_Perspective):
                player.steerRight()
            elif (camera.mode == CM_Ortho):
                if (player.direction.current() == NORTH):
                    player.steerRight()
                elif (player.direction.current() == SOUTH):
                    player.steerLeft()
            
        elif e.key == K_w:
            if (camera.mode == CM_Ortho):
                if (player.direction.current() == WEST):
                    player.steerRight()
                elif (player.direction.current() == EAST):
                    player.steerLeft()

        elif e.key == K_a:
            if (camera.mode == CM_Perspective):
                player.steerLeft()
            elif (camera.mode == CM_Ortho):
                if (player.direction.current() == NORTH):
                    player.steerLeft()
                elif (player.direction.current() == SOUTH):
                    player.steerRight()
            
        elif e.key == K_s:
            if (camera.mode == CM_Ortho):
                if (player.direction.current() == WEST):
                    player.steerLeft()
                elif (player.direction.current() == EAST):
                    player.steerRight()

def run():
    setup()
    while 1:
        clock.tick(100)
        
        ### handle inputs
        for e in pygame.event.get():
            handleInputEvent(e)

        ### game logic
        if(not player.was_killed()):
            player.step(trailMatrix, playerEnabled)
            if(not enemy.was_killed()):
               enemy.robotStep(trailMatrix, player, playerEnabled)
            else:
               enemy.removeTrail(trailMatrix)
        else:
           global trailMatrix 
           trailMatrix = {}
           player.reset(0.,0., trailMatrix)
           enemy.reset(200.,0., trailMatrix)
           camera.bindToPlayer(player)

        ### drawing
        render()

run()