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

logging.basicConfig(
    filename="./gamelog.log",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

logger = logging.getLogger("main")


def check_collision():
    hits = pygame.sprite.spritecollide(
        player1, globals.obstacles_group, False, collided=pygame.sprite.collide_mask
    )
    if hits:
        logger.info("Collision detected:")
        if player1.hit_count < 3:
            # Increase hit count and display it
            player1.hit_count += 1
            logger.debug("Hit count: " + str(player1.hit_count))

            # Remove the obstacles from the list
            for obj in hits:
                game_obstacles.remove_obstacle(obj)
                obj.hide_obstacle(DISPLAYSURF)

            # Convert the player sprite to that of the obstacle
            player1.convert_to_obstacle(DISPLAYSURF, hits[0])
        else:
            logger.debug("Game over")
            pygame.quit()
            sys.exit()


while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            dir = (
                globals.Direction.UP
                if event.key == pygame.K_UP
                else globals.Direction.DOWN
            )
            player1.staff_movement(DISPLAYSURF, dir)

    # Display the player
    player1.draw(DISPLAYSURF)

    # Check for collisions
    # player1.check_collision()
    check_collision()

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
