import random
import pygame
import sys
import notes
import platforms
import globals
import obstacles
import logging

from pygame.locals import *
from textcontent import *

# Basic pygame boilerplate code with event loop
pygame.init()
DISPLAYSURF = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("The Eighth Run")

FramePerSec = pygame.time.Clock()

# Setup player and obstacles
game_obstacles = obstacles.ObstacleList()
player = notes.Player()

# Setup logging
logging.basicConfig(
    filename="./gamelog.log",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

logger = logging.getLogger("main")


BLINK_EVENT = pygame.USEREVENT + 1
show_prompt = True
pygame.time.set_timer(BLINK_EVENT, 500)


def check_collision():
    """
    Check for collisions between the player and obstacles. If there is a collision, convert the player sprite to that of the obstacle. After 3 collisions, the game ends.
    """
    hits = pygame.sprite.spritecollide(
        player, globals.obstacles_group, False, collided=pygame.sprite.collide_mask
    )
    if hits:
        logger.info("Collision detected:")
        pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 50, globals.WIDTH, 50))
        if player.hit_count < 3:
            # Increase hit count and display it
            player.hit_count += 1
            logger.debug("Hit count: " + str(player.hit_count))

            # Remove the obstacles from the list
            for obj in hits:
                game_obstacles.remove_obstacle(obj)
                obj.hide_obstacle(DISPLAYSURF)

            # Convert the player sprite to that of the obstacle
            player.convert_to_obstacle(DISPLAYSURF, hits[0])
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
            if display_splash:
                display_splash = False

                # Hide the splash screen
                pygame.draw.rect(
                    DISPLAYSURF, (0, 0, 0), (0, 0, globals.WIDTH, globals.HEIGHT)
                )
                continue

            if event.key == pygame.K_UP:
                dir = globals.Direction.UP
            elif event.key == pygame.K_DOWN:
                dir = globals.Direction.DOWN
            else:
                dir = None

            player.staff_movement(DISPLAYSURF, dir)
        elif event.type == BLINK_EVENT:
            show_prompt = not show_prompt

    if display_splash:
        # Display splash screen
        (
            (splash_text, splash_text_rect),
            info_lines,
            (prompt_text, prompt_text_rect),
        ) = setup_splash_screen()
        DISPLAYSURF.blit(splash_text, splash_text_rect)
        if show_prompt:
            DISPLAYSURF.blit(prompt_text, prompt_text_rect)
        else:
            pygame.draw.rect(
                DISPLAYSURF, (0, 0, 0), (0, 600, globals.WIDTH, globals.HEIGHT - 100)
            )

        for info_line in info_lines:
            DISPLAYSURF.blit(info_line[0], info_line[1])

    else:
        # Display the player
        player.draw(DISPLAYSURF)

        # Check for collisions
        # player.check_collision()
        check_collision()

        # Display the hit count
        hit_count_text, hit_count_text_rect = hits_text(player.hit_count)
        DISPLAYSURF.blit(hit_count_text, hit_count_text_rect)

        score_text, score_text_rect = scores_text(player.score)
        DISPLAYSURF.blit(score_text, score_text_rect)
        prev_score = player.score
        player.score += 0.01

        # Remove the score from the screen if it changes
        if int(prev_score) != int(player.score):
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (globals.WIDTH - 200, 50, 200, 50))

        # Increase the speed of the obstacles every 15 points
        if int(prev_score / globals.SPEED_LEVEL) != int(
            player.score / globals.SPEED_LEVEL
        ):
            game_obstacles.speed += 1

        # Increase the probability of adding an obstacle every 30 points
        if int(prev_score / globals.PROB_LEVEL) != int(
            player.score / globals.PROB_LEVEL
        ):
            globals.probability += 1

        # Display and move the obstacles
        # Starting probability of adding an obstacle is 10 / 1000
        if random.randint(0, 1000) < globals.probability:
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
