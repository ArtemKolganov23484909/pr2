import pygame
from lvls.classes import Screen, SettingsButton, ScoreButton, Rocket, Square
from lvls.functions import *

pygame.init()
screen = Screen(550, 1250)
settings_button = SettingsButton(5, 5, 100, 50)
score_button = ScoreButton(120, 5, 100, 50)
rocket = Rocket(250, screen.height * 0.75, 'sprites/rocket.png', screen, speed=get_speed('lvls/maps/map1.txt'))
first = 1
running = True
numbers_loaded = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.move_left()
            elif event.key == pygame.K_RIGHT:
                rocket.move_right()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocket.stop()
    
    screen.draw()
    rocket.update()
    rocket.draw()
    
    if not numbers_loaded:
        read_numbers_from_file('lvls/maps/map1.txt', screen)
        numbers_loaded = True
    if first:
        settings_button.draw(screen)
        read_numbers_from_file('lvls/maps/map1.txt', screen)
    score_button.draw(screen)
    screen.update()

pygame.quit()