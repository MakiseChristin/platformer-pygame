import pygame

pygame.init()
lent = 1280
bret = 720
sc = pygame.display.set_mode((lent, bret))
pygame.display.set_caption('Platformer')
bg1 = pygame.image.load("pic.png").convert()
bg2 = pygame.image.load("pic.png").convert()
px1 = bg1.get_width()
py1 = bg1.get_height()
px2 = bg1.get_width()
clock = pygame.time.Clock()
x = 0
x2 = px2

neko = True
while neko:
    x2 -= 10
    x -= 10
    sc.blit(bg1, [x, 0])
    sc.blit(bg2, [x2, 0])
    if x < px1*(-1):
        x = px1
    if x2 < px2*(-1):
        x2 = px2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            neko = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()
