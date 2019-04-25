import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1200
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Collision Detection")

dirty = 80
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255 - dirty, dirty, dirty)
GREEN = (dirty, 255 - dirty, dirty)
BLUE = (dirty, dirty, 255 - dirty)

playerImage = pygame.image.load('InventWithPython_resources/player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('InventWithPython_resources/cherry.png')


foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                             random.randint(0, WINDOWHEIGHT - FOODSIZE),
                             FOODSIZE,
                             FOODSIZE))

# movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6

# Set up the music.
pickUpSound = pygame.mixer.Sound('InventWithPython_resources/pickup.wav')
pygame.mixer.music.load('InventWithPython_resources/background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True


# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == K_w:
                moveUp =  True
                moveDown = False
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
                
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
                
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                                 random.randint(0, WINDOWHEIGHT - FOODSIZE),
                                 FOODSIZE,
                                 FOODSIZE))
                                 
    windowSurface.fill(WHITE)
     
    # move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
        
    # Draw the block onto the surface.
    windowSurface.blit(playerStretchedImage, player)



    # check for intersection with foodCounter
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()
				
    # draw the food
    for food in foods:
        windowSurface.blit(foodImage, food)
        
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
