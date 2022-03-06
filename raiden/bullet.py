""" Bullet objects used by the player and the enemy.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
"""

# Imports
import pygame

# Global Constants
BLACK = 0, 0, 0
WHITE = 255, 255, 255

# Class definition
class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordinate) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.color = WHITE
        self.width = 5
        self.height = 5
        self.coordinate = coordinate
        self.speed = 2
        self.damage = 20 

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1], self.width, self.height)
    
    def update(self) -> None:
        self.coordinate = (self.coordinate[0], self.coordinate[1]-5)
        self.rect = pygame.Rect(self.coordinate, (self.width, self.height))
        return super().update()

def main():
    print("----------------------------------------")
    print("bullet.py file")
    print("----------------------------------------")
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60

    screen = pygame.display.set_mode([640, 480])
    
    bullets = pygame.sprite.Group()

    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            bullet = Bullet((200, 200))
            bullets.add(bullet)

        # Fill the background with white
        screen.fill(BLACK)

        bullets.draw(screen)

        bullets.update()
        pygame.display.update()

        clock.tick(fps)


if __name__ == '__main__':
    main()