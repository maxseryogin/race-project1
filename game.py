import pygame,time,random,sys,os
from pygame.locals import *
WINDOWWIDTH = 800
WINDOWHEIGHT = 700
TEXTCOLOR = (225, 20, 50)
FPS = 60
BADDIEMINSIZE = 20
BADDIEMAXSIZE = 15
BADDIEMINSPEED = 6
BADDIEMAXSPEED = 6
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 8
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
count=1000
colors = [(105,105,105)]
button_rect = pygame.Rect(150, 350, 200, 100)
button_rect_ = pygame.Rect(500, 350, 200, 100)
plus_button_rect = pygame.Rect(650, 50, 50, 50)
minus_button_rect = pygame.Rect(750, 50, 50, 50)
help_button1_rect = pygame.Rect(10, 10, 50, 50)
back_button1 = pygame.Rect(10, 10, 50, 50)
a = 1
def terminate():
    pygame.quit()
    sys.exit()
def waitForPlayerToPressKey():
    global a, PLAYERMOVERATE
    start_button = pygame.Surface((100, 50))
    start_button.fill(WHITE)
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    start_text = font.render("Начать", True, BLACK)
    start_text_rect = start_text.get_rect()
    start_text_rect.center = start_button_rect.center
    exit_button = pygame.Surface((100, 50))
    exit_button.fill(WHITE)
    exit_button_rect = exit_button.get_rect()
    exit_button_rect.topleft = (10, 10)
    exit_text = font.render("Выход", True, BLACK)
    exit_text_rect = exit_text.get_rect()
    exit_text_rect.center = exit_button_rect.center
    help_button = pygame.Surface((100, 50))
    help_button.fill(WHITE)
    help_button_rect = help_button.get_rect()
    help_button_rect.topleft = (120, 10)
    help_text = font.render("Справка", True, BLACK)
    help_text_rect = help_text.get_rect()
    help_text_rect.center = help_button_rect.center
    back_button = pygame.Surface((100, 50))
    back_button.fill(WHITE)
    back_button_rect = back_button.get_rect()
    back_button_rect.topleft = (10, 10)
    back_text = font.render("Назад", True, BLACK)
    back_text_rect = exit_text.get_rect()
    back_text_rect.center = back_button_rect.center
    control_button = pygame.Surface((100, 50))
    control_button.fill(GRAY)
    control_button_rect = control_button.get_rect()
    control_button_rect.center = (580, 600)
    control_text = font.render("Мышка", True, BLACK)
    control_text_rect = control_text.get_rect()
    control_text_rect.center = control_button_rect.center
    control_button_ = pygame.Surface((100, 50))
    control_button_.fill(GRAY)
    control_button_rect_ = control_button_.get_rect()
    control_button_rect_.center = (700, 600)
    control_text_ = font.render("Клава", True, BLACK)
    control_text_rect_ = control_text_.get_rect()
    control_text_rect_.center = control_button_rect_.center
    in_menu = True
    instruction_text = ['W, UP - вверх', 'S, DOWN - вниз', 'A, LEFT - влево', 'D, RIGHT - вправо','CAPSLOCK - замедление времени', 'Q - локальное "радио"','R - остановить радио','V -турбобуст', 'E - отмотка времени','ESC - пауза']
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if start_button_rect.collidepoint(event.pos):
                        return
                    elif in_menu:
                        if exit_button_rect.collidepoint(event.pos):
                            terminate()
                        elif help_button_rect.collidepoint(event.pos):
                            windowSurface.fill(GRAY)
                            windowSurface.blit(back_button, back_button_rect)
                            for i, text in enumerate(instruction_text):
                                instruction = font.render(text, True, BLACK)
                                instruction_rect = instruction.get_rect()
                                instruction_rect.centerx = windowSurface.get_rect().centerx
                                instruction_rect.top = 50 + i * 30
                                windowSurface.blit(instruction, instruction_rect)
                            in_menu = False
                            windowSurface.blit(back_text, back_text_rect)
                        elif control_button_rect.collidepoint(event.pos):
                            a = 1
                            PLAYERMOVERATE = 100
                        elif control_button_rect_.collidepoint(event.pos):
                            a = 2
                            PLAYERMOVERATE = 8
                    else:
                        if back_button_rect.collidepoint(event.pos):
                            windowSurface.fill(BLACK)
                            windowSurface.blit(exit_button, exit_button_rect)
                            windowSurface.blit(help_button, help_button_rect)
                            windowSurface.blit(control_button, control_button_rect)
                            windowSurface.blit(control_button_, control_button_rect_)
                            windowSurface.blit(start_button, start_button_rect)
                            windowSurface.blit(exit_text, exit_text_rect)
                            windowSurface.blit(help_text, help_text_rect)
                            windowSurface.blit(start_text, start_text_rect)
                            windowSurface.blit(control_text,control_text_rect)
                            windowSurface.blit(control_text_, control_text_rect_)
                            in_menu = True
        if in_menu:
            windowSurface.fill(BLACK)
            windowSurface.blit(exit_button, exit_button_rect)
            windowSurface.blit(help_button, help_button_rect)
            windowSurface.blit(control_button, control_button_rect)
            windowSurface.blit(control_button_, control_button_rect_)
            windowSurface.blit(start_button, start_button_rect)
            windowSurface.blit(exit_text, exit_text_rect)
            windowSurface.blit(help_text, help_text_rect)
            windowSurface.blit(start_text, start_text_rect)
            windowSurface.blit(control_text, control_text_rect)
            windowSurface.blit(control_text_, control_text_rect_)
        pygame.display.update()
