import pygame    #BASE
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("First Programm")


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            exit()

    pygame.display.update()

