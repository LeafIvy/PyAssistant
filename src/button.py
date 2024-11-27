import pygame as pg


class Button:
    def __init__(self, msg, font, text_surf, color, center):
        self.text = text_surf
        self.font = font
        self.color = color
        self.rect = self.text.get_rect(center=center)
        self.size = self.rect.size
        self.rect.width += 20
        self.rect.height += 20

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, (self.rect.centerx-self.size[0]/2, self.rect.centery-self.size[1]/2))
