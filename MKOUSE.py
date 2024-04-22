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

        elif event.type==pygame.MOUSEBUTTONDOWN:
            print(f'Нажата кнопка под номером: {event.button}')
        elif event.type==pygame.MOUSEMOTION:
            print(f'Позиция мыши: {event.pos}')
"""elif event.type==pygame.MOUSEMOTION:
     print(f'Позиция мыши: {event.rel}') разница от перемещения"""


    wind.fill(DAR)


    pygame.display.update()
    clock.tick(FPS)
