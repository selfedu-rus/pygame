import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Rect")
pygame.display.set_icon(pygame.image.load("app.bmp"))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()

ground = H-70           # высота земли
jump_force = 20         # сила прыжка
move = jump_force+1     # текущая вертикальная скорость

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=W//2)

print(rect)
rect.bottom = ground
print(rect)

rect_update = pygame.Rect(rect.x, 0, rect.width, ground)
sc.fill(WHITE)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force

    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force+1

    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.update(rect_update)

    clock.tick(FPS)
