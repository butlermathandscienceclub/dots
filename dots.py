import random 
import pygame
import sys
import time
from pygame.locals import *
import time as t
pygame.init()

game_clock = pygame.time.Clock()
static_players = [ ]
p1win = False
p2win = False



green1x = random.randrange(0, 600)
green1y = random.randrange(0, 600)

green2y = random.randrange(0, 600)
green2x = random.randrange(0, 600)

green3x = random.randrange(0, 600)
green3y = random.randrange(0, 600)

green4x = random.randrange(0, 600)
green4y = random.randrange(0, 600)

green5x = random.randrange(0, 600)
green5y = random.randrange(0, 600)


cir2x = random.randrange(0, 600)
cir2y = random.randrange(0, 600)
circlex = random.randrange(0, 600)
circley = random.randrange(0, 600)
circle2Size = 40
circleSize = 40
p2count = 0
p2limit = 3
whight = 750
wwidth = 750
player_random_limit = 3
player_random_count = 0
playerx = 300
playery = 50
DRAWNEW = False
player2x = 50
player2y = 300
main_window = pygame.display.set_mode((wwidth, whight), 0, 32)
hashit = False
pygame.display.set_caption('Circles and dots in a box!')
circle_num = random.randrange(15, 20)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (208, 16, 222)
YELLOW = (227, 224, 25)
GREEN = (32, 212, 50)                                 
player = pygame.draw.circle(main_window, BLACK, (playerx, playery), 20, 0)
player2 = pygame.draw.circle(main_window, BLACK, (player2x, player2y), 20, 0)
extra_cicle = pygame.draw.circle(main_window, YELLOW, (circlex, circley), 40, 5)
circle_pos = [ ]
MOVESPEED2 = 10
MOVESPEED = 10
static_position = [ ]
extra_circle2 = pygame.draw.circle(main_window, RED, (cir2x, cir2y), circle2Size, 5)


green1 = pygame.draw.circle(main_window, GREEN, (green1x, green1y), 20, 0)
green2 = pygame.draw.circle(main_window, GREEN, (green2x, green2y), 20, 0)
green3 = pygame.draw.circle(main_window, GREEN, (green3x, green3y), 20, 0)
green4 = pygame.draw.circle(main_window, GREEN, (green4x, green4y), 20, 0)
green5 = pygame.draw.circle(main_window, GREEN, (green5x, green5y), 20, 0)


start = pygame.mixer.Sound('box.wav')
start.play()




for number in range(0, circle_num):
    circlexposition = random.randrange(0, 600)
    circleyposition = random.randrange(0, 600)
    circle_pos.append(circlexposition)
    circle_pos.append(circleyposition)


