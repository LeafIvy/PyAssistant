import pygame as pg
from sys import exit


def quit_win():
    pg.quit()
    exit()


pg.init()

screen = pg.display.set_mode((1000, 700))
clock = pg.time.Clock()

pg.display.set_caption("Python Assistant")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_win()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                quit_win()

    screen.fill('blue')

    pg.display.update()
    clock.tick(60)