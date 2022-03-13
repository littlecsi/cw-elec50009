from pickle import REDUCE
from re import S
import pygame
import os
import random
import time

import plane
import bullet

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, vel):
        self.y -= vel
    
    def off_screen(self, height):
        return self.y <= height and self.y >= 0
    
    def collision(self, obj):
        return collide(self, obj)
            
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(plane.Plane):
    lives = 5
    speed = 7
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

def main():
    BLACK = 0, 0, 0
    RED = 255, 0, 0

    WIDTH, HEIGHT = 640, 480

    run = True
    FPS = 60

    pygame.init()
    clock = pygame.time.Clock()

    players = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    VELOCITY_PLANE = 5

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Raiden")
    
    player1 = Player(20, 25, RED, (320, 420))
    players.add(player1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w] and player1.coordinate[1] - VELOCITY_PLANE > 50: #UP
            player1.update('N')
        if keys_pressed[pygame.K_s] and player1.coordinate[1] + VELOCITY_PLANE + player1.height < HEIGHT: #DOWN
            player1.update('S')
        if keys_pressed[pygame.K_a] and player1.coordinate[0] - VELOCITY_PLANE > WIDTH*(1/4): #LEFT
            player1.update('W')
        if keys_pressed[pygame.K_d] and player1.coordinate[0] + VELOCITY_PLANE + player1.width < WIDTH*(3/4): #RIGHT
            player1.update('E')
        if keys_pressed[pygame.K_SPACE]:
            player1.shoot(bullets)

        screen.fill(BLACK)

        players.draw(screen)  
        bullets.draw(screen)      
        
        bullets.update()
        pygame.display.update()

        clock.tick(FPS)
        
if __name__ == '__main__':
    main()