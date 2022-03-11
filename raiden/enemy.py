"""contains enemy class objects to be called from raiden.py

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
"""

# Imports
import pygame
import random

import plane

# Class definition
class Enemy(plane.Plane):
    def __init__(self, width, height, color, coordinate, health, speed) -> None:
        super().__init__(width, height, color, coordinate)
        self.health = health
        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1], self.width, self.height)

class EasyEnemy(Enemy):
    width, height = 30, 30
    color = 255, 165, 0
    def __init__(self, coordinate, health=60, speed=2) -> None:
        super().__init__(self.width, self.height, self.color, coordinate, health, speed)

    def update(self) -> None:
        self.coordinate = (self.coordinate[0], self.coordinate[1]+self.speed)
        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))

class NormalEnemy(Enemy):
    width, height = 20, 20
    color = 255, 0, 255
    def __init__(self, coordinate, health=80, speed=2) -> None:
        super().__init__(self.width, self.height, self.color, coordinate, health, speed)

    def update(self) -> None:
        dir = random.choices(['W', 'SW', 'S', 'SE', 'E'], weights=[1, 2, 8, 2, 1], k=1)[0]
        if dir == 'W':
            self.coordinate = (self.coordinate[0]-self.speed*2, self.coordinate[1])
        elif dir == 'SW':
            self.coordinate = (self.coordinate[0]-self.speed, self.coordinate[1]+self.speed)
        elif dir == 'S':
            self.coordinate = (self.coordinate[0], self.coordinate[1]+self.speed)
        elif dir == 'SE':
            self.coordinate = (self.coordinate[0]+self.speed, self.coordinate[1]+self.speed)
        elif dir == 'E':
            self.coordinate = (self.coordinate[0]+self.speed*2, self.coordinate[1])

        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))
 
def generate_enemy(choice: str, coordinate: set, enemies: pygame.sprite.Group) -> pygame.sprite.Group:
    if choice=="easy":
        enemies.add(EasyEnemy(coordinate))
    elif choice=="normal":
        enemies.add(NormalEnemy(coordinate))

    return enemies
