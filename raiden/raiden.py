# Import Libraries
import pygame
import random
import sys
import time
from datetime import date

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

    running = True

    name_font = pygame.font.Font(None, 36)
    font = pygame.font.Font(None, 26)
    
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    input_rect = pygame.Rect(WIDTH//3, HEIGHT//2, 140, 32)

    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False
    get_name = True

    players = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    aws_client = client.Client()
    print("CONNECTED TO SERVER!")

    player1 = player.Player(20, 25, RED, (280, 420))
    players.add(player1)

    count = FPS

    while get_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aws_client.close_client()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player1.name = player1.name[:-1]
                elif event.key == pygame.K_RETURN:
                    get_name = False
                    break
                else:
                    player1.name += event.unicode

        # it will set background color of screen
        screen.fill(BLACK)
    
        if active:
            color = color_active
        else:
            color = color_passive
            
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text = font.render("NAME: ", 1, WHITE)
        screen.blit(text, (WIDTH//4-15, HEIGHT//2+8))
    
        text_surface = font.render(player1.name, True, (255, 255, 255))
        
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
        
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aws_client.close_client()
                pygame.quit()
                sys.exit()
                
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and player1.coordinate[1] - player.Player.speed > 50: #UP
            player1.update('N')
        if key[pygame.K_DOWN] and player1.coordinate[1] + player.Player.speed + player1.height < HEIGHT: #DOWN
            player1.update('S')
        if key[pygame.K_LEFT] and player1.coordinate[0] - player.Player.speed > WIDTH*(1/4): #LEFT
            player1.update('W')
        if key[pygame.K_RIGHT] and player1.coordinate[0] + player.Player.speed + player1.width < WIDTH*(3/4): #RIGHT
            player1.update('E')
        if key[pygame.K_SPACE]:
            player1.shoot(bullets)

        count += 1
        if count >= FPS:
            choice = random.choices(["easy", "normal"], weights=[4,1], k=1)[0]
            rand_coord = (random.randint(int(WIDTH/4), int(WIDTH*3/4)-50), 20)
            enemies = enemy.generate_enemy(choice=choice, coordinate=rand_coord, enemies=enemies)
            count = 0

        # If bullet hits enemy, it destroys enemy
        for bul in bullets:
            planes_hit_list = pygame.sprite.spritecollide(bul, enemies, True)
            for hit in planes_hit_list:
                if isinstance(hit, enemy.EasyEnemy):
                    player1.score += 5
                elif isinstance(hit, enemy.NormalEnemy):
                    player1.score += 10

        # If player hits enemy, it destroys enemy and player loses a life point
        if pygame.sprite.spritecollide(player1, enemies, True):
            player1.lives -= 1

        # If enemy planes reach the bottom, player loses a life point
        for enemy_plane in enemies:
            if enemy_plane.coordinate[1] > HEIGHT-50:
                enemy_plane.kill()
                player1.lives -= 1


        # Drawing on the board
        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE, (160, 0), (160, 480), 5)
        pygame.draw.line(screen, WHITE, (480, 0), (480, 480), 5)

        for user in players:
            offset = 0
            for _ in range(user.lives):
                pygame.draw.circle(screen, user.color, (15+offset,15), 5)
                offset += 15
        
        # display score
        text = font.render(str(player1.score), 1, WHITE)
        screen.blit(text, (10, 460))

        # Draw objects
        players.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)

        # Update bullets and enemy planes to update
        bullets.update()
        enemies.update()

        pygame.display.flip()
        pygame.display.update()

        # If game ends, leave while loop
        if player1.lives <= 0:
            # Start sending info to database
            aws_client.send_msg("END")
            aws_client.receive()
            aws_client.send_msg(player1.name)
            aws_client.receive()
            aws_client.send_msg(str(player1.score))
            aws_client.receive()
            aws_client.send_msg(str(date.today()))
            aws_client.receive()
            highest_score = aws_client.receive()

            screen.fill(BLACK)

            end_font = pygame.font.Font(None, 40)

            txt = "Name: " + player1.name + ", Score: " + str(player1.score)
            text = end_font.render(txt, 1, WHITE)
            screen.blit(text, (WIDTH//4, HEIGHT//2))

            if int(highest_score) > player1.score:
                txt = "Highest score: " + highest_score
            else:
                txt = "NEW HIGH SCORE!"
            text = end_font.render(txt, 1, WHITE)
            screen.blit(text, (WIDTH//4, HEIGHT//2+30))

            pygame.display.flip()
            time.sleep(3)

            screen.fill(BLACK)

            txt = "Highest Score:"

            aws_client.close_client()
            pygame.quit()
            sys.exit()

        clock.tick(FPS)

if __name__ == '__main__':
    main()