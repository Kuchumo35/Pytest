import pygame 
import random
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bg.jpg')

pygame.display.set_caption('One Piece')

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

meatImg = []
meatX = []
meatY = []
meatX_change = []
meatY_change =  []
num_of_meats = 1

for i in range(num_of_meats):
    meatImg.append(pygame.image.load('meat.png')) 
    meatX.append(random.randint(0, 735))
    meatY.append(random.randint(50, 150)) 
    meatX_change.append(40)
    meatY_change.append(0.2) 

shootImg = pygame.image.load('star.png')
shootX = 0
shootY = 480
shootX_change = 0
shootY_change = 5
shoot_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#game over text
gameover_font = pygame.font.Font('freesansbold.ttf', 64)


def game_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    gameover_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))

def meat(x, y, i):
    screen.blit(meatImg[i], (x, y))

def fire_shoot(x, y):
    global shoot_state
    shoot_state = "fire"
    screen.blit(shootImg, (x+16, y+10))

def isCollision(meatX, meatY, shootX, shootY):
    distance = math.sqrt((math.pow(meatX - shootX, 2)) + (math.pow (meatY - shootY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                
                playerX_change = +1
            if event.key == pygame.K_SPACE:
                if shoot_state is "ready":
                    shootX = playerX
                    fire_shoot(playerX, shootY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                
                playerX_change = 0

    playerX += playerX_change
    if playerX <0 :
        playerX = 0 
    elif playerX >= 736:
        playerX = 736


    for i in range(num_of_meats):

        #game over
        if meatY[i] > 700:
            for j in range(num_of_meats):
                meatY[j] = 2000
            game_over_text()
            break
    
        meatY[i] += meatY_change[i]
        if meatY[i] <= 0:
            meatY_change[i] = 0.1
            meatX[i] += meatX_change[i]
        elif meatY[i] >= 736:
            meatY_change[i] = -0.1
            meatX[i] += meatX_change[i]

    collision = isCollision(meatX[i], meatY[i], shootX, shootY)
    if collision:
        shootY = 480
        shoot_state = "ready"
        score_value += 1
        
        meatX[i] = random.randint(0, 735)
        meatY[i] = random.randint(50, 150)

    meat(meatX[i], meatY[i], i)


    if shootY <= 0 :
        shootY = 480
        shoot_state = "ready"

    if shoot_state is "fire":
        fire_shoot(shootX, shootY)
        shootY -= shootY_change

   

    player(playerX, playerY)
    game_score(textX, textY)
    pygame.display.update()
