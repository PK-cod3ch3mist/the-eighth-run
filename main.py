import random
import pygame
import sys
import notes
import platforms
import constant
import obstacles
import logging

from pygame.locals import *

# Basic pygame boilerplate code with event loop
pygame.init()
DISPLAYSURF = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))
pygame.display.set_caption("The Eighth Run")

FramePerSec = pygame.time.Clock()

game_obstacles = obstacles.ObstacleList()

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Display the player
    player1 = notes.Player()
    player1.draw(DISPLAYSURF)

    # Display and move the obstacles
    if random.randint(0, 100) < 1:
        game_obstacles.add_obstacle()
    game_obstacles.move_obstacles(DISPLAYSURF)

    # Display the 5 staff lines at equal intervals in the y direction
    staff1 = platforms.Staff(constant.STAFFPOS[0])
    staff2 = platforms.Staff(constant.STAFFPOS[1])
    staff3 = platforms.Staff(constant.STAFFPOS[2])
    staff4 = platforms.Staff(constant.STAFFPOS[3])
    staff5 = platforms.Staff(constant.STAFFPOS[4])
    staff1.draw(DISPLAYSURF)
    staff2.draw(DISPLAYSURF)
    staff3.draw(DISPLAYSURF)
    staff4.draw(DISPLAYSURF)
    staff5.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(constant.FPS)
