import pygame
from myclass import*
pygame.init()
WIDTH, HEIGHT = 500, 500
SIZE=50
Lvl_map = ["1111111111",
           "1101011011",
           "1000000001"]
blocks = []
x,y = 0,0
for line in Lvl_map:
    for char in line:
        for num in line:
            if num == "1":
                blocks.append(sprite(x,y,SIZE,SIZE,0,None,(120,10,30)))
            x += SIZE
        y += SIZE
        x = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = sprite(x = 0,y = 400,w = 100,h = 30,speedx = 10,speedy = 0,image = None,color =(67,248,167))
ball = Ball(x = 250,y = 250,r = SIZE,speed = 5,color = (8,85,235))
run = True
while run:
    window.fill(BLUE)
    player.draw(window)
    player.move(window)
    ball.draw(window)
    ball.move(window)
    if ball.rect.colliderect(player.rect):
        ball.dy*= -1
    for b in blocks:
        b.draw(window)
        if ball.rect.colliderect(b.rect):
            ball.dy*= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(50)
            