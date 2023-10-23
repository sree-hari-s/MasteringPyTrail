import pygame
import random
import sys
from pygame.locals import *
import setuptools
import os

pygame.init()
pygame.mixer.init()

# BASIC THINGS
screenwidth = 720
screenheight = 480
screen = pygame.display.set_mode((screenwidth, screenheight))
base_path = getattr(sys, '_MEIPASS', os.path.dirname(
    os.path.abspath(__file__)))
background = pygame.image.load(os.path.join(
    base_path, 'images/city.png')).convert_alpha()
background = pygame.transform.smoothscale(background, (720, 480))
background_flip = pygame.transform.flip(background, True, False)
clock = pygame.time.Clock()
font1 = pygame.font.Font('freesansbold.ttf', 64)
font2 = pygame.font.Font('freesansbold.ttf', 24)
pygame.display.set_caption('PIZZA DELIVERY TRUCK SIMULATOR')
icon = pygame.image.load(os.path.join(
    base_path, 'images/delivery.png'))
pygame.display.set_icon(icon)

# SOUNDS
boing = pygame.mixer.Sound(
    os.path.join(
        base_path, 'audio/Cartoon Boing.mp3'))
hushari = pygame.mixer.Sound(os.path.join(
    base_path, 'audio/Hushari_edit.wav'))
wide = pygame.mixer.Sound(
    os.path.join(
        base_path, 'audio/widememe.mp3'))
conro = pygame.mixer.Sound(
    os.path.join(
        base_path, 'audio/Conro - Thrill of it.mp3'))
title_song = pygame.mixer.Sound(os.path.join(
    base_path, 'audio/toobadtobesad.wav'))
channel1 = pygame.mixer.Channel(0)

# VEHICLE
vehicle = pygame.image.load(os.path.join(
    base_path, 'images/pizza-truck.png')).convert_alpha()
vehicleX = 50
vehicleY = 400
vehiclewidth = 64
vehicleheight = 64
vehicleY_change = 10

# OBSTACLE
obstacle = pygame.image.load(
    os.path.join(
        base_path, 'images/postbox.png')).convert_alpha()
obstacle = pygame.transform.smoothscale(obstacle, (32, 32))
obstacleX = screenwidth + 10
obstacleY = 432
obstaclewidth = 32
obstacleheight = 32
obstacleVel = 5


# OBSTACLE MOVEMENT MECHANISM
def obstacle_generator(x):
    return {'x': x, 'y': 432}


obs1 = obstacle_generator(int(screenwidth + 10))
OBS = [obs1]


# BACKGROUND MOVEMENT MECHANISM
def background_roller(x, img):
    return {'x': x, 'y': 0, 'img': img}


background1 = background_roller(0, background)
background2 = background_roller(720, background_flip)
backgroundie = [background1, background2]
backgroundVel = 5

# JUMP MECHANISM
jump = False
grounded = True


# COLLISION MECHANISM
def isCollision(vx, vy, ox, oy):
    global vehiclewidth, vehicleheight, obstaclewidth, obstacleheight
    if (abs(vy - oy) <= obstacleheight) and (abs(vx - ox) < obstaclewidth):

        return True
    else:
        return False


# TITLE AND GAMEOVER MECHANISM
title = pygame.image.load(os.path.join(
    base_path, 'images/_title.png')).convert_alpha()
title = pygame.transform.smoothscale(title, (400, 400))
title_bg = pygame.image.load(os.path.join(
    base_path, 'images/pizzabg_pc2.jpg')).convert()
title_bg = pygame.transform.smoothscale(title_bg, (screenwidth, screenheight))
ggameover = False
gameover = False
restart_command = False


score_value = 0

