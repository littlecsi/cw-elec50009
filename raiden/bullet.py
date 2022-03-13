# Imports
import pygame

# Class definition
class Bullet(pygame.sprite.Sprite):
    WHITE = 255, 255, 255
    def __init__(self, coordinate) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.color = self.WHITE
        self.width = 5
        self.height = 5
        self.coordinate = coordinate
        self.speed = 10
        self.damage = 20 

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1], self.width, self.height)
    
    def update(self) -> None:
        self.coordinate = (self.coordinate[0], self.coordinate[1]-self.speed)
        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))