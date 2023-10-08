from player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score
from highscore import Highscore
from gameover import Gameover
from button import Button
import pygame

pygame.init()

# Screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Title and Icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load('Python game/Images/icon.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("Python game/Images/background2.png")

# Main Menu Variables
newGame_button = Button(320, 245, "New Game", 160, 40)
continueGame_button = Button(290, 270, "Continue Game", 220, 40)
menuQuit_button = Button(350, 295, "Quit", 100, 40)

# Game Variables
player = Player("Python game/Images/player.png", 368, 500, False, False)
enemies = [Enemy("Python game/Images/alien.png") for _ in range(1)]
bullet = Bullet("Python game/Images/bullet.png", player.x + 16, player.y - 16, False)
score = Score(0, 0, 0, "comicsans", 20)
highscore = Highscore(0, 20, "comicsans", 20)
gameover = Gameover(218, 190, "comicsans", 70)
pause_button = Button(665, 10, "Pause", 125, 40)
mainMenu_button = Button(315, 270, "Main Menu", 170, 40) 
quit_button = Button(350, 320, "Quit", 100, 40)
game_started = False

# Menu Function
def main_menu():

    #Variables
    global background
    global newGame_button
    global game_started

    # Main Loop
    while True:

        # Hide Previous Window
        screen.fill((0, 0, 0))

        # Background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            # Quit Menu
            if event.type == pygame.QUIT:
                pygame.quit()

        # Draw Menu
        if game_started:
            newGame_button.y = 220
            menuQuit_button.y = 320
            if continueGame_button.draw(screen):
                Game()
        if newGame_button.draw(screen):
            if game_started:
                score.reset()
                for enemy in enemies:
                    enemy.reset()
                player.reset()
                bullet.reset()
            game_started = True
            Game()
        if menuQuit_button.draw(screen):
            pygame.quit()

        pygame.display.update()

# Game Function
def Game():

    # Variables
    global background
    global player
    global enemy
    global bullet
    global score
    global highscore
    global gameover
    global pause_button
    global quit_button
    paused = False

    # Main Loop
    while True:

        # Hide Previous Window
        screen.fill((0, 0, 0))

        # Background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                pygame.quit()

            # Check if key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.moving_left = True
                if event.key == pygame.K_RIGHT:
                    player.moving_right = True
                if event.key == pygame.K_SPACE:
                    if not bullet.Is_fired():
                        bullet.reload(player.x + 16, player.y - 16)
                        if paused == False:
                            bullet.fire()

            # Check if key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.moving_left, player.moving_right = False, False
            
        # Draw Player
        player.draw(screen)

        # Player Movement
        if paused == False:
            player.move()
        if player.moving_left and player.x <= -64:
            player.teleport("right")
        if player.moving_right and player.x >= 800:
            player.teleport("left")

        # Draw Enemy
        for enemy in enemies:
            enemy.draw(screen)

        # Enemy Movement
        for enemy in enemies:
            if paused == False:
                enemy.move()
            if enemy.x <= 0:
                enemy.change_direction("right")
            if enemy.x >= 736:
                enemy.change_direction("left")
            if enemy.game_over_collision():
                for enemy in enemies:
                    enemy.teleport_away()
                player.teleport_away()
                bullet.teleport_away()
                score.teleport_away()
                highscore.teleport_away()
                gameover.draw(screen)
                pause_button.teleport_away()
                background = pygame.image.load("Python game/Images/pause_background2.png")
                break

        # Bullet Movement
        if bullet.Is_fired():
            bullet.draw(screen)
            if paused == False:
                bullet.move()
            if bullet.has_missed():
                bullet.reload(player.x + 16, player.y - 16)
        
        # Bullet Collision
        for enemy in enemies:
            if bullet.hit_enemy(enemy.x, enemy.y):
                score.increase_value()
                if score.value > highscore.value:
                    highscore.increase_value()
                enemy.respawn()
                bullet.reload(player.x + 16, player.y - 16)

        # Draw Score
        if paused == False:
            score.draw(screen)

        # Draw Highscore
        if paused == False:
            highscore.draw(screen)

        # Pause Game
        if paused == False:
            if pause_button.draw(screen):
                background = pygame.image.load("Python game/Images/pause_background2.png")
                player.change_image("Python game/Images/pause_player.png")
                for enemy in enemies:
                    enemy.change_image("Python game/Images/pause_alien.png")
                bullet.change_image("Python game/Images/pause_bullet.png")
                pause_button.change_text("Resume")
                pause_button.teleport_center(337.75, 220)
                paused = True
        if paused == True:
            if pause_button.draw(screen):
                background = pygame.image.load("Python game/Images/background2.png")
                player.change_image("Python game/Images/player.png")
                for enemy in enemies:
                    enemy.change_image("Python game/Images/alien.png")
                bullet.change_image("Python game/Images/bullet.png")
                pause_button.change_text("Pause")
                pause_button.set_original()
                paused = False
            if quit_button.draw(screen):
                    pygame.quit()
            if mainMenu_button.draw(screen):
                background = pygame.image.load("Python game/Images/background2.png")
                player.change_image("Python game/Images/player.png")
                for enemy in enemies:
                    enemy.change_image("Python game/Images/alien.png")
                bullet.change_image("Python game/Images/bullet.png")
                pause_button.change_text("Pause")
                pause_button.set_original()
                paused = False
                main_menu()

        pygame.display.update()

main_menu()