def playerHasHitBaddie(playerRect, baddies):
    global score_
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            if score_ >= 1000:
                return False
            return True
    return False
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def pause_game():
    paused = True
    volume = 0.1
    pygame.mixer.music.set_volume(volume)
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        if paused:
            windowSurface.fill((0, 0, 0))
            pygame.draw.rect(windowSurface, (0, 155, 155), button_rect)
            pygame.draw.rect(windowSurface, (0, 155, 155), button_rect_)
            drawText('ПАУЗА', font, windowSurface, (WINDOWWIDTH / 2.2), (WINDOWHEIGHT / 3))
            drawText('Нажмите чтобы продолжить или чтобы выйти', font, windowSurface, (WINDOWWIDTH / 2.6) - 110,(WINDOWHEIGHT / 3) + 50)
            pygame.draw.rect(windowSurface, (0, 255, 155), plus_button_rect)
            pygame.draw.rect(windowSurface, (0, 155, 155), minus_button_rect)
            drawText('Громкость', font, windowSurface, 675, 20)
            drawText(str(int(volume * 100)), font, windowSurface, 713, 64)
            if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(windowSurface, (0, 155, 155), button_rect)
                paused = not paused
            elif button_rect_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(windowSurface, (0, 155, 155), button_rect_)
                terminate()
            elif plus_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(windowSurface, (0, 155, 155), plus_button_rect)
                if volume < 1.0:
                    volume += 0.1
                    pygame.mixer.music.set_volume(volume)
                    pygame.time.delay(200)
            elif minus_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(windowSurface, (0, 155, 155), minus_button_rect)
                if volume > 0.0:
                    volume -= 0.1
                    pygame.mixer.music.set_volume(volume)
                    pygame.time.delay(200)
            else:
                pygame.draw.rect(windowSurface, (0, 155, 155), button_rect)
                pygame.draw.rect(windowSurface, (0, 155, 155), button_rect_)
                pygame.draw.rect(windowSurface, (0, 155, 155), plus_button_rect)
                pygame.draw.rect(windowSurface, (0, 155, 155), minus_button_rect)
                button_text = font.render('Продолжить', True, (100, 200, 15))
                text_rect = button_text.get_rect(center=button_rect.center)
                windowSurface.blit(button_text, text_rect)
                button_text_ = font.render('Выйти', True, (100, 200, 15))
                text_rect_ = button_text_.get_rect(center=button_rect_.center)
                windowSurface.blit(button_text_, text_rect_)
                plus_button_text = font.render('+', True, (100, 200, 15))
                plus_text_rect = plus_button_text.get_rect(center=plus_button_rect.center)
                windowSurface.blit(plus_button_text, plus_text_rect)
                minus_button_text = font.render('-', True, (100, 200, 15))
                minus_text_rect = minus_button_text.get_rect(center=minus_button_rect.center)
                windowSurface.blit(minus_button_text, minus_text_rect)
                pygame.display.update()
pygame.init()
pygame.mixer.init()
font = pygame.font.Font('ofont.ru_Boozy.ttf', 30)
music_files = ['music/music1.mp3','music/music2.mp3','music/music3.mp3','music/music4.mp3','music/music5.mp3','music/music6.mp3','music/music7.mp3','music/music8.mp3','music/music9.mp3','music/music10.mp3','music/music11.mp3']
current_track_index = 0
pygame.mixer.music.load(music_files[current_track_index])
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Гонки')
gameOverSound = pygame.mixer.Sound('music/crash.wav')
pygame.mixer.music.load('music/car.mp3')
laugh = pygame.mixer.Sound('music/lose.mp3')
playerImage = pygame.image.load('image/car1.png')
playerRect = playerImage.get_rect()
new_width = playerRect.width - 10
new_height = playerRect.height - 10
playerImage = pygame.transform.scale(playerImage, (new_width, new_height))
car3 = pygame.image.load('image/car3.png')
car4 = pygame.image.load('image/car4.png')
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
pygame.display.update()
waitForPlayerToPressKey()
zero=0
pygame.mixer.music.load(music_files[random.randint(0,10)])
pygame.mixer.music.play()
if not os.path.exists("data/save.dat"):
    f=open("data/save.dat",'w')
    f.write(str(zero))
    f.close()
