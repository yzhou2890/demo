

# demo of pygame - keyboard: m, LEFT, RIGHT, UP, DOWN

import pygame, time
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)


while True:

    def f0():
        print('key released')

    def f1():
        print('key \'m\' pressed')

    def f_up():
        print('Up arrow pressed')

    def f_down():
        print('Down arrow pressed')

    def f_left():
        print('Left arrow pressed')

    def f_right():
        print('Right arrow pressed')


    for event in pygame.event.get():
        if (event.type == KEYUP):
            f0()
            time.sleep(0.3)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m: 
                f1()
                time.sleep(0.3)
         
            if event.key == pygame.K_UP: 
                f_up()
                time.sleep(0.3)

            if event.key == pygame.K_DOWN: 
                f_down()
                time.sleep(0.3)

            if event.key == pygame.K_LEFT: 
                f_left()
                time.sleep(0.3)

            if event.key == pygame.K_RIGHT: 
                f_right()
                time.sleep(0.3)
