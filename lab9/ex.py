import pygame,random
from sys import exit
from pygame.math import Vector2
class Fruit:
    def __init__(self):
        self.random()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size ,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    def random(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size,block.y * cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
                
    def add_block(self):
        self.new_block = True
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    def update(self):
        self.snake.move_snake()
        self.chek_col()
        self.fail()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()     
    def chek_col(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random()   
            self.snake.add_block() 
    def fail(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()     
    def game_over():
        pygame.QUIT()
        exit()
        
            
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock = pygame.time.Clock()

main_game = Main()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y !=1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y !=-1:
                    main_game.snake.direction = Vector2(0,+1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(+1,0)
    screen.fill((50,200,50))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)