v=open("data/save.dat",'r')
topScore = int(v.readline())
v.close()
score_ = 0
while count>0:
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    score_ = 0
    if a == 2:
        while True:
            score += 5
            score_ += 5
            if score_ == 2000:
                score_ = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == ord('e'):
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
                    if event.key == K_v:
                        PLAYERMOVERATE *=4
                if event.type == KEYUP:
                    if event.key == ord('e'):
                        reverseCheat = False
                        score = 0
                    if event.key == K_CAPSLOCK:
                        slowCheat = False
                        score = 0
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False
                    if event.key == K_v:
                        PLAYERMOVERATE /=4
                    if event.key == K_ESCAPE:
                        pause_game()
                    if event.key == ord('q'):
                        current_track_index += 1
                        if current_track_index >= len(music_files):
                            current_track_index = 0
                        pygame.mixer.music.load(music_files[current_track_index])
                        pygame.mixer.music.play()
                    if event.key == ord('r'):
                        pygame.mixer.music.stop()
            if not reverseCheat and not slowCheat:
                baddieAddCounter += 2
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize =30
                last_spawn_time = 0
                if pygame.time.get_ticks() - last_spawn_time > 1000:
                    newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 15, 30),
                                 'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                                 'surface': pygame.transform.scale(random.choice(sample), (15, 30)),
                                 }
                    last_spawn_time = pygame.time.get_ticks()
                else:
                    newBaddie = None
                baddies.append(newBaddie)
                sideLeft = {'rect': pygame.Rect(0,0,126,600),
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
            if score_ >= 1000:
                drawText('Бессмертность: %s' % 'Да', font, windowSurface, 200, 40)
            elif score_ <= 2000:
                drawText('Бессмертность: %s' % 'Нет', font, windowSurface, 200, 40)
            drawText('Лучший счет: %s' % (topScore), font, windowSurface, 200, 20)
            windowSurface.blit(playerImage, playerRect)
            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])
            pygame.display.update()
            if playerHasHitBaddie(playerRect, baddies):
                if score > topScore:
                    g=open("data/save.dat",'w')
                    g.write(str(score))
                    g.close()
                    topScore = score
                break
            mainClock.tick(FPS)
    elif a == 1:
        while True:
            score += 5
            score_ += 5
            if score_ == 2000:
                score_ = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == ord('e'):
                        reverseCheat = True
                    if event.key == K_CAPSLOCK:
                        slowCheat = True
                    if event.key == K_ESCAPE:
                        pause_game()
                    if event.key == K_v:
                        PLAYERMOVERATE *= 200
                if event.type == KEYUP:
                    if event.key == ord('e'):
                        reverseCheat = False
                    if event.key == K_CAPSLOCK:
                        slowCheat = False
                    if event.key == ord('q'):
                        current_track_index += 1
                        if current_track_index >= len(music_files):
                            current_track_index = 0
                        pygame.mixer.music.load(music_files[current_track_index])
                        pygame.mixer.music.play()
                    if event.key == K_v:
                        PLAYERMOVERATE /= 200
                    if event.key == ord('r'):
                        pygame.mixer.music.stop()
            mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
            sprite_pos = pygame.math.Vector2(playerRect.center)
            distance = mouse_pos.distance_to(sprite_pos)
            if distance > 0:
                direction = (mouse_pos - sprite_pos).normalize()
                playerRect.move_ip(direction * min(distance, PLAYERMOVERATE))
            if not reverseCheat and not slowCheat:
                baddieAddCounter += 2
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize = 30
                newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 15, 30),
                             'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                             'surface': pygame.transform.scale(random.choice(sample), (15, 30)),
                             }
                baddies.append(newBaddie)
                sideLeft = {'rect': pygame.Rect(0, 0, 126, 600),
                            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                            'surface': pygame.transform.scale(wallLeft, (126, 599)),
                            }
                baddies.append(sideLeft)
                sideRight = {'rect': pygame.Rect(500, 0, 203, 600),
                             'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                             'surface': pygame.transform.scale(wallRight, (303, 580)),
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
            if score_ >= 1000:
                drawText('Бессмертность: %s' % 'Да', font, windowSurface, 200, 40)
            elif score_ <= 2000:
                drawText('Бессмертность: %s' % 'Нет', font, windowSurface, 200, 40)
            drawText('Лучший счет: %s' % (topScore), font, windowSurface, 200, 20)
            windowSurface.blit(playerImage, playerRect)
            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])
            pygame.display.update()
            if playerHasHitBaddie(playerRect, baddies):
                if score > topScore:
                    g = open("data/save.dat", 'w')
                    g.write(str(score))
                    g.close()
                    topScore = score
                break
            mainClock.tick(FPS)
    pygame.mixer.music.stop()
    count=count-1
    gameOverSound.play()
    time.sleep(1)