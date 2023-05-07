import pygame,time,random,sys,os
from pygame.locals import *
WINDOWWIDTH = 800
WINDOWHEIGHT = 700
TEXTCOLOR = (225, 20, 50)
FPS = 60
BADDIEMINSIZE = 35
BADDIEMAXSIZE = 35
BADDIEMINSPEED = 6
BADDIEMAXSPEED = 6
ADDNEWBADDIERATE = 8
PLAYERMOVERATE = 8
count=3
colors = [(105,105,105)]
def terminate():
    pygame.quit()
    sys.exit()
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_DELETE:
                    terminate()
                return
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def pause_game():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_4:
                    paused = not paused
                elif event.key == K_ESCAPE:
                    terminate()
        if paused:
            windowSurface.fill((250,100,0))
            drawText('Пауза', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Нажмите 4 чтобы продолжить или ESC чтобы выйти в главное меню', font, windowSurface, (WINDOWWIDTH / 3) - 110, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        mainClock.tick(FPS)
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Гонки')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None, 30)
gameOverSound = pygame.mixer.Sound('music/crash.wav')
pygame.mixer.music.load('music/car.mp3')
laugh = pygame.mixer.Sound('music/lose.mp3')
playerImage = pygame.image.load('image/car1.png')
car3 = pygame.image.load('image/car3.png')
car4 = pygame.image.load('image/car4.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('image/car2.png')
sample = [car3,car4,baddieImage]
WALLHEIGHT = 300 # or any other value you like
wallLeft = pygame.image.load('image/left.png')
wallLeftRect = wallLeft.get_rect()
wallLeftRect.bottom = WINDOWHEIGHT - 100 # or any other value you like
wallLeftRect.left = 0
wallRight = pygame.image.load('image/right.png')
wallRightRect = wallRight.get_rect()
wallRightRect.bottom = WINDOWHEIGHT - 100 # or any other value you like
wallRightRect.right = WINDOWWIDTH
drawText('Нажмите любую кнопку для старта.(кроме Delete.=))', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
pygame.display.update()
waitForPlayerToPressKey()
zero=0
if not os.path.exists("data/save.dat"):
    f=open("data/save.dat",'w')
    f.write(str(zero))
    f.close()
v=open("data/save.dat",'r')
topScore = int(v.readline())
v.close()
while count>0:
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    while True:
        score += 10
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == ord('q'):
                    reverseCheat = True
                if event.key == K_CAPSLOCK:
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == ord('q'):
                    reverseCheat = False
                    score =0
                if event.key == K_CAPSLOCK:
                    slowCheat = False
                    score = 0
                if event.key == K_DELETE:
                    terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False
                if event.key == K_ESCAPE:
                    pause_game()
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 2
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize =30
            newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(random.choice(sample), (23, 47)),
                        }
            baddies.append(newBaddie)
            sideLeft= {'rect': pygame.Rect(0,0,126,600),
                       'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                       'surface':pygame.transform.scale(wallLeft, (126, 599)),
                       }
            baddies.append(sideLeft)
            sideRight= {'rect': pygame.Rect(500,0,203,600),
                       'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                       'surface':pygame.transform.scale(wallRight, (303, 580)),
                       }
            baddies.append(sideRight)
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)
        windowSurface.fill(random.choice(colors))
        windowSurface.blit(wallLeft, wallLeftRect)
        windowSurface.blit(wallRight, wallRightRect)
        drawText('Счет: %s' % (score), font, windowSurface, 200, 0)
        drawText('Лучший счет: %s' % (topScore), font, windowSurface,200, 20)
        drawText('Жизни: %s' % (count), font, windowSurface,200, 40)
        windowSurface.blit(playerImage, playerRect)
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
        pygame.display.update()
        if score == 5000:
                    drawText('Win!', font, windowSurface, (WINDOWWIDTH / 3) + 80, (WINDOWHEIGHT / 3))
                    pudge = pygame.mixer.Sound('music/pudge.mp3')
                    pudge.play()
                    time.sleep(18)
                    terminate()
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                g=open("data/save.dat",'w')
                g.write(str(score))
                g.close()
                topScore = score
            break
        mainClock.tick(FPS)
    pygame.mixer.music.stop()
    count=count-1
    gameOverSound.play()
    time.sleep(1)
    if count==0:
        laugh.play()
        drawText('Игра окончена.', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Игра рестартается сама.:)', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(4)
        waitForPlayerToPressKey()
        count=3
        gameOverSound.stop()
