# user moves the player with the mouse and hears the sounds when collided with the enemy

import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (170, 0, 150)
SQUARE = (250, 107, 255)
COLORS = (SQUARE, RED, BLACK)

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60


############################################################
############################################################


class Box:
    def __init__(self, display, x, y, width, height, color, img):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0
        self.y_speed = random.randint(3, 5)
        self.color = color
        self.img = img

    def draw_box(self):
        self.display.blit(self.img, [self.x, self.y])

    def update(self):
        self.x += self.speed

        if self.x <= 0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def drop_box(self):

        if self.y > DISPLAY_HEIGHT:
            self.x = random.randrange(0, DISPLAY_WIDTH, 5)
            self.y = random.randrange(-100, 0, 5)
            self.y_speed = random.randint(3, 5)

        self.y += self.y_speed

    def is_collided(self, other):
        if (self.x <= other.x <= self.x + self.width or self.x <= other.x + other.width <= self.x + self.width) and \
                (
                        self.y < other.y + other.width < self.y + self.width or self.y <= other.y + other.width <= self.y + self.width):
            return True
            print('yes')


pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25, True, False)
game_score = 0
text = font.render(f"Score: {game_score}", True, WHITE)

# images w/ urls
background_img = pygame.image.load("bg.png")
# https://opengameart.org/content/backgrounds-3
player_img = pygame.image.load("chicken_player.png")
# https://opengameart.org/content/lpc-chicken-rework
enemy_img = pygame.image.load("drumstick.png")
points_img = pygame.image.load("apple.png")
# https://opengameart.org/content/64-16x16-food-sprites
collide_sound = pygame.mixer.Sound("Chicken Sound Effect.ogg")
# https://opengameart.org/content/chicken-sound-effect

# create player
player_width = 50
x_loc = (DISPLAY_WIDTH - player_width) / 2
y_loc = DISPLAY_HEIGHT - 2 * player_width
player = Box(screen, x_loc, y_loc, player_width, player_width, SQUARE, player_img)

# create enemies
enemy_width = 15
enemy_list = []
for i in range(5):
    x_coord = random.randrange(0, DISPLAY_WIDTH, 5)
    random_y = random.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_coord, random_y, enemy_width, enemy_width, WHITE, enemy_img))

points_width = 15
points_list = []
for i in range(5):
    x_coord = random.randrange(0, DISPLAY_WIDTH, 5)
    random_y = random.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_coord, random_y, points_width, points_width, WHITE, points_img))

running = True
while running:

    pos = pygame.mouse.get_pos()
    player.x = pos[0] - .5 * player.width
    player.y = pos[1] - .5 * player.width

    # pressed_lft = pygame.mouse.get_pressed()[0]
    # print(pressed_lft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player.speed = 5
        #     elif event.key == pygame.K_LEFT:
        #         player.speed = -5
        # elif event.type == pygame.KEYUP:
        #     player.speed = 0

    screen.blit(background_img, [0, 0])

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()
        # if player.is_collided(enemy):
        #   game_score += 1
        #   print(game_score)
        #   collide_sound.play()

    for points in points_list:
        points.draw_box()
        points.drop_box()

    player.draw_box()
    player.update()
    screen.blit(text, [DISPLAY_WIDTH - 90, 20])

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
