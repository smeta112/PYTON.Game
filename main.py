import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("First Programm")

WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

while True:
#while flRun:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           # pygame.quit()

        #elif event.type == pygame.QUIT:
            exit()

    pygame.draw.rect(screen, BLUE, (10, 10, 50, 30), 5) #5 - тощина линии
    pygame.draw.line(screen, RED, (10, 50), (60, 50), 5)
    pygame.draw.aaline(screen, GREEN, (50, 90), (100, 90), 5)

    pygame.draw.polygon(screen, WHITE, [[100, 100], [170, 130], [190, 95]], 4)
    pygame.draw.circle(screen, BLUE, (300, 250), 50)
    pygame.draw.ellipse(screen, BLUE, (240, 70, 150, 70), 5) #5 - тощина линии

    pygame.display.update()