while True:
    MOVERIGHT = False
    MOVELEFT = False 
    MOVEUP = False
    MOVEDOWN = False

    MOVERIGHT2 = False
    MOVELEFT2 = False 
    MOVEUP2 = False
    MOVEDOWN2 = False
    main_window.fill(WHITE)

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                MOVELEFT = True
                MOVERIGHT = False
            if event.key == K_RIGHT:
                MOVELEFT = False
                MOVERIGHT = True
            if event.key == K_UP:
                MOVEUP = True
                MOVEDOWN = False
            if event.key == K_DOWN:
                MOVEUP = False
                MOVEDOWN = True
            
            if event.key == K_a:
                MOVELEFT2 = True
                MOVERIGHT2 = False
            if event.key == K_d:
                MOVELEFT2 = False
                MOVERIGHT2 = True
            if event.key == K_w:
                MOVEUP2 = True
                MOVEDOWN2 = False
            if event.key == K_s:
                MOVEUP2 = False
                MOVEDOWN2 = True
            if event.key == K_k:
                if MOVESPEED > 40:
                    MOVESPEED = 10
                else:
                    MOVESPEED += 3
            if event.key == K_m:
                if MOVESPEED <= 1:
                    MOVESPEED = 10
                else:
                    MOVESPEED -= 3
            if event.key == K_f:
                if MOVESPEED2 > 40:
                    MOVESPEED2 = 10
                else:
                    MOVESPEED2 += 3
            if event.key == K_c:
                if MOVESPEED2 <= 1:
                    MOVESPEED2 = 10
                else:    
                    MOVESPEED2 -= 3 
            if event.key == K_z:        
                if p2count <= p2limit:
                    player2x = random.randrange(0, 600) 
                    player2y = random.randrange(0, 600)
                    p2count += 1 
                else:
                    pass
            if event.key == K_l:
                if player_random_count <= player_random_limit:
                    playerx = random.randrange(0, 600) 
                    playery = random.randrange(0, 600)
                    player_random_count += 1 
                else:
                    pass
        if event.type == MOUSEBUTTONDOWN:
            circle_pos.append(event.pos[0])
            circle_pos.append(event.pos[1])
            
        if MOVEDOWN and player.bottom < whight:
            playery += MOVESPEED
        if MOVEUP and player.top > 0:
            playery -= MOVESPEED
        if MOVELEFT and player.left > 0:
            playerx -= MOVESPEED
        if MOVERIGHT and player.right < wwidth:
            playerx += MOVESPEED
        
        if MOVEDOWN2 and player2.bottom < whight:
            player2y += MOVESPEED2
        if MOVEUP2 and player2.top > 0:
            player2y -= MOVESPEED2
        if MOVELEFT2 and player2.left > 0:
            player2x -= MOVESPEED2
        if MOVERIGHT2 and player2.right < wwidth:
            player2x += MOVESPEED2
            
    if player.colliderect(player2):
        playerx = random.randrange(0, 600)
        playery = random.randrange(0, 600)
        player2x = random.randrange(0, 600)
        player2y = random.randrange(0, 600)
    if player.colliderect(extra_cicle):
        circleSize += 5

        playerx = random.randrange(0, 600)
        playery = random.randrange(0, 600)
    if player2.colliderect(extra_cicle):
        circleSize += 3
        player2x = random.randrange(0, 600)
        player2y = random.randrange(0, 600)
    if player.colliderect(extra_circle2):
        circle2Size += 3
        playerx = random.randrange(0, 600)
        playery = random.randrange(0, 600)
    if player2.colliderect(extra_circle2):
        circle2Size += 5
        player2x = random.randrange(0, 600)
        player2y = random.randrange(0, 600)
    if player.colliderect(green1) or player.colliderect(green2) or player.colliderect(green3) or player.colliderect(green4) or player.colliderect(green5):
        circleSize -= 3
        playerx = random.randrange(0, 600)
        playery = random.randrange(0, 600)
    if player2.colliderect(green1) or player2.colliderect(green2) or player2.colliderect(green3) or player2.colliderect(green4) or player2.colliderect(green5):
        circle2Size -= 3
        player2x = random.randrange(0, 600)
        player2y = random.randrange(0, 600)        
    
    player = pygame.draw.circle(main_window, BLACK, (playerx, playery), 20, 0)
    player2 = pygame.draw.circle(main_window, RED, (player2x, player2y), 20, 0)    
    extra_cicle = pygame.draw.circle(main_window, BLACK, (circlex, circley), circleSize, 5)
    extra_circle2 = pygame.draw.circle(main_window, RED, (cir2x, cir2y), circle2Size, 5)


    green1 = pygame.draw.circle(main_window, GREEN, (green1x, green1y), 20, 0)

    green2 = pygame.draw.circle(main_window, GREEN, (green2x, green2y), 20, 0)

    green3 = pygame.draw.circle(main_window, GREEN, (green3x, green3y), 20, 0)

    green4 = pygame.draw.circle(main_window, GREEN, (green4x, green4y), 20, 0)

    green5 = pygame.draw.circle(main_window, GREEN, (green5x, green5y), 20, 0)
    
    if circleSize > 80:
        p1win = True
        break

    if circle2Size > 80:
        p2win = True
        break


    for circl in range(len(circle_pos)):
        if circl % 2 != 0:
            continue
        else:
                pygame.draw.circle(main_window, YELLOW, (circle_pos[circl], circle_pos[circl+1]), random.randrange(20, 51), 5)        
    if circleSize <= 10:
        circleSize += 5
    if circle2Size <= 10:
        circle2Size += 5                   
        
    pygame.display.update()
    game_clock.tick(40)
           
if p1win:
    main_window.fill(BLACK)
if p2win:
    main_window.fill(RED)    
    
pygame.display.update()
t.sleep(1)
pygame.quit()
sys.exit()

                