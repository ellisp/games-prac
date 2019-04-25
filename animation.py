import pygame, sys, time
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Animation')

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

dirty = 80

WHITE = (255, 255, 255)
RED = (255 - dirty, dirty, dirty)
GREEN = (dirty, 255 - dirty, dirty)
BLUE = (dirty, dirty, 255 - dirty)

b1 = {'rect':pygame.Rect(300, 80 , 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150 , 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    windowSurface.fill(WHITE)

    for b in boxes:

        # Move the box
        if b['dir'] == DOWNLEFT:
             b['rect'].left -= MOVESPEED
             b['rect'].top  += MOVESPEED
        if b['dir'] == DOWNRIGHT:
             b['rect'].left += MOVESPEED
             b['rect'].top  += MOVESPEED
        if b['dir'] == UPLEFT:
             b['rect'].left -= MOVESPEED
             b['rect'].top  -= MOVESPEED
        if b['dir'] == UPRIGHT:
             b['rect'].left += MOVESPEED
             b['rect'].top  -= MOVESPEED


        # check if box has moved out of window
        if b['rect'].top < 0:
             if b['dir'] == UPLEFT:
                 b['dir'] = DOWNLEFT
             if b['dir'] == UPRIGHT:
                 b['dir'] == DOWNRIGHT

        if b['rect'].bottom > WINDOWHEIGHT:
             if b['dir'] == DOWNLEFT:
                 b['dir'] = UPLEFT
             if b['dir'] == DOWNRIGHT:
                 b['dir'] = UPRIGHT

        if b['rect'].left < 0:
             if b['dir'] == DOWNLEFT:
                 b['dir'] = DOWNRIGHT
             if b['dir'] == UPLEFT:
                 b['dir'] = UPRIGHT

        if b['rect'].left > WINDOWWIDTH:
             if b['dir'] == DOWNRIGHT:
                 b['dir'] = DOWNLEFT
             if b['dir'] == UPRIGHT:
                 b['dir'] = UPLEFT

        # draw box on surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # draw the window on screen
    pygame.display.update()
    time.sleep(0.02)
