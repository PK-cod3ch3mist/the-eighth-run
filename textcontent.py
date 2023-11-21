import pygame
import sys
import globals

from pygame.locals import *

# Setup font for splash screen
pygame.font.init()
title_font_path = "./assets/fonts/Monoton/Monoton-Regular.ttf"
title_font_size = 54
title_font_obj = pygame.font.Font(title_font_path, title_font_size)

# Setup font for in game text
game_font_path = "./assets/fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
game_font_size = 30
game_font_obj = pygame.font.Font(game_font_path, game_font_size)


# TODO: Build a better game over screen with credits and stuff
def game_over_func():
    game_over_text = title_font_obj.render(
        "Game Over", True, (255, 100, 100)
    ).convert_alpha()
    game_over_text_rect = game_over_text.get_rect(
        center=(globals.WIDTH / 2, globals.HEIGHT - 100)
    )
    return (game_over_text, game_over_text_rect)


def hits_text(hit_count: int):
    hit_count_text = game_font_obj.render(
        "Hits left: " + "x " * (3 - hit_count), True, (255, 255, 255)
    ).convert_alpha()
    hit_count_text_rect = hit_count_text.get_rect()
    hit_count_text_rect.center = (hit_count_text_rect.width / 2 + 10, 75)
    return (hit_count_text, hit_count_text_rect)


def scores_text(score: int):
    score_text = game_font_obj.render(
        "Score: " + str(int(score)), True, (255, 255, 255)
    ).convert_alpha()
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (globals.WIDTH - score_text_rect.width / 2 - 10, 75)
    return (score_text, score_text_rect)


def setup_splash_screen():
    # Setup splash screen text
    splash_text = title_font_obj.render(
        "The Eighth Run", True, (255, 255, 255)
    ).convert_alpha()
    splash_text_rect = splash_text.get_rect(center=(globals.WIDTH / 2, 100))
    info_text_line1 = game_font_obj.render(
        "Welcome to The Eighth Run!", True, (255, 255, 255)
    ).convert_alpha()
    info_text_line1_rect = info_text_line1.get_rect(center=(globals.WIDTH / 2, 200))
    info_text_line2 = game_font_obj.render(
        "Use the up and down arrow keys to move the player (green)",
        True,
        (255, 255, 255),
    ).convert_alpha()
    info_text_line2_rect = info_text_line2.get_rect(center=(globals.WIDTH / 2, 250))
    info_text_line3 = game_font_obj.render(
        "Avoid the obstacles (red notes)",
        True,
        (255, 100, 100),
    ).convert_alpha()
    info_text_line3_rect = info_text_line3.get_rect(center=(globals.WIDTH / 2, 300))
    info_text_line6 = game_font_obj.render(
        "Collect the powerups (blue rests)", True, (100, 100, 255)
    ).convert_alpha()
    info_text_line6_rect = info_text_line6.get_rect(center=(globals.WIDTH / 2, 350))
    info_text_line4 = game_font_obj.render(
        "If hit an obstacle, you will convert into it",
        True,
        (255, 255, 255),
    ).convert_alpha()
    info_text_line4_rect = info_text_line4.get_rect(center=(globals.WIDTH / 2, 400))
    info_text_line5 = game_font_obj.render(
        "You can take maximum 3 hits", True, (255, 255, 255)
    ).convert_alpha()
    info_text_line5_rect = info_text_line5.get_rect(center=(globals.WIDTH / 2, 450))
    prompt_text = game_font_obj.render(
        "Press any key to start", True, (255, 255, 255)
    ).convert_alpha()
    prompt_text_rect = prompt_text.get_rect(
        center=(globals.WIDTH / 2, globals.HEIGHT - 100)
    )
    info_lines = (
        (info_text_line1, info_text_line1_rect),
        (info_text_line2, info_text_line2_rect),
        (info_text_line3, info_text_line3_rect),
        (info_text_line4, info_text_line4_rect),
        (info_text_line5, info_text_line5_rect),
        (info_text_line6, info_text_line6_rect),
    )
    return (
        (splash_text, splash_text_rect),
        info_lines,
        (prompt_text, prompt_text_rect),
    )
