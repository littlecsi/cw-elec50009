import pygame

import plane
import bullet

class Player(plane.Plane):
    name = ""
    lives = 5
    speed = 7
    score = 0
    def __init__(self, width, height, color, coordinate):
        super().__init__(width, height, color, coordinate)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1], self.width, self.height)
    
    def update(self, dir) -> None:
        if dir == 'N': 
            self.coordinate = (self.coordinate[0], self.coordinate[1]-self.speed)
        elif dir == 'S': 
            self.coordinate = (self.coordinate[0], self.coordinate[1]+self.speed)
        elif dir == 'W': 
            self.coordinate = (self.coordinate[0]-self.speed, self.coordinate[1])
        elif dir == 'E': 
            self.coordinate = (self.coordinate[0]+self.speed, self.coordinate[1])
        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))
    
    def shoot(self, bullets) -> pygame.sprite.Group:
        bullets.add(bullet.Bullet((self.coordinate[0]+self.width/2, self.coordinate[1]-15)))
        return bullets