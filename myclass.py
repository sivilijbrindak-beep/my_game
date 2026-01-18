import pygame
pygame.init()
from random import randint 
class sprite:
    def __init__(self,x=10,y=10,w=50,h=50,speed=0,speedx = 0,speedy = 0,image=None,color=(200,0,0)):
        self.image = image
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.rect = pygame.Rect(x,y,w,h)
        self.load_img()
    def draw(self,window):
        if self.image:
            window.blit(self.image,self.rect)
        else:
            pygame.draw.rect(window,self.color,self.rect)
    def move(self,window):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.y >= self.speedy:
            self.rect.y -= self.speedy
        if key[pygame.K_s] and self.rect.bottom <= window.get_height() - self.speedy:
            self.rect.y += self.speedy
        if key[pygame.K_a] and self.rect.x >= self.speed:
            self.rect.x -= self.speedx
        if key[pygame.K_d] and self.rect.right <= window.get_width() - self.speedx:
            self.rect.x += self.speedxx
        

    def load_img(self):
        if self.image:
            self.image = pygame.image.load(self.image)
            self.image = pygame.transform.scale(self.image,(self.recv.w,self.rect.h))


class Ball:
    def __init__(self,x=50,y=50,radius=30,speed=0,color=(0,0,0)):
        
        self.rect = pygame.Rect(x,y,r*2,r*2)
        self.speed = speed
        self.color = color  
        self.r = r
        self.dx = 1
        self.dy = -1

    def move(self,window):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy
        if self.rect.x <= 0 or self.rect.right >= window.get_width(): 
            self.dx*= -1
            self.speed = randint(5,10)
        if self.rect.y <= 0:
            self.dy*= -1
            self.speed = randint(5,10)
    def draw(self,window):
        pygame.draw.circle(window,self.color,self.rect.center,self.r)

       