# Imports
import pygame

import plane

# Class definition
class Enemy(plane.Plane):
    def __init__(self, width, height, color, coordinate, speed) -> None:
        super().__init__(width, height, color, coordinate)
        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1], self.width, self.height)

class EasyEnemy(Enemy):
    width, height = 30, 30
    color = 255, 165, 0
    def __init__(self, coordinate, speed=2) -> None:
        super().__init__(self.width, self.height, self.color, coordinate, speed)

    def update(self) -> None:
        self.coordinate = (self.coordinate[0], self.coordinate[1]+self.speed)
        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))

class NormalEnemy(Enemy):
    width, height = 20, 20
    color = 255, 0, 255
    def __init__(self, coordinate, speed=5) -> None:
        super().__init__(self.width, self.height, self.color, coordinate, speed)

    def update(self) -> None:
        self.coordinate = (self.coordinate[0], self.coordinate[1]+self.speed)
        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))
 
def generate_enemy(choice: str, coordinate: set, enemies: pygame.sprite.Group) -> pygame.sprite.Group:
    if choice=="easy":
        enemies.add(EasyEnemy(coordinate))
    elif choice=="normal":
        enemies.add(NormalEnemy(coordinate))

    return enemies
