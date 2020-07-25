import pygame
import random
from abc import ABC, abstractmethod

pygame.init()

# Screen
WIDTH = 700
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Images
BACKGROUND = pygame.image.load("images/background.png")
PLAYER_IMG = pygame.image.load("images/player.png")
ENEMY_IMG = pygame.image.load("images/enemy.png")

# Colors
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60


class Car(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Enemy(Car):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.moving_speed = 30

    def draw(self):
        pass

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


def render():
    win.fill(WHITE)
    win.blit(BACKGROUND, (0, 0))
    player.draw()
    pygame.display.update()


def main():
    global player

    run = True

    player = Player()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            player.move()

        render()


while True:
    if __name__ == "__main__":
        main()
