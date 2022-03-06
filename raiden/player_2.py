import pygame
import os
import random
import time
pygame.font.init()

WIDTH, HEIGHT = 640, 480
VELOCITY_PLANE = 5 
PLANE_WIDTH, PLANE_HEIGHT = 100, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raiden")


#Player Plane
PLAYER_1_PLANE_IMAGE = pygame.image.load(os.path.join("images", "zeri.png"))
#PLAYER_2_PLANE_IMAGE = pygame.image.load(os.path.join("images", "player_2_plane.png"))
PLAYER_1_PLANE = pygame.transform.scale(PLAYER_1_PLANE_IMAGE, (PLANE_WIDTH, PLANE_HEIGHT))

#Laser
LASER_IMAGE = pygame.image.load(os.path.join("images", "laser.png"))
LASER = pygame.transform.scale(LASER_IMAGE, (PLANE_WIDTH, PLANE_HEIGHT))

#Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images", "space.png")), (WIDTH, HEIGHT))

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
class Plane:
    COOLDOWN = 30
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            """elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)"""

    
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

class Player(Plane):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_1_PLANE
        self.laser_img = LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT): 
                self.lasers.remove(laser)
            """else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)"""
                        
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2, (offset_x, offset_y)) != None
 

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5

    PLAYER_VELOCITY = 5
    LASER_VELOCITY = 5

    
    player = Player(300, 300)
    

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BACKGROUND, (0,0))

        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and player.y - VELOCITY_PLANE > 0: #UP
            player.y -= VELOCITY_PLANE
        if keys_pressed[pygame.K_s] and player.y + VELOCITY_PLANE + player.get_height() < HEIGHT: #DOWN
            player.y += VELOCITY_PLANE
        if keys_pressed[pygame.K_a] and player.x - VELOCITY_PLANE > 0: #LEFT
            player.x -= VELOCITY_PLANE
        if keys_pressed[pygame.K_d] and player.x + VELOCITY_PLANE + player.get_width() < WIDTH : #RIGHT
            player.x += VELOCITY_PLANE
        if keys_pressed[pygame.K_SPACE]:
            player.shoot()

        player.move_lasers(LASER_VELOCITY)
        
main()