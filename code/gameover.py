import pygame

class Gameover:
    def __init__(self, x, y, font, size):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, size)

    def draw(self, screen: pygame.Surface):
        text = self.font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (self.x, self.y))