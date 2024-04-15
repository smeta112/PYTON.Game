import pygame
pygame.init()

W = 600
H = 400

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("First Programm")

ccllock = pygame.time.Clock()
FPS = 100

x = W//2 #int
y = H//2


WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

flRight = flLeft = False
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x+=5
    elif keys[pygame.K_RIGHT]:
        x-=5

    screen.fill((125, 76, 148))  #Каждый раз перезаливка

    pygame.draw.rect(screen, BLUE, (x, y, 50, 30))
    pygame.display.update()
    ccllock.tick(FPS)





"""
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            flRight=True
        elif event.key == pygame.K_LEFT:
            flLeft=True
    elif event.type == pygame.KEYUP:
        if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
            flRight = flLeft = False

if flRight:
    x+=5
elif flLeft:
    x-=5
"""