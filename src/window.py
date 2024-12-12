import pygame as pg
from sys import exit
from .button import Button


def quit_win():
    pg.quit()
    exit()


class App:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((1000, 700))
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 50)
        msg = 'Voice Command'
        text_surf = self.font.render(msg, True, '#4169E1')
        self.button = Button(msg, self.font, text_surf, '#0096FF', (500, 350), self.button_clicked)

        pg.display.set_caption("Python Assistant")

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit_win()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        quit_win()

            self.screen.fill('#00008B')
            self.button.draw(self.screen)
            self.button.perform()
            pg.display.update()
            self.clock.tick(60)

    def button_clicked(self):
        print("hey")
