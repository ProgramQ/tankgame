import pygame,sys
from pygame.locals import *
import MAP

class Cloud:
    def __init__(self):
        self.cloud = pygame.image.load("cloud.png").convert_alpha()
        self.rect = pygame.rect.Rect(-64,50, 60, 28)
    
    def draw(self, surface):
        surface.blit(self.cloud, self.rect)

    def update(self):
        self.rect.x += 1


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAP.MAPWIDTH * MAP.TILESIZE, MAP.MAPHEIGHT * MAP.TILESIZE))

pygame.display.set_caption('Tank Game')
DISPLAYSURF.fill((10, 218, 255))

mcloud = Cloud()

while True:
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
 
    #loop through each row
    for row in range(MAP.MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAP.MAPWIDTH):
            #draw the resource at that position in the tilemap.
            if MAP.tilemap[row][column] == 1:
                pygame.draw.rect(DISPLAYSURF, (210,180,140), (column * MAP.TILESIZE, row * MAP.TILESIZE, MAP.TILESIZE, MAP.TILESIZE))
 
    mcloud.update()
    mcloud.draw(DISPLAYSURF)

    #update the display
    pygame.display.update()