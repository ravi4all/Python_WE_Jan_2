import pygame

pygame.init()

red = 255,0,0
black = 0,0,0

width,height = 800,600

screen = pygame.display.set_mode((width,height))

x = 0
y = 0

move_x = 1
move_y = 1

while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    pygame.draw.circle(screen,black,[x,y],50)

    x += move_x
    y += move_y

    if x > width - 50:
        move_x = -1
    elif x < 0:
        move_x = 1
    elif y > height - 50:
        move_y = -1
    elif y < 0:
        move_y = 1

    pygame.display.update()
