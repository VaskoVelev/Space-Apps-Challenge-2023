import pygame

class Player:
    def __init__(self, image, x, y, moving_left, moving_right):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.moving_left = moving_left
        self.moving_right = moving_right
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.moving_left == True:
            self.x -= 0.5
        if self.moving_right == True:
            self.x += 0.45

    def teleport(self, direction):
        if direction == "left":
            self.x = -64
        if direction == "right":
            self.x = 800

    def teleport_away(self):
        self.x = 1000
        self.y = 1000

    def change_image(self, image):
        self.image = pygame.image.load(image)

    def reset(self):
        self.x = 368
        self.y = 500