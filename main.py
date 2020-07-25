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
BLACK = (0, 0, 0)

# Fonts
END_FONT = pygame.font.SysFont('arial', 40)

# Clock
clock = pygame.time.Clock()
FPS = 60


# Abstract class for car
class Car(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self):
        pass


# Class enemy inherits the Car class
class Enemy(Car):
    def __init__(self):
        self.x = 800
        self.y = random.choice([124, 234])

    moving_speed = 0

    def draw(self):
        win.blit(ENEMY_IMG, (self.x, self.y))

    def move(self):
        self.x -= self.moving_speed


# Class player inherits the Car class
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


# Spawning an enemy depending on the condition
def enemy_spawn(enemy):
    if enemy.x <= -ENEMY_IMG.get_width():
        enemies.append(Enemy())
        enemies.pop(0)


# Checking for collisions
def has_collided(enemy):
    if enemy.x <= player.x + PLAYER_IMG.get_width() <= enemy.x + ENEMY_IMG.get_width() and player.y == enemy.y:
        return True

    return False


# Drawing the screen
def render():
    win.fill(WHITE)
    win.blit(BACKGROUND, (0, 0))
    player.draw()

    for enemy in enemies:
        enemy.draw()

    pygame.display.update()


# Displaying end message
def display_message(subject):
    pygame.time.delay(500)
    win.fill(WHITE)
    display_text = END_FONT.render(subject, 1, BLACK)
    win.blit(display_text, ((WIDTH - display_text.get_width()) // 2, (HEIGHT - display_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(2000)


# Main function
def main():
    global player, enemies

    # Getting the ticks from the beginning of the game
    start_ticks = pygame.time.get_ticks()
    last_second = 0

    run = True

    # Setting initial moving speed
    Enemy.moving_speed = 5

    player = Player()
    enemies = [Enemy()]  # Array of enemies

    while run:
        clock.tick(FPS)

        # Seconds from the start of the game
        seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            player.move()  # Moving the player

        # Looping through the enemies
        for enemy in enemies:
            enemy.move()
            enemy_spawn(enemy)

            # Ending the game if it has collided
            if has_collided(enemy):
                display_message("You lost!")
                run = False

        # Increasing enemy move speed
        if seconds % 5 == 0 and seconds != last_second:
            Enemy.moving_speed += 1
            last_second = seconds  # Making sure that it executes once every second

        render()


while True:
    if __name__ == "__main__":
        main()
