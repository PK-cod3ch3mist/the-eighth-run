import random
import pygame
import sys
import notes
import platforms
import globals
import obstacles
import logging
import movinglist
import powerups

from pygame.locals import *
from textcontent import *

# Basic pygame boilerplate code with event loop
pygame.init()
DISPLAYSURF = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("The Eighth Run")

FramePerSec = pygame.time.Clock()

# Setup player and obstacles
game_objects = movinglist.MovingList()
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

# Splash screen display boolean
display_splash = True

# Game over display boolean
game_over = False

# Load and play opening-track.wav music file
pygame.mixer.music.load("./assets/music/opening-track.wav")
pygame.mixer.music.play(loops=-1, fade_ms=500)


def check_collision():
    """
    Check for collisions between the player and obstacles. If there is a collision, convert the player sprite to that of the obstacle. After 3 collisions, the game ends.
    """
    hits = pygame.sprite.spritecollide(
        player, globals.moving_group, False, collided=pygame.sprite.collide_mask
    )
    if hits:
        # check if the player is colliding with an obstacle
        if isinstance(hits[0], obstacles.Obstacle):
            logger.info("Collision detected with obstacle.")
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 50, globals.WIDTH, 50))
            if player.hit_count < 3:
                # Increase hit count and display it
                player.hit_count += 1
                logger.debug("Hit count: " + str(player.hit_count))

                # Remove the obstacles from the list
                for obj in hits:
                    game_objects.remove_object(obj)
                    obj.hide(DISPLAYSURF)

                # Convert the player sprite to that of the obstacle
                player.convert_to_obstacle(DISPLAYSURF, hits[0])
            else:
                logger.debug("Game over")
                global game_over
                game_over = True

                # Change the music back to opening-track.wav
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load("./assets/music/opening-track.wav")
                pygame.mixer.music.play(loops=-1, fade_ms=500)

                # Draw the screen black
                pygame.draw.rect(
                    DISPLAYSURF, (0, 0, 0), (0, 0, globals.WIDTH, globals.HEIGHT)
                )
                return True

        # check if the player is colliding with a powerup
        elif isinstance(hits[0], powerups.Powerup):
            logger.info("Collision detected with powerup.")
            # Remove the powerup from the list
            for obj in hits:
                game_objects.remove_object(obj)
                obj.hide(DISPLAYSURF)

            # If powerup of type 0, increase the hit count
            if hits[0].powerup_type == 0 and player.hit_count > 0:
                player.hit_count -= 1
                pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 50, globals.WIDTH, 50))
                logger.debug("New hit count: " + str(player.hit_count))

            # If powerup of type 1, increase the score
            elif hits[0].powerup_type == 1:
                player.prev_score = player.score
                player.score += 10
                logger.debug("New score: " + str(player.score))

    return False


def difficulty_increase():
    # Increase the speed of the obstacles every SPEED_LEVEL points
    if int(player.prev_score / globals.SPEED_LEVEL) != int(
        player.score / globals.SPEED_LEVEL
    ):
        game_objects.speed += globals.SPEED_INCREASE

    # Increase the probability of adding an obstacle every PROB_LEVEL points
    if int(player.prev_score / globals.PROB_LEVEL) != int(
        player.score / globals.PROB_LEVEL
    ):
        globals.obstacle_probability += globals.PROB_INCREASE

    # Decrease the blank space between obstacles every SPACE_LEVEL points
    if (
        int(player.prev_score / globals.SPACE_LEVEL)
        != int(player.score / globals.SPACE_LEVEL)
        and globals.blank_space > globals.MIN_BLANK_SPACE
    ):
        globals.blank_space -= globals.SPACE_DECREASE


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

                # Stop the current music and unload it
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()

                # Load and play the start-beat.wav music file as game music
                pygame.mixer.music.load("./assets/music/pace-beat.wav")
                pygame.mixer.music.play(loops=-1, fade_ms=0)
                continue

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                dir = globals.Direction.UP
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
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

    elif game_over:
        # Display game over screen
        game_over_lines = game_over_func(player.score)
        for line in game_over_lines:
            DISPLAYSURF.blit(line[0], line[1])

    else:
        # Display the player
        player.draw(DISPLAYSURF)

        # Check for collisions
        # player.check_collision()
        is_game_over = check_collision()
        if is_game_over:
            continue

        # Display the hit count
        hit_count_text, hit_count_text_rect = hits_text(player.hit_count)
        DISPLAYSURF.blit(hit_count_text, hit_count_text_rect)

        score_text, score_text_rect = scores_text(player.score)
        DISPLAYSURF.blit(score_text, score_text_rect)

        # Remove the score from the screen if it changes
        if int(player.prev_score) != int(player.score):
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (globals.WIDTH - 200, 50, 200, 50))

        # Increase the difficulty
        difficulty_increase()

        # Display and move the obstacles
        # Starting probability of adding an obstacle is 10%
        if random.random() < globals.obstacle_probability:
            game_objects.add_obstacle()

        # Starting probability of adding a powerup is 1%
        if random.random() < globals.powerup_probability:
            game_objects.add_powerup()

        game_objects.move_objects(DISPLAYSURF)

        player.prev_score = player.score
        player.score += 0.01

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
