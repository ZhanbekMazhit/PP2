import pygame
import time
import random
import sys

# Инициализация Pygame
pygame.init()

# Размер окна
window_x = 1000
window_y = 500

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Создание окна
pygame.display.set_caption('Snake Game with Menu')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Функция главного меню
def main_menu():
    menu_font = pygame.font.SysFont('times new roman', 50)
    while True:
        game_window.fill(black)
        draw_text('Snake Game', menu_font, white, game_window, window_x//2, window_y//4)
        draw_text('Нажмите ENTER, чтобы начать', pygame.font.SysFont('times new roman', 30), blue, game_window, window_x//2, window_y//2)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER
                    return  # Начать игру

# Функция для экрана "Game Over"
def game_over_screen(score, level):
    while True:
        game_window.fill(black)
        draw_text(f'Ваш счёт: {score}', pygame.font.SysFont('times new roman', 40), red, game_window, window_x//2, window_y//3)
        draw_text(f'Уровень: {level}', pygame.font.SysFont('times new roman', 30), white, game_window, window_x//2, window_y//2)
        draw_text('Нажмите R для рестарта или Q для выхода', pygame.font.SysFont('times new roman', 30), blue, game_window, window_x//2, window_y//1.5)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Рестарт
                    return True
                if event.key == pygame.K_q:  # Выход
                    pygame.quit()
                    sys.exit()

# Функция игры
def game():
    snake_speed = 10
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    
    def spawn_fruit():
        while True:
            new_fruit = [random.randrange(1, (window_x//10)) * 10,
                         random.randrange(1, (window_y//10)) * 10]
            if new_fruit not in snake_body:
                return new_fruit

    fruit_position = spawn_fruit()
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    level = 1
    foods_eaten = 0

    # Функция для отображения счета и уровня
    def show_score(color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render(f'Счет: {score}  Уровень: {level}', True, color)
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        game_window.blit(score_surface, score_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        if change_to == 'UP':
            direction = 'UP'
        if change_to == 'DOWN':
            direction = 'DOWN'
        if change_to == 'LEFT':
            direction = 'LEFT'
        if change_to == 'RIGHT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position == fruit_position:
            score += 10
            foods_eaten += 1
            fruit_spawn = False

            if foods_eaten % 3 == 0:
                level += 1
                snake_speed += 2
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = spawn_fruit()
        fruit_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            if game_over_screen(score, level):
                return
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            if game_over_screen(score, level):
                return
        for block in snake_body[1:]:
            if snake_position == block:
                if game_over_screen(score, level):
                    return

        show_score(blue, 'times new roman', 35)
        pygame.display.update()
        fps.tick(snake_speed)

# Запуск главного меню
while True:
    main_menu()
    game()
