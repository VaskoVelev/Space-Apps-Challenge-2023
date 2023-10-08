import pygame

class Score:
    def __init__(self, value, x, y, font, size):
        self.value = value
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, size)

    def draw(self, screen: pygame.Surface):
        text = self.font.render(f"Score: {str(self.value)}", True, (255, 255, 255))
        screen.blit(text, (self.x, self.y))

    def increase_value(self):
        self.value += 1

    def teleport_away(self):
        self.x = 1000
        self.y = 1000

    def reset(self):
        self.value = 0