# Libraries used
import pygame

# Initiate the pygame module
pygame.init()

# Variables
lent = 1280
bret = 720
sc = pygame.display.set_mode((lent, bret))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]

# Loading image and its properties
bg1 = pygame.image.load("pic.png").convert()
bg2 = pygame.image.load("pic.png").convert()
px1 = bg1.get_width()
py1 = bg1.get_height()
px2 = bg1.get_width()
x = 0
x2 = px2
neko = True
rs = 40
rx = rs + 20
ry = 498 - rs
xvel = 10


# Keep the game loop running and prevent it from closing automatically
def run():
    global neko
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            neko = False
            quit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                neko = False
                quit()
                pygame.quit()

# Boxes
def box(color, xc, yc, s1, s2):
    pygame.draw.rect(sc, color, [xc, yc, s1, s2])

# Main game loop
while neko:
    run()

    # sc.fill(black)
    sc.blit(bg1, [x, 0])
    sc.blit(bg2, [x2, 0])

    box(blue, rx, ry, rs, rs)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and rx > 0:
        if rx >= 640:
            x += xvel
            x2 += xvel
        if rx < 640:
            rx -= xvel
    if keys[pygame.K_RIGHT]:
        if rx >= 640:
            x -= xvel
            x2 -= xvel
        if rx < 640:
            rx += xvel

    if x < px1 * (-1):
        x = px1
    if x2 < px2*(-1):
        x2 = px2


    pygame.display.update()
    clock.tick(60)

pygame.quit()
