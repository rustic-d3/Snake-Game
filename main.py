import pygame

pygame.init()

# pygame setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x = 40
y = 40

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y+=10
    
            if event.key == pygame.K_UP:
                y-=10
            if event.key == pygame.K_LEFT:
                x-=10
            if event.key == pygame.K_RIGHT:
                x+=10

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen,pygame.Color(255, 12, 133), pygame.Rect(x, y, 100, 100))
        

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()