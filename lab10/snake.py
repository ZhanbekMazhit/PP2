import pygame
import time
import random
import psycopg2

# === PostgreSQL подключение ===
conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="k15b11tu06",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# === Инициализация ===
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()
snake_block = 10

font = pygame.font.SysFont("bahnschrift", 25)

# === Функции PostgreSQL ===
def get_user(username):
    cur.execute("SELECT score, level FROM users WHERE username = %s;", (username,))
    return cur.fetchone()

def save_user(username, score, level):
    if get_user(username):
        cur.execute("UPDATE users SET score = %s, level = %s WHERE username = %s;", (score, level, username))
    else:
        cur.execute("INSERT INTO users (username, score, level) VALUES (%s, %s, %s);", (username, score, level))
    conn.commit()

# === Отрисовка змеи ===
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, black, [block[0], block[1], snake_block, snake_block])

# === Основной цикл игры ===
def game_loop(username, level_start):
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

    snake = []
    length = 1
    score = 0
    level = level_start
    speed = 15 + (level * 2)

    foodx = random.randint(0, (width - snake_block) // 10) * 10
    foody = random.randint(0, (height - snake_block) // 10) * 10

    while not game_over:

        while game_close:
            win.fill(white)
            msg = font.render("Game Over! Q - Выйти | R - Рестарт", True, red)
            win.blit(msg, [width // 6, height // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        save_user(username, score, level)
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop(username, level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_user(username, score, level)
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0
                elif event.key == pygame.K_p:  # Пауза и сохранение
                    save_user(username, score, level)
                    print("Игра сохранена.")

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += dx
        y += dy
        win.fill(white)
        pygame.draw.rect(win, green, [foodx, foody, snake_block, snake_block])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == [x, y]:
                game_close = True

        draw_snake(snake)
        score_text = font.render(f"Score: {score}  Level: {level}", True, black)
        win.blit(score_text, [10, 10])
        pygame.display.update()

        if x == foodx and y == foody:
            foodx = random.randint(0, (width - snake_block) // 10) * 10
            foody = random.randint(0, (height - snake_block) // 10) * 10
            length += 1
            score += 10
            if score % 50 == 0:
                level += 1
                speed += 2

        clock.tick(speed)

    pygame.quit()

# === Старт игры ===
def start():
    username = input("Введите имя пользователя: ").strip()
    user_data = get_user(username)
    level = user_data[1] if user_data else 1
    print(f"Привет, {username}! Уровень: {level}")
    game_loop(username, level)

start()

cur.close()
conn.close()