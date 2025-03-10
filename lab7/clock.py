import pygame
import datetime
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400,1000))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
mike = pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/clock.png")
mike_lefthand=pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/leftarm.png")
mike_righthand=pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/rightarm.png")
RED = (255, 0, 0)
black = (50,50,5)
clock_center=(700,525)

def rotate_image(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    now=datetime.datetime.now()
    seconds = now.second + now.microsecond / 1_000_000 
    minutes = now.minute + seconds / 60
    hours = (now.hour % 12) + minutes / 60
    minute_angle = minutes * 6  
    hour_angle = hours * 30
    
    screen.blit(mike,(0,0))  
    pygame.draw.circle(screen, RED, (200,800), 50)
    pygame.draw.circle(screen, black, (700,525), 30)
    rotated_minute, minute_rect = rotate_image(mike_lefthand, minute_angle, clock_center)
    rotated_hour, hour_rect = rotate_image(mike_righthand, hour_angle, clock_center)
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_hour, hour_rect.topleft)
    pygame.display.update()
    clock.tick(60)
    