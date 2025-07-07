import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

pygame.display.set_caption('Space Invaders!')

playerimage = pygame.image.load('Player.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerimage, (x, y))

enemyimage = pygame.image.load('Enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 0.2

def enemy(x,y):
    screen.blit(enemyimage, (x,y))

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    screen.fill((255, 0, 0))

    if playerX<0:
        playerX=0
    elif playerX>=736:
        playerX = 736

    if enemyX<=0:
        enemyX_change = 0.3
    elif enemyX>=736:
        enemyX_change = -0.3

    if enemyY<=0:
        enemyY_change = 0.2
    elif enemyY>=300:
        enemyY_change = -0.2

    playerX = playerX_change+playerX
    player(playerX, playerY)
    enemyX+=enemyX_change
    enemyY+=enemyY_change
    enemy(enemyX, enemyY)
    pygame.display.update()