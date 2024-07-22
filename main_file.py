import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load('Background.wav')
mixer.music.play(-1)


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space shooter Game')
icon = pygame.image.load('space.png')
pygame.display.set_icon(icon)

background = pygame.image.load('bg.png')
spaceshipimg = pygame.image.load('spaceship.png')

alienimg = []
alienX = []
alienY = []
alienSpeedX = []
alienSpeedY = []

no_of_aliens = 6

for i in range(no_of_aliens):

    alienimg.append(pygame.image.load('enemy.png'))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(30, 150))
    alienSpeedX.append(-1)
    alienSpeedY.append(70)

score = 0

bulletimg = pygame.image.load('bullet.png')
check = False
bulletX = 386
bulletY = 480

spaceshipX = 370
spaceshipY = 480
changeX = 0

font = pygame.font.SysFont('Arial', 32 , 'bold')

def score_text():
    img = font.render(f'score:{score}',True,'white')
    screen.blit(img,(10,10))

font_gameOver = pygame.font.SysFont('Arial', 64 , 'bold')

def game_over():
    img_gameOver = font_gameOver.render('GAME OVER',True,'white')
    screen.blit(img_gameOver,(200,250))


running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1
            if event.key == pygame.K_RIGHT:
                changeX = 1
            if event.key == pygame.K_SPACE:
                if check is False:
                   bulletSound = mixer.Sound('gunshot.wav')
                   bulletSound.play()
                   check = True
                   bulletX = spaceshipX + 16

        if event.type == pygame.KEYUP:
            changeX = 0

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736

    spaceshipX += changeX

    for i in range(no_of_aliens):
        if alienY[i] > 420:
           for j in range(no_of_aliens):
                  alienY[j] = 2000
                  game_over()


        alienX[i] += alienSpeedX[i]
        if alienX[i] <= 0:
            alienY[i] += alienSpeedY[i]
            alienSpeedX[i] = 0.3
        if alienX[i] >= 736:
             alienY[i] += alienSpeedY[i]
             alienSpeedX[i] = -0.3


        distance = math.sqrt(math.pow(bulletX-alienX[i],2) + pow(bulletY-alienY[i],2))
        if distance < 30:
            explosionSound= mixer.Sound('explosion.wav')
            explosionSound.play()
            bulletY = 480
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 1
        screen.blit(alienimg[i], (alienX[i], alienY[i]))

    if bulletY <= 0:
        bulletY = 480
        check = False

    if check is True:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= 2


    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))

    score_text()

    pygame.display.update()
