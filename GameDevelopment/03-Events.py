import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((800,600))

while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    pygame.draw.rect(screen,black,[0,0,50,50])

    pygame.display.update()
