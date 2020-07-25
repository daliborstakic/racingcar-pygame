import pygame
import random
from abc import ABC, abstractmethod

pygame.init()

# Screen
win = pygame.display.set_mode((700, 400))

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
        self.x = 0
        self.y = 0

    def draw(self):
        pass

    def move(self):
        pass


def render():
    win.fill(WHITE)
    pygame.display.update()


def main():
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        render()


while True:
    if __name__ == "__main__":
        main()