while True:
    screen.fill((255, 255, 255))
    score = font2.render("score = " + str(score_value), True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            break

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                jump = True
            elif event.key == K_e:
                pygame.quit()
                sys.exit()
                break

        if event.type == KEYUP:
            if event.key == K_s:
                pygame.event.clear()
                ggameover = True
                title_song.fadeout(1000)
            elif event.key == K_r:
                pygame.event.clear()
                restart_command = True

    # TITLE SCREEN
    if not ggameover:
        pygame.event.set_allowed(KEYUP)
        screen.blit(title_bg, (0, 0))
        screen.blit(title, ((screenwidth - 400) / 2, (screenheight - 400) / 2))
        title_song.play(-1, 0, 1000)

    if ggameover:
        if gameover:
            pygame.event.clear()
            pygame.event.set_blocked(KEYDOWN)
            pygame.event.set_allowed(KEYUP)

            channel1.fadeout(1200)
            gameover_text = font1.render('GAME OVER', True, (0, 0, 0))
            restart = font2.render(
                'Press "r" to play again', True, (255, 0, 0))
            screen.blit(background, (0, 0))
            screen.blit(gameover_text, ((screenwidth - 64) /
                        2 - 150, (screenheight - 64) / 2))
            screen.blit(restart, ((screenwidth - 64) / 2 -
                        100, (screenheight - 64) / 2 + 100))
            screen.blit(score, (screenwidth/2 - 50, 0))
            if restart_command:
                score_value = 0
                gameover = False
                restart_command = False
                collision = False

        if not gameover:
            pygame.event.set_allowed(KEYDOWN)
            pygame.event.set_blocked(KEYUP)

            if not channel1.get_busy():
                music_no = random.randint(1, 2)
                if music_no == 1:
                    conro.set_volume(0.5)
                    conro.play(0, 120000)

                elif music_no == 2:
                    wide.set_volume(0.5)
                    wide.play()

            # BACKGROUND MOVEMENT
            for bg in backgroundie:
                bg['x'] -= backgroundVel
            if backgroundie[0]['x'] <= -background.get_width():
                backgroundie.remove(backgroundie[0])
                bg3 = background_roller(screenwidth, background)
                backgroundie.insert(0, bg3)
            if backgroundie[1]['x'] <= -int(screenwidth):
                backgroundie.remove(backgroundie[1])
                bg3 = background_roller(screenwidth, background_flip)
                backgroundie.insert(1, bg3)
            for bg in backgroundie:
                screen.blit(bg['img'], (bg['x'], 0))

            # COLLISION MECHANISM
            collision = isCollision(
                vehicleX, vehicleY, OBS[0]['x'], OBS[0]['y'])

            if collision:
                hushari.play()
                vehicleX = 50
                vehicleY = 400
                OBS.remove(OBS[0])
                obs3 = obstacle_generator(int(screenwidth + 10))
                OBS.append(obs3)

                grounded = True
                jump = False
                ggameover = True
                gameover = True

            # JUMP MECHANISM
            if jump:  # is necessary or else the vehicle will jump once at the beginning of the game.
                if grounded:
                    if 0 <= vehicleY <= 400:
                        vehicleY -= vehicleY_change
                        if vehicleY <= 250:
                            grounded = False
                        if vehicleY == 390:
                            boing.play()

                if not grounded:
                    vehicleY += vehicleY_change
                    if vehicleY >= 400:
                        grounded = True
                        jump = False
                        if OBS[0]['x'] < vehicleX:
                            score_value += 10

            # OBSTACLE MOVEMENT
            random_obstacle = random.randrange(0, int(screenwidth/2), 5)
            for obs in OBS:
                obs['x'] -= obstacleVel
            if OBS[0]['x'] <= random_obstacle:
                if len(OBS) == 1:
                    obs2 = obstacle_generator(
                        int(screenwidth + random.randint(10, 20)))
                    OBS.append(obs2)
            if OBS[0]['x'] <= -obstaclewidth:
                OBS.remove(OBS[0])
            for obs in OBS:
                screen.blit(obstacle, (obs['x'], 432))

            screen.blit(vehicle, (vehicleX, vehicleY))
            screen.blit(score, (0, 0))

    clock.tick(32)
    pygame.display.update()
