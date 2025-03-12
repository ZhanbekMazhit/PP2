import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400,1000))
pygame.display.set_caption('ball')
clock = pygame.time.Clock()
RED = (255,0,0)
screen.fill((255, 255, 255)) 
x,y=0,0
speed = 20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  
        x -= speed
    if keys[pygame.K_d]:  
        x += speed
    if keys[pygame.K_w]:  
        y -= speed
    if keys[pygame.K_s]:  
        y += speed
    x = max(50, min(x, 1350))  
    y = max(50, min(y, 950))   
    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen,RED,(x,y),50)
    pygame.display.update()
    clock.tick(60)