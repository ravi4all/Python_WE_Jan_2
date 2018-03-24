import pygame
import random

pygame.init()

red = 255,0,0
black = 0,0,0
white = 255,255,255

width = 1067
height = 600

screen = pygame.display.set_mode((width,height))

bg_img = pygame.image.load('images/background.png')

my_tank = pygame.image.load("images/tank_1.png")

ufo_1 = pygame.image.load("images/ufo_1.png")
ufo_2 = pygame.image.load("images/ufo_2.png")
ufo_3 = pygame.image.load("images/ufo_3.png")

bullet = pygame.image.load("images/bullet_1.png")

x = (width/2) - my_tank.get_width()/2
y = height - my_tank.get_height()

move_x = 0

bullet_x = x + my_tank.get_width() / 2
bullet_y = y + 40

move_bullet = 0

ufo_x1 = -ufo_1.get_width()
ufo_x2 = width

clock = pygame.time.Clock()
FPS = 500

bullet_list = []
bullet_dict = {'x' : bullet_x, 'y' : bullet_y}
bullet_list.append(bullet_dict)

def fire(bullet_pos, bullet):
    for i in range(len(bullet_pos)):
        bullet_pos[i]['y'] -= 10
        print(bullet_pos)
        screen.blit(bullet, [bullet_pos[i]['x'], bullet_pos[i]['y']])


while True:

    screen.fill(white)
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 5
            elif event.key == pygame.K_LEFT:
                move_x = -5
            elif event.key == pygame.K_SPACE:
                move_bullet = 10
                bullet_y = y + 40
                bullet_dict['y'] = bullet_y
                bullet_list.append(bullet_dict.copy())

        elif event.type == pygame.KEYUP:
            move_x = 0

    # screen.blit(bullet, (bullet_x, bullet_list[0]['y']))
    screen.blit(my_tank, (x,y))
    screen.blit(ufo_1,(ufo_x1,10))
    screen.blit(ufo_2, (ufo_x2, 10))

    x += move_x
    bullet_y -= move_bullet
    # print(bullet_y)

    # for i in range(15):
    #     ufo_x1 += i

    ufo_x1 += 5
    ufo_x2 -= 5

    fire(bullet_list, bullet)

    if x < 0 or x > width - my_tank.get_width():
        move_x = 0

    if ufo_x1 > width:
        ufo_x1 = -ufo_1.get_width()
    elif ufo_x2 < -ufo_2.get_width():
        ufo_x2 = width

    pygame.display.update()
    # clock.tick(FPS)
