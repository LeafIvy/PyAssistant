import pygame as pg
from sys import exit


def quit_win():
    pg.quit()
    exit()


class App:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((1000, 700))
        self.clock = pg.time.Clock()

        pg.display.set_caption("Python Assistant")

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit_win()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        quit_win()

            self.screen.fill('blue')

            pg.display.update()
            self.clock.tick(60)
