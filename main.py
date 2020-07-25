import pygame
import random
from abc import ABC, abstractmethod

pygame.init()

# Images
BACKGROUND = pygame.image.load("images/background.png")
PLAYER_IMG = pygame.image.load("images/player.png")
ENEMY_IMG = pygame.image.load("images/enemy.png")

# Screen
WIDTH = 700
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing car")
pygame.display.set_icon(PLAYER_IMG)

# Colors
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60


class Car(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Enemy(Car):
    def __init__(self):
        self.x = 800
        self.y = random.choice([124, 234])
        self.moving_speed = 5

    def draw(self):
        win.blit(ENEMY_IMG, (self.x, self.y))

    def move(self):
        self.x -= self.moving_speed


class Player(Car):
    def __init__(self):
        self.x = 50
        self.y = 124

    def draw(self):
        win.blit(PLAYER_IMG, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.y = 234

        elif keys[pygame.K_UP]:
            self.y = 124


def enemy_spawn(enemy):
    if enemy.x == WIDTH // 2:
        enemies.append(Enemy())

    if enemy.x <= -ENEMY_IMG.get_width():
        enemies.pop(0)


def has_collided(enemy):
    if enemy.x <= player.x <= enemy.x + ENEMY_IMG.get_width() and player.y == enemy.y:
        return True

    return False


def render():
    win.fill(WHITE)
    win.blit(BACKGROUND, (0, 0))
    player.draw()

    for enemy in enemies:
        enemy.draw()

    pygame.display.update()

def display_message(subject):
    pass

def main():
    global player, enemies

    run = True

    player = Player()
    enemies = [Enemy()]

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            player.move()

        for enemy in enemies:
            enemy.move()
            enemy_spawn(enemy)

            if has_collided(enemy):
                run = False

        render()


while True:
    if __name__ == "__main__":
        main()
