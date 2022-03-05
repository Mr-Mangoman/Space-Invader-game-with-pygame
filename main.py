import pygame 
import random
import math 

#Initializing 
pygame.init()

#create a screen 
screen = pygame.display.set_mode((1000,600))

#background
background = pygame.image.load('background for game.png')

playerimg = pygame.image.load('spaceship (1).png')
playerX = 500
playerY = 500
playerX_change = 0

enemyimg = pygame.image.load('ufo.png')
enemyX = random.randint(0,936)
enemyY = random.randint(50,300)
# enemyX_change - isko 0 mat rakhna kyunki while loop me add hota 
# hai jisse enemy x-direction me move karta hai 
enemyX_change = 2
enemyY_change = 20

#Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" # bullet_state is just a variable 
#ready means it's not fire yet
# fire state means it's fired  

#BULLET2
bullet2img = pygame.image.load('bullet.png')
bullet2X = 0
bullet2Y = 500
bullet2X_change = 0
bullet2Y_change = 7
bullet2_state = "ready"

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletimg ,(x + 16 ,y + 10))


def fire_bullet2(x,y):
    global bullet2_state 
    bullet2_state = "fire"
    screen.blit(bulletimg ,(x + 16 ,y + 10))


def player():
    screen.blit(playerimg,(playerX, playerY))

def player(x,y):
    screen.blit(playerimg, (x,y)) 

def enemy(x,y):
    screen.blit(enemyimg,(enemyX, enemyY))   

    

#game loop
running = True
while running :


    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    # how to fill a screen 
    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = +3 
            if event.key == pygame.K_SPACE:
                if bullet2_state is "ready" :
                    fire_bullet2(playerX,bullet2Y)

                # bulletX = playerX (agar yeh kardenge toh bullet apna
                #  path pe hi straight jayega aur spacehip ko follow nahi karega 
                # kyunki pahle hi bulletX ka position fix ho jayega )
                #LEKIN mujhe maza nahi aaya isiliye abhi yeh de-active hai 

                if bullet_state is "ready" : #isse multiple space bar ka problem ruk jayega  
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        


    # algo rithm for boundary 
    playerX += playerX_change 

    if playerX <= 0 :
        playerX = 0
    elif playerX >= 936 :
        playerX = 936 

    #enemy movement 
    enemyX += enemyX_change 
    #enemyX - yaha pe enemyX_change add ho raha isliye 
    # loop me enemy ka x-direction move ho raha isiliye 
    # upar zero nahi karna tha

    if enemyX <= 0 :
        enemyX_change = 2.8
        enemyY += enemyY_change

    elif  enemyX >= 936 :
         enemyX_change = -2.9 
         enemyY += enemyY_change
    
    #BULLLET MOVEMENT
    if bullet_state is "fire" : 
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

    if bullet2_state is "fire"  :
        fire_bullet2(playerX,bullet2Y)
        bullet2Y -= bullet2Y_change
    #Multipple bullet 
    # yaha pe bullet jab y- axis ka 1 pe pahuch jata hai
    # tab bullet wapas reset ho jata hai at bulletY i.e. 500 
    # aur bullet ka state bhi "ready" ho jaata hai

    if bulletY <= 1 :
        bulletY = 500 
        bullet_state = "ready" 
    
   # if bullet2Y <= 1 :
       # bullet2Y = 500 
       # bullet2_state = "ready"

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()