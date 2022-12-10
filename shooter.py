import pygame
import random
import math
from pygame import mixer
#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption("Space boy Prime")
icon = pygame.image.load("astronaut (1).png")
pygame.display.set_icon(icon)
background = pygame.image.load("download.jpg")

#addmusic
mixer.music.load("Kenny Mason - DIP ft. DavidTheTragic.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#add user
img_player = pygame.image.load("spaceship.png")
player_x = 368
player_y = 500
x_change = 0

#add enemy
img_enemy = []
enemy_x = []
enemy_y = []
x_enemy_change = []
y_enemy_change = []
no_enemies = 8

for e in range(no_enemies):
    img_enemy.append(pygame.image.load("ufo.png"))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    x_enemy_change.append(0.3)
    y_enemy_change.append(50)

#add AMMUNITION
img_bullet = pygame.image.load("bullet (1).png")
bullet_x = 0
bullet_y = 500
x_change = 0
bullet_speed = 3
visibility = False

#Score
score = 0
my_score = pygame.font.Font("freesansbold.ttf", 32)
score_x = 10
score_y = 10


end_font = pygame.font.Font("freesansbold.ttf", 40)

def final_text():
    my_final = end_font.render("GAME OVER", True, (255,255,255))
    screen.blit(my_final, (200,200))



def player(x,y):
    screen.blit(img_player, (x, y))

def enemy(x,y,en):
    screen.blit(img_enemy[en], (x, y))

def shoot(x,y):
    global visibility
    visibility = True
    screen.blit(img_bullet, (x + 12,y + 6))

def collide(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    if distance < 27:
        return True
    else:
        return False

def displayscore(x,y):
    text = my_score.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text,(x,y))
#run loop
is_running = True
while is_running:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.4
            if event.key == pygame.K_RIGHT:
                x_change = +0.4
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("mixkit-short-laser-gun-shot-1670.wav")
                bullet_sound.play
                if not visibility:
                    bullet_x = player_x
                    shoot(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0


    player_x += x_change
    #Screen boundary
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736


    #enemy movement
    for enem in range(no_enemies):
        #end
        if enemy_y[enem] > 500:
            for k in range(no_enemies):
                enemy_y[k] = 1000
            final_text()
            break
        enemy_x[enem] += x_enemy_change[enem] 
    
        # ENEMY Screen boundary
        if enemy_x[enem]  <= 0:
            x_enemy_change[enem]  = 0.3
            enemy_y[enem]  += y_enemy_change[enem] 
        elif enemy_x[enem]  >= 736:
            x_enemy_change[enem]  = -0.3
            enemy_y[enem]  += y_enemy_change[enem] 
        
        enemy(enemy_x[enem],enemy_y[enem],enem)

        collision = collide(enemy_x[enem],enemy_y[enem], bullet_x, bullet_y)
        if collision:
            bullet_y = 500
            visibility = False
            score += 1
            enemy_x[enem] = random.randint(0,736)
            enemy_y[enem] = random.randint(50,200)
            print(score)
    #bullet movement
    if bullet_y <= -32:
        bullet_y = 500
        visibility= False
    if visibility:
        shoot(bullet_x, bullet_y)
        bullet_y -= bullet_speed
        
    player(player_x,player_y)
    displayscore(score_x,score_y)
    pygame.display.update()
