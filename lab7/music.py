import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1260,900))
pygame.display.set_caption('VSIX Prince')
clock = pygame.time.Clock()
prince = pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/VSIX.jpeg")
pause = pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/pause.png")
play = pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/play.png")
skip = pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/next.png")
back = pygame.image.load("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/image/back.png")
new_size=(150,150)
font2 = pygame.font.SysFont(None, 20)
pause=pygame.transform.scale(pause, new_size)
play=pygame.transform.scale(play, new_size)
skip=pygame.transform.scale(skip, new_size)
back=pygame.transform.scale(back, new_size)
pause_rect = pause.get_rect(topleft=(400, 750))
play_rect = play.get_rect(topleft=(600, 750))
skip_rect = skip.get_rect(topleft=(800, 750))
back_rect = back.get_rect(topleft=(200, 750))
playlist = [
    "C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/music/1.mp3",
    "C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/music/2.mp3",
    "C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab7/music/3.mp3"
]   

cur_track=0
pygame.mixer.music.load(playlist[cur_track])
while True:
    screen.fill((255, 255, 255))   
    screen.blit(prince,(0,0))
    screen.blit(pause, pause_rect.topleft)
    screen.blit(play, play_rect.topleft)
    screen.blit(skip, skip_rect.topleft)
    screen.blit(back, back_rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_rect.collidepoint(mouse_pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.play()
            if pause_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
            if skip_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
                cur_track = (cur_track + 1) % len(playlist)  # Следующая песня (зациклено)
                pygame.mixer.music.load(playlist[cur_track])
                pygame.mixer.music.play()
            if back_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
                cur_track = (cur_track - 1) % len(playlist)  # Предыдущая песня (зациклено)
                pygame.mixer.music.load(playlist[cur_track])
                pygame.mixer.music.play()
    text2 = font2.render((playlist[cur_track]), True, (20, 20, 50))           
    pygame.display.update()
    clock.tick(60)