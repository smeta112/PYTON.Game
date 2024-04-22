import pygame
pygame.init()

W = 500
H = 500
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COL = (35, 117, 99)
DAR = (6, 18, 23)

wind = pygame.display.set_mode((W,H))
pygame.display.set_caption("Обработка событий с клавиатуры")
clock = pygame.time.Clock()

x = W//2
y = H//2

move=0
speed = 5


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and event.mod==pygame.KMOD_LCTRL:
                move-=speed
            elif event.key==pygame.K_RIGHT and event.mod==pygame.KMOD_LCTRL:
                move+=speed

        elif event.type==pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                move=0

    x+=move

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=5
    elif keys[pygame.K_RIGHT]:
        x+=5
    elif keys[pygame.K_UP]:
        y -= 5
    elif keys[pygame.K_DOWN]:
        y += 5

    wind.fill(DAR)
    pygame.draw.rect(wind, COL, (x, y, 20, 50), 3)

    pygame.display.update()
    clock.tick(FPS)











'''pygame.quit()
           flRun = False'''
