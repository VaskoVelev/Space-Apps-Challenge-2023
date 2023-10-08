import pygame

class Highscore:
    def __init__(self, x, y, font, size):
        with open("Python game/Other files/highscore.txt", "r") as f:
            self.value = int(f.read())
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, size)

    def draw(self, screen: pygame.Surface):
        text = self.font.render(f"Highscore: {str(self.value)}", True, (255, 255, 255))
        screen.blit(text, (self.x, self.y))

    def increase_value(self):
        self.value += 1
        with open("Python game/Other files/highscore.txt", "w") as f:
            f.write(str(self.value))
    
    def teleport_away(self):
        self.x = 1000
        self.y = 1000