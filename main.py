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

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 4

for i in range(number_of_enemies):    
    enemyimg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0,936))
    enemyY.append(random.randint(50,300))
    # enemyX_change - isko 0 mat rakhna kyunki while loop me add hota 
    # hai jisse enemy x-direction me move karta hai 
    enemyX_change.append(2)
    enemyY_change.append(20)

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
bullet2Y_change = 9
bullet2_state = "ready"

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletimg ,(x + 16 ,y + 10))


#def fire_bullet2(x,y):
    #global bullet2_state 
    #bullet2_state = "fire"
    #screen.blit(bulletimg ,(x + 16 ,y + 10)) 
    #above code kaam nahi kar raha for second bullet 

#def isCollision2(enemyX , enemyY , bullet2X , bullet2Y ):
    #distance = math.sqrt((math.pow((enemyX - bullet2X),2)) + (math.pow((enemyY - bullet2Y),2)))
    #if distance < 27:
       # return True
    #else :
       # return False (for second bullet baad meh koshish karna)
        
def isCollision(enemyX , enemyY , bulletX , bulletY ):
    distance = math.sqrt((math.pow((enemyX - bulletX),2)) + (math.pow((enemyY - bulletY),2)))
    if distance < 27:
        return True
    else :
        return False 


def player():
    screen.blit(playerimg,(playerX, playerY))

def player(x,y):
    screen.blit(playerimg, (x,y)) 

def enemy(x,y,i):
    screen.blit(enemyimg[i],(enemyX[i], enemyY[i]))   

score_value = 0
font = pygame.font.Font("freesansbold.ttf" , 32 )

textX = 10
textY = 10 

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True ,(255,255,255))
    screen.blit(score , (x,y))
    

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
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = +4 
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready" : #isse multiple space bar ka problem ruk jayega  
                    bulletX = playerX #(agar yeh kardenge toh bullet apna  
                    # path pe hi straight jayega aur spacehip ko follow nahi karega  
                    # kyunki pahle hi bulletX ka position fix ho jayega )
                    #LEKIN mujhe maza nahi aaya isiliye abhi yeh de-active hai 
                    fire_bullet(bulletX,bulletY) 
                
                #if bulletY <= 300 :(for second bullet baad meh koshish karna)
                    #if bullet2_state =="ready" :
                       # fire_bullet2(playerX,bullet2Y)

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
    for i in range(number_of_enemies): 
        enemyX[i] += enemyX_change[i] 
       #enemyX - yaha pe enemyX_change add ho raha isliye 
       # loop me enemy ka x-direction move ho raha isiliye 
       # upar zero nahi karna tha

        if enemyX[i] <= 0 :
            enemyX_change[i] = 2.8
            enemyY[i] += enemyY_change[i]

        elif  enemyX[i] >= 936 :
             enemyX_change[i] = -2.9 
             enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i] , enemyY[i] , bulletX , bulletY)
        if collision :
            bulletY = 500 
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,936)
            enemyY[i] = random.randint(50,300)

        enemy(enemyX[i],enemyY[i],i)

    
    #BULLLET MOVEMENT
    if bullet_state == "fire" : 
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #if bullet2_state == "fire"  : (for second bullet baad meh koshish karna)
     #   fire_bullet2(playerX,bullet2Y)
      #  bullet2Y -= bullet2Y_change
    #Multipple bullet 
    # yaha pe bullet jab y- axis ka 1 pe pahuch jata hai
    # tab bullet wapas reset ho jata hai at bulletY i.e. 500 
    # aur bullet ka state bhi "ready" ho jaata hai

    if bulletY <= 1 :
        bulletY = 500 
        bullet_state = "ready" 
    
    #if bullet2Y <= 1 :(for second bullet baad meh koshish karna)
       # bullet2Y = 500 
        #bullet2_state = "ready"

    

   # collision2 = isCollision2(enemyX , enemyY , bullet2X , bullet2Y)
    #if collision2 :
       # bullet2Y = 500 
       # bullet2_state = "ready"
        #score += 1
        #print(score)
        #enemyX = random.randint(0,936)
        #enemyY = random.randint(50,300)



    player(playerX,playerY)
    show_score(textX , textY)

    pygame.display.update()