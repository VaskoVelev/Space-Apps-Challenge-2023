import pygame
import random

class Enemy:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.x = random.randint(0, 736)
        self.y = random.randint(0, 90)
        self.direction = random.choice(["left", "right"])
        self.speed = random.uniform(0.45, 0.6)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 0.06
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "right":
            self.x += self.speed

    def change_direction(self, direction):
        self.direction = direction

    def respawn(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(0, 90)

    def game_over_collision(self):
        if self.y >= 600:
            return True
        return False
    
    def teleport_away(self):
        self.x = 1000
        self.y = 1000

    def change_image(self, image):
        self.image = pygame.image.load(image)

    def reset(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(0, 90)
        self.direction = random.choice(["left", "right"])
        self.speed = random.uniform(0.45, 0.6)
