# This file contains all the constant quantities used in the program
import pygame
import sys
from enum import Enum

from pygame.locals import *

WIDTH = 1000
HEIGHT = 750
STAFFPOS = (175, 275, 375, 475, 575)
FPS = 60

obstacle_probability = 10
powerup_probability = 1

# FIXME: Determine the best values for these constants
SPEED_LEVEL = 15
PROB_LEVEL = 30
START_SPEED = 2
BLANK_SPACE = 200

# Staff change sounds
pygame.mixer.init()

# TODO: Change these sounds to be more vintage like
STAFFSOUNDS = (
    pygame.mixer.Sound("assets/sounds/E3.wav"),
    pygame.mixer.Sound("assets/sounds/G3.wav"),
    pygame.mixer.Sound("assets/sounds/B3.wav"),
    pygame.mixer.Sound("assets/sounds/D4.wav"),
    pygame.mixer.Sound("assets/sounds/F4.wav"),
)

TOTAL_STAFFS = len(STAFFSOUNDS)
TOTAL_NOTES = 6
TOTAL_POWERUPS = 2


class Direction(Enum):
    UP = -1
    DOWN = 1


moving_group = pygame.sprite.Group()
