import pygame
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (150,150,78), fruit_rect)




pygame.init()

# pygame setup
cell_nums = 20
cell_size = 35

fruit = FRUIT()
screen = pygame.display.set_mode((cell_nums * cell_size, cell_nums * cell_size))
clock = pygame.time.Clock()
running = True
surface = pygame.Surface((200,200))




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((200, 100, 75))
    fruit.draw_fruit()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()