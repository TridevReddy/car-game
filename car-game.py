import pygame
import math
import random

# initialize Pygame
pygame.init()
# Colours
Red = (255, 0, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
light_green = (0, 255, 42)
light_blue = (0, 229, 255)
yellow = (255, 251, 0)

# Screen
screen = pygame.display.set_mode((800, 500))
screen.fill(light_green)
pygame.display.update()
height = 600
# Images
player_img = pygame.transform.scale(pygame.image.load("car2_final.png"), (80, 150))
road_img = pygame.transform.scale(pygame.image.load("road2.png"), (600, 600))
road2_img = pygame.transform.scale(pygame.image.load("road2.png"), (600, 600))
road3_img = pygame.transform.scale(pygame.image.load("road2.png"), (600, 600))
enemy1_img = pygame.transform.scale(pygame.image.load("enemy1.png"), (80, 150))
enemy2_img = pygame.transform.scale(pygame.image.load("enemy2.png"), (80, 150))
enemy3_img = pygame.transform.scale(pygame.image.load("enemy3.png"), (80, 150))

#Fonts
crashed_font = pygame.font.SysFont("comicsans", 60)

# Player
player_x = 300
player_y = 350
playerx_change = 0
car_sound = pygame.mixer.Sound("car_mp3.mp3")
car_sound.set_volume(0.1)
car_crash_sound = pygame.mixer.Sound("car_crash.mp3")
car_crash_sound.set_volume(0.1)
crash_sound = True



def playercar(x, y):
    screen.blit(player_img, (x, y))


# Road
road_x = 100
road_y = -100
road2_x = 100
road2_y = -699
road3_x = 100
road3_y = -1299

i = 0
counter = 0


def road(x, y):
        screen.blit(road_img, (100, i))
        screen.blit(road_img, (100, height + i))


# Enemy 1
enemy1_x = random.randint(100, 620)
enemy1_y = random.randint(-500, -100)
enemy1_y_change = 0.5


def enemy1(x, y):
    screen.blit(enemy1_img, (x, y))


# Enemy 2
enemy2_x = random.randint(100, 620)
enemy2_y = random.randint(-900, -500)
enemy2_y_change = 0.5


def enemy2(x, y):
    screen.blit(enemy2_img, (x, y))


# Enemy 3
enemy3_x = random.randint(100, 620)
enemy3_y = random.randint(-1400, -900)
enemy3_y_change = 0.5


def enemy3(x, y):
    screen.blit(enemy3_img, (x, y))

#Collision


crash = crashed_font.render("CRASHED!", True, (255,255,255))
def collision():

    car_sound.stop()
    car_crash_sound.play()
    pygame.display.update()

car_sound.play(5)

# Infinite loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and counter == 0:
                playerx_change = 0.5
            if event.key == pygame.K_LEFT and counter == 0:
                playerx_change = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    player_x += playerx_change
    if player_x <= 100:
        player_x = 100

    if player_x > 630:
        player_x = 630

    enemy1_y += enemy1_y_change
    if enemy1_y > 800:
        enemy1_y = random.randint(-500, -100)
        enemy1_x = random.randint(100, 620)
    enemy2_y += enemy2_y_change
    if enemy2_y > 800:
        enemy2_y = random.randint(-900, -500)
        enemy2_x = random.randint(100, 620)
    enemy3_y += enemy3_y_change
    if enemy3_y > 800:
        enemy3_y = random.randint(-1400, -900)
        enemy3_x = random.randint(100, 620)
    # Background Scrolling
    if i == -height:
        screen.blit(road_img, (100, height - i))
        i = 0
    i -= 1

    dist1 = math.sqrt((player_x - enemy1_x) ** 2 + (player_y - enemy1_y) ** 2)
    dist2 = math.sqrt((player_x - enemy2_x) ** 2 + (player_y - enemy2_y) ** 2)
    dist3 = math.sqrt((player_x - enemy3_x) ** 2 + (player_y - enemy3_y) ** 2)

    if counter!=0:
        enemy1_y_change = 0
        enemy2_y_change = 0
        enemy3_y_change = 0
        i = 1
        #screen.blit(road_img, (100, 500))

    if dist1<75 or dist2<75 or dist3<75:
        counter+=1
        screen.blit(crash, (270, 200))
        pygame.display.update()
        if crash_sound:
            collision()
            crash_sound = False


    road(road_x, road_y)
    playercar(player_x, player_y)
    enemy1(enemy1_x, enemy1_y)
    enemy2(enemy2_x, enemy2_y)
    enemy3(enemy3_x, enemy3_y)
    pygame.display.update()
