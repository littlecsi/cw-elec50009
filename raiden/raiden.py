# Import Libraries
import pygame
import random
import sys

import player
import enemy
import client

# Global Constants
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0

WIDTH, HEIGHT = 640, 480
FPS = 30

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    players = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    aws_client = client.Client(client_port=13000)
    print("CONNECTED TO SERVER!")
    aws_client.send_client_detail()
    aws_client.receive()

    print("CHECKPOINT")

    player1 = player.Player(20, 25, RED, (280, 420))
    players.add(player1)

    count = FPS

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and player1.coordinate[1] - player.Player.speed > 50: #UP
            player1.update('N')
            aws_client.send_msg('N')
        if key[pygame.K_DOWN] and player1.coordinate[1] + player.Player.speed + player1.height < HEIGHT: #DOWN
            player1.update('S')
            aws_client.send_msg('S')
        if key[pygame.K_LEFT] and player1.coordinate[0] - player.Player.speed > WIDTH*(1/4): #LEFT
            player1.update('W')
            aws_client.send_msg('W')
        if key[pygame.K_RIGHT] and player1.coordinate[0] + player.Player.speed + player1.width < WIDTH*(3/4): #RIGHT
            player1.update('E')
            aws_client.send_msg('E')
        if key[pygame.K_SPACE]:
            player1.shoot(bullets)
            aws_client.send_msg('shoot')

        count += 1
        if count>=FPS:
            choice = random.choices(["easy", "normal"], weights=[4,1], k=1)[0]
            rand_coord = (random.randint(int(WIDTH/4), int(WIDTH*3/4)-50), 20)
            enemies = enemy.generate_enemy(choice=choice, coordinate=rand_coord, enemies=enemies)
            count = 0

        for bul in bullets:
            pygame.sprite.spritecollide(bul, enemies, True)

        for user in players:
            if pygame.sprite.spritecollide(user, enemies, True):
                user.lives -= 1

        # Drawing on the board
        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE, (160, 0), (160, 480), 5)
        pygame.draw.line(screen, WHITE, (480, 0), (480, 480), 5)

        for user in players:
            offset = 0
            for _ in range(user.lives):
                pygame.draw.circle(screen, user.color, (15+offset,15), 5)
                offset += 15

        players.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)

        bullets.update()
        enemies.update()

        pygame.display.flip()
        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    main()