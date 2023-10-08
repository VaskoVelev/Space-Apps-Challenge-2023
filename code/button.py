import pygame
from pygame.locals import *

class Button:
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (0, 0, 0)

    def __init__(self, x, y, text, width, height):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.text = text
        self.width = width
        self.height = height
        self.clicked = False

    def draw(self, screen: pygame.Surface):
        action = False
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        font = pygame.font.SysFont('comicsans', 30)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y - 2))
        return action
    
    def set_original(self):
        self.x = self.original_x
        self.y = self.original_y

    def change_text(self, text):
        self.text = text
    
    def teleport_away(self):
        self.x = 1000
        self.y = 1000

    def teleport_center(self, x, y):
        self.x = x
        self.y = y
