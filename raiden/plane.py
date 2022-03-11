import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self, width, height, color, coordinate):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.coordinate = coordinate
    
    # def draw(self, window):
    #     window.blit(self.ship_img, (self.x, self.y))
    #     for laser in self.lasers:
    #         laser.draw(window)