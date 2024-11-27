import pygame as pg


class Button:
    def __init__(self, msg, font, text_surf, color, center, func=None):
        self.text = text_surf
        self.font = font
        self.color = color
        self.rect = self.text.get_rect(center=center)
        self.size = self.rect.size
        self.rect.width += 30
        self.rect.height += 30

        self.func = func

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect, border_radius=20)
        pg.draw.rect(screen, '#0437F2', self.rect, 5, 20)
        screen.blit(self.text, (self.rect.centerx-self.size[0]/2, self.rect.centery-self.size[1]/2))

    def perform(self):
        self.func()
