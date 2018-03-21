import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((800,600))

x = 0
y = 0

while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    # pygame.draw.rect(screen,black,[x,y,50,50])
    pygame.draw.circle(screen,black,[x,y],50)

    x += 1
    y += 1

    pygame.display.update()
