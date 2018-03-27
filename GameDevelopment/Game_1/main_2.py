import pygame
from pygame.locals import *

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

shot = pygame.mixer.Sound('gunShot.wav')
bgm = pygame.mixer.Sound('ve_music.wav')
bgm.play(-1)

def fire(bullet_pos, bullet):
    for i in range(len(bullet_pos)):
        bullet_pos[i]['y'] -= 10
        screen.blit(bullet, [bullet_pos[i]['x'], bullet_pos[i]['y']])

def score(s):
    font = pygame.font.SysFont(None,45)
    text = font.render('Score : {}'.format(s), True, red)
    screen.blit(text, (10,10))

def show_timer(t):
    font = pygame.font.SysFont(None, 45)
    text = font.render('Time Left : {}'.format(t), True, red)
    screen.blit(text, (700, 10))

def gameOver(s):
    font_1 = pygame.font.SysFont(None, 100)
    text_1 = font_1.render('Game Over', True, red)
    font_2 = pygame.font.SysFont(None, 100)
    text_2 = font_2.render('Score : {}'.format(s), True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text_1, (300,100))
        screen.blit(text_2, (400, 300))
        pygame.display.update()

def main():
    x = (width / 2) - my_tank.get_width() / 2
    y = height - my_tank.get_height()

    move_x = 0

    bullet_x = x + my_tank.get_width() / 2
    bullet_y = y + 40

    move_bullet = 0

    ufo_x1 = -ufo_1.get_width()
    ufo_x2 = width

    bullet_list = []
    bullet_dict = {'x': bullet_x, 'y': bullet_y}
    bullet_list.append(bullet_dict)

    counter = 0

    seconds = 10
    pygame.time.set_timer(USEREVENT + 1, 1000)

    while True:

        screen.fill(white)
        screen.blit(bg_img, (0, 0))

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT + 1:
                seconds -= 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 5
                elif event.key == pygame.K_LEFT:
                    move_x = -5
                elif event.key == pygame.K_SPACE:
                    move_bullet = 10
                    bullet_y = y + 40
                    bullet_x = x + my_tank.get_width() / 2
                    bullet_dict['y'] = bullet_y
                    bullet_dict['x'] = bullet_x
                    bullet_list.append(bullet_dict.copy())
                    shot.play()

            elif event.type == pygame.KEYUP:
                move_x = 0

            if seconds == -1:
                gameOver(counter)

        screen.blit(my_tank, (x,y))
        screen.blit(ufo_1,(ufo_x1,10))
        screen.blit(ufo_2, (ufo_x2, 10))

        x += move_x
        bullet_y -= move_bullet

        ufo_rect_1 = pygame.Rect(ufo_x1, 10, ufo_1.get_width(), ufo_1.get_height())
        ufo_rect_2 = pygame.Rect(ufo_x2, 10, ufo_2.get_width(), ufo_2.get_height())
        bullet_rect = pygame.Rect(bullet_dict['x'], bullet_dict['y'], bullet.get_width(), bullet.get_height())

        ufo_x1 += 5
        ufo_x2 -= 5

        fire(bullet_list, bullet)
        score(counter)
        show_timer(seconds)

        if bullet_rect.colliderect(ufo_rect_1):
            ufo_x1 = -ufo_1.get_width()
            counter += 1
        elif bullet_rect.colliderect(ufo_rect_2):
            ufo_x2 = width
            counter += 1

        if x < 0 or x > width - my_tank.get_width():
            move_x = 0

        if ufo_x1 > width:
            ufo_x1 = -ufo_1.get_width()
        elif ufo_x2 < -ufo_2.get_width():
            ufo_x2 = width

        pygame.display.update()

if __name__ == '__main__':
    main()