import pygame

class Bullet:
    def __init__(self, image, x, y, is_fired):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.is_fired = is_fired

    def fire(self):
        self.is_fired = True
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 1.15

    def reload(self, x, y):
        self.is_fired = False
        self.x = x
        self.y = y

    def Is_fired(self):
        if self.is_fired == True:
            return True
        return False

    def hit_enemy(self, x, y):
        if self.y <= y + 64 and self.y >= y + 20:
            if self.x + 16 >= x and self.x <= x + 64:
                if self.is_fired:
                    return True
        return False

    def has_missed(self):
        if self.y <= 0:
            return True
        return False
    
    def teleport_away(self):
        self.x = 1000
        self.y = 1000
    
    def change_image(self, image):
        self.image = pygame.image.load(image)

    def reset(self):
        self.is_fired = False