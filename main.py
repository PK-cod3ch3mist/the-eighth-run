import random
import pygame
import sys
import notes
import platforms
import globals
import obstacles
import logging

from pygame.locals import *

# Basic pygame boilerplate code with event loop
pygame.init()
DISPLAYSURF = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("The Eighth Run")

FramePerSec = pygame.time.Clock()

game_obstacles = obstacles.ObstacleList()
player1 = notes.Player()

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.staff_up(DISPLAYSURF)
            elif event.key == pygame.K_DOWN:
                player1.staff_down(DISPLAYSURF)

    # Display the player
    player1.draw(DISPLAYSURF)

    # Check for collisions
    player1.check_collision()

    # Display and move the obstacles
    if random.randint(0, 1000) < 10:
        game_obstacles.add_obstacle()
    game_obstacles.move_obstacles(DISPLAYSURF)

    # Display the 5 staff lines at equal intervals in the y direction
    staff_lines = [
        platforms.Staff(globals.STAFFPOS[0]),
        platforms.Staff(globals.STAFFPOS[1]),
        platforms.Staff(globals.STAFFPOS[2]),
        platforms.Staff(globals.STAFFPOS[3]),
        platforms.Staff(globals.STAFFPOS[4]),
    ]
    for staff_line in staff_lines:
        staff_line.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(globals.FPS)
