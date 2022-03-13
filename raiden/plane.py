import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self, width, height, color, coordinate):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.coordinate = coordinate