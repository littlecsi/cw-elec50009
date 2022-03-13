"""imports all sub-modules to execute the raiden game.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
"""
# Import Libraries
from turtle import width
import pygame
import random
import sys

import player
import enemy

# Global Constants
BLACK = 0, 0, 0
RED = 255, 0, 0

WIDTH, HEIGHT = 640, 480
FPS = 30

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    users = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    user = player.Player(20, 25, RED, (280, 420))
    users.add(user)

    count = FPS

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and user.coordinate[1] - player.Player.speed > 50: #UP
            user.update('N')
        if key[pygame.K_DOWN] and user.coordinate[1] + player.Player.speed + user.height < HEIGHT: #DOWN
            user.update('S')
        if key[pygame.K_LEFT] and user.coordinate[0] - player.Player.speed > WIDTH*(1/4): #LEFT
            user.update('W')
        if key[pygame.K_RIGHT] and user.coordinate[0] + player.Player.speed + user.width < WIDTH*(3/4): #RIGHT
            user.update('E')
        if key[pygame.K_SPACE]:
            user.shoot(bullets)
        
        count += 1
        if count>=FPS:
            choice = random.choices(["easy", "normal"], weights=[4,1], k=1)[0]
            rand_coord = (random.randint(int(WIDTH/4), int(WIDTH*3/4)-50), 20)
            enemies = enemy.generate_enemy(choice=choice, coordinate=rand_coord, enemies=enemies)
            count = 0

        for bul in bullets:
            collided_sprite_list = pygame.sprite.spritecollide(bul, enemies, False)
            for sprite in collided_sprite_list: sprite.kill()

        screen.fill(BLACK)

        users.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)

        bullets.update()
        enemies.update()

        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    main()