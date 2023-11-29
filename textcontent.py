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
game_font_size = 28
game_font_obj = pygame.font.Font(game_font_path, game_font_size)

subtitle_font_size = 42
subtitle_font_obj = pygame.font.Font(game_font_path, subtitle_font_size)


def general_text(
    text: str,
    pos_x: int,
    pos_y: int,
    head_level: int = 2,
    l_align: int = 0,
    color: tuple = (255, 255, 255),
):
    if head_level == 0:
        text_obj = title_font_obj.render(text, True, color).convert_alpha()
    elif head_level == 1:
        text_obj = subtitle_font_obj.render(text, True, color).convert_alpha()
    elif head_level == 2:
        text_obj = game_font_obj.render(text, True, color).convert_alpha()
    else:
        raise ValueError("Invalid head_level value")
    text_rect = text_obj.get_rect()
    text_rect.center = (pos_x + l_align * text_rect.width / 2, pos_y)
    return (text_obj, text_rect)


def game_over_func(score: int, highscores: list):
    game_over_text, game_over_text_rect = general_text(
        "Game Over", globals.WIDTH / 2, 75, head_level=0
    )
    lines = [(game_over_text, game_over_text_rect)]
    lines.append(
        general_text(
            "Your Score: " + str(int(score)),
            pos_x=globals.WIDTH / 2,
            pos_y=150,
            l_align=0,
        )
    )
    lines.append(general_text("Highscores:", globals.WIDTH / 2, 200, head_level=1))
    y_position = 250
    num = 1
    for s in highscores:
        lines.append(
            general_text(str(num) + ". " + str(s), globals.WIDTH / 2, y_position)
        )
        y_position += 50
        num += 1

    prompt_text, prompt_text_rect = general_text(
        "Press any key to restart", globals.WIDTH / 2, globals.HEIGHT - 50
    )
    # TODO: Add credits if any in slight grey color
    y_position += 25
    lines.append(
        general_text(
            "Credits:",
            pos_x=globals.WIDTH / 2,
            pos_y=y_position,
            head_level=1,
            color=(150, 150, 150),
        )
    )
    y_position += 50
    lines.append(
        general_text(
            "Developed by: Pratyush Kumar",
            globals.WIDTH / 2,
            y_position,
            color=(150, 150, 150),
        )
    )
    y_position += 50
    lines.append(
        general_text(
            "Music by: Pratyush Kumar (developed using GarageBand)",
            globals.WIDTH / 2,
            y_position,
            color=(150, 150, 150),
        )
    )
    return (lines, (prompt_text, prompt_text_rect))


def hits_text(hit_count: int):
    hit_count_text, hit_count_text_rect = general_text(
        "Hits left: " + "x " * (3 - hit_count), pos_x=10, pos_y=75, l_align=1
    )
    return (hit_count_text, hit_count_text_rect)


def scores_text(score: int):
    score_text, score_text_rect = general_text(
        "Score: " + str(int(score)), pos_x=globals.WIDTH - 10, pos_y=75, l_align=-1
    )
    return (score_text, score_text_rect)


def setup_splash_screen():
    # Setup splash screen text
    splash_text, splash_text_rect = general_text(
        "The Eighth Run", globals.WIDTH / 2, 100, head_level=0
    )
    info_lines = []
    info_lines.append(
        general_text("Welcome to The Eighth Run!", globals.WIDTH / 2, 200)
    )
    info_lines.append(
        general_text(
            "Use up/down arrow keys or W/S keys to move the player (green)",
            globals.WIDTH / 2,
            250,
            color=(100, 255, 100),
        )
    )
    info_lines.append(
        general_text(
            "Avoid the obstacles (red notes)",
            globals.WIDTH / 2,
            300,
            color=(255, 100, 100),
        )
    )
    info_lines.append(
        general_text(
            "Collect the powerups (blue rests)",
            globals.WIDTH / 2,
            350,
            color=(100, 100, 255),
        )
    )
    info_lines.append(
        general_text(
            "If hit an obstacle, you will convert into it", globals.WIDTH / 2, 400
        )
    )
    info_lines.append(
        general_text("You can take maximum 3 hits", globals.WIDTH / 2, 450)
    )
    prompt_text, prompt_text_rect = general_text(
        "Press any key to start", globals.WIDTH / 2, globals.HEIGHT - 100
    )
    return (
        (splash_text, splash_text_rect),
        info_lines,
        (prompt_text, prompt_text_rect),
    )
