import pygame
from pygame.math import Vector2
import random

class SNAKE:
    def __init__(self):
        self.body = [Vector2(10, 10), Vector2(11,10), Vector2(12,10)]
        self.direction = Vector2(-1, 0)
    def draw_snake(self):
        for blocks in self.body:
            block = pygame.Rect(blocks.x * cell_size, blocks.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255,9,9), block)
            
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_nums-1)
        self.y = random.randint(0, cell_nums-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (150,150,78), fruit_rect)
            
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.new_block = False
    def update(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_for_food(self):
        self.new_block = False
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.x = random.randint(0, cell_nums-1)
            self.fruit.y = random.randint(0, cell_nums-1)
            self.snake.body.insert(0, self.fruit.pos)
            self.fruit.pos = Vector2(self.fruit.x, self.fruit.y)
            self.new_block = True
    def check_for_collision(self):
        if self.snake.body[0] in self.snake.body[1:] and self.new_block == False:
            self.game_over()
        if not 0 <= self.snake.body[0].x < cell_nums:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_nums:
            self.game_over()
    def game_over(self):
        print("Collision has been detected") 
        pygame.quit()
        





pygame.init()

# pygame setup
cell_nums = 20
cell_size = 35

main = MAIN()
screen = pygame.display.set_mode((cell_nums * cell_size, cell_nums * cell_size))
clock = pygame.time.Clock()
running = True
surface = pygame.Surface((200,200))
MOVE_TRIGGER = pygame.USEREVENT
pygame.time.set_timer(MOVE_TRIGGER, 100)




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOVE_TRIGGER:
            main.snake.move_snake()
            main.check_for_food()
            main.check_for_collision()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                main.snake.direction = Vector2(-1, 0)
    
    screen.fill((200, 100, 75))
    
    main.update()

    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()