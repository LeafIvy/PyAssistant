import pygame as pg


class Button:
    def __init__(self, msg, font, text_surf, color, center, func):
        self.text = text_surf
        self.font = font
        self.color = color
        self.rect = self.text.get_rect(center=center)
        self.size = self.rect.size
        self.rect.width += 30
        self.rect.height += 30

        self.func = func
        self.is_pressed = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect, border_radius=20)
        pg.draw.rect(screen, '#0437F2', self.rect, 5, 20)
        screen.blit(self.text, (self.rect.centerx-self.size[0]/2, self.rect.centery-self.size[1]/2))
        self.right_clicked = pg.mouse.get_pressed()[0]
        if self.right_clicked and self.rect.collidepoint(pg.mouse.get_pos()):
            self.color = '#4682B4'
        else:
            self.color = '#0096FF'

    def perform(self):
        if (self.right_clicked and self.rect.collidepoint(pg.mouse.get_pos())) and self.is_pressed == False:
            self.is_pressed = True
            self.func()
        if not self.right_clicked:
            self.is_pressed = False
